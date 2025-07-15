import streamlit as st
from inference_sdk import InferenceHTTPClient
from PIL import Image
import json

# Initialize the InferenceHTTPClient with Roboflow serverless endpoint
client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="wRYqcYsBKcNci74NV5KP"
)

# Load your recipes database
with open("recipes_db.json", "r") as file:
    recipes = json.load(file)

# Function to generate recipe based on detected ingredients
def generate_recipe(detected_ingredients):
    unique_ingredients = list(set(detected_ingredients))
    matching_recipes = []
    for recipe, details in recipes.items():
        if any(ingredient in unique_ingredients for ingredient in details["ingredients"]):
            matching_recipes.append(recipe)
    return matching_recipes, unique_ingredients

# Streamlit App
st.title("AI Recipe Generator from Image 🍳")
st.write("Upload a food image and get recipes based on detected ingredients!")

image = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

if image:
    img = Image.open(image)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    # Save temporarily
    img_path = "uploaded_image.jpg"
    img.save(img_path)

    # Run workflow detection using Roboflow
    result = client.run_workflow(
        workspace_name="lipika",
        workflow_id="detect-and-classify",
        images={"image": img_path},
        use_cache=True
    )

    # Extract detected ingredients from result
    detected_classes = []
    for step in result["steps"]:
        predictions = step.get("predictions", [])
        for prediction in predictions:
            detected_classes.append(prediction.get("class"))

    st.write("Detected Ingredients:", detected_classes)

    # Recipe generation
    recipes_found, unique_ingredients = generate_recipe(detected_classes)

    if recipes_found:
        st.success(f"Found {len(recipes_found)} recipe(s) matching your ingredients!")
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
