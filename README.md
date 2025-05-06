# PolitScope

PolitScope is a web-based browser extension designed to address the growing issue of political bias present in social media, a challenge that contributes to the increasing polarization in society today. As bias escalates on social media, it's more important than ever to have reliable methods for detecting and analyzing it. This study explores the use of natural language processing (NLP) to create an automated system for identifying political bias. The methodology involves cleaning and embedding text using the RoBERTa model, then clustering similar text to create a baseline model. This model is saved and used to compare and dynamically detect bias in newly collected web text. Through a series of experiments, we evaluate PolitScope's effectiveness, examining how various parts of speech influence bias detection. While the results show that PolitScope is not yet perfect, the tool demonstrates the potential of NLP in highlighting political bias in online social media platforms, and contributing to the broader conversation about bias in digital media.

---

## Why PolitScope?

The spread of political content across social platforms has made it increasingly difficult to differentiate between fact, opinion, and bias. Existing tools tend to focus on **misinformation detection** or **sentiment analysis**, but these approaches often miss how **framing, word choice, and context** influence political bias. PolitScope provides a more nuanced lens by utilizing unsupervised, data-driven NLP techniques such as RoBERTa and K-Means clustering.

---

## Features

- **Bias Classification**: Classifies input text as politically biased or non-biased.
- **Transformer-Based NLP**: Uses Roberta and K-Means for accurate language understanding.
- **Experiments**: Experiments designed to measure how accurate PolitScope's classification is.
- **Visual Feedback**: A browser extension that provides direct visual reports on bias content.
- **Wide Input Sources**: PolitScope is designed to integrate directly into your browsing experience, and designed to accept a wide variety of textual content.

---

## Tech Stack

- **Python**
- **Transformers (HuggingFace)** (for RoBERTa embedding generations)
- **scikit-learn/Numpy** (for K-Means clustering and analysis)
- **pandas** (for data handling)
- **Matplotlib** (for experimental visualizations)
- **Fast API** (for communication between front and backend)
- **pickle** (for saving our trained model)

---

## Running PolitScope

PolitScope is currently a proof of concept, designed to demonstrate the potential of an automated bias detection tool that can evaluate online content in real time. While the primary focus of this research was to develop the bias detection model and a functional front-end interface, future work will explore how this prototype can be scaled into a fully deployable Chrome extension. For now, the system offers a working demonstration of the detection pipeline, from web content collection to bias classification and user display.

To run PolitScope, begin by downloading the `frontend` folder and visit the [Chrome Extensions](chrome://extensions) page. Enable `Developer Mode` in the top right corner, then select `Load unpacked` and choose the frontend directory. This will install the PolitScope extension directly onto your browser.

Next, open a terminal window, and navigate to the `backend` directory, and run the following command:

```text
uvicorn main:app --reload
```

This will start the backend API server. Once the server confirms that it's running and listening, the extension and backend will begin communicating. From this point, you can visit any website and PolitScope will automatically begin analyzing the textual content on that given page.

For development and debugging purposes, print statements have been left in the backend code. If you watch the terminal while browsing, you’ll see different stages of the algorithm logging outputs, which can confirm that key components, such as text extraction, embedding, and classification, are functioning correctly. If you prefer not to monitor the terminal, you can simply wait a moment, and the classification results will appear directly in the tool’s interface. In order to see the list of results, click on the PolitScope extension popup In the output, PolitScope includes a red warning to the users about the results, and a holistic report of bias sentences on the current webpage.
