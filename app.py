import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("🔬 Periodic Table Highlighter")

# Periodic Table Data (simplified layout)
elements = [
# symbol, name, atomic_number, group, period

("H","Hydrogen",1,1,1), ("He","Helium",2,18,1),

("Li","Lithium",3,1,2), ("Be","Beryllium",4,2,2),
("B","Boron",5,13,2), ("C","Carbon",6,14,2),
("N","Nitrogen",7,15,2), ("O","Oxygen",8,16,2),
("F","Fluorine",9,17,2), ("Ne","Neon",10,18,2),

("Na","Sodium",11,1,3), ("Mg","Magnesium",12,2,3),
("Al","Aluminium",13,13,3), ("Si","Silicon",14,14,3),
("P","Phosphorus",15,15,3), ("S","Sulfur",16,16,3),
("Cl","Chlorine",17,17,3), ("Ar","Argon",18,18,3),

("K","Potassium",19,1,4), ("Ca","Calcium",20,2,4),
("Sc","Scandium",21,3,4), ("Ti","Titanium",22,4,4),
("V","Vanadium",23,5,4), ("Cr","Chromium",24,6,4),
("Mn","Manganese",25,7,4), ("Fe","Iron",26,8,4),
("Co","Cobalt",27,9,4), ("Ni","Nickel",28,10,4),
("Cu","Copper",29,11,4), ("Zn","Zinc",30,12,4),
("Ga","Gallium",31,13,4), ("Ge","Germanium",32,14,4),
("As","Arsenic",33,15,4), ("Se","Selenium",34,16,4),
("Br","Bromine",35,17,4), ("Kr","Krypton",36,18,4),

("Rb","Rubidium",37,1,5), ("Sr","Strontium",38,2,5),
("Y","Yttrium",39,3,5), ("Zr","Zirconium",40,4,5),
("Nb","Niobium",41,5,5), ("Mo","Molybdenum",42,6,5),
("Tc","Technetium",43,7,5), ("Ru","Ruthenium",44,8,5),
("Rh","Rhodium",45,9,5), ("Pd","Palladium",46,10,5),
("Ag","Silver",47,11,5), ("Cd","Cadmium",48,12,5),
("In","Indium",49,13,5), ("Sn","Tin",50,14,5),
("Sb","Antimony",51,15,5), ("Te","Tellurium",52,16,5),
("I","Iodine",53,17,5), ("Xe","Xenon",54,18,5),

("Cs","Cesium",55,1,6), ("Ba","Barium",56,2,6),
("La","Lanthanum",57,3,6),
("Ce","Cerium",58,3,8), ("Pr","Praseodymium",59,3,8),
("Nd","Neodymium",60,3,8), ("Pm","Promethium",61,3,8),
("Sm","Samarium",62,3,8), ("Eu","Europium",63,3,8),
("Gd","Gadolinium",64,3,8), ("Tb","Terbium",65,3,8),
("Dy","Dysprosium",66,3,8), ("Ho","Holmium",67,3,8),
("Er","Erbium",68,3,8), ("Tm","Thulium",69,3,8),
("Yb","Ytterbium",70,3,8), ("Lu","Lutetium",71,3,8),

("Hf","Hafnium",72,4,6), ("Ta","Tantalum",73,5,6),
("W","Tungsten",74,6,6), ("Re","Rhenium",75,7,6),
("Os","Osmium",76,8,6), ("Ir","Iridium",77,9,6),
("Pt","Platinum",78,10,6), ("Au","Gold",79,11,6),
("Hg","Mercury",80,12,6), ("Tl","Thallium",81,13,6),
("Pb","Lead",82,14,6), ("Bi","Bismuth",83,15,6),
("Po","Polonium",84,16,6), ("At","Astatine",85,17,6),
("Rn","Radon",86,18,6),

("Fr","Francium",87,1,7), ("Ra","Radium",88,2,7),
("Ac","Actinium",89,3,7),
("Th","Thorium",90,3,9), ("Pa","Protactinium",91,3,9),
("U","Uranium",92,3,9), ("Np","Neptunium",93,3,9),
("Pu","Plutonium",94,3,9), ("Am","Americium",95,3,9),
("Cm","Curium",96,3,9), ("Bk","Berkelium",97,3,9),
("Cf","Californium",98,3,9), ("Es","Einsteinium",99,3,9),
("Fm","Fermium",100,3,9), ("Md","Mendelevium",101,3,9),
("No","Nobelium",102,3,9), ("Lr","Lawrencium",103,3,9),

("Rf","Rutherfordium",104,4,7), ("Db","Dubnium",105,5,7),
("Sg","Seaborgium",106,6,7), ("Bh","Bohrium",107,7,7),
("Hs","Hassium",108,8,7), ("Mt","Meitnerium",109,9,7),
("Ds","Darmstadtium",110,10,7), ("Rg","Roentgenium",111,11,7),
("Cn","Copernicium",112,12,7), ("Nh","Nihonium",113,13,7),
("Fl","Flerovium",114,14,7), ("Mc","Moscovium",115,15,7),
("Lv","Livermorium",116,16,7), ("Ts","Tennessine",117,17,7),
("Og","Oganesson",118,18,7)
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
