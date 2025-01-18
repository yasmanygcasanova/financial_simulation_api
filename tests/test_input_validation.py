# tests/test_input_validation.py

import pytest

from app.validation.input_validation import InvalidInputError, validate_growth_rate


def test_validate_growth_rate():
    # Teste com valor válido
    try:
        validate_growth_rate(0.5)
    except InvalidInputError:
        pytest.fail("validate_growth_rate raised InvalidInputError unexpectedly!")

    # Teste com valor negativo
    with pytest.raises(InvalidInputError):
        validate_growth_rate(-0.5)

    # Teste com valor acima do limite
    with pytest.raises(InvalidInputError):
        validate_growth_rate(1.5)

    # Teste com tipo inválido
    with pytest.raises(TypeError):
        validate_growth_rate("invalid")
