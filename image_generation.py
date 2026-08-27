from huggingface_hub import InferenceClient
import os

# 1. Paste your free Hugging Face User Access Token
# Create one for free at: https://huggingface.co/settings/tokens
HF_TOKEN = os.environ["GEMINI_API_KEY"]

# recipe=Recipe("onion","rice","chicken")

# 2. Initialize the official client
client = InferenceClient(api_key=HF_TOKEN)

# 3. Generate the image using a reliable public model
def recipe_image(recipe_name:str):
    image = client.text_to_image(
        prompt=f"show me the picture of the food {recipe_name}",
        model="black-forest-labs/FLUX.1-schnell"
    )

    # 4. Save the generated image
    return image.save("static/recipe_here.png")
