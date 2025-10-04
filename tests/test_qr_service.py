import pytest
from src.services.qr_service import QRService


def test_generate_qr_from_url_returns_bytes():
    service = QRService()
    url = "https://example.com"

    qr_bytes = service.generate_qr(url)

    # basic assertions
    assert isinstance(qr_bytes, bytes)  # data returned is in fact of class bytes
    assert len(qr_bytes) > 0  # data returned is not empty


def test_qr_is_different_for_different_urls():
    service = QRService()
    qr1 = service.generate_qr("https://example.com/1")
    qr2 = service.generate_qr("https://example.com/2")
    assert qr1 != qr2


def test_invalid_url_raises_error():
    service = QRService()
    with pytest.raises(ValueError):
        service.generate_qr("")
