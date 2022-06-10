_base_ = [
    '../_base_/models/pspnet_r50-d8.py', '../_base_/datasets/cityscapes.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]
crop_size = (512, 1024)
preprocess_cfg = dict(size=crop_size)
model = dict(
    preprocess_cfg=preprocess_cfg,
    pretrained='torchvision://resnet50',
    backbone=dict(type='ResNet', dilations=(1, 1, 2, 4), strides=(1, 2, 2, 2)))
