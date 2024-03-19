from argparse import ArgumentParser, Namespace

import numpy as np
from ultralytics import YOLO
from ultralytics.engine.results import Results, Boxes

from deep_text_recognition_benchmark.dtrb import DTRB

parser: ArgumentParser
opt: Namespace

plate_detector: YOLO
plate_recognizer: DTRB

image: np.ndarray
results: Results
boxes: Boxes

conf: float
x1: int
y1: int
x2: int
y2: int
current_class: str
plate_image: np.ndarray
text_pred: str
score: float

