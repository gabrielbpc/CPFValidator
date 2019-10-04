from validator import Validator

def test_sShouldReturnTrueWhenValidatingThisCPF():
    assert Validator().validate("36812594881") == True