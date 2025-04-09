from django.db import models

# Create your models here.
import torch
import timm
from torch import nn

class InsectModel(nn.Module):
    def __init__(self, num_classes):
        super(InsectModel, self).__init__()
        self.model = timm.create_model('vit_base_patch16_224', pretrained=False, num_classes=num_classes)

    def forward(self, x):
        return self.model(x)

def load_model(weight_path, num_classes):
    model = InsectModel(num_classes)
    model.load_state_dict(torch.load(weight_path, map_location=torch.device('cpu')))
    model.eval()
    return model
