import pytest
from LebwohlLasher import main

@pytest.mark.parametrize("PROGNAME, ITERATIONS, SIZE, TEMPERATURE,PLOTFLAG,expect", [
    ("LebwohlLasher", 50, 50, 0.5, 0, 1),
    ("LebwohlLasher", 10, 100, 0.5, 1, 1),
    ("LebwohlLasher", 50, 50, 0.5, 0, 1)
])

def test_main(PROGNAME,ITERATIONS, SIZE, TEMPERATURE, PLOTFLAG, expect):
    output = main(PROGNAME,ITERATIONS, SIZE, TEMPERATURE,PLOTFLAG)
    assert output == expect
    

