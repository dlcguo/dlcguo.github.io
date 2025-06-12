---
layout: page
title: Neural Nets for Recognition
description: a neural network from ground-up to recognize characters
img: /assets/img/projects/nn/nn_cover.webp
importance: 2
category: code
related_publications: false
images:
  slider: true
---

<swiper-container keyboard="true" navigation="true" pagination="true" pagination-clickable="true" pagination-dynamic-bullets="true" rewind="true" style="width: 65%">
    <swiper-slide>{% include figure.liquid loading="eager" path="/assets/img/projects/nn/box_01_list.webp" class="img-fluid rounded z-depth-1" %}</swiper-slide>
    <swiper-slide>{% include figure.liquid loading="eager" path="/assets/img/projects/nn/box_04_deep.webp" class="img-fluid rounded z-depth-1" %}</swiper-slide>
    <swiper-slide>{% include figure.liquid loading="eager" path="/assets/img/projects/nn/box_03_haiku.webp" class="img-fluid rounded z-depth-1" %}</swiper-slide>
    <swiper-slide>{% include figure.liquid loading="eager" path="/assets/img/projects/nn/box_02_letters.webp" class="img-fluid rounded z-depth-1" %}</swiper-slide>
</swiper-container>
<div class="caption">
  Examples of detecting bounding boxes of characters
</div>

This project was for the Fall 2024 iteration of the Computer Vision (16-385) course, meaning the code cannot be made public. The work done can be briefly categorized into 3 parts:

1. Implementing auxiliary functions such as initializing weights and activation functions
2. Implementing forward pass and backpropagation functions
3. Implementing a script that processes an image, detects bounding boxes of characters, and recognizes text using our trained neural network

To keep this page brief, we will touch upon the parts I found more interesting.

## Part 1

First, our initialization function, which takes input size and output size as parameters, utilizes the Xavier initialization function. See the full paper [here](https://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf). Essentially, this is a weight initialization technique that helps with proper convergence during training. The idea is that by keeping the variance of gradients roughly the same across all layers, issues like vanishing or exploding gradients can be avoided.

Our model uses the mini-batch training method. We choose this method since it is balanced in that it has a more smooth and stable convergence than stochastic gradient descent while being faster and less computationally straining than a full batch gradient descent.

## Part 2

There was nothing done substantially different from other implementations of neural networks. However, we do mention that we calculated gradients both using analytical gradients computed from chain rule and using an $$\epsilon$$ offset to calculate gradients numerically with central differences. As imagined, the resulting neural network accuracies were not significantly different.

## Part 3

Finally, extending our model to analyze the text inside images was the most frustrating, albeit not the most difficult part. The main issue is that we have to account for spaces and line breaks. This means that it is complex to translate the characters we detect into text that has spaces and new lines.
The procedure I took to approximate this is creating a threshold for new lines and spaces that uses a ratio of distance between adjacent bounding boxes (for each character) and the size of the bounding boxes.

An additional noteworthy point is that after detecting bounding boxes for the letters, we must apply transformations to the pixels captured in individual bounding boxes to match the shape the model was trained on. This is necessary to ensure proper results from the trained neural network.

One final point we make is that because there is a large variety of ways people handwrite "5" and "S", as well as "O" and "0", the recognition of these characters was particularly prone to misclassification.
