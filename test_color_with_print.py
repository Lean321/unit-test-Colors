from colors import fcolor_print
import io
import sys

def test_fcolor_print():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    fcolor_print('quit')                                     # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.
    assert capturedOutput.getvalue() == 'bye\n'
