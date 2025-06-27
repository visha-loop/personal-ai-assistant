import requests
import random
import json
import os
from datetime import datetime
import re

def get_weather(city):
    """Get weather information for a city"""
    # Enhanced mock weather with more cities
    mock_weather = {
        "london": "London: 15°C, Cloudy ☁️",
        "delhi": "Delhi: 28°C, Sunny ☀️", 
        "mumbai": "Mumbai: 32°C, Humid 🌧️",
        "bangalore": "Bangalore: 22°C, Pleasant 🌤️",
        "hyderabad": "Hyderabad: 30°C, Hot 🔥",
        "chennai": "Chennai: 35°C, Very Hot 🌡️",
        "kolkata": "Kolkata: 29°C, Humid 💨",
        "pune": "Pune: 26°C, Nice 😊",
        "ahmedabad": "Ahmedabad: 33°C, Dry Heat 🏜️",
        "jaipur": "Jaipur: 31°C, Warm 🌅",
        "new york": "New York: 12°C, Cold ❄️",
        "tokyo": "Tokyo: 18°C, Cool 🌸",
        "paris": "Paris: 14°C, Chilly 🥶",
        "sydney": "Sydney: 25°C, Perfect 🏖️"
    }
    
    city_lower = city.lower()
    if city_lower in mock_weather:
        return mock_weather[city_lower]
    else:
        return f"Weather data for {city} is not available yet, but I'm sure it's lovely! 🌍"

def tell_joke():
    """Return a random programming joke"""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything! ⚛️",
        "Why did the programmer quit his job? He didn't get arrays! 📊",
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡",
        "Why do Java developers wear glasses? Because they don't C#! 👓",
        "What's a programmer's favorite hangout place? The Foo Bar! 🍺",
        "Why did the developer go broke? Because he used up all his cache! 💸",
        "What do you call a programmer from Finland? Nerdic! 🇫🇮",
        "Why do programmers hate nature? It has too many bugs! 🦟",
        "What's the object-oriented way to become wealthy? Inheritance! 💰",
        "Why was the JavaScript developer sad? Because he didn't Node how to Express himself! 😢",
        "How do you comfort a JavaScript bug? You console it! 🐞"
    ]
    return random.choice(jokes)

def get_study_tip():
    """Return a helpful study tip for CS students"""
    tips = [
        "💡 Take breaks every 45 minutes to keep your brain fresh!",
        "📚 Use the Pomodoro Technique: 25 min focused work, 5 min break",
        "🎯 Practice coding daily, even if it's just 15 minutes",
        "👥 Join study groups or coding communities for support",
        "📝 Keep notes of what you learn - writing helps memory",
        "🔄 Review previous topics regularly to strengthen understanding",
        "💻 Build projects to apply what you learn in class",
        "❓ Don't be afraid to ask questions - every expert was once a beginner!",
        "🧠 Use active recall - test yourself instead of just re-reading",
        "🎵 Try coding with focus music or binaural beats",
        "📱 Use apps like Anki for spaced repetition learning",
        "🏃‍♂️ Take walks while thinking about coding problems"
    ]
    return random.choice(tips)

def get_motivation():
    """Return motivational quotes for students"""
    quotes = [
        "🚀 Every expert was once a beginner. Keep going!",
        "💪 The only way to do great work is to love what you do.",
        "🎯 Success is the sum of small efforts repeated day in and day out.",
        "🌟 Your future self will thank you for the hard work you do today.",
        "⚡ Code is like humor. When you have to explain it, it's bad - but you're learning!",
        "🏆 The best time to plant a tree was 20 years ago. The second best time is now.",
        "🔥 Don't watch the clock; do what it does. Keep going.",
        "💎 Pressure makes diamonds. You're becoming brilliant!",
        "🌈 After every storm comes a rainbow. Keep coding!",
        "🎖️ Success is not final, failure is not fatal: it's the courage to continue that counts."
    ]
    return random.choice(quotes)

