from huggingface_hub import InferenceClient
import os
import glob

# 1. Paste your free Hugging Face User Access Token
# Create one for free at: https://huggingface.co/settings/tokens
HF_TOKEN = os.environ["HF_API_KEY"]

# recipe=Recipe("onion","rice","chicken")

# 2. Initialize the official client
client = InferenceClient(api_key=HF_TOKEN)

# 3. Generate the image using a reliable public model
def recipe_image(recipe_name:str):
    image = client.text_to_image(
        prompt=f"show me the picture of the food {recipe_name}",
        model="black-forest-labs/FLUX.1-schnell"
    )
    old_file= os.path.join("static","recipe_here.png")

    if old_file:
        os.remove(old_file)
    return image.save(f"static/recipe_here.png")

