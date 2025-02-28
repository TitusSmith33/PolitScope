// Extract page text
function getPageText() {
    return document.body.innerText;
}

// Send text to background script
function sendTextToBackground() {
    const text = getPageText();
    const data = { content: text }; // Format as JSON

    chrome.runtime.sendMessage({ action: "saveText", data });
}

sendTextToBackground();

// Highlight biased sentences
function highlightBiasedText(biasedSentences) {
    biasedSentences.forEach(sentence => {
        document.body.innerHTML = document.body.innerHTML.replace(
            new RegExp(sentence, "g"),
            `<span class="highlight-bias">${sentence}</span>`
        );
    });
}
