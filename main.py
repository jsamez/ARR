
import cv2
import tkinter as tk
from recipe_recommender import RecipeRecommender
from gui import display_message, get_user_input

def main():
    root = tk.Tk()
    root.title("Food Detection and Recipe Recommendation")
    recommender = RecipeRecommender(model_path='path_to_your_best_model.pt')

    cap = cv2.VideoCapture(0)  # 웹캠 실행
    if not cap.isOpened():
        messagebox.showerror("오류", "웹캠을 열 수 없습니다.")
        exit()

    def update_frame():
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("오류", "웹캠에서 프레임을 읽을 수 없습니다.")
            return
        
        detected_ingredients = recommender.detect_ingredients(frame)
        new_detected = detected_ingredients - recommender.detected_once
        if new_detected:
            recommender.detected_once.update(new_detected)
            if not recommender.initial_detected:
                recommender.initial_detected.update(recommender.detected_once)
                recommender.main_ingredient = next(iter(recommender.detected_once))
            
            recommended_recipes = recommender.recommend_recipe(recommender.detected_once)
            if recommended_recipes:
                selected_recipe = get_user_input(recommended_recipes, root)
                display_message("선택한 요리 레시피", selected_recipe)
            else:
                display_message("알림", "추천 요리를 찾을 수 없습니다.")

        cv2.imshow('Food Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            root.quit()
        root.after(10, update_frame)

    root.after(10, update_frame)
    root.mainloop()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    