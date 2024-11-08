# Introduction Outline for PolitScope

## Introduction to Political Bias

* Definition of political bias: Explain political bias in media (e.g., articles, social media) and its significance in modern discourse.
* Impact of bias on public opinion: Discuss how bias can shape individuals' political views and beliefs.
* Importance of detecting political bias: Need for unbiased information, especially in today’s fragmented media landscape.

## The Problem

Current challenges with political bias detection:

* Detection of bias is often manual and labor-intensive.
* Existing tools may be inaccurate, oversimplified, or too focused on true/false.

The role of dynamic, real-time detection:

* Users often scroll through pages with no real-time feedback.
* Need for dynamic tools that update instantly as users browse through content.

## The Goal of PolitScope

Purpose of PolitScope:

* A tool for dynamically detecting political bias on web pages as users scroll through them.
* Immediate feedback on the political nature of content being read.

Target audience:

* General internet users, particularly younger generations who consume large amounts of online media & young voters (16-25).
* Users interested in understanding political biases they encounter during their online activities -- young people still developing political beliefs need to build their base on unbiased fair information

Real-time, dynamic approach:

* Unlike static tools, PolitScope aims to assess content on the fly, without requiring users to input specific text -- which addresses the issue of "people often don't know the content they encounter is bias"

## Why This Approach?

Growing concern over bias in media:

* Growing mistrust in media sources and increasing political polarization.
* Need for more objective tools that empower users to critically analyze content -- goes back to the point that people often don't know they are being influenced by bias

Interactive and accessible solution:

* Allows users to passively interact with the tool as they browse, making bias detection more accessible, and does the **work** for them.

## Technologies Used

Chrome extension framework:

* Easy to integrate with browsers and widely used for lightweight, interactive tools.

Machine learning models:

* (BERT/RoBERTa **MAYBE**) Pre-trained language models capable of understanding the subtleties in text to determine political bias.
* Unsupervised machine learning
* Supervised machine learning

Sentiment analysis and classification:

* Combining sentiment analysis with classification techniques to assess bias (left, right, neutral).
* Pros and cons of sentiment analysis versus keyword-based detection.

## The Workflow of PolitScope

How PolitScope works:

* Text content from a webpage is dynamically analyzed as the user scrolls.
* PolitScope continuously scans and flags biased language, presenting visual cues like highlights or badges.

User Interaction:

* Minimal effort required from users; tool runs seamlessly as they browse.
* Options for users to click and see the specific bias analysis or explanation.

## Uniqueness and Innovation of PolitScope

Real-time detection:

* Unlike static solutions that require text input, PolitScope works by detecting bias on content as users scroll.
* Makes for seamless integration with the browsing experience:

Adaptable to multiple sources:

* Can be applied to various types of online content, including news articles, social media posts, and blogs.

## Research Questions and Objectives

Key research questions:

* How can we accurately and efficiently detect political bias in real-time on web pages?
* What models and techniques provide the best results for classifying bias in diverse types of content?

Objectives of the project:

* To build and refine PolitScope into a robust, reliable tool.
* To evaluate the effectiveness of various machine learning techniques (e.g., BERT, RoBERTa) in detecting bias across different types of content.
