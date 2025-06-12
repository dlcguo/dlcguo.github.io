---
layout: summary
title: "FreeTimeGS: Free Gaussian Primitives at Anytime and Anywhere for Dynamic Scene Reconstruction"
giscus_comments: true
bib_id: 2506.05348v2
---

### Important Points

#### 1. Higher Degrees of Freedom (4D) Gaussian Primitives

{% include figure.liquid path="/assets/img/summaries/FreeTimeGS/pipeline.webp" width="600px" class="z-depth-1"
caption="FreeTimeGS Pipeline Overview" %}

FreeTimeGS takes a different path from some other recent works. Rather than training a heavy, global deformation field, the authors give each Gaussian primitive with its own simple linear motion function. By only modeling short-range shifts between primitives and the observed scene, this approach sidesteps the ill-posedness of fitting a full warp and keeps optimization both stable and less expensive. Each primitive still learns its spatial position, orientation, scale, velocity, temporal center, duration, opacity, and spherical-harmonic coefficients.

#### 2. 4D Regularization

Optimizing FreeTimeGS with only rendering losses can result in reaching local minima in fast-moving regions, where some primitives become fully opaque which blocks gradient flow to others. To address this, the authors add a regularization term that penalizes high spatial opacity early in training while detaching the temporal opacity from gradients. This helps ensure all primitives remain semi-transparent initially, promoting better gradient propagation which subsequently leads to higher-quality reconstructions in dynamic regions.

#### 3. Periodic Relocation

While 4D regularization improves rendering quality, it often increases the number of primitives required. To maintain a more compact representation, FreeTimeGS implements a periodic relocation strategy where after every fixed number of iterations, low-opacity primitives are moved to areas with high photometric or opacity gradients. This targeted resampling concentrates primitives where they are most needed for more efficient coverage.

### Critique

I would have liked a comparison with the [Shape of Motion](https://arxiv.org/pdf/2407.13764) paper since FreeTimeGS and Shape of Motion are quite similar in assigning linear transformations to individual Gaussians.

### Concluding Thoughts

Despite mentions of relying on per-scene optimization and not supporting relighting, I think this work is promising just from the merit of significantly outperforming other SOTA models.
