import os
from google import genai
from django.conf import settings
from anthropic import Anthropic
from openai import OpenAI

gemini_client = None
claude_client = None
openai_client = None

if settings.GEMINI_API_KEY:
    gemini_client = genai.Client(api_key=settings.GEMINI_API_KEY)

if settings.CLAUDE_API_KEY:
    claude_client = Anthropic(api_key=settings.CLAUDE_API_KEY)

if settings.OPENAI_API_KEY:
    openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_workout_plan(profile, level, goal):
    prompt = f"""
    You are a professional fitness trainer.

    User details:
    - Age: {profile.age}
    - Height: {profile.height} cm
    - Weight: {profile.weight} kg
    - BMI: {round(profile.weight / ((profile.height/100)**2), 2)}
    - Fitness level: {level}
    - Goal: {goal}

    Generate a 7-day workout plan.
    Include:
    - Day-wise exercises
    - Sets and reps
    - Rest days
    Keep it safe and realistic.
    """

    if gemini_client:
        try:
            response = gemini_client.models.generate_content(
                model="gemini-3-pro-preview",
                # model="gemini-2.0-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            print("Gemini failed:",e)

    if claude_client:
        try:
            response = claude_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=800,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            print("Claude failed:",  e)
    
    if openai_client:
        try:
            response = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a professional fitness trainer."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800
            )
            return response.choices[0].message.content
        except Exception as e:
            print("OpenAI ChatGPT failed:", e)
    
    # Fallback plan if all APIs fail
    return f"""
📋 AI Service Temporarily Unavailable - Generating Sample Plan

Sample {level.title()} Workout Plan for {goal}:

Day 1: Full Body Strength
- Warm up: 5 min light cardio
- Push-ups: 3 x 10-12 reps
- Squats: 3 x 12-15 reps
- Planks: 3 x 30-45 seconds
- Cool down: 5 min stretching

Day 2: Cardio & Core
- 20-30 minutes of brisk walking, jogging, or cycling
- Core work: 3 x 15 crunches
- 3 x 10 leg raises
- Cool down: 5 min stretching

Day 3: Upper Body
- Bench Press or Dumbbell Press: 3 x 8-10 reps
- Rows: 3 x 10-12 reps
- Shoulder Press: 3 x 10 reps
- Bicep Curls: 2 x 12 reps
- Cool down: 5 min stretching

Day 4: Rest Day
- Light stretching or yoga
- Focus on recovery and hydration

Day 5: Lower Body
- Lunges: 3 x 12 reps (each leg)
- Leg Press: 3 x 12-15 reps
- Calf Raises: 3 x 15 reps
- Hamstring Curls: 3 x 12 reps
- Cool down: 5 min stretching

Day 6: Full Body & Cardio
- 15 min cardio (warm-up)
- Circuit: 3 rounds of:
  - 10 Push-ups
  - 15 Squats
  - 10 Burpees
- 5 min cool-down stretching

Day 7: Rest and Recovery
- Light stretching or yoga
- Prepare for next week's training

Note: AI personalized plan coming soon. This is a generic template. Adjust intensity based on your fitness level.
"""
    