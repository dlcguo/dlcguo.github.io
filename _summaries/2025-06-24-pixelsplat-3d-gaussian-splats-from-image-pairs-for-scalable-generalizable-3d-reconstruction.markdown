---
layout: summary
title: "pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction"
giscus_comments: true
bib_id: 2312.12337v4
---

### Important Points

#### 1. Adaptive Density Control Revisited

In 3D-GS, Gaussian primitives initialized randomly must move through space to arrive at their final location. During this process, two issues lead to local minima: gradients vanish if the distance to the optimal location exceeds more than a few standard deviations (the paper dubs this as "local support"), and Gaussians require a path where the loss is monotonically decreasing to its final location. Prior 3D-GS required "Adaptive Density Control" to address this problem. 

pixelSplat revisits Adaptive Density Control via a differentiable reparameterization trick. It roughly goes like this:

1. For each pixel, the network outputs logits which are softmaxed into a discrete distribution
   $$
   \phi = [\phi_1, \phi_2, \dots, \phi_Z], 
   \quad
   \phi_z = P(z)
   $$
   over $Z$ predefined depth-bins.

2. Sample
   $$
   z \sim \mathrm{Categorical}(\phi)\,,
   $$
   then recover a continuous depth
   $$
   d = b_z + \delta_z
   $$
   (where \(b_z\) is the bin center and \(\delta_z\) a learned offset), and unproject:
   $$
   \mu = o + d \, d_u
   $$
   with camera origin $o$ and ray direction $d_u$.

3. Instead of a hard spawn/prune, set the Gaussian's opacity to
   $$
   \alpha = \phi_z\,.
   $$
   During backpropagation, by the chain rule:
   $$
   \frac{\partial L}{\partial \phi_z}
   = \frac{\partial L}{\partial \alpha}
     \frac{\partial \alpha}{\partial \phi_z}
   = \frac{\partial L}{\partial \alpha}\,,
   $$
   effectively "reparameterizing" the sampling step and allowing gradients to update $\phi$ directly.

By restructuring Adaptive Density Control into a probabilistic sampling approach combined with the reparameterization trick, PixelSplat generates Gaussians where the loss indicates that more density is needed, and prunes in low-error regions while remaining differentiable.

#### 2. Scale Ambiguity Problem

Most existing datasets for 3D reconstruction provide poses that are computed using structure from-motion (SfM) software. Because SfM reconstructs each scene
only up to scale, different scenes are scaled by individual, arbitrary scale factors. Intuitively, this can be thought of you only ever recovering relative distances; there is no fixed correspondence between units in the 3D reconstruction and units of the real world.

The implication is that a neural network making predictions about the geometry of a scene from a single image cannot predict the depth that matches the poses reconstructed by structure-from-motion. pixelSplat uses a two-view encoder in attempt to resolve scale ambiguity by performing depth estimations.

### Concluding Thoughts

This paper is on the older side but is definitely influential in setting an example of how future works can use probabilistic models in 3D-GS. Since its publishment, a steady flow of follow-up papers has built on and refined its ideas.