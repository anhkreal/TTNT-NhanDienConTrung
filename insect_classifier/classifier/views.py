from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ImageUploadForm
from .models import load_model
import torch
import cv2
import numpy as np
from albumentations import Compose, Resize
from albumentations.pytorch import ToTensorV2
from PIL import Image

# Load class map (adjusted to match index 0-based model output)
with open("./classes.txt", "r") as f:
    class_map = {}
    for line in f:
        parts = line.strip().split(maxsplit=1)
        if len(parts) == 2:
            class_idx = int(parts[0]) - 1  # subtract 1 to make it zero-based
            class_name = parts[1]
            class_map[class_idx] = class_name

model = load_model("./vit_best.pth", num_classes=len(class_map))

def transform_image(image):
    transform = Compose([Resize(224, 224), ToTensorV2()])
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR).astype(np.float32) / 255.0
    transformed = transform(image=image)
    return transformed['image'].unsqueeze(0)


def predict_view(request):
    label = None
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image.open(form.cleaned_data['image']).convert("RGB")
            input_tensor = transform_image(image)
            with torch.no_grad():
                output = model(input_tensor)
                pred = torch.argmax(output, dim=1).item()
                label = class_map.get(pred, "Không xác định")
    else:
        form = ImageUploadForm()
    return render(request, 'classifier/predict.html', {'form': form, 'label': label})
