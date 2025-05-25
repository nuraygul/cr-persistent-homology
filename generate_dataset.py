
import numpy as np
from simulate_maps import generate_base_map, generate_jet_equiv_map

def sample_unit_sphere(n_samples=500, dim=3):
    X = np.random.randn(n_samples, dim)
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    return X

def generate_dataset(n_samples_per_class=50):
    data, labels = [], []
    for _ in range(n_samples_per_class):
        base = sample_unit_sphere()
        fX = generate_base_map(base)
        for jet_level, label in zip([2, 1, 0], ['A', 'B', 'C']):
            gX = generate_jet_equiv_map(base, jet_level=jet_level)
            data.append((fX, gX))
            labels.append(label)
    return data, labels
