# ONNX-Models
Converted ONNX Model Zoo.

<img width="1280" src="./overview.png">

ONNX(Open Neural Network Exhange) is an open format built to represent machine learning models.

# How to use

Please review the model zoo, and if you locate the desired ONNX model, download it from the provided Google Drive link and integrate it into your project.

# Image Restoration

### MIRNetv2
- constrast enhancement

    <img width="300" src="./projects/mirnetv2/disney01.png"> 
    <img width="300" src="./projects/mirnetv2/disney01_result.png"> 
- super resolution

    <img width="300" src="./projects/mirnetv2/mirnet_sp.jpg"> 
    <img width="300" src="./projects/mirnetv2/mirnet_sp_result.png"> 

| Name | Size | Output | Original Project | License  | Year | Conversion Script | onnx  | onnx quantization |
| ------------- | ------------- | ------------- | ------------- |------------- |------------- | -- | -- | -- |
| MIRNetv2ContrastEnhancement   |   256 x 256  |   Image(RGB 256x256)    |   [swz30/MIRNetv2](https://github.com/swz30/MIRNetv2)  | [ACADEMIC PUBLIC LICENSE](https://github.com/swz30/MIRNetv2/blob/main/LICENSE.md)  |2022| [jupyter notebook](./scripts/mirnetv2_onnx.ipynb) | [onnx model](./onnx_models/mirnetv2.onnx) | [onnx 양자화 model](./onnx_models/mirntev2_quant.onnx) |
| MIRNetv2_super_resolution   |   512 x 512  |   Image(RGB 512x512)    |   [swz30/MIRNetv2](https://github.com/swz30/MIRNetv2)  | [ACADEMIC PUBLIC LICENSE](https://github.com/swz30/MIRNetv2/blob/main/LICENSE.md)  |2022| [jupyter notebook](./scripts/mirnetv2_onnx.ipynb) | [onnx model](./onnx_models/mirnetv2/mirnetv2_sp.onnx) | [onnx 양자화 model](./onnx_models/mirnetv2/mirnetv2_sp_quant.onnx) |

### IS-Net
- Highly Accurate Dichotomous Image Segmentation

    <img width="300" src="./projects/isnet/original.jpg"> 
    <img width="300" src="./projects/isnet/result.png"> 

|   Name    |   Input Size    | Original Project    |   License | Year  | Conversion Scipt  |
|-|-|-|-|-|-|
|   [IS-Net](https://drive.google.com/drive/folders/1o5ph5eXhY0s7SCDJSSQNYa6WNOMH9PP8?usp=sharing)  |  1024 x 1024 |    [xuebinqin/DIS](https://github.com/xuebinqin/DIS) | [Apache](https://github.com/xuebinqin/DIS/blob/main/LICENSE.md) |   2022    |  [jupyter notebook](./projects/isnet/conversion_isnet.ipynb)|

### BisNet v1 & v2
- Image Segmentation

    <img width="300" src="./projects/bisenet/origin.jpg"> 
    <img width="300" src="./projects/bisenet/result.png"> 
- Face parsing

    <img width="300" src="./projects/face-parsing/origin.png"> 
    <img width="300" src="./projects/face-parsing/result.png"> 

|   Name    |   Input Size    | Original Project    |   License | Year  | Conversion Scipt  |
|-|-|-|-|-|-|
|   [BiSeNet](https://drive.google.com/drive/folders/1b1FAQpIKLucqdLd8X4XCSI-5mT4hcNR5?usp=sharing)  |  512 x 512 |    [CoinCheung/BiSeNet](https://github.com/CoinCheung/BiSeNet) | [MIT](https://github.com/CoinCheung/BiSeNet/blob/master/LICENSE) |   2018(v1) / 2020(v2)    |  [jupyter notebook](./projects/bisenet/conversion_bisenet.ipynb)|
|   [face-parsing](https://drive.google.com/drive/folders/117I6WXaFmVx_6v-GphBVBIMXg2zF-Mcm?usp=sharing)    | 512 x 512 |   [zllrunning/face-parsing.PyTorch](https://github.com/zllrunning/face-parsing.PyTorch?tab=readme-ov-file)    | [MIT](https://github.com/zllrunning/face-parsing.PyTorch?tab=MIT-1-ov-file#readme)    | 2019  | [jupyter notebook](./projects/face-parsing/conversion_faceparsing.ipynb)

# Thanks

Images were taken from Disney images. <br>
My project was inspired by [CoreML-Models](https://github.com/john-rocky/CoreML-Models/blob/master/README.md#mirnetv2) project