def get_coding_fact():
    """Return interesting coding facts"""
    facts = [
        "🤖 The first computer bug was an actual bug - a moth stuck in a Harvard Mark II computer in 1947!",
        "💾 The term 'debugging' was coined by Admiral Grace Hopper when she found that moth!",
        "🐍 Python was named after Monty Python's Flying Circus, not the snake!",
        "☕ Java was originally called Oak, but they had to change it due to trademark issues!",
        "🌐 The first website ever created is still online: info.cern.ch",
        "📱 There are more possible games of chess than atoms in the observable universe!",
        "🔢 The first computer programmer was Ada Lovelace in 1843!",
        "💻 The '@' symbol was used in programming before email was invented!",
        "🎮 The first computer game was created in 1958 - it was called 'Tennis for Two'!",
        "🚀 NASA still uses software from the 1970s for some of their missions!"
    ]
    return random.choice(facts)

def calculate_expression(expression):
    """Safely calculate mathematical expressions"""
    try:
        # Remove spaces and check for valid characters
        clean_expr = re.sub(r'[^0-9+\-*/().\s]', '', expression)
        if clean_expr:
            result = eval(clean_expr)
            return f"🧮 {expression} = {result}"
        else:
            return "🤔 That doesn't look like a valid math expression!"
    except:
        return "❌ Sorry, I couldn't calculate that. Try something like '5 + 3' or '2 * 8'"

