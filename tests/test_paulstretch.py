from pathlib import Path

import pytest

import numpy as np
import soundfile as sf

import paulstretch as ps



audio_files = Path("tests/audio").glob("*")
stretch_factors = (0.23, 1, 11, 336.2)
data_types = ("float64", "float32")

    
def test_call():
    ps.stretch(y=np.zeros((2,10000)), sr=48000, stretch_factor=10)


@pytest.mark.parametrize("stretch_factor", stretch_factors)
@pytest.mark.parametrize("data_type", data_types)
@pytest.mark.parametrize("audio_file", audio_files)
def test_stretch(audio_file, data_type, stretch_factor):
    
    y, sr = sf.read(audio_file, dtype=data_type)
    
    y_out = ps.stretch(y=y, sr=sr, stretch_factor=stretch_factor)

    assert isinstance(y_out, np.ndarray), "Output should be a numpy array"
    assert y_out.dtype == y.dtype, "Data type of output should the be same as input"