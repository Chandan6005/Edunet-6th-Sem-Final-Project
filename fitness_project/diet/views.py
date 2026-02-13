from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Diet

# Create your views here.

@login_required
def diet_view(request):
    profile = request.user.profile
    goal = (profile.goal or "").strip().lower()

    meals = []

    if goal in ["weight_loss", "weight loss"]:
        meals = [
            {"meal_type": "Breakfast", "food": "Oatmeal with fruits", "calories": 300},
            {"meal_type": "Lunch", "food": "Grilled chicken salad", "calories": 400},
            {"meal_type": "Dinner", "food": "Vegetable soup + roti", "calories": 350},
        ]

    elif goal in ["muscle_gain", "muscle gain"]:
        meals = [
            {"meal_type": "Breakfast", "food": "Eggs + Peanut butter toast", "calories": 500},
            {"meal_type": "Lunch", "food": "Rice + Chicken + Veggies", "calories": 700},
            {"meal_type": "Dinner", "food": "Paneer + Chapati", "calories": 600},
        ]

    elif goal in ["maintenance"]:
        meals = [
            {"meal_type": "Breakfast", "food": "Smoothie + Nuts", "calories": 400},
            {"meal_type": "Lunch", "food": "Balanced veg/non-veg meal", "calories": 500},
            {"meal_type": "Dinner", "food": "Light dinner + Salad", "calories": 350},
        ]

    print("DEBUG GOAL:", profile.goal)
    return render(request, "diet.html", {
        "meals": meals,
        "goal": goal
    })