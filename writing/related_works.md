# Related Works

## Themes

### Political Polarization and Media Bias

Main focus of this theme: Research exploring the current political climate, the polarization trends, and how media bias impacts public opinion and democracy. Potentially explaining why polarization is dangerous.
Influence on project: Provides context for why a tool like PolitScope is necessary and underscores the significance of real-time bias detection. Tied more to motivation and grounds the issue at hand with sound evidence and explanation.

Political Polarization in the US:
https://www.pewresearch.org/politics/2014/06/12/political-polarization-in-the-american-public/

Exploration of left vs right and how it is shifting
https://www.facinghistory.org/resource-library/political-polarization-united-states

US has fasting growing polarization out of all democracies
https://www.brown.edu/news/2020-01-21/polarization

### Social Media as a Platform for Political Discourse

Main focus of this theme: Studies examining how social media shapes political communication and amplifies biases. Study about how much $$ goes into political spending on social media. How political content on social media differs than getting it from other sources. Hate speech and target ads, etc. and how they are perceived.
Influence on project: Highlights the importance of focusing on digital platforms and informs how PolitScope can address biases inherent in real-time social media feeds. More driven to the motivation behind the project. Also helps drive the issue at hand in concrete evidence.

Graph about social media per age:

- <https://soax.com/research/time-spent-on-social-media>
- <https://www.statista.com/statistics/1484565/time-spent-social-media-us-by-age/>

Pew Research about politics on social media:
<https://www.pewresearch.org/internet/2024/06/12/how-americans-navigate-politics-on-tiktok-x-facebook-and-instagram/>

Political ad spending:
www.statista.com/statistics/1325158/political-digital-ad-spending-usa/.

Social media usage:
soax.com/research/time-spent-on-social-media.

VooDoo doll on social media (if they can control how you act and predict what you will do, imagine the implecations this has for politics and political beliefs and polarization): https://futurism.com/the-byte/google-company-voodoo-doll-avatar

### Bias Detection and Sentiment Analysis Techniques

Focus of this theme: Research on the technical approaches to detecting bias in text, including machine learning models and natural language processing. I think this section is going to be a lot of previous works (state of the art) that used different machine learning techniques. Why to use technique x over y, and how sentiment analysis is used in political discourse historically. This section is less motivation for the research and more so motivation towards which approaches we chose to take, and why.
Influence on project: Provides insight into the effectiveness of different techniques and justifies the use of advanced models like RoBERTa, the sentiment analysis, the k-clusters, etc.

- K-means clusters/Hierarchical clusters/ DBSCAN
<https://www.ibm.com/topics/unsupervised-learning>
- Examples of unsupervised learning
<https://www.altexsoft.com/blog/unsupervised-machine-learning/>
- Text embedding: word2vec, GloVe, FastText
- what is Bert (lot of good information about BERT including examples)
<https://h2o.ai/wiki/bert/>
- RoBERTa information (updated, newer, better version of BERT)
<https://huggingface.co/docs/transformers/en/model_doc/roberta>

### Data Collection and Preprocessing for Machine Learning

Focus of this theme: Research studies on methods of acquiring and cleaning datasets for machine learning tasks, particularly in the political domain. This is one that I anticipate I am going to need more sources and information on, but this section will highlight why we chose to take what data based on previous research standards/ what worked.
Influence on project: Helps address the trade-offs between web scraping and pre-selected datasets and highlights some of the ethical considerations in data collection. I could also imagine how the question about how to get data when pre-selected and human labeled data is inherently bias, so addressing that concern.

### Evaluation and Validation of Bias Detection Tools

Focus for theme: Studies assessing the accuracy, usability, and ethical concerns of creating a bias detection tools. Additionally, looking at what research has been done to identify themes in bias. What causes bias in general, and are there themes that exists? Do those exist in other fields? Political Science? How does political bias detection differ from other forms of general bias detection.
Influence on project: Informs how to benchmark PolitScope against competitors and address gaps in existing tools. Also introduces a large section of the second part of PolitScope, which is the evaluation and research questions associated to how bias is detected and what builds bias, are there patterns that arise?
