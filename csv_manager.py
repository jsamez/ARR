
import csv
import pandas as pd

def append_to_csv(values, filename='food_info.csv'):
    try:
        with open(filename, 'x', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['음식 이름', '재료', '레시피'])
            writer.writerows(values)
    except FileExistsError:
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(values)

def load_recipes_from_csv(filename='food_info.csv'):
    df = pd.read_csv(filename, encoding='utf-8')
    recipes = {
        frozenset(row['재료'].split(',')): {
            'ingredients': row['재료'].split(','),
            'recipe': row['레시피'],
            'name': row['음식 이름']
        }
        for _, row in df.iterrows()
    }
    return recipes
    