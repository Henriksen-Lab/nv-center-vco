# This is a module that contains a callable
import numpy as np
from os import path
import numpy as np

resources_dir = path.join(path.dirname(__file__), 'resources')
splinePath = resources_dir+"/VCO_interpolated_spline_object.npy"
interpolatedCurve = np.load(
    splinePath, allow_pickle=True)[()]


def voltageToFrequency(voltage):
    '''Returns the frequency outputted for a given voltage based on a linear univariate spline interpolation with S=0.0001'''
    microwaveFrequency = interpolatedCurve(voltage)
    return microwaveFrequency
