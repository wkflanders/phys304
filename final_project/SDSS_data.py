from astroML.datasets import sdss_corrected_spectra

def retrieve_sdss_spectra():
    # Fetching data set form astroML
    data = sdss_corrected_spectra.fetch_sdss_corrected_spectra()
    # Grabbing spectra from data
    spectra = sdss_corrected_spectra.reconstruct_spectra(data)
    # Grabbing wavelengths from data
    wavelengths = sdss_corrected_spectra.compute_wavelengths(data)

    return spectra, wavelengths