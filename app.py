import streamlit as st
from inference_sdk import InferenceHTTPClient
from PIL import Image
import json

# ✅ Correct API URL for hosted model inference
client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="wRYqcYsBKcNci74NV5KP"
)

# Load recipes from JSON file
with open("recipes_db.json") as f:
    recipes = json.load(f)

# Function to generate matching recipes
def generate_recipe(detected):
    # Normalize detected ingredients to lowercase
    unique = list(set(i.lower() for i in detected))
    matches = []
    for recipe, details in recipes.items():
        recipe_ingredients = [i.lower() for i in details["ingredients"]]
        if any(ingredient in unique for ingredient in recipe_ingredients):
            matches.append(recipe)
    return matches, unique

# Streamlit UI
st.title("🍲 AI-Powered Recipe Generator")

uploaded = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    path = "uploaded.jpg"
    img.save(path)

    result = client.infer(path, model_id="ingredient-detection-2-kgs04/1")

    # Collect detected ingredients
    detected = [p["class"] for p in result["predictions"]]
    found, unique = generate_recipe(detected)

    st.write("✅ Detected Ingredients:", unique)

    if found:
        st.success(f"🎉 {len(found)} recipe(s) found!")
        choice = st.selectbox("Choose a recipe:", found)
        if choice:
            st.subheader(f"🍽️ {choice}")
            st.write("**Ingredients:**")
            st.markdown(", ".join(recipes[choice]["ingredients"]))
            st.write("**Steps:**")
            for idx, step in enumerate(recipes[choice]["steps"], 1):
                st.markdown(f"{idx}. {step}")
    else:
        st.error("❌ No recipes matched these ingredients.")


