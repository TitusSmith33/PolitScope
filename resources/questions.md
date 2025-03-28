# Key Questions

How do you upload extensions to the app store (for v1.0.0)?
What is the standard level for Chrome extensions?

hypothes.is -- html

mess around with entropy score and maybe only take the really confident embedding score

maybe test with jupiter lab so i can get visualization of outputs from the clustering.

- 2 demensional representation of the data: PCA

The normalization of distances and entropy might be problematic. Using np.max(min_distances) and np.max(entropies) to normalize can be sensitive to outliers. If the scale of the new data's embeddings differs from the training set, the normalization might not work as expected, leading to inaccurate confidence scores.

why look at the whole group when calculating confidence (consider what happens when there is one sentence), vs just calculating a confidence score for each individual sentence.

--hyperparameters

measure success-- how to measure bias without the impact of personal bias -- accuracy of model prediction

TODO:

if we just use the distances from the original sentence, are we really testing PolitScope or are we testing RoBERTa?

for the constants on the confidence level experiment -- how do we measure accuracy??
