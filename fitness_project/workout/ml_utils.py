import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, 'ml\\workout_model.pkl'))
goal_encoder = joblib.load(os.path.join(BASE_DIR,'ml\\goal_encoder.pkl'))
level_encoder = joblib.load(os.path.join(BASE_DIR,'ml\\level_encoder.pkl'))

GOAL_ENCODING = {
    'lose': 0,
    'maintain': 1,
    'gain': 2
}

def predict_workout_level(age, height, weight,bmi, goal):
    goal_encoded = GOAL_ENCODING.get(goal, 1)

    X = [[age, height, weight, bmi, goal_encoded]]
    prediction = model.predict(X)
    
    return prediction[0]