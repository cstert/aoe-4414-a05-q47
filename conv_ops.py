# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
# Determines output shape and operation count of a convolution layer
# Parameters:
# c_in: input channel count
# h_in: input height count
# w_in: input width count
# n_filt: number of filters in the convolution layer
# h_filt: filter height count
# w_filt: filter width count
# s: stride of convolution filters
# p: amount of padding on each of the four input map slides

# Output:
# Produces output channel count, output height count, output width count, number of additions performed, number of multiplications performed, and number of divisions performed
#
# Written by Celia Sterthous
# Other contributors: None
#
# See the LICENSE file for the license.
# import Python modules
import math 
import sys # argv

# parse script arguments
if len(sys.argv)==9:
    c_in = int(sys.argv[1])
    h_in = int(sys.argv[2])
    w_in = int(sys.argv[3])
    n_filt = int(sys.argv[4])
    h_filt = int(sys.argv[5])
    w_filt = int(sys.argv[6])
    s = int(sys.argv[7])
    p = int(sys.argv[8])
else:
 print(\
 'Usage: '\
 'python3 arg1 arg2 ...'\
 )
 exit()
# write script below this line
h_out = (h_in-h_filt+2*p)/s+1
w_out = (w_in-w_filt+2*p)/s+1
c_out = n_filt
mpf = c_in*h_filt*w_filt
muls = mpf*h_out*w_out*n_filt
adds = muls
divs = 0

# Print the results
print(int(c_out))  # Output channel count
print(int(h_out))  # Output height count
print(int(w_out))  # Output width count
print(int(adds))   # Number of additions performed
print(int(muls))   # Number of multiplications performed
print(int(divs))   # Number of divisions performed