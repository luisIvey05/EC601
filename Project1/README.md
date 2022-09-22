# Photogrammetry: From Images to 3D Point Clouds

## Problem Statement/Applications
Photogrammetry is the art, science, and technology of data acquisition of real-world measurements of physical objects or terrain features from an image or images [1]. The images may be taken from above as an ariel shot overlooking a large-scale land area, terrestrial images capturing a scene from eye level, or images capturing just a single object. The photogrammetry pipeline is a multi-step process that converts a series of images into a 3D model. Some applications include preservation, video games, and autonomous vehicles.

Photogrammetry is revolutionizing archaeology by replacing archaic and slow site mapping methods with faster and newer technologies. The transition to photogrammetry techniques has come at a crucial time where recent weather patterns, rising sea levels, and frequently occurring wildfires have induced the disappearance of ancient ruins[2]. These techniques can easily measure the Earth's surface with highly accurate point clouds that can be used to generate a 3D reconstruction of the terrain.
(https://sites.temple.edu/tudsc/files/2015/10/Screen-Shot-2015-10-14-at-11.44.35-AM.png)
> **Fig 1** Photoscan model of Palmyra’s Tetrapylon 
Due to recent photogrammetry's high-resolution 3D object modeling techniques, many realistic computer games have introduced these models into their virtual environments. The Assassin's Creed series has frequently used photogrammetry to speed production time when creating in-game ancient artifacts and famous landmarks [3]. For example, Assassin's Creed Unity had fully restored the damaged Notre Dame cathedral, which players could experience in-game.
(https://i.guim.co.uk/img/media/d6dec9475aff1a117081a20a25ea67ba98248cff/0_126_3989_2394/master/3989.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=e78ebb13265d96fb7e028c80d27dfdec)
> **Fig 2** Norte Dame cathedral as seen in the game.
Another application of photogrammetry is the use of real-time applications such as localization for autonomous vehicles. Localization is the process of finding objects in space and time relative to other objects [4]. More specifically, the distance between an autonomous vehicle to a vehicle in front of it is calculated based on a photogrammetry scheme. Photogrammetry can also be extended for 3D object detection, tracking, and segmentation in autonomous vehicle applications [5]. 
(https://www.anolytics.ai/wp-content/uploads/2019/06/bg-1024x586.jpg)
> **Fig 3** 3D point cloud for Autonmous Vehicles
## Current Research
### Model-Driven/Classical Approach:
A model-driven/classical approach aims to use a multiview stereo vision procedure to recover the lost depth dimension from the 2D images. This solution requires a multi-step pipeline to transform a series of images into a 3D representation. The pipeline consists of feature extraction, image matching, structure motion/multi-view stereo, depth estimation, dense point cloud, meshing, and texturing. This technique has been extensively investigated, which has inspired many open-sourced libraries to compile various existing algorithms (in an efficient manner) that solve the photogrammetry problem. One of those libraries is Open3D [6] which speeds up production time, has an optimized backend that supports parallelization, has been used in several published research projects, and can create a 3D reconstruction of a scene or object.

Open3D scene reconstruction system takes in RGB-D images and follows three crucial steps to output a mesh model of the scene. The first step builds the geometric surfaces using a few sequenced images. The second step consists of globally aliging fragments to obtain fragment poses and runs a camera calibration function. The final step outputs a mesh model of the scene by integrating the RGB-D images. Open3D also produces the visualization of the mesh model. The pipeline for scene reconstruction has been optimized by using C++ as the backend programming language and OpenMP to parallelize many subtasks. However, the need for multiple images and the process of calibrating the camera being used has led to research in producing data-driven approaches for acquiring 3D point clouds from a single image.
(https://raw.githubusercontent.com/isl-org/Open3D-ML/master/docs/images/getting_started_ml_visualizer.gif)
> ** Fig 4 ** Open3D scene reconstruction

  ### Data-Driven/Current State-Of-The-Art Approaches:
  
Data-driven/current end-to-end training approaches consist of three different core concepts being used for the photogrammetry problem. Parameterization-based 3D reconstruction takes an input image and estimates the object's shape based on prior training shape category data, including multiple object viewpoints [7]. This solution requires the input image to fit into existing shape categories. Template deformation-based 3D reconstruction takes an input image and estimates a deformation field which is applied to a template 3D shape, resulting in the reconstructed 3D model [8]. The residual learning technique simplifies the reconstruction process by nudging the template in small amounts to the desired shape rather than creating the shape from scratch. This process also avoids the constraints of the prior shape category strategy presents. Lastly, point-based methods take 3D points (or an image that is then converted to a 3D representation) and estimate the 3D shape using an unordered set of N (x, y, z) points [9]. Addressing the problem through this approach requires modeling local geometric structures based on points and approximating rotation at the feature level. However, these concepts do not scale for an entire scene. The current state-of-the-art approaches have shifted to exploiting the underlying continuous volumetric of a scene to capture large-scale scenes.

NeRFusion [10] extends the successful NeRF approach (an architecture that uses fully-connected networks to render the continuous volumetric scene using camera rays) for large-scale scene rendering. NeRFusion proposes an input image sequence to predict local radiance fields using direct network inference and globally acquires the scene reconstruction with recurrent neural networks. The result is a real-time sparse scene representation at 22 fps.
(https://cseweb.ucsd.edu/~zex014/papers/2022_nerfusion/icon.png)
> ** Fig 5 ** NeRFusion scene reconstruction
## Conclusion
In conclusion, photogrammetry has shown promising results in archeological preservation, 3D object modeling in video games, and autonmous vehicles using classical model-driven and data-driven state-of-the-art approaches. In researching photogrammetries methods of 3D representation many benifits and constraints come with the two different approaches. In future research, it would be intersting combine both techniques to deliver and more robust but real-time solution to many applications that currently use photogrammetry.

## References
[1] Aber, J. S., Marzolff, I., & Ries, J. B. (2010, May 14). _Photogrammetry_. Small-Format Aerial Photography.<br />
[2] Zaffos, J. (n.d.). _Why the Earth Must Be Mapped_. Anthropology and geography.<br />
[3] Rochefort, S. de. (2021, November 24). _Assassin's creed unity can't help rebuild Notre-Dame, and that's OK_. Polygon.<br />
[4] Hossan, Md, et al. "A new vehicle localization scheme based on combined optical camera communication and photogrammetry." _Mobile Information Systems_ 2018 (2018).<br />
[5] Guo, Yulan, et al. "Deep learning for 3d point clouds: A survey." _IEEE transactions on pattern analysis and machine intelligence_ 43.12 (2020): 4338-4364.<br />
[6] Zhou, Qian-Yi, Jaesik Park, and Vladlen Koltun. "Open3D: A modern library for 3D data processing." arXiv preprint arXiv:1801.09847 (2018).<br />
[7] Y. Ben-Shabat, M. Lindenbaum, and A. Fischer, “3D point cloud classification and segmentation using 3D modified fisher vector representation for convolutional neural networks,” 2017, arXiv: 1711.08241.<br />
[8] J. Yang et al., “Modeling point clouds with self-attention and gumbel subset sampling,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2019, pp. 3318–3327.<br />
[9] S. Lan, R. Yu, G. Yu, and L. S. Davis, “Modeling local geo-metric structure of 3D point clouds using Geo-CNN,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit.,2019, pp. 998–1008.<br />
[10] Zhang, Xiaoshuai, et al. "NeRFusion: Fusing Radiance Fields for Large-Scale Scene Reconstruction." _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_. 2022.<br />

