from validator import Validator

def test_ShouldReturnFalseWhenValidatingThisCPF():
    assert Validator().validate("11122233381") == False

def test_ShouldReturnTrueWhenValidatingThisCPF():
    assert Validator().validate("33880753016") == True