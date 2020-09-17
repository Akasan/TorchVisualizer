import torch


class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, data, labels, transform=None):
        self.transform = transform
        self.data = data
        self.labels = labels

    def __len__(self):
        return self.data.size(0)

    def __getitem__(self, idx):
        data = self.data[idx]
        label = self.labels[idx]

        if self.transform is not None:
            data = self.transform(data)

        return data, label

    def size(self):
        return self.data.size()