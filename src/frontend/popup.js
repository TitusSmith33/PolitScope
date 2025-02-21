document.addEventListener("DOMContentLoaded", function() {
  chrome.storage.local.get("biasedSentences", (data) => {
      const biasList = document.getElementById("bias-list");

      if (data.biasedSentences && data.biasedSentences.length > 0) {
          data.biasedSentences.forEach(sentence => {
              let listItem = document.createElement("li");
              listItem.textContent = sentence;
              listItem.addEventListener("click", () => scrollToSentence(sentence));
              biasList.appendChild(listItem);
          });
      } else {
          biasList.innerHTML = "<li>No biased content detected.</li>";
      }
  });
});

function scrollToSentence(sentence) {
  let elements = document.getElementsByClassName("highlight-bias");
  for (let el of elements) {
      if (el.innerText === sentence) {
          el.scrollIntoView({ behavior: "smooth", block: "center" });
          break;
      }
  }
}
