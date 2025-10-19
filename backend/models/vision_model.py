from PIL import Image
#vision model for image classification using resnet18 ,pretrained model

class VisionModel:
   

    def __init__(self, num_classes=5):
        self.num_classes = num_classes
        self.model = None
        self.transform = None

    def _ensure_loaded(self):
        if self.model is not None: #if already model is there skip it
            return
        import torch
        import torch.nn as nn
        import torchvision.models as models
        import torchvision.transforms as transforms
        # pretrained model is used resnet18
        self.model = models.resnet18(pretrained=True)
        self.model.fc = nn.Linear(self.model.fc.in_features, self.num_classes)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                [0.485, 0.456, 0.406],
                [0.229, 0.224, 0.225]
            )
        ])

    def predict(self, image_path):
        try:
            img = Image.open(image_path).convert('RGB')  # to open the image using PIL and ensure it is in RGB format
        except Exception as e:
            return {"error": f"Unable to open image: {e}"}

        self._ensure_loaded()
        import torch

        img_t = self.transform(img).unsqueeze(0)
        with torch.no_grad():
            preds = self.model(img_t)
        return {"predicted_class_id": int(preds.argmax(1).item())}
#predicted class id is returned as output
#image processing for resnet done using resizing,converting to tensor.