from .coco import CocoDataset
from .xml_style import XMLDataset
### IMPORT YOUR DATASET FORMAT AND PASS IT IN MYDATASET FUNC

@DATASETS.register_module
class MyDataset(CocoDataset):

    CLASSES = ('Wheat-Heads') ## ADD ALL YOUR CLASSES
