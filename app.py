import streamlit as st
from inference_sdk import InferenceHTTPClient
from PIL import Image
import json

# Initialize the InferenceHTTPClient with your API key and Roboflow endpoint
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="wRYqcYsBKcNci74NV5KP"
)

# Load the recipes database (from the saved 'recipes_db.json' file)
with open("recipes_db.json", "r") as file:
    recipes = json.load(file)

# Function to generate recipe based on detected ingredients
def generate_recipe(detected_ingredients):
    # Remove redundant ingredients (e.g., "egg", "egg" -> "egg")
    unique_ingredients = list(set(detected_ingredients))
    
    matching_recipes = []
    for recipe, details in recipes.items():
        # Check if any ingredient in the recipe matches any of the unique detected ingredients
        if any(ingredient in unique_ingredients for ingredient in details["ingredients"]):
            matching_recipes.append(recipe)
    return matching_recipes, unique_ingredients

# Streamlit UI elements
st.title("Recipe Generator from Image")
st.write("Upload an image, and I will detect the ingredients and generate a recipe!")

# Image upload
image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# If an image is uploaded, process it
if image:
    # Display the uploaded image
    img = Image.open(image)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Save the image to a temporary file for inference
    img_path = "uploaded_image.jpg"
    img.save(img_path)

    # Run inference on the uploaded image
    result = CLIENT.infer(img_path, model_id="ingredients_yolo/3")

    # Extract detected classes from the result
    detected_classes = [prediction["class"] for prediction in result["predictions"]]
    st.write("Detected ingredients:", detected_classes)

    # Generate and display recipes based on detected ingredients
    recipes_found, unique_ingredients = generate_recipe(detected_classes)

    if recipes_found:
        st.write("I found the following recipes based on the detected ingredients:")
        for recipe in recipes_found:
            st.write(f"- {recipe}")
        
        # Ask the user to select a recipe from the list
        selected_recipe = st.selectbox("Choose a recipe to get the full instructions", recipes_found)

        # Display the selected recipe's ingredients and steps
        if selected_recipe:
            recipe_details = recipes[selected_recipe]
            st.write(f"### {selected_recipe}")
            st.write("**Ingredients**:")
            for ingredient in recipe_details["ingredients"]:
                st.write(f"- {ingredient}")
            st.write("**Steps**:")
            for step in recipe_details["steps"]:
                st.write(f"- {step}")
    else:
        st.write("Sorry, I couldn't find any recipes based on the detected ingredients.")
