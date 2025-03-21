document.addEventListener("DOMContentLoaded", async function () {
    const biasList = document.getElementById("biasList");

    chrome.storage.local.get("biasSentences", function (data) {
        if (data.biasSentences && data.biasSentences.length > 0) {
            data.biasSentences.forEach(sentence => {
                const li = document.createElement("li");
                li.textContent = sentence;
                li.onclick = () => scrollToSentence(sentence);
                biasList.appendChild(li);
            });
        } else {
            biasList.innerHTML = "<li>No biased sentences detected.</li>";
        }
    });
});

function scrollToSentence(sentence) {
    let found = false;
    document.querySelectorAll("p, span, div").forEach(el => {
        if (!found && el.innerText.includes(sentence)) {
            el.scrollIntoView({ behavior: "smooth", block: "center" });
            found = true;
        }
    });
}
