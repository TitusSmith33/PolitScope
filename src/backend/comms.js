chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "saveText") {
        chrome.storage.local.set({ input_text: message.data }, () => {
            console.log("Page text saved to local storage.");
        });
    }
});

chrome.storage.local.get(["input_text"], (result) => {
    if (result.input_text) {
        console.log("Retrieved text:", result.input_text.content);
    }
});