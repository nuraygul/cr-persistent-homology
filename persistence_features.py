
import numpy as np
from ripser import ripser
from persim import PersistenceImager
from scipy.interpolate import interp1d

def compute_diagrams(point_cloud):
    return ripser(point_cloud)['dgms']

def betti_curve(diagrams, max_scale=1.0, resolution=100):
    x_vals = np.linspace(0, max_scale, resolution)
    betti = np.zeros(resolution)
    for b, d in diagrams[1]:
        betti += np.logical_and(x_vals >= b, x_vals <= d)
    return betti

def persistence_image(diagrams):
    pimgr = PersistenceImager()
    pimgr.fit(diagrams[1])
    return pimgr.transform(diagrams[1]).flatten()
