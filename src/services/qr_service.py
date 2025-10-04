import io
from qrcode import QRCode, constants


class QRService:
    def generate_qr(self, url: str) -> bytes:
        if not url or not isinstance(url, str):
            raise ValueError("URL must be a non-empty string")

        qr = QRCode(
            version=1, error_correction=constants.ERROR_CORRECT_L, box_size=10, border=4
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        return buffer.getvalue()
