import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import auto_increment as ai


def test_auto_increment_sequence():
    ai.BM = 0
    assert ai.auto_increment() == 5300001
    assert ai.auto_increment() == 5300002
