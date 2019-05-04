
![alt text](https://github.com/chenyangzhu/stat154-project2/raw/master/image/Figure_1a_img1_vis.png)

# Cloud Detection with Bancroft Model
### Flying Ramen Pokémon
Chenyang Zhu and Ling Xie, UC Berkeley

## Introduction
In this paper, we perform task on detecting cloud on icy surface. Our dataset is 3 384x384 images with 8 features for each pixels. This work is based on Shi et al. [2018], and we build logistic regression, linear discriminant analysis, quadratic discriminant analysis and random forest.

Apart from using balanced split methods and spatial split methods, we created a new model, called Bancroft model, to extract neighbor information in surrounding pixels. Bancroft Model smooths out pixels around a certain pixel and add the average information to a new feature of this pixel. In this way, we managed to boost the classification accuracy by 1% over traditional shallow random forest (max depth 10-30) algorithm.
