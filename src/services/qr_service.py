import qrcode
import base64
from io import BytesIO


class QRService:
    def generate_qr(self, data: str) -> str:
        if not data or not isinstance(data, str):
            raise ValueError("URL must be a non-empty string")

        qr = qrcode.make(data)
        buf = BytesIO()
        qr.save(buf, format="PNG")
        img_bytes = buf.getvalue()
        base64_str = base64.b64encode(img_bytes).decode("utf-8")

        return f"data:image/png;base64,{base64_str}"
