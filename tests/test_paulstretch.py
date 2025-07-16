import numpy as np
import soundfile as sf

import paulstretch as ps



def test_call():
    y_in = np.zeros((2,10000), dtype=np.float32)
    sr = 44100
    factor = 10

    y_out = ps.stretch(y_in, sr, factor)

    assert isinstance(y_out, np.ndarray), "Output should be a numpy array"