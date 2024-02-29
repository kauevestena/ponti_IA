from lib import *
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry

sam = sam_model_registry['vit_h']()
