# Simple-Primitives-matching
This is the official code of Zero-shot 3D Model Synthesis via Implicit Diffusion and Primitive Matching.

## Composite Dataset
We provide the download link for our customized dataset, please refer to: [Baidu](https://pan.baidu.com/s/1mLVURfCBo7P3FUALvdeVOQ?pwd=fjxn)

Partial images and text in the dataset:

![image](https://github.com/lym930/Simple-Primitives-matching/blob/main/data/synthetic_dataset/synthetic_dataset.png)

## Dependency
  ```sh
  python==3.7
  numpy==1.21.6
  mayavi==4.8.1
  plyfile==0.9
  scipy==1.7.3
  scikit-image==0.19.3
  PyQt5==5.15.10
  mesh2sdf
  ```
## Implementation
### Preparing mesh files
Our algorithm accepts meshes in `.obj` format, so you may need to use implicit diffusion models (for example, [Imagedream](https://github.com/bytedance/ImageDream)) or [3Ddemo](https://www.tripo3d.ai/) to generate 3D models with mesh format of `.obj`.

### Convert meshes into SDF
Please run: 

```sh
python mesh2sdf_convert.py $location of the mesh file$
```

to generate SDF from meshes. You can also decide the resolution of SDF and whether it is normalized, please refer to [Marching-primitives](https://github.com/FisherYuuri/Marching-Primitives-Python/tree/main) for more details.

### Algorithm Implementation
Please run `main.py` to convert your SDF into a 3D model composed of multiple simple primitives. `main.py` will finally visualize the results and save a model file in `.csv` format, which stores the parameters of each primitive unit. When you have obtained this model file, you can run `vis_primitive.py` to view your 3D model more conveniently.

The visualisation of this code results：

![image]()
  
## Acknowledgements
We would like to thank the developers of [Marching-Primitives](https://github.com/ChirikjianLab/Marching-Primitives) for their open-source contributions, which greatly supported the development of our work. Additionally, we would like to thank the following authors for their open-source contributions.

```sh
@article{wang2023imagedream,
  title={Imagedream: Image-prompt multi-view diffusion for 3d generation},
  author={Wang, Peng and Shi, Yichun},
  journal={arXiv preprint arXiv:2312.02201},
  year={2023}
}
```sh

```sh
@inproceedings{liu2024one,
  title={One-2-3-45++: Fast single image to 3d objects with consistent multi-view generation and 3d diffusion},
  author={Liu, Minghua and Shi, Ruoxi and Chen, Linghao and Zhang, Zhuoyang and Xu, Chao and Wei, Xinyue and Chen, Hansheng and Zeng, Chong and Gu, Jiayuan and Su, Hao},
  booktitle={Proceedings of the IEEE/CVF conference on computer vision and pattern recognition},
  pages={10072--10083},
  year={2024}
}
```

```sh
@article{long2023wonder3d,
  title={Wonder3d: Single image to 3d using cross-domain diffusion},
  author={Long, Xiaoxiao and Guo, Yuan-Chen and Lin, Cheng and Liu, Yuan and Dou, Zhiyang and Liu, Lingjie and Ma, Yuexin and Zhang, Song-Hai and Habermann, Marc and Theobalt, Christian and others},
  journal={arXiv preprint arXiv:2310.15008},
  year={2023}
}
```

```sh
@inproceedings{shi2023mvdream,
  title={MVDream: Multi-view Diffusion for 3D Generation},
  author={Shi, Yichun and Wang, Peng and Ye, Jianglong and Mai, Long and Li, Kejie and Yang, Xiao},
  booktitle={The Twelfth International Conference on Learning Representations},
  year={2023}
}
```

```sh
@article{tochilkin2024triposr,
  title={Triposr: Fast 3d object reconstruction from a single image},
  author={Tochilkin, Dmitry and Pankratz, David and Liu, Zexiang and Huang, Zixuan and Letts, Adam and Li, Yangguang and Liang, Ding and Laforte, Christian and Jampani, Varun and Cao, Yan-Pei},
  journal={arXiv preprint arXiv:2403.02151},
  year={2024}
}
```
