import io
import sys
sys.stdout = buffer = io.StringIO()

from app import calculateArea
import app
import pytest



@pytest.mark.it('Create variables a,b,c to store each function call')
def test_for_variables(capsys):

    captured = buffer.getvalue
    assert app.a is not None
    assert type(app.a) is int
    assert app.b is not None
    assert type(app.b) is int
    assert app.c is not None
    assert type(app.c) is int

@pytest.mark.it('Print var a,b,& c to get area of the figures')
def test_for_area_of_figures(capsys):
    captured = buffer.getvalue()

    def calculateArea(length,edge):
        length * edge
        return True

    assert app.a == calculateArea(2, 2)




