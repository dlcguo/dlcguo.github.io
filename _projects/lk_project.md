---
layout: page
title: Lucas-Kanade Video Tracking
description: an implementation of 3 basic tracking algorithms
img: /assets/img/projects/lucas_kanade/lucas_kanade_cover.webp
importance: 1
category: code
related_publications: false
---

This project was for the Fall 2024 iteration of the Computer Vision (16-385) course, meaning the code cannot be made public. The task was essentially to replicate three variants of basic tracking algorithms using concepts covered during lecture: Lucas-Kanade Alignment with Translation, Lucas-Kanade Alignment with Affine Transformation, and Inverse Compositional Alignment with Affine Transformation.

The Lucas-Kanade algorithm is an iterative optimization method for aligning an template image with a new image (current frame). The goal is to find the parameters of a warp $$W(x; p)$$ that minimize the pixel-wise difference between the template and the warped image. This is achieved by solving the following minimization:

$$
L(p) = \sum_x \left[ T(x) - I(W(x; p)) \right]^2
$$

where $$T(x)$$ is the template, $$I(W(x; p))$$ is the warped image, and $$p$$ represents the warp parameters.

The algorithm assumes a close initial estimate of $$p$$ and refines it by computing a small update $$\Delta p$$. With linearization, the relation between the warp and the template can be expressed as a linear system. The solution for $$\Delta p$$ is obtained using:

$$
\Delta p = H^{-1} J^\top b
$$

where

- $$H$$ = Hessian matrix, capturing second-order information about the error
- $$J$$ = Jacobian matrix, representing gradients of the error with respect to $$p$$
- $$b$$ = Error vector, the difference between the template and the warped image

The Inverse Compositional Alignment is an optimization of the Lucas-Kanade method to lower computational cost. It does this by precomputing the Jacobian and Hessian, which are constant when aligning a fixed template to a sequence of frames. The consequence is that we now focus on adjusting the warp parameters $$\Delta p$$ that relate the template $$T$$ to the current image $$I$$. Therefore, we invert the roles of the template and current image (as compared to standard Lucas-Kanade) by solving for how the template $$T$$ maps back to the image $$I$$.

This means that when iteratively updating $$p$$, the inverse compositional method modifies the warp parameters $$\Delta p$$ in the opposite direction as before. The updating equation becomes:

$$
\Delta p = H^{-1} J^\top \left[I(W(x; p)) - T \right]
$$

Our three chosen tracking algorithm variants differ in their flexibility and computational efficiency. The first variant, Lucas-Kanade with Translation, as the name suggests, focuses solely on translational motion by optimizing for $$x$$ and $$y$$ displacements. Because of this simplicity, this version is more computationally efficient than the other two variants. That said, it is therefore limited to scenarios that do not include rotation, scaling, and deformation.

<div class="row mt-3">
  <div class="col-sm-6 mt-3 mt-md-0 mx-auto">
    {% include video.liquid path="/assets/video/projects/lucas_kanade/landing_lk_edit.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
  </div>
</div>
<div class="caption">
  Lucas-Kanade Alignment with Translation on landing video
</div>

In this case, we can observe that the varying dimensions of the landing pad are not accounted for by the bounding box. However, this tracking algorithm is still able to capture the relative location of the target object.

<div class="row mt-3">
  <div class="col-sm-6 mt-3 mt-md-0 mx-auto">
    {% include video.liquid path="/assets/video/projects/lucas_kanade/car2_lk_edit.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
  </div>
</div>
<div class="caption">
  Lucas-Kanade Alignment with Translation on car2 video
</div>

We observe that the translation-based algorithm does properly track the target car. Hold this in memory--we will see an unexpected result when tracking the same car using the remaining variants.

In contrast, Lucas-Kanade with Affine Transformation extends the model to account for more complex motions including rotation, scaling, and shearing. That is to say, _affine transformations_. Our implementation now optimizes six parameters to do so, offering greater accuracy/adaptability in aligning objects at the cost of increased computational complexity.

<div class="row mt-3">
  <div class="col-sm-6 mt-3 mt-md-0 mx-auto">
    {% include video.liquid path="/assets/video/projects/lucas_kanade/landing_lk_affine_edit.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
  </div>
</div>
<div class="caption">
  Lucas-Kanade Alignment with Affine Transformation on landing video
</div>

With the same landing video, we can see that our implementation is now able to properly adjust to the various sizes of the landing box.

<div class="row mt-3">
  <div class="col-sm-6 mt-3 mt-md-0 mx-auto">
    {% include video.liquid path="/assets/video/projects/lucas_kanade/car2_lk_affine_edit.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
  </div>
</div>
<div class="caption">
  Lucas-Kanade Alignment with Affine Transformation on car2 video
</div>

As mentioned prior, we see the surprising result that the more complex Lucas-Kanade algorithm is unable to properly track what the simpler version could.
In particular, the affine transformation algorithm completely degenerates after the car is temporarily blocked by a traffic light. The reason is because once the target object is blocked, the computed residuals used for updating parameters become invalid, causing the warp matrix to diverge.

Finally, we move on to the Inverse Compositional Alignment with Affine Transformation. We can essentially think of this algorithm as a weaker version of the standard affine Lucas-Kanade method. We are still able to handle affine transformations, albeit to less accuracy, while having less per-iteration computational overhead.

<div class="row mt-3">
  <div class="col-sm mt-3 mt-md-0">
    {% include video.liquid path="/assets/video/projects/lucas_kanade/car1_lk_affine_edit.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
  </div>
    <div class="col-sm mt-3 mt-md-0">
    {% include video.liquid path="/assets/video/projects/lucas_kanade/car1_ic_affine_edit.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
  </div>
</div>
<div class="caption">
  Lucas-Kanade Alignment with Affine Transformation on car1 video (left), Inverse Compositional Alignment with Affine Transformation on car1 video (right)
</div>

The cost of decreasing computational complexity can be seen here. After the target car passes the bridge (which creates a brightness change), the more complex tracking algorithm on the left is able to continue tracking the car whereas the more efficient algorithm on the right fails.

Overall, I had fun with this programming as it was my first experience with video tracking. While the end results were not perfect, they were more than satisfactory given the relatively basic nature of the algorithms.
