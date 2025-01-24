document.getElementById('highlightBtn').addEventListener('click', function() {
  const word = document.getElementById('wordInput').value.trim();
  if (word) {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        func: highlightWord,
        args: [word]
      });
    });
  }
});

function highlightWord(word) {
  if (word.length === 0) return;

  const regex = new RegExp(`(${word})`, 'gi');
  document.body.innerHTML = document.body.innerHTML.replace(
    regex,
    `<mark>$1</mark>`
  );
}
