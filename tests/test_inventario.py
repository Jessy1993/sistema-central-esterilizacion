import pytest

from inventario import Instrumental


def test_registrar_ingreso_actualiza_stock():
    """CP-01: verifica que el ingreso aumente correctamente el stock."""
    instrumental = Instrumental("Pinza quirúrgica", 10)

    resultado = instrumental.registrar_ingreso(5)

    assert resultado == 15
    assert instrumental.consultar_stock() == 15


def test_registrar_salida_actualiza_stock():
    """CP-02: verifica que una salida disminuya correctamente el stock."""
    instrumental = Instrumental("Tijera quirúrgica", 10)

    resultado = instrumental.registrar_salida(4)

    assert resultado == 6
    assert instrumental.consultar_stock() == 6


def test_no_permite_salida_mayor_al_stock():
    """CP-03 CRÍTICO: impide entregar más instrumental del disponible."""
    instrumental = Instrumental("Bandeja quirúrgica", 5)

    with pytest.raises(
        ValueError,
        match="No existe suficiente instrumental disponible"
    ):
        instrumental.registrar_salida(8)


def test_no_permite_stock_inicial_negativo():
    """CP-04: evita registrar un instrumental con stock negativo."""
    with pytest.raises(
        ValueError,
        match="El stock inicial no puede ser negativo"
    ):
        Instrumental("Separador quirúrgico", -2)
