from astroML.datasets import sdss_corrected_spectra

def retrieve_sdss_spectra():

    data = sdss_corrected_spectra.fetch_sdss_corrected_spectra()
    spectra = sdss_corrected_spectra.reconstruct_spectra(data)
    wavelengths = sdss_corrected_spectra.compute_wavelengths(data)

    return spectra, wavelengths