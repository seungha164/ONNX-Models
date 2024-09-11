import torch
import numpy as np

def toAsciiTensor(str = 'a smile cat', device = 'cuda'):
    # 1. 아스키 코드화
    ascii_codes = np.array([ord(char) for char in str])
    ascii_codes = torch.tensor(ascii_codes)
    # 2. 나머지 '-1'로 채워서, [1,100] 사이즈의 tensor화
    arr = torch.full((1, 100), -1).to(device = device)
    arr[0, :ascii_codes.size(0)] = ascii_codes
    return arr