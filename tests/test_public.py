"""Public tests for Lab 05. Hidden tests are harder!"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import lab05 as lab  # noqa: E402

import numpy as np

def test_line():
    x = np.arange(5).reshape(-1, 1)
    assert np.allclose(lab.least_squares(x, 2 * x.ravel() + 3), [3, 2])
