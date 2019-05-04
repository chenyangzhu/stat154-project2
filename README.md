
![alt text](https://github.com/chenyangzhu/stat154-project2/raw/master/image/Figure_1a_img1_vis.png)

# Cloud Detection with Bancroft Model
### Flying Ramen Pokémon
Chenyang Zhu and Ling Xie, UC Berkeley

## Introduction
In this paper, we perform task on detecting cloud on icy surface. Our dataset is 3 384x384 images with 8 features for each pixels. This work is based on Shi et al. [2018], and we build logistic regression, linear discriminant analysis, quadratic discriminant analysis and random forest.

Apart from using balanced split methods and spatial split methods, we created a new model, called Bancroft model, to extract neighbor information in surrounding pixels. Bancroft Model smooths out pixels around a certain pixel and add the average information to a new feature of this pixel. In this way, we managed to boost the classification accuracy by 1% over traditional shallow random forest (max depth 10-30) algorithm.

## Repository Introduction

In this repository, we uploaded the codes used to generate the beautiful pictures in our paper. You can easily clone this repository by using
```
git clone https://github.com/chenyangzhu/stat154-project2

cd stat154-project2
jupyter-notebook
```

The structure of this repository is as follows.
```
├── code
     ├── all_codes.py
     ├── CVGeneric.py
     └── detail_explanation.ipynb
├── data
    ├── im1.csv
    ├── im2.csv
    └── img3.csv
├── image
    ├── Figure_1a_img1_vis.png
    ...
    └── Figure_11b_feature_importance.png
```
We store all the codes in `codes` file, all the data we used in `data` and all the beautiful pictures in `image`.
You can also see a detailed tutorial in the `detail_explanation.ipynb` file.


## Major Results

We apply four common classification algorithms to the detection problem and the results are shown in the following charts.

|                     | Log-reg  | Log-reg | LDA      | LDA     | QDA      | QDA     | Rand-forest | Rand-forest |
|---------------------|----------|---------|----------|---------|----------|---------|-------------|-------------|
| Split method        | balanced | spatial | balanced | spatial | balanced | spatial | balanced    | spatial     |
| time                | 8.1s     | 8.1s    | 2.6s     | 2.6s    | 1.0s     | 1.0s    | 283s        | 283s        |
| Validation Accuracy | 0.8703   | 0.9025  | 0.8722   | 0.8732  | 0.8732   | 0.8359  | 0.9534      | 0.9358      |
| Test Accuracy       | 0.8911   | 0.9220  | 0.8990   | 0.9271  | 0.9063   | 0.9120  | 0.9450      | 0.9300      |

We use ROC Curve, F1 score and log-loss function to show that the best algorithm is random forest, we then tune the random forest algorithm. The result is,

| CV Method       | Min Samples Split | Tree Number | Val. Acc. | Val. All. | Max Depth |
|-----------------|-------------------|-------------|-----------|-----------|-----------|
| Balanced Method | 300               | 200         | 30        | 0.9424    | 0.9526    |
| Spatial Method  | 300               | 50          | 10        | 0.8980    | 0.9103    |

Finally, we apply the Bancroft method, and we show that Bancroft model has the best classification result.

![alt text](https://github.com/chenyangzhu/stat154-project2/raw/master/image/Figure_11a_new_feature_vis.png)

## Contact

Ling Xie,  xieling {at} berkeley {dot} edu

Chenyang Zhu, chenyang {dot} zhu {at} berkeley {dot} edu
