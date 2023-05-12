# William Flanders

from SDSS_data import retrieve_sdss_spectra
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Fetching data
spectra = retrieve_sdss_spectra()[0]
wavelength = retrieve_sdss_spectra()[1]

# Plotting spectra
def spectra_plot(n):
    fig = plt.figure(figsize=(10, 8))
    n_plots = n

    for i in range(n_plots):
        ax = fig.add_subplot(n_plots, 1, i+1)
        ax.plot(wavelength, spectra[i])
        ax.set_ylabel(r"Flux")
    ax.set_xlabel(r"Wavelength")
    plt.show()

# Calculating the principal components
def compute_evals(n):
    spec_mean = spectra.mean(0)
    n_components = n
    # Using sklearn PCA class to calculate components
    pca = PCA(n_components - 1, svd_solver='randomized')
    pca.fit(spectra)
    pca_comp=np.vstack([spec_mean,pca.components_])
    eigenvals = pca.explained_variance_ratio_
    # Returning evals and evecs
    return eigenvals, pca_comp

# Plotting the principal components
def plot_pca(pca_comp, n):
    fig = plt.figure(figsize=(12,10))
    for j in range(n):
        ax = fig.add_subplot(n, 1, j+1)
        if j == 0:
            ax.set_title(r"Mean")
            ax.plot(wavelength, pca_comp[j])
            ax.set_ylabel(r"Flux")
        elif j == 1:
            ax.set_title(str(j) + r"st Component")
            ax.plot(wavelength, pca_comp[j])
            ax.set_ylabel(r"Flux")
        elif j == 2:
            ax.set_title(str(j) + r"nd Component")
            ax.plot(wavelength, pca_comp[j])
            ax.set_ylabel(r"Flux")
        elif j == 3:
            ax.set_title(str(j) + r"rd Component")
            ax.plot(wavelength, pca_comp[j])
            ax.set_ylabel(r"Flux")
        else:
            ax.set_title(str(j) + r"th Component")
            ax.plot(wavelength, pca_comp[j])
            ax.set_ylabel(r"Flux")
    ax.set_xlabel(r"Wavelength")
    plt.show()


if __name__ == "__main__":
    evals = compute_evals(5)[0]
    pca_comp = compute_evals(5)[1]
    plot_pca(pca_comp, 5)
    spectra_plot(5)