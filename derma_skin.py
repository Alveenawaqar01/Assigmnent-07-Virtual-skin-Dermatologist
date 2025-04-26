

# skin_derma_app_ui_upgrade.py

import streamlit as st

# --- Classes ---

class Symptom:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

class Condition:
    def __init__(self, name, related_symptoms, treatment):
        self.name = name
        self.related_symptoms = related_symptoms
        self.treatment = treatment

class DiagnosisEngine:
    def __init__(self, conditions):
        self.conditions = conditions

    def diagnose(self, user_symptoms):
        best_match = None
        max_matches = 0

        for condition in self.conditions:
            matches = len(set(user_symptoms) & set(condition.related_symptoms))
            if matches > max_matches:
                max_matches = matches
                best_match = condition

        return best_match

# --- Symptoms and Conditions ---

redness = Symptom("Redness")
dryness = Symptom("Dryness")
itching = Symptom("Itching")
acne = Symptom("Acne")
scaling = Symptom("Scaling")
rash = Symptom("Rash")
pigmentation = Symptom("Pigmentation")
sensitivity = Symptom("Sensitivity")
blisters = Symptom("Blisters")
swelling = Symptom("Swelling")
flaking = Symptom("Flaking")
pain = Symptom("Pain")
cracks = Symptom("Cracks")
bumps = Symptom("Bumps")

# Conditions
eczema = Condition(
    "Eczema",
    [redness, dryness, itching, flaking, cracks],
    "✅ Moisturize frequently\n✅ Use gentle cleansers\n✅ Apply hydrocortisone creams"
)
acne_vulgaris = Condition(
    "Acne Vulgaris",
    [acne, redness, bumps],
    "✅ Use benzoyl peroxide\n✅ Salicylic acid cleansers\n✅ Dermatologist consultation for medications"
)
psoriasis = Condition(
    "Psoriasis",
    [scaling, redness, dryness, flaking],
    "✅ Coal tar or salicylic acid treatments\n✅ Heavy moisturization\n✅ Phototherapy"
)
melasma = Condition(
    "Melasma",
    [pigmentation, sensitivity],
    "✅ Daily sunscreen\n✅ Vitamin C serums\n✅ Chemical peels (doctor supervised)"
)
contact_dermatitis = Condition(
    "Contact Dermatitis",
    [rash, itching, redness, swelling],
    "✅ Avoid allergens\n✅ Soothe with creams\n✅ Mild steroid creams if prescribed"
)
herpes_simplex = Condition(
    "Herpes Simplex",
    [blisters, pain, swelling],
    "✅ Antiviral creams\n✅ Medical consultation\n✅ Avoid skin contact during flare"
)
athlete_foot = Condition(
    "Athlete's Foot",
    [itching, scaling, cracks, flaking],
    "✅ Use antifungal powder\n✅ Keep feet dry\n✅ Breathable footwear"
)
urticaria = Condition(
    "Urticaria (Hives)",
    [rash, itching, swelling],
    "✅ Antihistamines\n✅ Cool compresses\n✅ Avoid known triggers"
)

conditions = [eczema, acne_vulgaris, psoriasis, melasma, contact_dermatitis, herpes_simplex, athlete_foot, urticaria]

engine = DiagnosisEngine(conditions)

# --- Streamlit App ---

# Page setup
st.set_page_config(page_title="Skin Dermatologist - Virtual Dermatologist", page_icon="🧴", layout="wide")

# Sidebar
with st.sidebar:
    st.title("🧴 Skin Derma")
    st.markdown("##### Your Virtual Dermatologist")
    st.image("https://cdn-icons-png.flaticon.com/512/809/809957.png", width=150)
    st.markdown("---")
    st.write("🔹 Select symptoms\n🔹 Get instant diagnosis\n🔹 Professional advice")

st.markdown("<h1 style='text-align: center; color: #6C63FF;'>🩺 Virtual Skin Dermatologist</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: grey;'>A smart AI-based Dermatology Assistant</h5>", unsafe_allow_html=True)
st.write("## ")

# Symptoms selection
st.subheader("🔍 Select Your Symptoms:")
all_symptoms = [redness, dryness, itching, acne, scaling, rash, pigmentation, sensitivity,
                blisters, swelling, flaking, pain, cracks, bumps]

symptom_options = [symptom.name for symptom in all_symptoms]
selected_symptoms_names = st.multiselect("Which symptoms are you noticing?", symptom_options)

selected_symptoms = [s for s in all_symptoms if s.name in selected_symptoms_names]

# Diagnose
if st.button("🔎 Diagnose My Skin Condition", use_container_width=True):
    st.markdown("---")
    if selected_symptoms:
        diagnosis = engine.diagnose(selected_symptoms)
        if diagnosis:
            st.success(f"🩺 **Possible Condition:** {diagnosis.name}")
            st.markdown(f"### 💊 Recommended Care Plan:\n{diagnosis.treatment}")
        else:
            st.warning("⚠️ No matching skin condition found. Please consult a professional dermatologist.")
    else:
        st.error("❗ Please select at least one symptom.")

# Footer
st.markdown("---")
st.markdown("<center><small>Made with ❤️ for Healthy Skin | Skin Derma 2025</small></center>", unsafe_allow_html=True)
