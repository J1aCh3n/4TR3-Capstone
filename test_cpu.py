import torch

if (torch.cuda.is_available()):
    print("avaiable")
else:
    print("false")