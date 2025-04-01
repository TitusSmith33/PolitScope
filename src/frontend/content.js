async function extractText() {
    // Remove unnecessary sections before extracting text
    const ignoreSections = ["header", "footer", "nav", ".sidebar", ".advertisement"];
    document.querySelectorAll(ignoreSections.join(", ")).forEach(el => el.remove());

    let mainText = "";
    document.querySelectorAll("article, main, p").forEach(el => {
        if (el.offsetParent !== null) {  // Ensure it's visible
            let text = el.innerText.trim();
            if (text.split(" ").length > 5) {  // Ignore very short text
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

async function highlightBias(sentences) {
    const similarity = await import('https://cdn.jsdelivr.net/npm/string-similarity@4.0.4/+esm');

    document.querySelectorAll("article, main, p").forEach(el => {
        let text = el.innerText.trim();
        let textSentences = text.split('. ').map(s => s.trim());

        sentences.forEach(sentence => {
            let bestMatch = similarity.findBestMatch(sentence, textSentences);
            
            if (bestMatch.bestMatch.rating > 0.2) {  // Lower threshold
                let matchedSentence = bestMatch.bestMatch.target;

                // Normalize both texts to prevent failed replacements
                let normalizedText = el.innerHTML.replace(/\s+/g, " ").trim();
                let normalizedMatch = matchedSentence.replace(/\s+/g, " ").trim();

                if (normalizedText.includes(normalizedMatch)) {
                    el.innerHTML = el.innerHTML.replace(
                        normalizedMatch, 
                        `<span style="background-color: yellow; font-weight: bold;">${normalizedMatch}</span>`
                    );
                } else {
                    console.warn("Match not found in element text:", normalizedMatch);
                }
            }
        });
    });
}


extractText();
