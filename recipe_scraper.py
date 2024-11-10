
import requests
import json
from bs4 import BeautifulSoup

def food_info(name):
    url = f"https://www.10000recipe.com/recipe/list.html?q={name}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        food_list = soup.find_all(attrs={'class': 'common_sp_link'})
        if food_list:
            food_id = food_list[0]['href'].split('/')[-1]
            new_url = f'https://www.10000recipe.com/recipe/{food_id}'
            new_response = requests.get(new_url)
            if new_response.status_code == 200:
                soup = BeautifulSoup(new_response.text, 'html.parser')
                food_info = soup.find(attrs={'type': 'application/ld+json'})
                result = json.loads(food_info.text)
                ingredients = ','.join(result['recipeIngredient'])
                recipe = [f"{i + 1}. {step['text']}" for i, step in enumerate(result['recipeInstructions'])]
                return {'name': name, 'ingredients': ingredients, 'recipe': recipe}
    print(f"'{name}'에 해당하는 요리를 찾을 수 없습니다.")
    return None
    