import streamlit as st
from transformers import pipeline, set_seed

# Page config
st.set_page_config(page_title="AI Story Generator", page_icon="📖")

# Title
st.title("📖 AI Story Generator")
st.write("Enter a prompt and watch the AI generate a creative story!")

# Input
prompt = st.text_input("🪄 Enter your story prompt:", placeholder="E.g. A robot discovers emotions")

# Seed for reproducibility
seed = st.slider("🎲 Random Seed", 0, 1000, 42)

# Load generator once (caching speeds things up)
@st.cache_resource
def load_generator():
    return pipeline("text-generation", model="gpt2")

generator = load_generator()

# Generate story
if st.button("Generate Story"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        set_seed(seed)
        with st.spinner("Generating story..."):
            story_output = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
        st.success("Here's your AI-generated story:")
        st.write(story_output)
