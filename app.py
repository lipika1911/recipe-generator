import streamlit as st
from inference_sdk import InferenceHTTPClient
from PIL import Image
import json

# Initialize the InferenceHTTPClient with the correct model endpoint
client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="wRYqcYsBKcNci74NV5KP"
)

# Load recipes database
with open("recipes_db.json", "r") as file:
    recipes = json.load(file)

def generate_recipe(detected_ingredients):
    unique_ingredients = list(set(detected_ingredients))
    matching_recipes = []
    for recipe, details in recipes.items():
        if any(ingredient in unique_ingredients for ingredient in details["ingredients"]):
            matching_recipes.append(recipe)
    return matching_recipes, unique_ingredients

st.title("AI Recipe Generator from Image 🍽️")
st.write("Upload an image and get recipes based on detected ingredients!")

image = st.file_uploader("Upload your food image", type=["jpg", "jpeg", "png"])

if image:
    img = Image.open(image)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    img_path = "uploaded_image.jpg"
    img.save(img_path)

    # ✅ Use correct model ID from your reference
    result = client.infer(img_path, model_id="ingredient-detection-2-kgs04/1")

    # Extract detected classes
    detected_classes = [prediction["class"] for prediction in result["predictions"]]
    st.write("Detected Ingredients:", detected_classes)

    recipes_found, unique_ingredients = generate_recipe(detected_classes)

    if recipes_found:
        st.success(f"Found {len(recipes_found)} recipe(s)!")
        selected_recipe = st.selectbox("Choose a recipe", recipes_found)

        if selected_recipe:
            recipe_details = recipes[selected_recipe]
            st.subheader(selected_recipe)
            st.markdown("**Ingredients:**")
            for ingredient in recipe_details["ingredients"]:
                st.write(f"- {ingredient}")
            st.markdown("**Steps:**")
            for step in recipe_details["steps"]:
                st.write(f"- {step}")
    else:
        st.error("No matching recipes found for detected ingredients.")
