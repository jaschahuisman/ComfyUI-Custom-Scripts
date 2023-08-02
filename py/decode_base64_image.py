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
                "base64_encoded_image": ("STRING", {"multiline": False, "dynamicPrompts": False}),
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

        # 1. Make sure to remove the prefix, if it exists.
        # We only want the raw base64 string.
        if base64_encoded_image.startswith("data:"):
            base64_encoded_image = base64_encoded_image.split(",")[1]

        # 2. Decode the base64 string into bytes.
        image_bytes = base64.b64decode(base64_encoded_image)

        # 3. Convert the bytes into a PIL image.
        image = Image.open(io.BytesIO(image_bytes))

        # 4. Convert the PIL image into a numpy array.
        image = np.array(image).astype(np.float32) / 255.0

        # 5. Convert the numpy array into a PyTorch tensor.
        result_image = torch.from_numpy(image)[None,]

        results.append(result_image)

        return (results,)

NODE_CLASS_MAPPINGS = {
    "DecodeBase64Image": DecodeBase64Image,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DecodeBase64Image": "Decode base64 image",
}
