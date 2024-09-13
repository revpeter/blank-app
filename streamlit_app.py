import streamlit as st
from utils import run_simulations
from numpy import mean

colorList = [
    "Piros",
    "Kék",
    "Zöld",
    "Sárga",
    "Narancssárga",
    "Lila",
    "Rózsaszín",
    "Barna",
    "Fekete",
    "Fehér",
    "Szürke",
    "Bíbor",
    "Babakék",
    "Arany",
    "Ezüst",
    "Türkiz",
    "Mályva",
    "Krém",
    "Olajzöld",
    "Bézs"
]

st.set_page_config(
        page_title="Színes oszlopok",
        page_icon=":rainbow:"
)

st.title(":rainbow: Színes oszlopok problémája")

### Input params ###
with st.container(border=True):
    col1, col2, col3 = st.columns(3)
    nSim = col1.number_input("Szimulációk száma", min_value=1, max_value=20, value=1)
    nRepeat = col2.number_input("Ismétlések száma", min_value=10, max_value=1000000, value=1000)
    nCols = col3.number_input("Oszlopok száma", min_value=1, max_value=10, value=5)

    colors = st.multiselect("Felhasznált szinek", 
                            options=colorList, 
                            max_selections=10, 
                            default=["Piros", "Kék", "Zöld", "Sárga"])

    hCols = len(colors)

### Start button ###
if hCols >= 2:
    startBtn = st.button("Szimulációk futtatása")
else:
    startBtn = st.button("Szimulációk futtatása", disabled=True)
    st.markdown("**Legalább 2 színt ki kell válaszatni.**")

if startBtn:
    exactResults, atleastResults = run_simulations(nSim=nSim, nRepeat=nRepeat, nCols=nCols, hCols=hCols, colors=colors)
    
    st.header("Eredmények", divider=True, anchor=False)
    st.markdown("Az eredményeket külön minden szimulációban kiszámoltuk, majd ezeknek vettük az átlagait.")

    with st.container(border=True):
        noMatch = round(mean(exactResults[0])*100, 1)
        st.markdown(f"Annak az esélye, hogy nincsenek egyező oszlopok: **{noMatch}%**")

    with st.container(border=True):
        for exact_key in list(exactResults.keys())[:-1]:
            someMatch = round(mean(exactResults[exact_key])*100, 1)
            st.markdown(f"Annak az esélye, hogy pontosan {exact_key} oszlop ugyanolyan: **{someMatch}%**")

    with st.container(border=True):
        for atleast_key in atleastResults.keys():
            atleastMatch = round(mean(atleastResults[atleast_key])*100, 1)
            st.markdown(f"Annak az esélye, hogy legalább {atleast_key} oszlop ugyanolyan: **{atleastMatch}%**")