import requests
import json

def get_random_joke():
    """
    Fetch a random joke from the JokeAPI and display it.
    API: https://jokeapi.dev/
    """
    try:
        # Using JokeAPI - a free API that doesn't require authentication
        url = "https://jokeapi.dev/joke/Any"
        
        # Add parameters for better joke filtering
        params = {
            "format": "json",
            "safe-mode": True  # Filter out offensive jokes
        }
        
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # Raise an error for bad status codes
        
        joke_data = response.json()
        
        # Handle different joke types
        if joke_data["type"] == "single":
            # Single-part joke
            print("\n🎭 Random Joke:")
            print("-" * 50)
            print(joke_data["joke"])
            print("-" * 50)
        else:
            # Two-part joke (setup and delivery)
            print("\n🎭 Random Joke:")
            print("-" * 50)
            print(f"Setup: {joke_data['setup']}")
            print(f"Punchline: {joke_data['delivery']}")
            print("-" * 50)
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")
    except json.JSONDecodeError:
        print("Error parsing joke data")

def get_joke_by_category(category="Any"):
    """
    Fetch a joke by specific category.
    Available categories: General, Knock-Knock, Programming, Misc, Dark, Pun, Spooky, Christmas
    """
    try:
        url = f"https://jokeapi.dev/joke/{category}"
        
        params = {
            "format": "json",
            "safe-mode": True
        }
        
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        
        joke_data = response.json()
        
        if joke_data.get("error"):
            print(f"Error: {joke_data['message']}")
            return
        
        if joke_data["type"] == "single":
            print(f"\n🎭 {category} Joke:")
            print("-" * 50)
            print(joke_data["joke"])
            print("-" * 50)
        else:
            print(f"\n🎭 {category} Joke:")
            print("-" * 50)
            print(f"Setup: {joke_data['setup']}")
            print(f"Punchline: {joke_data['delivery']}")
            print("-" * 50)
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")

def main():
    """Main function to run the joke generator"""
    print("🎉 Welcome to the Random Joke Generator!")
    print("\nOptions:")
    print("1. Get a random joke")
    print("2. Get a joke by category")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            get_random_joke()
        elif choice == "2":
            print("\nAvailable categories:")
            print("General, Knock-Knock, Programming, Misc, Dark, Pun, Spooky, Christmas")
            category = input("Enter category: ").strip()
            if category:
                get_joke_by_category(category)
            else:
                print("Invalid category!")
        elif choice == "3":
            print("Thanks for laughing with us! Goodbye! 😄")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
