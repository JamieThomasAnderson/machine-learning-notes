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

# Online Learning

### What is Online Learning?

Online machine learning is a technique in the field of computer science where the process of learning evolves as data is received **sequentially**. With each new piece of data, the prediction model gets updated and refines its forecasts for future data. This approach is different from **batch learning** methods where the prediction model is created by analyzing the whole dataset in one go.

Online learning is optimal for systems that must react quickly to a changing data or if lacking computing resources. Additionally, when datasets are too large to fit in a in one machine's main memory, we can load part of the data in batches, learning in steps from each batch in a process called [out-of-core](../machine-learning-concepts/out-of-core.md) learning.

**Learning rate** is a parameter of online learning systems which determines how rapidly the model should adapt to changing data. A high learning rate will lead a system to quickly adapt to new data but will quickly forget past data. A will adapt more slowly, ignoring noise and moving in trends rather than swift adaptations.

The issue with online systems is a degrading performance when abnormal data steers learning in a direction - here, clients can see the downturn in performance. Thus, we usually disable learning via some criteria when performances becomes worse.
