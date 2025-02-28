import streamlit as st

if 'names_scores' not in st.session_state:
    st.session_state.names_scores = {}

st.write("Peer Ranker")

name = st.text_input("Enter a Cadet")

# Categories to rate
categories = ["Job Knowledge", "Leadership Skills", "Professional Qualities","Organisational Skills", "Judgment and Decisions","Communication Skills"]
# Get ratings for each category
ratings = {}
if name:
    st.subheader(f"Rate {name}")
    for category in categories:
        rating = st.slider(f"Rate {category} (1-5):", 1, 5, 3)
        ratings[category] = rating

    if st.button("Submit Rating"):
        total_score = sum(ratings.values())
        st.session_state.names_scores[name] = total_score
        st.success(f"Submitted {name} with total score: {total_score}")

# Display ranked names
if st.session_state.names_scores:
    st.subheader("Ranked Names")
    ranked_names = sorted(st.session_state.names_scores.items(), key=lambda x: x[1], reverse=True)
    for rank, (name, score) in enumerate(ranked_names, start=1):
        st.write(f"{rank}. {name}: {score}")


