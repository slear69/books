import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("🔬 Periodic Table Highlighter")

# Periodic Table Data (simplified layout)
elements = [
    # symbol, name, atomic_number, group, period
    ("H", "Hydrogen", 1, 1, 1),
    ("He", "Helium", 2, 18, 1),
    ("Li", "Lithium", 3, 1, 2),
    ("Be", "Beryllium", 4, 2, 2),
    ("B", "Boron", 5, 13, 2),
    ("C", "Carbon", 6, 14, 2),
    ("N", "Nitrogen", 7, 15, 2),
    ("O", "Oxygen", 8, 16, 2),
    ("F", "Fluorine", 9, 17, 2),
    ("Ne", "Neon", 10, 18, 2),
    # Add more elements as needed...
]

df = pd.DataFrame(elements, columns=["symbol", "name", "atomic_number", "group", "period"])

# User Input
user_input = st.text_input("Enter Element Name or Symbol (e.g., Oxygen or O):")

# Normalize input
user_input = user_input.strip().capitalize()

# Create figure
fig = go.Figure()

for _, row in df.iterrows():
    color = "lightblue"
    
    # Highlight if match
    if user_input and (
        user_input == row["symbol"] or
        user_input == row["name"]
    ):
        color = "yellow"
    
    fig.add_trace(go.Scatter(
        x=[row["group"]],
        y=[-row["period"]],
        mode="markers+text",
        marker=dict(size=60, color=color, line=dict(color="black", width=1)),
        text=row["symbol"],
        textposition="middle center",
        hovertext=f"{row['name']} ({row['atomic_number']})",
        hoverinfo="text",
        showlegend=False
    ))

fig.update_layout(
    title="Periodic Table",
    xaxis=dict(title="Group", showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(title="Period", showgrid=False, zeroline=False, showticklabels=False),
    plot_bgcolor="white",
    height=600,
)

st.plotly_chart(fig, use_container_width=True)
