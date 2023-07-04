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

# Batch Learning

### **What is Batch Learning?**

Batch learning involves training learning systems using all the available data without the ability to develop incrementally. These methods require substantial computing resources and are typically trained offline before being deployed into production, a process known as offline learning. Since the model does not continue learning after the initial training, its performance gradually deteriorates as the surrounding environment evolves. This phenomenon, referred to as **model rot**, can be mitigated by regularly retraining the model.&#x20;

For instance, even a model trained to classify pictures of cats and dogs may require periodic retraining. This need arises not due to overnight mutations in cats and dogs but due to changes in cameras, image formats, sharpness, brightness, and size ratios. Keeping up with these variations ensures that the model remains effective and adaptable to the evolving image data.
