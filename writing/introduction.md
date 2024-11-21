# Introduction

Are we allowed to include sites in the intro??

## Introductory Paragraphs

* Briefly introduce PolitScope as a tool to detect political bias dynamically while users browse web pages.
* Mention the increasing prevalence of bias in digital media and the need for automated tools to address it.
* State how PolitScope uses advanced models like RoBERTa and sentiment analysis to achieve this goal.

In an age dominated by digital media, the information we consume has a profound impact on our perceptions, beliefs, and decisions. However, much of this content is shaped by underlying biases that are often hidden from view. Bias refers to a tendency, prejudice, or inclination that skews perception, judgment, or action in a particular direction, often in a way that is unfair or unbalanced. It can manifest consciously or unconsciously and is influenced by cultural, social, and individual factors. Online, bias often emerges through algorithms, content prioritization, or selective exposure to information, affecting how individuals interpret or engage with digital content.

As individuals navigate their increasingly complex social media feeds, news websites, and online discussions, subtle biases in language and framing can influence their perspectives without their awareness. When we encounter unrecognized biases, they influence our perspective, or beliefs, and even how we act. This phenomenon is applicable in many fields of study, such as product consumption, cultural perceptions, and political views. This research specifically focuses on how political bias contributes to the growing political polarization seen in the United States, creating an urgent need for tools that promote critical media consumption.

Our research is designed to meet this need. We developed a tool; PolitScope, that is a browser extension aimed at identifying political bias in real time as users browse the web. By leveraging advanced natural language processing (NLP) techniques and pre-trained models, PolitScope dynamically detects and highlights language that may include some varying level of underlying political bias. This is designed to help users better understand the perspectives embedded in the content they consume. Unlike tools that require manual input or focus on fact-checking content, PolitScope operates seamlessly in the background, providing a user-free experience, and focused on the underlying bias that may not be as recognizable to an average media consumer.

To uncover and classify political bias in online content, PolitScope employs advanced natural language processing (NLP) techniques and machine learning models. The foundation of this approach lies in RoBERTa, a pre-trained transformer model designed for robust textual analysis. By leveraging RoBERTa's capabilities, PolitScope extracts word embeddings—mathematical representations of words and their relationships—directly from textual data. These embeddings enable the identification of nuanced patterns in tone, context, and word usage that are often indicative of bias.

After generating the embeddings, PolitScope uses clustering algorithms, such as K-means or Latent Dirichlet Allocation (LDA), to group related words and phrases into meaningful clusters. Sentiment analysis is then applied to these clusters, providing insights into the emotional undertones and contextual leanings of the text. By synthesizing these analyses, the tool classifies political bias with precision. Beyond classification, PolitScope enables deeper evaluations of political text by exploring critical questions such as which words or phrases contribute most to bias, whether sentiment or context has a greater impact, and how bias shifts in response to different textual inputs. This dual focus on detection and evaluation positions PolitScope as both a diagnostic tool and a platform for advancing our understanding of political bias.

The significance of PolitScope extends beyond individual users. In today’s polarized political environment, the tool seeks to foster greater media literacy, encouraging critical evaluation of the information we encounter daily. By uncovering bias and promoting awareness, PolitScope has the potential to empower individuals to make more informed decisions and contribute to healthier public discourse. This is the first (yet crucial) step towards addressing the diverging political polarization that plagues the United States.

## Background of the Problem

* The growing consumption of news through digital platforms often introduces unconscious bias.
* Political polarization amplified by biased news impacts public perception and democracy.
* Current tools for detecting bias are limited in real-time application and usability.

If allowed a lot of sourcing will be helpful in this section

In today’s digital landscape, the way we consume news has shifted dramatically, with social media becoming a primary source of information for younger generations. However, this shift comes with its own set of challenges. Unlike traditional media, which is subject to more rigorous editorial standards, digital platforms are filled with content that often carries hidden political biases. These biases can subtly influence the way we think, act, and perceive the world around us.

Political content on social media is particularly powerful because it is designed to persuade, influence, and convince. This type of content doesn’t just inform, it shapes opinions, often in ways we don’t realize. When left unchecked, these biases contribute to growing political polarization, creating an "us versus them" mentality that divides society further. This polarization has profound consequences for public discourse and democracy, making it harder to find common ground and fostering an increasingly adversarial political environment.

While awareness of misinformation has grown, with tools now available to help users identify false or misleading information, these tools fall short when it comes to addressing bias. The problem of bias is more nuanced and insidious than mere misinformation. Bias doesn’t just change what we believe; it shapes how we think, often without us even knowing it. This lack of awareness leaves users vulnerable to manipulation, with their thoughts and beliefs subtly molded by the content they consume.

PolitScope seeks to address this critical gap. Unlike existing tools, which focus on verifying truth versus falsehood, PolitScope is designed to identify and expose the underlying biases hidden within political content. By bringing these biases to light, we can empower individuals to critically evaluate the information they encounter and take the first step toward addressing the larger issue of political polarization in the United States.

## Statement of the Problem

* People are unaware of the biases present in the information they consume.
* There is a lack of user-friendly tools to dynamically highlight political bias in real-time.
* Existing solutions focus on static content or require user interaction.

## Purpose of the Study

* To develop an automated, user-free tool to identify and highlight political bias dynamically on web pages.
* To explore the integration of machine learning models and sentiment analysis for bias detection.

## Research Questions

* ??

## Significance of the Study

* Empowers users to critically evaluate the content they consume.
* Contributes to the growing field of media literacy and automated bias detection.
* Provides a foundation for further research and development of bias-detection technologies.

## Definition of Terms

* What is this section

## Assumptions, Limitations, and Delimitations

Assumptions:

* Users will trust and adopt PolitScope for their browsing needs.

Limitations:

* Bias detection may not be 100% accurate due to evolving language and complex biases.
* Real-time processing speed could vary depending on hardware and network conditions.

Delimitations:

* Focuses only on text-based content, not multimedia (images, videos, etc.).
* Targets English-language content initially.

## Ethical Dilemma(s)

* Transparency: How to ensure the tool’s users understand its predictions and limitations.
* Data Privacy: Collecting and processing user data without compromising their privacy.
* Bias in Model: The risk of the tool itself exhibiting bias due to training data.
