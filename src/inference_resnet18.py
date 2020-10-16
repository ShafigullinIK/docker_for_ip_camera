import torch, albumentations as A
from albumentations.pytorch import ToTensorV2


class Predict:
    def __init__(self, thresh, path_to_model):
        """
            thresh: float - порог для классификации
            path_to_model: str - путь до модели.pth
        """
        self.thresh = thresh
        self.model = Predict.__load_model(path_to_model).to('cpu')
        self.transform = Predict.__transform()

    def predict(self, image):
        image = self.transform(image=image)["image"]
        image = image.unsqueeze(0)
        self.model.eval()
        with torch.no_grad():
            image = image.to('cpu', non_blocking=False)
            output = self.model(image)
            predictions = torch.sigmoid(output).data.cpu().numpy()
        return 'open' if predictions >= self.thresh else 'close'

    @staticmethod
    def __transform():
        val_transform = A.Compose(
        [
            A.Resize(224, 224),
            A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
            ToTensorV2()
        ])

        return val_transform


    @staticmethod
    def __load_model(path):
        return torch.load(path, map_location=torch.device('cpu'))
