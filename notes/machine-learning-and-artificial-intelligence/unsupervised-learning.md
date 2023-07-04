---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Unsupervised Learning

### What is Unsupervised Learning?

Unsupervised learning is a fundamental paradigm in machine learning where the training data lacks explicit labels or annotations. Unlike supervised learning, where the data is labelled with desired outputs, unsupervised learning algorithms operate on **unlabeled data** - without a "teacher". This characteristic allows the algorithms to explore and discover hidden structures, patterns, or relationships within the data without any prior knowledge or guidance.

#### Typical unsupervised learning tasks are:

* Clustering
* Anomaly Detection
* Novelty Detection
* Association Rule Learning

### Self-supervised Learning

Self-supervised learning relies on the data to provide the supervision necessary for learning, eliminating the need for explicit labels from humans - as this can be time-consuming.

In the self-supervised paradigm, algorithms generate their labels by performing "pretext" tasks, such as predicting the next word in a sentence or reconstructing missing image parts. This approach allows models to effectively utilize vast amounts of unlabeled data, reducing dependence on costly labelled datasets. Following self-supervised pretraining, models develop a robust understanding of data distribution and can be fine-tuned using smaller labelled datasets, a process is known as transfer learning.
