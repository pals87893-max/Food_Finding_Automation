import os
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional,TypeVar,Type

T=TypeVar("T", bound=BaseModel)


class Recipe(BaseModel):
    recipe_name: str = Field(description="Name of the recipe.")
    ingredients: List[str] = Field(description="List of ingredients.")
    prep_time_minutes: Optional[int] = Field(description="Prep time in minutes.")


client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
def get_structured_response(prompt: str, schema: Type[T],model_name:str) -> T:
    interaction = client.interactions.create(
        model=f"{model_name}",
        input=prompt,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": Recipe.model_json_schema()
        },
    )
    return schema.model_validate_json(interaction.output_text)

def recipie(ingredients:str,model_name:str)-> Recipe:
    prompt=f"""You are a recipe generator that returns structured data.

Task: Create a recipe using these ingredients: {ingredients}
Note: Don't add any extra ingredients that can't be found in the house normally.

Requirements for your response:
- recipe_name: A short, appetizing name for the dish (string, required).
- ingredients: A complete list of ALL ingredients needed for the recipe, including quantities (e.g. "2 ripe bananas", "1 cup flour"), not just the ones I gave you — add any staple ingredients needed to actually make the dish. Must be a list of strings.
- prep_time_minutes: Your best estimate of preparation time in minutes, as a plain integer only (e.g. 15, not "15 minutes" or "about 15"). If truly unknown, omit this field or return null — do not guess a string.

Return only the structured data matching the required schema. Do not include any explanation, commentary, or text outside the schema fields."""
    return get_structured_response(prompt,Recipe,model_name)
