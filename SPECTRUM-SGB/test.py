import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS

hdul1 = fits.open('../Svetlio/MILES_library_v9.1_FITS/s0024.fits')
hdul2 = fits.open('../Svetlio/MILES_library_v9.1_FITS/s0013.fits')

data1 = hdul1[0].data
header1 = hdul1[0].header
obj_name1 = header1.get('OBJECT', 'Unknown')

data2 = hdul2[0].data
header2 = hdul2[0].header
obj_name2 = header2.get('OBJECT', 'Unknown')

flux1 = data1[0]
w1 = WCS(header1, naxis = 1)
wavelength1 = w1.wcs_pix2world(np.arange(len(flux1)), 0)[0]

flux2 = data2[0]
w2 = WCS(header2, naxis = 1)
wavelength2 = w2.wcs_pix2world(np.arange(len(flux2)), 0)[0]

fig, axs = plt.subplots(1, 2, figsize=(12, 5))
axs[0].plot(wavelength1, flux1, label = obj_name1)
axs[0].set_title('Normalized Flux')
axs[0].set_xlabel('Wavelength (Å)')
axs[0].set_ylabel('Flux')
axs[0].set_ylim(0, )
axs[0].legend()

axs[1].plot(wavelength2, flux2, c = 'orange', label = obj_name2)
axs[1].set_title('Normalized Flux')
axs[1].set_xlabel('Wavelength (Å)')
axs[1].set_ylabel('Flux')
axs[1].set_ylim(0, )
axs[1].legend()

plt.show()
fig.savefig("spectra.png")