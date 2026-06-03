import numpy as np
import sys

filename = "./tests/integration_test_20s.bin"
data = np.fromfile(filename, dtype=np.int8)
print(f"File size: {len(data)} bytes")
if len(data) > 0:
    print(f"Mean: {np.mean(data)}")
    print(f"Std: {np.std(data)}")
    print(f"Max: {np.max(data)}")
    print(f"Min: {np.min(data)}")
    # Interleaved I/Q
    I = data[0::2]
    Q = data[1::2]
    print(f"I mean: {np.mean(I)}, std: {np.std(I)}")
    print(f"Q mean: {np.mean(Q)}, std: {np.std(Q)}")
