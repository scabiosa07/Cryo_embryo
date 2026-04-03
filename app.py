import streamlit as st  
from utils import embryo_quality_score, simulate_freezing, thawing_success  
  
st.title("🧪 Virtual Lab: Embryo Cryopreservation")  
  
st.header("Step 1: Select Embryo")  
  
stage = st.selectbox("Embryo Stage", ["Blastocyst", "Cleavage"])  
morphology = st.selectbox("Morphology Quality", ["Good", "Average", "Poor"])  
  
score = embryo_quality_score(stage, morphology)  
st.write(f"Embryo Quality Score: {score}")  
  
st.header("Step 2: Add Cryoprotectant")  
  
cryoprotectant = st.selectbox("Select Cryoprotectant", ["DMSO", "Glycerol"])  
  
st.header("Step 3: Freezing")  
  
temperature = st.slider("Set Freezing Temperature (°C)", -200, 0, -196)  
  
if st.button("Start Freezing Simulation"):  
    survival_rate = simulate_freezing(temperature, cryoprotectant)  
    st.write(f"Post-Freezing Survival Rate: {survival_rate}%")  
  
    result = thawing_success(survival_rate)  
  
    st.header("Step 4: Thawing Result")  
    st.success(f"Result: {result}")  
