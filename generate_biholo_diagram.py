import numpy as np
import matplotlib.pyplot as plt

# Sample points on ∂B² ⊂ ℝ⁴ (3-sphere)
n_points = 300
z = np.random.randn(n_points, 4)
z /= np.linalg.norm(z, axis=1)[:, None]

# Holomorphic-like embedding: ℝ⁴ → ℝ⁶
def f(x):
    return np.hstack([x, x[0]*x[1], x[2]*x[3]])

X_f = np.array([f(p) for p in z])

# Small biholomorphic transformation Ψ: rotation in ℝ⁶
theta = np.pi / 12
R = np.eye(6)
R[[0, 1], [0, 1]] = [np.cos(theta), np.cos(theta)]
R[0, 1] = -np.sin(theta)
R[1, 0] = np.sin(theta)

X_g = X_f @ R.T

# Plot projections of Mf and Mg
fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(121)
ax1.scatter(X_f[:, 0], X_f[:, 1], alpha=0.5)
ax1.set_title("Projection of $M_f$")

ax2 = fig.add_subplot(122)
ax2.scatter(X_g[:, 0], X_g[:, 1], alpha=0.5)
ax2.set_title("Projection of $M_g = \Psi(M_f)$")

plt.tight_layout()
plt.savefig("persistence_cr_diffeo.png", dpi=300)
