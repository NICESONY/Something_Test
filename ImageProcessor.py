from PIL import Image
import requests
from transformers import AutoProcessor, AutoModel
import torch

model = AutoModel.from_pretrained("google/siglip-base-patch16-224")
processor = AutoProcessor.from_pretrained("google/siglip-base-patch16-224")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(images=image, return_tensors="pt")

with torch.no_grad():
    image_features = model.get_image_features(**inputs)

print(image_features.shape)
print(image_features)
# print(outputs.image_embeds)
# print(outputs.image_embeds.shape)
#print()