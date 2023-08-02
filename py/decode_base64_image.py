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

        # If the base64 string starts with "data:", remove the prefix,
        # as we need only the raw base64 string.
        if base64_encoded_image.startswith("data:"):
            base64_encoded_image = base64_encoded_image.split(",")[-1]

        # Decode the base64 string into an image
        decoded_image = base64.b64decode(base64_encoded_image)
        
        image_bytes = io.BytesIO(decoded_image)
        image = Image.open(image_bytes)
        
        # Convert the image to a torch tensor
        result_image = np.array(image).astype(np.float32) / 255.0
        result_image = torch.from_numpy(image)[None,]

        results.append(result_image)
                
        return (results,)

NODE_CLASS_MAPPINGS = {
    "DecodeBase64Image": DecodeBase64Image,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DecodeBase64Image": "Decode base64 image",
}
