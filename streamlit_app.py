import streamlit as st
import random
from collections import Counter

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
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

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
    st.button("Szimulációk futtatása", disabled=True)
    st.markdown("**Legalább 2 színt ki kell válaszatni.**")

if startBtn:
    sList = []

    for s in range(nSim):
        resDict = {i:0 for i in range(1, 1+nCols)}

        for r in range(nRepeat):
            ### Run simulation ###
            oneSimRes = [tuple(random.sample(colors, hCols)) for i in range(nCols)]
            
            ### Count matches ###
            countList = Counter(oneSimRes)
            
            ### Store results ###
            for v in countList.values():
                resDict[v] += 1

        ### Calc at least 2 matches ###
        sList.append(resDict)
    
    st.header("Eredmények", divider=True, anchor=False)
    st.markdown("Az eredményeket külön minden szimulációban kiszámoltuk, majd ezeknek vettük az átlagait.")

    noMatch = round((sum([i[1] / nRepeat for i in sList]) / nSim) * 100, 1)
    print([i[1] / nRepeat for i in sList])
    st.markdown(f"Annak az esélye, hogy nincsenek egyező oszlopok {noMatch}%")