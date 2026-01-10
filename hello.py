# app.py - SIMPLE RECIPE FINDER

# Step 1: Import what we need (just copy this)
import tkinter as tk
from tkinter import filedialog, messagebox
import requests
from PIL import Image, ImageTk
import os

# Step 2: Create main window
window = tk.Tk()
window.title("Recipe Finder")
window.geometry("600x700")

# Store data
recipes_data = []
api_key = "YOUR_API_KEY_HERE"  # We'll get this later

# Step 3: Create widgets (buttons, labels, etc.)
title_label = tk.Label(window, text="🍳 Recipe Finder", font=("Arial", 24))
title_label.pack(pady=20)

# Image preview
image_label = tk.Label(window, text="No image selected")
image_label.pack()

# Upload button
def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.png")]
    )
    
    if file_path:
        # Show image
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo, text="")
        image_label.image = photo  # Keep reference
        
        # Simulate finding recipes (we'll make real later)
        messagebox.showinfo("Success", "Image uploaded! (For now, we'll use dummy data)")
        
        # Show dummy recipes
        show_dummy_recipes()

upload_btn = tk.Button(window, text="📁 Upload Photo", 
                      command=upload_image, font=("Arial", 14))
upload_btn.pack(pady=10)

# Text input as alternative
tk.Label(window, text="Or type ingredients:", font=("Arial", 12)).pack(pady=10)
ingredients_entry = tk.Entry(window, width=50)
ingredients_entry.pack()

def search_by_text():
    ingredients = ingredients_entry.get()
    if ingredients:
        messagebox.showinfo("Searching", f"Finding recipes for: {ingredients}")
        show_dummy_recipes()

search_btn = tk.Button(window, text="🔍 Find Recipes", 
                      command=search_by_text, font=("Arial", 12))
search_btn.pack(pady=5)

# Recipe display area
tk.Label(window, text="Found Recipes:", font=("Arial", 14, "bold")).pack(pady=20)

recipe_listbox = tk.Listbox(window, height=15, width=70)
recipe_listbox.pack()

# Step 4: Show dummy recipes (for testing)
def show_dummy_recipes():
    recipe_listbox.delete(0, tk.END)
    
    dummy_recipes = [
        "Spaghetti Carbonara (20 mins)",
        "Vegetable Stir Fry (15 mins)",
        "Chicken Curry (40 mins)",
        "Tomato Soup (25 mins)",
        "Cheese Omelette (10 mins)",
        "Garlic Bread (15 mins)",
        "Fruit Salad (10 mins)",
        "Fried Rice (30 mins)"
    ]
    
    for recipe in dummy_recipes:
        recipe_listbox.insert(tk.END, f"🍽️ {recipe}")
    
    global recipes_data
    recipes_data = dummy_recipes

# Step 5: Run the app
window.mainloop()