from ultralytics import YOLO
from ultralytics.models.utils.ops import HungarianMatcher

# Load your model
model = YOLO("yolo11n-seg.pt")

# Configure Hungarian matcher parameters
matcher_config = {
    'cost_class': 1.0,    # Cost coefficient for class prediction
    'cost_bbox': 5.0,     # Cost coefficient for bbox prediction
    'cost_giou': 2.0,     # Cost coefficient for giou loss
    'use_focal': True     # Whether to use focal loss for classification
}

# Create the matcher instance
matcher = HungarianMatcher(**matcher_config)

# Set up training with the matcher
model.train(
    data="/work/NASASPaceResearch/hyperspectral_imges/blueberry_labeled_1/data.yaml",
    project='/work/NASASPaceResearch/seaqueue/yolo/util/runs',
    epochs=300,
    imgsz=640,
    matcher=matcher,  # Add the matcher to the training config
    match_type='hungarian'  # Explicitly specify the matching algorithm
)