def main():
    movie_database = {
        "Infinity War": [1, 0, 0, 0, 0],
        "The Martian": [0, 1, 0, 0, 0],
        "Raise the Titanic": [0, 0, 1, 0, 0],
        "The Hangover": [0, 0, 0, 1, 0],
        "Tenet": [1, 1, 0, 0, 0],
        "This Is the End": [0, 0, 0, 1, 0],
        "The Conjuring: The Devil Made Me Do It": [0, 0, 0, 0, 1]
    }

    print("--- DECODELABS AI RECOMMENDATION ENGINE ---")
    print("Available Genres: Action, Sci-Fi, Romance, Comedy, Horror")

    user_query = input("\nWhat kind of movies do you enjoy? ").lower()

    user_vector = [0, 0, 0, 0, 0]

    if "action" in user_query:
        user_vector[0] = 1
    if "sci-fi" in user_query or "sci fi" in user_query:
        user_vector[1] = 1
    if "romance" in user_query:
        user_vector[2] = 1
    if "comedy" in user_query:
        user_vector[3] = 1
    if "horror" in user_query:
        user_vector[4] = 1

    # Validation
    if user_vector == [0, 0, 0, 0, 0]:
        print("⚠️ Please enter a valid genre!")
        return

    print(f"\n[AI Logic] User Profile Vector: {user_vector}")

    recommendations = []

    for movie_name, movie_vector in movie_database.items():
        score = sum(1 for u, m in zip(user_vector, movie_vector) if u == 1 and m == 1)

        if score > 0:
            recommendations.append((movie_name, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    print("-" * 40)
    print("🎯 Top Recommendations (based on similarity score):")
    for movie, score in recommendations:
        print(f"-> {movie} (Match Score: {score})")
    print("-" * 40)


if __name__ == "__main__":
    main()
