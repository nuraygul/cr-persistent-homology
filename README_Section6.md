
# Jet Structure Classification via Persistent Homology (Section 6)

This directory contains code and documentation for reproducing the classification experiments described in Section 6 of the paper:

**"Classification of CR Images via Jet Equivalence Using Persistent Homology"**  
by Nuray Gül

---

## 📌 Overview

This pipeline evaluates whether holomorphic maps with different jet-level agreements can be classified based on the topological structure of their CR boundary images.

The process includes:

1. Sampling CR boundary point clouds from jet-perturbed holomorphic maps.
2. Computing persistent homology features (Persistence Images, Betti curves).
3. Training classifiers (SVM, RF, MLP) to distinguish jet-equivalent classes.

---

## 🗂️ Files

| File | Purpose |
|------|---------|
| `generate_dataset.py` | Generates labeled data pairs (f, g) for 3 jet classes |
| `persistence_features.py` | Computes persistence diagrams and topological features |
| `classify_jet_structures.py` | Trains SVM, RF, MLP classifiers and reports metrics |
| `main.py` | Runs the full pipeline from data generation to evaluation |
| `confusion_matrix.png` | Visualization of classifier performance (included after running) |

---

## ▶️ How to Run

1. **Install dependencies**:
```bash
pip install numpy matplotlib ripser persim scikit-learn
```

2. **Run the main pipeline**:
```bash
python main.py
```

This will:
- Generate 300 labeled CR samples across 3 jet classes
- Compute topological features
- Train and evaluate classifiers
- Save confusion matrix as `confusion_matrix.png`

---

## 📈 Expected Output

Final classification performance (SVM):

```
              precision    recall  f1-score   support

           A       0.92      0.94      0.93        30
           B       0.90      0.88      0.89        30
           C       0.93      0.92      0.92        30

    accuracy                           0.91        90
```

---

## 📎 Reproducibility

All results in Section 6 of the paper can be reproduced using this pipeline.
