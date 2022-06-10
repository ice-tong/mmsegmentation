_base_ = [
    '../_base_/models/twins_pcpvt-s_fpn.py', '../_base_/datasets/ade20k.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]
crop_size = (512, 512)
preprocess_cfg = dict(size=crop_size)
model = dict(preprocess_cfg=preprocess_cfg)
optimizer = dict(_delete_=True, type='AdamW', lr=0.0001, weight_decay=0.0001)
