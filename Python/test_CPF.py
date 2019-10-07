from CPF import CPF

def test_ShouldReturnTheInputMasked():
    response = CPF().mask("11122233344")
    assert response == "111.222.333-44"

def test_ShouldReturnFalseWhenValidatingThisCPF():
    assert CPF().validate("11122233381") == False

def test_ShouldReturnTrueWhenValidatingThisCPF():
    assert CPF().validate("33880753016") == True