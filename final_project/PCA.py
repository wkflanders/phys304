from SDSS_data import retrieve_sdss_spectra
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

spectra = retrieve_sdss_spectra()[0]
wavelength = retrieve_sdss_spectra()[1]

def spectra_plot(n):
    fig = plt.figure(figsize=(10, 8))
    # fig.subplots_adjust(left=0.05, right=0.95, wspace=0.05,
    #                     bottom=0.1, top=0.95, hspace=0.05)

    n_plots = n

    for i in range(n_plots):
        ax = fig.add_subplot(n_plots, 1, i+1)
        ax.plot(wavelength, spectra[i])
        ax.set_ylabel("Flux")
    ax.set_xlabel("Wavelength")
    plt.show()

def compute_evals(n, plot=True):
    spec_mean = spectra.mean(0)
    n_components = n

    pca = PCA(n_components - 1, svd_solver='randomized')
    pca.fit(spectra)
    pca_comp=np.vstack([spec_mean,pca.components_])
    eigenvals = pca.explained_variance_ratio_

    fig = plt.figure(figsize=(12,10))
    if plot is True:
        for j in range(n_components):
            ax = fig.add_subplot(n_components, 1, j+1)
            if j == 0:
                ax.set_title("Mean")
                ax.plot(wavelength, pca_comp[j])
                ax.set_ylabel("Flux")
            elif j == 1:
                ax.set_title(str(j) + "st Component")
                ax.plot(wavelength, pca_comp[j])
                ax.set_ylabel("Flux")
            elif j == 2:
                ax.set_title(str(j) + "nd Component")
                ax.plot(wavelength, pca_comp[j])
                ax.set_ylabel("Flux")
            elif j == 3:
                ax.set_title(str(j) + "rd Component")
                ax.plot(wavelength, pca_comp[j])
                ax.set_ylabel("Flux")
            else:
                ax.set_title(str(j) + "th Component")
                ax.plot(wavelength, pca_comp[j])
                ax.set_ylabel("Flux")
        ax.set_xlabel("Wavelength")
        plt.show()
    return eigenvals

if __name__ == "__main__":
    spectra_plot(5)

def reconstruct(n):
    eigenvals = compute_evals(n, False)
