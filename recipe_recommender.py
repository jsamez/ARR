
import cv2
from ultralytics import YOLO
from csv_manager import load_recipes_from_csv

class RecipeRecommender:
    def __init__(self, model_path, csv_file='food_info.csv', confidence_threshold=0.90):
        self.model = YOLO(model_path, verbose=False)
        self.recipes = load_recipes_from_csv(csv_file)
        self.detected_once = set()
        self.initial_detected = set()
        self.main_ingredient = None
        self.confidence_threshold = confidence_threshold

    def detect_ingredients(self, frame):
        results = self.model(frame, verbose=False)
        detected_ingredients = {self.model.names[int(detection.cls)] 
                                for result in results for detection in result.boxes 
                                if detection.conf >= self.confidence_threshold}
        return detected_ingredients

    def recommend_recipe(self, detected_ingredients):
        detected_set = frozenset(detected_ingredients)
        recommended_recipes = [
            recipe['name'] for ingredients, recipe in self.recipes.items()
            if len(ingredients & detected_set) >= 2 and self.main_ingredient in ingredients
        ]
        return recommended_recipes if recommended_recipes else None
    