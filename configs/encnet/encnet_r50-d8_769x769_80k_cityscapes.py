_base_ = [
    '../_base_/models/encnet_r50-d8.py',
    '../_base_/datasets/cityscapes_769x769.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_80k.py'
]
crop_size = (769, 769)
preprocess_cfg = dict(size=crop_size)
model = dict(
    preprocess_cfg=preprocess_cfg,
    decode_head=dict(align_corners=True),
    auxiliary_head=dict(align_corners=True),
    test_cfg=dict(mode='slide', crop_size=(769, 769), stride=(513, 513)))
