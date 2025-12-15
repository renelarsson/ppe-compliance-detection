import numpy as np

# Load the cache file
cache_file = "/workspaces/ppe-compliance-detection/data/labels/train.cache"
data = np.load(cache_file, allow_pickle=True)

# Inspect the contents
print(data)