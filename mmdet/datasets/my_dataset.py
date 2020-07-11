from .coco import CocoDataset
from .builder import DATASETS
### IMPORT YOUR DATASET FORMAT AND PASS IT IN MYDATASET FUNC

@DATASETS.register_module
class MyDataset(CocoDataset):

    CLASSES = ('Wheat-Heads') ## ADD ALL YOUR CLASSES
