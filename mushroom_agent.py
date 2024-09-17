import pandas as pd
from langchain import OpenAI, ConversationChain

# Load the mushroom dataset
mushroom_data = pd.read_csv('mushrooms.csv')

# Function to look up mushrooms by region and season
def get_mushrooms_by_region_and_season(region, season):
    mushrooms = mushroom_data[(mushroom_data['region'] == region) & (mushroom_data['season'] == season)]
    if mushrooms.empty:
        return f"No mushrooms found for {region} during {season}."
    return mushrooms[['species', 'edibility', 'description']].to_string(index=False)

# Basic foraging safety tips
def get_foraging_safety_tips():
    return (
        "Foraging Tips:\n"
        "- Never eat a mushroom unless you're 100% sure it's safe.\n"
        "- Avoid mushrooms with white gills, a skirt or ring, and a bulbous or sack-like base.\n"
        "- Always check for poisonous look-alikes.\n"
        "- Carry a mushroom guidebook or use an identification app."
    )

# Initialize LangChain conversational agent
llm = OpenAI(temperature=0.2)
conversation = ConversationChain(llm=llm)

# Main function to handle user input and provide answers
def mushroom_foraging_agent(user_input):
    if "foraging tips" in user_input.lower():
        return get_foraging_safety_tips()
    elif "what mushrooms" in user_input.lower():
        # Example query: "What mushrooms can I find in the Pacific Northwest in fall?"
        region = "Pacific Northwest"  # You can modify to extract region from user input
        season = "Fall"  # Same for season
        return get_mushrooms_by_region_and_season(region, season)
    else:
        return "Sorry, I don't understand that question. Please ask about mushrooms in a region or for foraging tips."

# Example interaction
if __name__ == '__main__':
    print("Welcome to the Mushroom Foraging Assistant!")
    while True:
        user_input = input("Ask a question: ")
        response = mushroom_foraging_agent(user_input)
        print(response)




def parse_user_query(user_input):
    # A simple way to detect region and season from user input (you can improve this later)
    if "Pacific Northwest" in user_input:
        region = "Pacific Northwest"
    else:
        region = "Unknown"
    
    if "fall" in user_input.lower():
        season = "Fall"
    elif "spring" in user_input.lower():
        season = "Spring"
    else:
        season = "Unknown"
    
    return region, season



############## interface

import streamlit as st

st.title("Mushroom Foraging Assistant")

user_input = st.text_input("Ask a question about mushrooms or foraging:")

if st.button('Submit'):
    response = mushroom_foraging_agent(user_input)
    st.write(response)
