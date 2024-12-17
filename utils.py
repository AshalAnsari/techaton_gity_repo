from PIL import Image
from io import BytesIO
import base64


async def bufferToBinary(buffer: str):
    padded_image_data = buffer + '=' * (4 - len(buffer) % 4)
    binary_data = base64.b64decode(padded_image_data)
        
    image = Image.open(BytesIO(binary_data))
    return image
