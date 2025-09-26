import streamlit as st
import pandas as pd

# Initialize session state
if "patients" not in st.session_state:
    st.session_state["patients"] = []

st.title("🧾 Patient Payment Tracker")

# Form to add patient
with st.form("add_patient"):
    name = st.text_input("Patient Name")
    payment = st.number_input("Amount Paid (₱)", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Add Payment")
    if submitted and name:
        st.session_state["patients"].append({"Name": name, "Amount": payment})
        st.success(f"Added {name} - ₱{payment:.2f}")

# Show patient table
if st.session_state["patients"]:
    df = pd.DataFrame(st.session_state["patients"])
    st.write("### Patient List")
    st.dataframe(df)

    # Dropdown to delete a wrong entry
    delete_index = st.selectbox(
        "🗑️ Select an entry to delete",
        options=range(len(df)),
        format_func=lambda x: f"{df.iloc[x]['Name']} – ₱{df.iloc[x]['Amount']:.2f}"
    )
    if st.button("Delete Selected Entry"):
        removed = st.session_state["patients"].pop(delete_index)
        st.warning(f"Deleted {removed['Name']} (₱{removed['Amount']:.2f})")

    # Total
    total = sum(p["Amount"] for p in st.session_state["patients"])
    st.markdown(f"💰 **Total Collected:** ₱{total:,.2f}")
