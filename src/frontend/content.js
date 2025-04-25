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
        chrome.storage.local.set({ biasSentences: result.bias_content });
        highlightBias(result.bias_content);
    } catch (error) {
        console.error("Error analyzing text:", error);
    }
}

function highlightBias(sentences) {
    const walker = document.createTreeWalker(
        document.body,
        NodeFilter.SHOW_TEXT,
        {
            acceptNode: (node) => {
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

    for (const sentence of sentences) {
        if (!sentence.trim()) continue;

        for (const node of textNodes) {
            const text = node.textContent;
            if (text.includes(sentence)) {
                const highlightedHTML = text.replaceAll(sentence, `<span style="background-color: yellow; font-weight: bold;">${sentence}</span>`);
                const spanWrapper = document.createElement("span");
                spanWrapper.innerHTML = highlightedHTML;

                node.parentNode.replaceChild(spanWrapper, node);
                break;
            }
        }
    }
}

extractText();
