import os
from typing import List
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

class ImageService:
    """
    Service responsible for generating images
    (used for mood boards, inspiration visuals, etc.)
    """

    @staticmethod
    def generate_moodboard_images(
        prompts: List[str],
        image_size: str = "1024x1024"
    ) -> List[str]:
        """
        Generates images for a mood board based on prompt list.

        Args:
            prompts (List[str]): List of image generation prompts
            image_size (str): Image resolution

        Returns:
            List[str]: List of generated image URLs
        """

        image_urls = []

        for prompt in prompts:
            try:
                response = client.images.generate(
                    model="gpt-image-1",
                    prompt=prompt,
                    size=image_size
                )

                # Extract image URL
                image_url = response.data[0].url
                image_urls.append(image_url)

            except Exception as e:
                print(f"[Image Generation Error]: {e}")
                image_urls.append("")

        return image_urls
