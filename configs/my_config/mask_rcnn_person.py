# The new config inherits a base config to highlight the necessary modification
_base_ = '../mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('person',)
data = dict(
    train=dict(
        img_prefix='balloon/train/',
        classes=classes,
        ann_file='/Users/hainguyen/Documents/deep_learning_projects/open-mmlab/data/annotations_coco_format/instances_default.json'),
    val=dict(
        # unnote if running local
        # img_prefix='/Users/hainguyen/Documents/deep_learning_projects/open-mmlab/data/frame_data_2',

        # unnote if run on colab
        img_prefix = '/content/drive/Shareddrives/Giang/HaiNguyen/UET_AI_Lab/frame_data_2',
        classes=classes,
        
        # unnote if run on colab
        ann_file='/content/drive/Shareddrives/Giang/HaiNguyen/UET_AI_Lab/annotations_coco_format/instances_default.json'),
    test=dict(
        # img_prefix='/Users/hainguyen/Documents/deep_learning_projects/open-mmlab/data/frame_data_2',
        # unnote if run on colab
        img_prefix = '/content/drive/Shareddrives/Giang/HaiNguyen/UET_AI_Lab/frame_data_2',
        classes=classes,
        # unnote if running local
        # ann_file='/Users/hainguyen/Documents/deep_learning_projects/open-mmlab/data/annotations_coco_format/instances_default.json'))
        ann_file='/content/drive/Shareddrives/Giang/HaiNguyen/UET_AI_Lab/annotations_coco_format/instances_default.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'