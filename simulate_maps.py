
import numpy as np

def generate_base_map(points):
    # Base map: identity + quadratic terms
    return points + 0.1 * (points ** 2)

def generate_jet_equiv_map(points, jet_level=2, epsilon=0.05):
    # Construct perturbations that preserve up to jet_level derivatives
    perturbed = generate_base_map(points)
    if jet_level <= 2:
        # Add cubic perturbation to preserve 2-jets
        perturbation = epsilon * (points ** 3)
    elif jet_level == 1:
        # Add quadratic and cubic perturbation (destroys 2-jets)
        perturbation = epsilon * (points ** 2 + points ** 3)
    else:
        # Add linear + higher-order terms (destroys all jets)
        perturbation = epsilon * (points + points ** 2 + points ** 3)
    return perturbed + perturbation
