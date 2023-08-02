import torch
import numpy as np
from PIL import Image
import base64
import io

class DecodeBase64Image:
    """
    A node that decodes a base64 string into an image.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base64_encoded_image": ("STRING", {"multiline": True, "dynamicPrompts": False}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "decode_base64_image"
    CATEGORY = "image"
    OUTPUT_IS_LIST = (True,)

    def decode_base64_image(self, base64_encoded_image):
        """
        Decodes a base64 string into a numpy image.
        """
        results = []

        decoded_image = base64.b64decode(base64_encoded_image)
        image = Image.open(io.BytesIO(decoded_image))
        image = np.array(image)

        results.append(image)
                
        return (results,)

NODE_CLASS_MAPPINGS = {
    "DecodeBase64Image": DecodeBase64Image,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DecodeBase64Image": "Decode base64 image",
}
