from PIL import Image
import requests

from transformers import AutoProcessor, AutoModel
from transformers import SiglipModel, SiglipProcessor

import torch

# model = AutoModel.from_pretrained("google/siglip-base-patch16-224")
# processor = AutoProcessor.from_pretrained("google/siglip-base-patch16-224")


model = SiglipModel.from_pretrained("google/siglip-base-patch16-224")
processor = SiglipProcessor.from_pretrained("google/siglip-base-patch16-224")


url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

candidate_labels = ["2 cats", "2 dogs"]
texts = [f'This is a photo of {label}.' for label in candidate_labels]
inputs = processor(text=texts, images=image, padding="max_length", return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

logits_per_image = outputs.logits_per_image
probs = torch.sigmoid(logits_per_image) # 시그모이드 활성화 함수를 적용한 확률입니다
print(f"{probs[0][0]:.1%} that image 0 is '{candidate_labels[0]}'")

## check lable 
print(candidate_labels)
print(texts)
print(outputs.logits_per_image)
print(torch.sigmoid(outputs.logits_per_image))

## print best_idx candidate and best_idx prob
probs = torch.sigmoid(outputs.logits_per_image)[0]
for label, p in zip(candidate_labels, probs):
    print(label, float(p))

best_idx = probs.argmax().item()
print(best_idx)
print("best:", candidate_labels[best_idx], float(probs[best_idx]))