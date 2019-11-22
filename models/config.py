import os
class Config:

    def __init__(self):

        self.scale = 224   # 224,384,512
        self.ratio = False
        self.gamma = 3.0
        self.theta = 0.01

        self.model = self.set_model()
        # self.model = 'weights/model_h5'

        self.draw = False
        self.crop = True
        self.log = True

        self.pic_extend = ('jpg', 'png', 'jpeg', 'bmp')

        self.image_path = 'test'
        self.log_path = 'logs'
        self.log_file = os.path.join(self.log_path, 'log.txt')
        self.box_out_path = 'box_results'
        self.crop_out_path = 'h5_test_crop_results'

        self.saliency_box_color = 'blue'       # 显着框
        self.aesthetics_box_color = 'yellow'   # 美学

    def set_model(self):
        path_base = 'weights/model_'
        path_ext = '.h5'
        path_scale = str(self.scale)
        path_ratio = 'square' if self.ratio else ''
        return path_base + path_ratio + '_' + path_scale + path_ext
