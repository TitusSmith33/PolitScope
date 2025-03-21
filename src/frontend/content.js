async function extractText() {
    let visibleText = "";
    document.querySelectorAll("p, span, div").forEach(el => {
        if (el.offsetParent !== null) { // Ensures only visible elements
            visibleText += el.innerText + " ";
        }
    });

    const requestData = { content: visibleText.trim() };
    
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

function highlightBias(sentences) {
    document.querySelectorAll("p, span, div").forEach(el => {
        sentences.forEach(sentence => {
            if (el.innerText.includes(sentence)) {
                el.innerHTML = el.innerHTML.replace(sentence, `<span style="background-color: yellow; font-weight: bold;">${sentence}</span>`);
            }
        });
    });
}

extractText();
