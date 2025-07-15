
# 🍲 AI-Powered Recipe Generator

An AI-powered web app that generates recipe suggestions from a single food image! Using a custom-trained YOLOv8 model hosted on Roboflow, the app detects ingredients from your uploaded image and matches them to a curated recipe database.




## 🚀 Live Demo

👉 [See It in Action!](https://www.youtube.com/watch?v=3_udCPpFdng)

## 💻 Deployed App

👉 [Try it live!](https://recipe-generator101.streamlit.app/)

## 📈 Model

👉 [View Model](https://universe.roboflow.com/lipika/ingredient-detection-2-kgs04/model/1)


## 📌 Features

- 🔍 **Ingredient Detection**: Upload a food image and instantly get a list of detected ingredients using a YOLOv8 object detection model.

- 🍽️ **Recipe Recommendations**: Get personalized recipe suggestions based on the ingredients detected.
  
- 🥕 **Works with Common Ingredients**: Carrot, cauliflower, eggs, garlic, ginger, onion, tomato, potato.

- 🖼️ **Interactive UI**: Simple and clean interface built with Streamlit.

- ⚡ **Real-Time AI Inference**: Uses Roboflow Inference API for fast, accurate predictions.


## 🧠 Model Information

- **Model Name:** `ingredient-detection-2-kgs04`
- **Platform:** [Roboflow Universe](https://universe.roboflow.com/lipika/ingredient-detection-2-kgs04/model/1)
- **Architecture:** YOLOv8 (Roboflow 3.0 Object Detection - Fast)
- **Training Data:** 1001 annotated images

### 📊 Performance Metrics

- **mAP@50:** 73.4%
- **Precision:** 73.3%
- **Recall:** 70.5%
## 💡 How It Works

1. **Upload Image** → Upload a photo of ingredients or a dish.

2. **Ingredient Detection** → The Roboflow model identifies ingredients present in the image.

3. **Recipe Matching** → Detected ingredients are matched against a pre-defined recipe database (`recipes_db.json`).

4. **Get Recipe** → Choose from available recipes, view ingredients and cooking steps.

## 🛠️ Tech Stack

| Technology    | Purpose                                     |
|----------------|---------------------------------------------|
| **Streamlit**  | Frontend UI for the web app                 |
| **Roboflow API** | Ingredient detection (YOLOv8 model inference) |
| **Python**     | Backend logic and API integration          |
| **PIL**        | Image processing                           |
| **JSON**       | Recipe storage and lookup                  |



## 🏁 Getting Started

### Clone the Repository
```bash
git clone https://github.com/lipika1911/recipe-generator.git
cd recipe-generator
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Run the App
```
streamlit run app.py
```
## ✅ Future Improvements
- 📈 Expand recipe database with more diverse recipes.

- 🏷️ Add category filters (veg/non-veg, breakfast, dinner, etc.).

- 🌍 Support multilingual recipes.

- 📲 Mobile-friendly responsive design.

## 📬 Contact

For feedback, ideas, or collaborations, reach out:

- 💻 **GitHub:** [lipika1911](https://github.com/lipika1911)

## 📄 License

This project is licensed under the [MIT License](./LICENSE).


## 👩‍💻 Author

Made with ❤️ by [Lipika](https://github.com/lipika1911)
