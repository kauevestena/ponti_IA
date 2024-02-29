from lib import *
import sys

sys.path.append(SEMANTIC_SAM_PATH)

from semantic_sam import prepare_image, plot_results, build_semantic_sam, SemanticSamAutomaticMaskGenerator