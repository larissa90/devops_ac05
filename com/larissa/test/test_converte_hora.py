import pytest
from com.larissa import converte_hora

def test_converte_hora():
    assert converte_hora.converteHora(13,20) == ('01:20 PM')

def test_converte_hora01():
    assert converte_hora.converteHora(0,50) == ('12:50 AM')

def test_converte_hora02():
    assert converte_hora.converteHora(24,0) == None

