import sqlite3
import json

# Open a connection to the SQLite database
conn = sqlite3.connect('myrecipe.db')
cursor = conn.cursor()

# Read the JSON data from a file (replace 'recipes.json' with your JSON file path)
with open('recipes1.json', 'r', encoding='utf-8') as json_file:
    recipes_data = json.load(json_file)

# Define the table schema (assuming a 'recipes' table)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        RecipeID INTEGER PRIMARY KEY,
        TranslatedRecipeName TEXT,
        TranslatedIngredients TEXT,
        TotalTimeInMins INTEGER,
        Cuisine TEXT,
        TranslatedInstructions TEXT,
        URL TEXT,
        CleanedIngredients TEXT,
        ImageURL TEXT,
        IngredientCount INTEGER
    )
''')

# Insert each recipe from the JSON data into the table
for recipe in recipes_data:
    cursor.execute('''
        INSERT INTO recipes (
            TranslatedRecipeName,
            TranslatedIngredients,
            TotalTimeInMins,
            Cuisine,
            TranslatedInstructions,
            URL,
            CleanedIngredients,
            ImageURL,
            IngredientCount
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        recipe['TranslatedRecipeName'],
        recipe['TranslatedIngredients'],
        recipe['TotalTimeInMins'],
        recipe['Cuisine'],
        recipe['TranslatedInstructions'],
        recipe['URL'],
        recipe['Cleaned-Ingredients'],
        recipe['image_url'],
        recipe['Ingredient-count']
    ))

# Commit the changes and close the database connection
conn.commit()
conn.close()
