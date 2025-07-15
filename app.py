import streamlit as st
from inference_sdk import InferenceHTTPClient
from PIL import Image
import json

# ✅ Correct API URL for hosted model inference
client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="wRYqcYsBKcNci74NV5KP"
)

with open("recipes_db.json") as f:
    recipes = json.load(f)

def generate_recipe(detected):
    unique = list(set(detected))
    matches = []
    for recipe, details in recipes.items():
        if any(ingredient in unique for ingredient in details["ingredients"]):
            matches.append(recipe)
    return matches, unique

st.title("Recipe Generator 🍲")
uploaded = st.file_uploader("Upload food image", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    path = "uploaded.jpg"
    img.save(path)

    result = client.infer(path, model_id="ingredient-detection-2-kgs04/1")

    detected = [p["class"] for p in result["predictions"]]
    st.write("Detected Ingredients:", detected)

    found, unique = generate_recipe(detected)

    if found:
        st.success(f"{len(found)} recipes found!")
        choice = st.selectbox("Choose one", found)
        if choice:
            st.subheader(choice)
            st.write("Ingredients:", *recipes[choice]["ingredients"])
            st.write("Steps:", *recipes[choice]["steps"])
    else:
        st.error("No recipes matched these ingredients.")

