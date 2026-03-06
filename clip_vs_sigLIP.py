from PIL import Image
import requests
from transformers import AutoProcessor, AutoModel
from transformers import SiglipModel, SiglipProcessor
import torch
import torch
import clip
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"


# siglip

# model = AutoModel.from_pretrained("google/siglip-base-patch16-224")
# processor = AutoProcessor.from_pretrained("google/siglip-base-patch16-224")


siglip_model = SiglipModel.from_pretrained("google/siglip-base-patch16-224")
processor = SiglipProcessor.from_pretrained("google/siglip-base-patch16-224")


# url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open("/home/son/SON/CLIP/data/dog.jpeg")

candidate_labels = ["a diagram", "a dog", "a cat"]
texts = [f'This is a photo of {label}.' for label in candidate_labels]
inputs = processor(text=texts, images=image, padding="max_length", return_tensors="pt")

with torch.no_grad():
    outputs = siglip_model(**inputs)

logits_per_image = outputs.logits_per_image
siglip_probs = torch.sigmoid(logits_per_image) # 시그모이드 활성화 함수를 적용한 확률입니다
# print(f"{siglip_probs[0][0]:.1%} that image 0 is '{candidate_labels[0]}'")
print("SigLIP Label probs:", siglip_probs)


## clip

device = "cuda" if torch.cuda.is_available() else "cpu"
clip_model, preprocess = clip.load("ViT-B/32", device=device)

image = preprocess(Image.open("/home/son/SON/CLIP/data/dog.jpeg")).unsqueeze(0).to(device)
text = clip.tokenize(["a diagram", "a dog", "a cat"]).to(device)

with torch.no_grad():
    image_features = clip_model.encode_image(image)
    text_features = clip_model.encode_text(text)
    
    logits_per_image, logits_per_text = clip_model(image, text)
    clip_probs = logits_per_image.softmax(dim=-1).cpu().numpy()

print("CLIP Label probs:", clip_probs)  