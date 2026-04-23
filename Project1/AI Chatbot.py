import time

def start_chatbot():
    print("--- DecodeLabs Rule-Based AI Interface ---")
    print("(Type 'exit' or 'bye' to close the session)\n")
    
    while True:
        user_text = input("You: ")
        clean_input = user_text.lower().strip()
        
        # 1. EXIT LOGIC
        exit_words = ["bye", "exit", "quit", "shukriya", "thank you", "allah hafiz","khuda hafiz","goodbye","see you later","take care","fare well","adios","au reveir","sayonara","zai jian","annyeonghi gaseyo"]
        if any(word in clean_input for word in exit_words):
            print("Chatbot: Thinking...")
            time.sleep(0.5)
            print("Chatbot: Goodbye! System shutting down. Have a great day!")
            break
        
        # 2. HOW ARE YOU LOGIC (Isay upar le aaye hain taake ye akele bhi kaam kare)
        elif any(word in clean_input for word in ["how are you", "kaise ho", "kya haal hai", "whats up", "how r u"]):
            response = "I'm doing great, functioning at 100% efficiency! How about you?"

        # 3. GREETINGS
        elif any(word in clean_input for word in ["hello", "hi", "hye", "hey","greetings","namaste", "salam","assalamualaikum","namasta","radha radha","parnam","pranam","vanakkam","satsriakal","shalom","bonjour","hola","ciao","konnichiwa","sawubona","merhaba","shalom aleichem","sawasdee","sawadeekap","ne hao","anaya","annyeong"]):
            response = "Hello! I am your DecodeLabs assistant. How can I help you today?"
            
        # 4. PROJECT LOGIC
        elif any(word in clean_input for word in ["project", "task", "about project", "working on", "assignment", "work"]):
            response = "This is Task 1: A Rule-Based AI Chatbot designed to demonstrate Python control flow."
            
        # 5. IDENTITY LOGIC
        elif any(word in clean_input for word in ["who are you", "what are you doing here","what are you doing", "introduce yourself", "your purpose", "your role", "who created you", "who developed you"]):
            response = "I am a Rule-Based AI bot developed by Mahnoor Fatima for the DecodeLabs Internship 2026."
            
        else:
            response = "I'm sorry, I don't have a rule for that yet. Could you try asking about the project?"

        # Output
        print("Chatbot: Processing...")
        time.sleep(0.5)
        print(f"Chatbot: {response}\n")

if __name__ == "__main__":
    start_chatbot()