def save_conversation(user_input, bot_response):
    """Save conversations to learn from them"""
    if not os.path.exists("data"):
        os.makedirs("data")
    
    conversation = {
        "user": user_input,
        "bot": bot_response,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    conversations_file = "data/conversations.json"
    
    if os.path.exists(conversations_file):
        try:
            with open(conversations_file, "r") as f:
                conversations = json.load(f)
        except:
            conversations = []
    else:
        conversations = []
    
    conversations.append(conversation)
    
    with open(conversations_file, "w") as f:
        json.dump(conversations, f, indent=2)

def get_conversation_stats():
    """Get statistics about conversations"""
    conversations_file = "data/conversations.json"
    
    if not os.path.exists(conversations_file):
        return "📊 This is our first conversation! Welcome! 🎉"
    
    try:
        with open(conversations_file, "r") as f:
            conversations = json.load(f)
        
        total = len(conversations)
        
        # Count different types of requests
        weather_count = sum(1 for c in conversations if "weather" in c["user"].lower())
        joke_count = sum(1 for c in conversations if "joke" in c["user"].lower())
        study_count = sum(1 for c in conversations if any(word in c["user"].lower() for word in ["study", "tip", "learn"]))
        
        stats = f"""📊 **Conversation Statistics:**
        
🗨️ Total conversations: {total}
🌤️ Weather requests: {weather_count}
😄 Jokes requested: {joke_count}
📚 Study tips given: {study_count}

Thanks for chatting with me! 🤖💕"""
        
        return stats
    except:
        return "📊 I'm still learning to count conversations! 🤖"

def get_time_greeting():
    """Get appropriate greeting based on time"""
    current_hour = datetime.now().hour
    
    if 5 <= current_hour < 12:
        return "🌅 Good morning!"
    elif 12 <= current_hour < 17:
        return "☀️ Good afternoon!"
    elif 17 <= current_hour < 21:
        return "🌆 Good evening!"
    else:
        return "🌙 Good night!"

def chatbot_response(user_input):
    """Main chatbot logic - the brain of our AI assistant"""
    user_input_lower = user_input.lower()
    
    # Weather requests
    if "weather" in user_input_lower:
        words = user_input.split()
        city = None
        
        if "in" in user_input_lower:
            try:
                in_index = [i for i, word in enumerate(words) if word.lower() == "in"][-1]
                if in_index + 1 < len(words):
                    city = words[in_index + 1]
            except:
                pass
        
        if city:
            response = get_weather(city)
        else:
            response = "🌤️ Please ask like: 'What's the weather in Delhi?' or 'Weather in Mumbai'"
    
    # Math calculations
    elif any(op in user_input for op in ['+', '-', '*', '/', 'calculate', 'math']):
        # Extract the mathematical part
        math_part = re.search(r'[\d+\-*/().\s]+', user_input)
        if math_part:
            response = calculate_expression(math_part.group())
        else:
            response = "🧮 Ask me to calculate something like '5 + 3' or 'what is 12 * 8?'"
    
    # Jokes
    elif "joke" in user_input_lower or "funny" in user_input_lower:
        response = "😄 Here's a joke for you:\n" + tell_joke()
    
    # Study tips
    elif any(word in user_input_lower for word in ["study", "tip", "learn", "focus"]):
        response = get_study_tip()
    
    # Motivation
    elif any(word in user_input_lower for word in ["motivat", "inspire", "encourage", "boost"]):
        response = get_motivation()
    
    # Coding facts
    elif any(word in user_input_lower for word in ["fact", "trivia", "interesting", "cool"]):
        response = "🤓 Here's a cool coding fact:\n" + get_coding_fact()
    
    # Time-based greetings
    elif any(greeting in user_input_lower for greeting in ["good morning", "good afternoon", "good evening", "good night"]):
        response = get_time_greeting() + " How can I help you today?"
    
    # Stats
    elif "stat" in user_input_lower or "how many" in user_input_lower:
        response = get_conversation_stats()
    
    # General greetings
    elif any(greeting in user_input_lower for greeting in ["hello", "hi", "hey", "howdy"]):
        greeting = get_time_greeting()
        response = f"{greeting} I'm your personal AI assistant! 🤖\n\nI can help you with:\n• 🌤️ Weather information\n• 😄 Programming jokes\n• 📚 Study tips\n• 💪 Motivation\n• 🤓 Coding facts\n• 🧮 Math calculations\n• 📊 Chat statistics\n\nWhat would you like to know?"
    
    # Help
    elif "help" in user_input_lower or "what can you do" in user_input_lower:
        response = """🤖 **I can help you with:**

🌤️ **Weather**: 'What's the weather in [city]?'
😄 **Jokes**: 'Tell me a joke'
📚 **Study tips**: 'Give me a study tip'
💪 **Motivation**: 'I need motivation'
🤓 **Coding facts**: 'Tell me something interesting'
🧮 **Math**: 'Calculate 5 + 3' or 'What is 12 * 8?'
📊 **Stats**: 'How many conversations have we had?'

Just ask me anything! I'm here to help! 🚀"""
    
    # About the creator
    elif any(word in user_input_lower for word in ["who made you", "creator", "developer", "built you"]):
        response = "🎓 I was built by a passionate 2nd year BTech Computer Science (AI & ML) student! This project showcases skills in Python, AI, web development, and data management. Pretty cool, right? 😊"
    
    # Thank you
    elif "thank" in user_input_lower:
        response = "😊 You're absolutely welcome! I'm here to help anytime! Keep learning and coding! 🚀"
    
    # Goodbye
    elif any(bye in user_input_lower for bye in ["bye", "goodbye", "see you", "exit", "quit"]):
        response = "👋 Goodbye! Thanks for chatting with me. Keep coding and stay awesome! 🌟"
    
    # Default response
    else:
        response = """🤔 I'm still learning! Here's what I can help with:

🌤️ Weather info (try: "weather in Delhi")
😄 Jokes (try: "tell me a joke")  
📚 Study tips (try: "study tip")
💪 Motivation (try: "motivate me")
🤓 Fun facts (try: "tell me something cool")
🧮 Math (try: "calculate 15 + 25")

What would you like to try? 🚀"""
    
    # Save this conversation
    save_conversation(user_input, response)
    
    return response

# Test the chatbot in terminal
if __name__ == "__main__":
    print("🤖 " + "="*50)
    print("   PERSONAL AI ASSISTANT v2.0")
    print("   Built by BTech CS AIML Student")
    print("="*50)
    print("\n💡 Try these commands:")
    print("   • weather in [city]")
    print("   • tell me a joke")
    print("   • study tip")
    print("   • motivate me")
    print("   • calculate 5 + 3")
    print("   • tell me something cool")
    print("   • help")
    print("\n   Type 'quit' to exit")
    print("-" * 50)
    
    while True:
        user_input = input(f"\n{get_time_greeting()} You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Bot: 👋 Goodbye! Thanks for chatting! Keep coding! 🚀")
            break
        
        response = chatbot_response(user_input)
        print(f"Bot: {response}")