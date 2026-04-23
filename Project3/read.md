# 🎬 AI Recommendation System (Project 3)

## 👩‍💻 Developer
Mahnoor Fatima  
Batch 2026 | DecodeLabs  

---

## 📌 Project Description
This project is a simple AI-based recommendation system that suggests movies based on user preferences.

It uses **pattern alignment** and **similarity scoring** instead of random suggestions.

---

## ⚙️ How It Works

1. Movies are stored as **binary vectors**  
   Example:
   - Action → [1,0,0,0,0]
   - Sci-Fi → [0,1,0,0,0]

2. User input is converted into a **user vector**

3. System compares:
   - User vector
   - Movie vector

4. A **similarity score** is calculated based on matching values

5. Movies are sorted and recommended

---

## 🧠 Technologies Used
- Python
- Logic Building
- Pattern Matching
- Similarity Score Algorithm

---

## 🎯 Features
✔ Takes user input  
✔ Converts input to vector  
✔ Matches patterns using AI logic  
✔ Displays ranked recommendations  

---

## 🚀 How to Run

```bash
python main.py

--- DECODELABS AI RECOMMENDATION ENGINE ---
Available Genres: Action, Sci-Fi, Romance, Comedy, Horror

What kind of movies do you enjoy? Horror

[AI Logic] User Profile Vector: [0, 0, 0, 0, 1]
----------------------------------------
🎯 Top Recommendations (based on similarity score):
-> The Conjuring: The Devil Made Me Do It (Match Score: 1)
----------------------------------------