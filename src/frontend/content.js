// Extract page text
function getPageText() {
    return document.body.innerText;
}

// Send text to background script


// Highlight biased sentences
function highlightBiasedText(biasedSentences) {
    biasedSentences.forEach(sentence => {
        document.body.innerHTML = document.body.innerHTML.replace(
            new RegExp(sentence, "g"),
            `<span class="highlight-bias">${sentence}</span>`
        );
    });
}
