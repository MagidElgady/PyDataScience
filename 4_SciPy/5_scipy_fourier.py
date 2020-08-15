# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson shows us how to use the fft and ifft functions in scipy to
# obtain a discrete Fourier transform of a real or complex sequence.

# fftpack has the functions we want
from scipy.fftpack import fft, ifft
import numpy as np

# Random array of variables
x = np.array([1, 2, 3, 4])
# Returns discrete Fourier transform of array
y = fft(x)
# Gives us DFT of each element in array
# with real and complex components
print("Discrete Fourier Transform of x:", y)

# Gives us the inverse DFT of each element in array
y1 = ifft(x)
print("Inverse Discrete Fourier Transform of x:", y1)
