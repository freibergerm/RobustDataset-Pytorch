from torchvision import transforms
from torchvision.datasets import FashionMNIST
from io_robust_dataset import IORobustDataset

class IORobustFashionMNISTDataset(IORobustDataset, FashionMNIST):
    pass

if __name__ == '__main__':

    train_set = IORobustFashionMNISTDataset(
       root='./data/FashionMNIST',
       train=True,
       download=True,
       transform=transforms.ToTensor())

