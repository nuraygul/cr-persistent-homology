
# Jet Equivalence and Persistent Homology in CR Geometry

This repository contains the Python code used in the experiments for the paper:

**"Classification of CR Images via Jet Equivalence Using Persistent Homology"**  



## Overview

The code simulates holomorphic maps from the unit ball $\mathbb{B}^n \subset \mathbb{C}^n$, generates CR boundary images, and analyzes their topological structure using persistent homology. It includes:

- Jet-level perturbation of holomorphic maps (2-jet, 1-jet, 0-jet)
- Topological feature extraction via persistent homology
- Feature conversion: Persistence Images and Betti curves
- Supervised classification using SVM based on topological signatures


## File Structure

| File | Description |
|------|-------------|
| `simulate_maps.py` | Generates holomorphic maps with controlled jet-level agreement |
| `generate_dataset.py` | Builds labeled dataset of CR image pairs for jet classes A, B, C |
| `persistence_features.py` | Computes persistence diagrams and extracts PH features |
| `classify_jet_structures.py` | Trains and evaluates a classifier to distinguish jet levels |


## Usage

1. **Install required libraries**:
   ```bash
   pip install numpy matplotlib ripser persim scikit-learn
   ```

2. **Run classification pipeline**:
   ```bash
   python classify_jet_structures.py
   ```

   This script:
   - Generates a dataset with three jet classes
   - Extracts topological features (persistence images, Betti curves)
   - Trains an SVM classifier
   - Prints accuracy and classification report


## Example Output

```
              precision    recall  f1-score   support

           A       0.92      0.94      0.93        30
           B       0.90      0.88      0.89        30
           C       0.93      0.92      0.92        30

    accuracy                           0.91        90
```

##  Citation

If you use this code in your research, please cite the associated paper:

> (2025). *Classification of CR Images via Jet Equivalence Using Persistent Homology*. Sakarya University Journal of Science (in review).

---

## Contact

For questions or collaboration:  ...@...
