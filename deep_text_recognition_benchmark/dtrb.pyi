from argparse import Namespace

import torch
import torchvision.transforms as transforms

from deep_text_recognition_benchmark.utils import CTCLabelConverter, AttnLabelConverter
from deep_text_recognition_benchmark.model import Model


class DTRB:
    def __init__(self, weights_path: str, opt: Namespace) -> None:
        self.opt: Namespace

        self.converter: CTCLabelConverter | AttnLabelConverter
        self.device: str

    def load_model(self, weights_path: str) -> None:
        self.model: Model | torch.nn.DataParallel

    def predict(self, image) -> list[str, float]:
        transform: transforms.Compose

        image_tensor: torch.Tensor

        length_for_pred: torch.IntTensor
        text_for_pred: torch.LongTensor

        preds: list
        preds_size: torch.IntTensor
        preds_index: int
        preds_str: list

        dashed_line: str
        head: str

        preds_prob: torch.Tensor
        preds_max_prob: torch.Tensor

        img_name: str
        pred: str
        pred_max_prob: torch.Tensor
