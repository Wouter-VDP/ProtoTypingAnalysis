import numpy as np
import pandas as pd
        
        
# Function returns true if the point is within the volume specified by arr.
def CheckBorderTPC(x,y,z,array= [[0,0],[0,0],[0,0]]):
    detectorx   =256.35     # In cm
    detectory   =116.5      # Symmetric around 0     
    detectorz   =1036.8
    if (0+array[0][0]) < x < (detectorx-array[0][1]):
            if (-detectory+array[1][0])< y < (detectory-array[1][1]):
                    if (0+array[2][0]) < z < (detectorz-array[2][1]):
                        return True
    return False


# Return true if the point is in the TPC with a tolerance.
def CheckBorderFixed(x,y,z,tolerance=0):
    arr = [[tolerance,tolerance],[tolerance,tolerance],[tolerance,tolerance]]
    return CheckBorderTPC(x,y,z,arr)


# Formatting
def sciNot(x):
    x=float(x)
    return "{:.1f}".format(x)

def sciNot2(x):
    x=float(x)
    return "{:.2f}".format(x)


# efficiency error unweighted
def effErr(teller,noemer):
    return np.sqrt(teller*(1-teller/noemer))/noemer
 
# weighted histogram error  
def hist_bin_uncertainty(data, weights, bin_edges):
    # Bound the data and weights to be within the bin edges
    in_range_index = [idx for idx in range(len(data)) if data[idx] > min(bin_edges) and data[idx] < max(bin_edges)]
    in_range_data = np.asarray([data[idx] for idx in in_range_index])
    in_range_weights = np.asarray([weights[idx] for idx in in_range_index])

    # Bin the weights with the same binning as the data
    bin_index = np.digitize(in_range_data, bin_edges)
    # N.B.: range(1, bin_edges.size) is used instead of set(bin_index) as if
    # there is a gap in the data such that a bin is skipped no index would appear
    # for it in the set
    binned_weights = np.asarray(
        [in_range_weights[np.where(bin_index == idx)[0]] for idx in range(1, len(bin_edges))])
    bin_uncertainties = np.asarray(
        [np.sqrt(np.sum(np.square(w))) for w in binned_weights])
    return bin_uncertainties

