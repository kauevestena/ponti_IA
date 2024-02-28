import sys
from constants import *
from PIL import Image
import torch
from torchvision.utils import draw_bounding_boxes
from torchvision.utils import draw_segmentation_masks
import numpy as np

sys.path.append(lang_sam_path)

from lang_sam import LangSAM

def draw_image_v2(image, masks, boxes, labels, alpha=0.3,colors=['white'],draw_bboxes=False):
    '''
        modified from the original at lang-segment-anything

    '''

    image = image.copy()
    image.flags.writeable = True

    image = torch.from_numpy(image).permute(2, 0, 1)
    if len(boxes) > 0 and draw_bboxes:
        image = draw_bounding_boxes(image, boxes, colors=['red'] * len(boxes), labels=labels, width=2)
    if len(masks) > 0:
        image = draw_segmentation_masks(image, masks=masks, colors=colors * len(masks), alpha=alpha)
    return image.numpy().transpose(1, 2, 0)


def write_detection_img(image_pil, masks, boxes, phrases, outpath,alpha=0.3,binary=False,clip=False):
    image_array = np.asarray(image_pil)

    colors = ['white']

    if binary:
        image_array = np.zeros_like(image_array)
        alpha = 1
    else:
        if clip:
            colors = ['black']
            alpha = 1
            masks = ~masks

    image = draw_image_v2(image_array, masks, boxes, phrases,alpha=alpha,colors=colors)
    image = Image.fromarray(np.uint8(image)).convert("RGB")
    image.save(outpath)
