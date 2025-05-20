from ultralytics import YOLO

# Load a pretrained YOLO11n model
# model = YOLO("yolo11n-seg.pt")
model = YOLO("/work/NASASPaceResearch/seaqueue/yolo/util/runs/train3/weights/best.pt")

# Run inference
# model.predict("/work/NASASPaceResearch/hyperspectral_imges/blueberry_labeled_1/test/images/IMG_0002_rgb_png.rf.38a448e8b2f4599454c7f3375b9d5798.jpg", save=True, imgsz=320, conf=0.1, project='/work/NASASPaceResearch/seaqueue/yolo/util/runs')

model.predict("https://ultralytics.com/images/bus.jpg", save=True, imgsz=320, conf=0.5, project='/work/NASASPaceResearch/seaqueue/yolo/util/runs')