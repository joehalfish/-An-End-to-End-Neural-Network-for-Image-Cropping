# -An-End-to-End-Neural-Network-for-Image-Cropping
文章：An-End-to-End-Neural-Network-for-Image-Cropping

pdf链接：https://arxiv.org/abs/1907.01432?context=cs.CV

本文核心在于两部分：

（1）从给定的图中找出注意力区域（蓝色框）

（2）然后从锚定区域中获得具有最高美学得分的美学区域（黄色框）

修改参数在config.py文件中，可修改的参数：

（1）scale： 224， 384， 512三种规模

（2）ratio：square or not

修改后对应的权重参数存在于文件weight中

box_results中存放是的有标记框的图片

crop_results中存放的是裁剪后的图片


代码运行步骤：

（1）修改好参数

（2）运行demo.py文件： python demo.py 图片文件夹路径
例如 python demo.py images
