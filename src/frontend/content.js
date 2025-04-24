async function extractText() {
    // Sections to ignore during text extraction
    const ignoreSections = ["header", "footer", "nav", ".sidebar", ".advertisement"];

    let mainText = "";

    // Collect all paragraphs and visible text within main content areas
    document.querySelectorAll("article, main, p").forEach(el => {
        // Skip elements that are part of ignored sections
        if (!el.closest(ignoreSections.join(", ")) && el.offsetParent !== null) {
            const text = el.innerText.trim();
            if (text.split(" ").length > 5) {
                mainText += text + " ";
            }
        }
    });

    const requestData = { content: mainText.trim() };

    try {
        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(requestData)
        });

        const result = await response.json();
        highlightBias(result.bias_content);
        chrome.storage.local.set({ biasSentences: result.bias_content });
    } catch (error) {
        console.error("Error analyzing text:", error);
    }
}

// Highlighting biased sentences using TreeWalker for precise DOM manipulation
async function highlightBias(sentences) {
    const similarity = await import('https://cdn.jsdelivr.net/npm/string-similarity@4.0.4/+esm');

    const walker = document.createTreeWalker(
        document.body,
        NodeFilter.SHOW_TEXT,
        {
            acceptNode: (node) => {
                // Filter out hidden or whitespace-only text nodes
                if (!node.parentElement.offsetParent) return NodeFilter.FILTER_REJECT;
                if (!node.textContent.trim()) return NodeFilter.FILTER_REJECT;
                return NodeFilter.FILTER_ACCEPT;
            }
        }
    );

    const textNodes = [];
    while (walker.nextNode()) {
        const node = walker.currentNode;
        if (!node.parentElement.closest("header, footer, nav, .sidebar, .advertisement")) {
            textNodes.push(node);
        }
    }

    for (const biasSentence of sentences) {
        for (const node of textNodes) {
            const text = node.textContent;
            const match = similarity.findBestMatch(biasSentence, [text]).bestMatch;

            if (match.rating > 0.1) {
                const span = document.createElement("span");
                span.style.backgroundColor = "yellow";
                span.style.fontWeight = "bold";
                span.textContent = text;

                node.parentNode.replaceChild(span, node);
                break; // Move to next bias sentence after a match
            }
        }
    }
}

extractText();
