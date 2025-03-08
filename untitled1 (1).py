# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19yCHSlQ6ihRxqblgSXrb3_WPRwuSCN7m
"""

pip install streamlit

import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="NutriWorkout - Diet & Exercise Planner",
    page_icon="🥗",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #388E3C;
        margin-bottom: 1rem;
    }
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .meal-category {
        font-weight: bold;
        margin-top: 10px;
        color: #388E3C;
    }
    .nutrition-info {
        background-color: #f5f5f5;
        padding: 10px;
        border-radius: 5px;
        margin-top: 5px;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Exercise data (calories burned in 30 minutes)
exercise_data = {
    "125": [
        ["Walking (3.5 mph)", 120],
        ["Bicycling (10-12 mph)", 240],
        ["Swimming (freestyle, moderate)", 300],
        ["Weight lifting (general)", 180],
        ["Yoga", 120],
        ["Running (6 mph)", 300],
        ["Dancing (aerobic)", 165],
        ["Hiking", 240],
        ["Elliptical trainer", 270],
        ["Stair climbing", 180]
    ],
    "155": [
        ["Walking (3.5 mph)", 149],
        ["Bicycling (10-12 mph)", 298],
        ["Swimming (freestyle, moderate)", 372],
        ["Weight lifting (general)", 223],
        ["Yoga", 149],
        ["Running (6 mph)", 372],
        ["Dancing (aerobic)", 205],
        ["Hiking", 298],
        ["Elliptical trainer", 335],
        ["Stair climbing", 223]
    ],
    "185": [
        ["Walking (3.5 mph)", 178],
        ["Bicycling (10-12 mph)", 355],
        ["Swimming (freestyle, moderate)", 444],
        ["Weight lifting (general)", 266],
        ["Yoga", 178],
        ["Running (6 mph)", 444],
        ["Dancing (aerobic)", 244],
        ["Hiking", 355],
        ["Elliptical trainer", 400],
        ["Stair climbing", 266]
    ]
}

# Meal data
meal_data = {
    "vegan": [
        "Tofu Scramble with Vegetables",
        "Chickpea Buddha Bowl",
        "Lentil Soup with Fresh Herbs",
        "Mushroom and Spinach Risotto",
        "Vegan Pad Thai",
        "Roasted Vegetable Tacos",
        "Quinoa Stuffed Bell Peppers"
    ],
    "vegetarian": [
        "Greek Yogurt with Berries and Granola",
        "Mediterranean Vegetable Frittata",
        "Caprese Sandwich with Fresh Mozzarella",
        "Spinach and Feta Stuffed Portobello Mushrooms",
        "Vegetable Curry with Basmati Rice",
        "Eggplant Parmesan",
        "Three Bean Chili"
    ],
    "paleo": [
        "Avocado and Bacon Omelette",
        "Grilled Chicken Salad with Olive Oil Dressing",
        "Baked Salmon with Roasted Asparagus",
        "Beef and Vegetable Stir Fry",
        "Turkey and Sweet Potato Skillet",
        "Zucchini Noodles with Shrimp",
        "Herb Crusted Pork Tenderloin"
    ],
    "keto": [
        "Cream Cheese Pancakes",
        "Bacon and Cheese Crustless Quiche",
        "Avocado and Tuna Salad",
        "Keto Beef Chili",
        "Butter Chicken with Cauliflower Rice",
        "Zucchini Lasagna",
        "Garlic Butter Steak with Mushrooms"
    ],
    "mediterranean": [
        "Greek Yogurt with Honey and Walnuts",
        "Mediterranean Breakfast Bowl",
        "Hummus and Vegetable Wrap",
        "Greek Salad with Grilled Chicken",
        "Baked Cod with Tomatoes and Olives",
        "Lemon Herb Mediterranean Pasta",
        "Grilled Lamb with Tzatziki Sauce"
    ],
    "glutenfree": [
        "Quinoa Breakfast Bowl",
        "Sweet Potato Toast with Avocado",
        "Rice Paper Veggie Wraps",
        "Gluten-Free Pasta with Pesto",
        "Stuffed Bell Peppers",
        "Grilled Fish Tacos with Corn Tortillas",
        "Chickpea and Vegetable Curry"
    ],
    "dairyfree": [
        "Coconut Yogurt with Fresh Fruit",
        "Avocado Toast with Poached Eggs",
        "Chicken and Vegetable Stir Fry",
        "Coconut Curry Soup",
        "Roasted Salmon with Sweet Potato",
        "Cashew Cream Pasta",
        "Grilled Chicken with Mango Salsa"
    ]
}

# Nutrition info (simplified for demo)
nutrition_info = {
    "high": {"calories": "350-400", "protein": "20-25g", "carbs": "30-35g", "fats": "15-20g"},
    "medium": {"calories": "250-300", "protein": "15-20g", "carbs": "20-25g", "fats": "10-15g"},
    "low": {"calories": "150-200", "protein": "10-15g", "carbs": "15-20g", "fats": "5-10g"}
}

# Helper functions
def get_random_items(array, count):
    """Get random items from an array"""
    return random.sample(array, count)

def get_random_nutrition_level():
    """Get a random nutrition level"""
    return random.choice(["low", "medium", "high"])

def get_exercises(weight):
    """Get exercises based on weight"""
    if weight <= 140:
        weight_category = "125"
    elif weight <= 170:
        weight_category = "155"
    else:
        weight_category = "185"

    return get_random_items(exercise_data[weight_category], 4)

def get_meals(diet):
    """Get meals based on diet"""
    if diet not in meal_data:
        return {
            "breakfast": ["Sample Breakfast"],
            "lunch": ["Sample Lunch 1", "Sample Lunch 2"],
            "dinner": ["Sample Dinner 1", "Sample Dinner 2", "Sample Dinner 3"]
        }

    all_meals = meal_data[diet]
    selected_meals = get_random_items(all_meals, min(6, len(all_meals)))

    return {
        "breakfast": selected_meals[0:1],
        "lunch": selected_meals[1:3],
        "dinner": selected_meals[3:6]
    }

# Main app
st.markdown("<h1 class='main-header'>NutriWorkout - Personalized Diet & Exercise Planner</h1>", unsafe_allow_html=True)
st.markdown("Get tailored exercise recommendations and meal plans based on your weight and dietary preferences, complete with nutrition information.")

# Create two columns for the form
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Your Weight (in pounds)", min_value=80, max_value=350, value=150)

with col2:
    diet = st.selectbox(
        "Your Diet Preference",
        options=["vegan", "vegetarian", "paleo", "keto", "mediterranean", "glutenfree", "dairyfree"],
        format_func=lambda x: x.capitalize()
    )

# Generate button
if st.button("Generate Plan", type="primary"):
    # Show loading spinner
    with st.spinner("Generating your personalized plan..."):
        # Add a small delay to simulate processing
        import time
        time.sleep(1)

        # Get exercises and meals
        exercises = get_exercises(weight)
        meals = get_meals(diet)

        # Create two columns for results
        col1, col2 = st.columns(2)

        # Display exercises
        with col1:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("<h2 class='sub-header'>📋 Recommended Exercises</h2>", unsafe_allow_html=True)
            st.markdown("<h3>30-Minute Exercise Recommendations:</h3>", unsafe_allow_html=True)

            for exercise in exercises:
                st.markdown(f"🔥 **{exercise[0]}**: {exercise[1]} calories burned")

            st.markdown("</div>", unsafe_allow_html=True)

        # Display meal plan
        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("<h2 class='sub-header'>🍽️ Personalized Meal Plan</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3>Meal Plan for {diet.capitalize()} Diet:</h3>", unsafe_allow_html=True)

            # Breakfast
            st.markdown("<div class='meal-category'>🥣 Breakfast</div>", unsafe_allow_html=True)
            for meal in meals["breakfast"]:
                nutrition_level = get_random_nutrition_level()
                st.markdown(f"**{meal}**")
                st.markdown(f"""<div class='nutrition-info'>
                    🔹 Calories: {nutrition_info[nutrition_level]['calories']} |
                    Protein: {nutrition_info[nutrition_level]['protein']} |
                    Carbs: {nutrition_info[nutrition_level]['carbs']} |
                    Fats: {nutrition_info[nutrition_level]['fats']}
                </div>""", unsafe_allow_html=True)

            # Lunch
            st.markdown("<div class='meal-category'>🍛 Lunch</div>", unsafe_allow_html=True)
            for meal in meals["lunch"]:
                nutrition_level = get_random_nutrition_level()
                st.markdown(f"**{meal}**")
                st.markdown(f"""<div class='nutrition-info'>
                    🔹 Calories: {nutrition_info[nutrition_level]['calories']} |
                    Protein: {nutrition_info[nutrition_level]['protein']} |
                    Carbs: {nutrition_info[nutrition_level]['carbs']} |
                    Fats: {nutrition_info[nutrition_level]['fats']}
                </div>""", unsafe_allow_html=True)

            # Dinner
            st.markdown("<div class='meal-category'>🍽️ Main Course</div>", unsafe_allow_html=True)
            for meal in meals["dinner"]:
                nutrition_level = get_random_nutrition_level()
                st.markdown(f"**{meal}**")
                st.markdown(f"""<div class='nutrition-info'>
                    🔹 Calories: {nutrition_info[nutrition_level]['calories']} |
                    Protein: {nutrition_info[nutrition_level]['protein']} |
                    Carbs: {nutrition_info[nutrition_level]['carbs']} |
                    Fats: {nutrition_info[nutrition_level]['fats']}
                </div>""", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

    # Success message
    st.success("Your personalized plan has been generated!")

# Footer
st.markdown("---")
st.markdown("© 2025 NutriWorkout. Created for demonstration purposes.")