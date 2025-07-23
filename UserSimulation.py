from SpeakingPromptGen import generate_prompt_response
import InitializeConversation as ic
import json

# Simulate user input
SkillNum = int(input("Enter the number of skills you want to practice (1-5): "))

Dynamicblock = ""

for i in range(SkillNum):
    S = input(f"Enter skill number {i+1}: ")
    S = S.strip() 
    Dynamicblock += "- " + S + "\n"

print("Dynamic Block:\n" + Dynamicblock)
    
# Generate the prompt response
response = generate_prompt_response(Dynamicblock)

#Jsonify the response

data = json.loads(response)

#Extract sections
briefing = data["briefing"]
objectives = data["objectives"]
spoken_prompt = data["spoken_prompt"]

print (f"\nBriefing: {briefing}")

for i, objective in enumerate(objectives, start=1):
    print(f"Objective {i}: {objective}") 

# Start the conversation session
ic.start_conversation_session(spoken_prompt)
