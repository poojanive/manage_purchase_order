import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Manage Purchase Orders",
    page_icon="📦",
    layout="wide"
)


st.title("📦 Manage Purchase Orders")
st.caption("SAP MM | Procurement Dashboard")


col1, col2, col3, col4 = st.columns(4)

col1.metric("📄 Total Purchase Orders", "250")
col2.metric("⏳ Pending Purchase Orders", "35")
col3.metric("💰 High Value Purchase Orders", "12")
col4.metric("💵 Total Procurement Value", "₹2.8 Cr")

st.markdown("---")


# -------------------------------
filter1, filter2, filter3 = st.columns(3)

with filter1:
    supplier = st.selectbox(
        "Supplier",
        ["All Suppliers", "Dell", "HP", "Lenovo"]
    )

with filter2:
    status = st.selectbox(
        "Status",
        ["All Status", "Pending", "Approved", "Rejected"]
    )

with filter3:
    priority = st.selectbox(
        "Priority",
        ["All Priorities", "High", "Medium", "Low"]
    )


data = {
    "PO ID": ["PO1001", "PO1002", "PO1003", "PO1004", "PO1005"],
    "Supplier": ["Dell", "HP", "Lenovo", "Dell", "HP"],
    "Material ID": ["M101", "M102", "M103", "M104", "M105"],
    "Material": ["Laptop", "Monitor", "Keyboard", "Mouse", "Printer"],
    "Quantity": [20, 15, 50, 40, 10],
    "Amount (₹)": [1200000, 850000, 250000, 180000, 500000],
    "Status": ["Pending", "Approved", "Pending", "Rejected", "Pending"],
    "Priority": ["High", "Medium", "High", "Low", "Medium"]
}

df = pd.DataFrame(data)


filtered_df = df.copy()

if supplier != "All Suppliers":
    filtered_df = filtered_df[
        filtered_df["Supplier"] == supplier
    ]

if status != "All Status":
    filtered_df = filtered_df[
        filtered_df["Status"] == status
    ]

if priority != "All Priorities":
    filtered_df = filtered_df[
        filtered_df["Priority"] == priority
    ]

st.markdown("## 📋 Purchase Orders")

st.dataframe(
    filtered_df,
    use_container_width=True
)
st.markdown("---")
st.subheader("🔍 Purchase Order Details")

if len(filtered_df) > 0:

    selected_po = st.selectbox(
        "Select Purchase Order",
        filtered_df["PO ID"]
    )

    selected_row = filtered_df[
        filtered_df["PO ID"] == selected_po
    ].iloc[0]

    st.write("### 📄 Purchase Order Information")

    st.write(f"**PO ID:** {selected_row['PO ID']}")
    st.write(f"**Supplier:** {selected_row['Supplier']}")
    st.write(f"**Material:** {selected_row['Material']}")
    st.write(f"**Material ID:** {selected_row['Material ID']}")
    st.write(f"**Quantity:** {selected_row['Quantity']}")
    st.write(f"**Amount:** ₹{selected_row['Amount (₹)']:,}")
    st.write(f"**Status:** {selected_row['Status']}")
    st.write(f"**Priority:** {selected_row['Priority']}")

    st.markdown("---")
   # -------------------------------
# Procurement Risk Analysis
# -------------------------------
st.markdown("---")
st.subheader("🤖 AI Procurement Risk Analysis")

amount = selected_row["Amount (₹)"]
priority_value = selected_row["Priority"]
status_value = selected_row["Status"]

risk_factors = []

# Check priority
if priority_value == "High":
    risk_factors.append("High priority purchase order")

# Check order value
if amount > 1000000:
    risk_factors.append("High procurement value")

# Check status
if status_value == "Pending":
    risk_factors.append("Purchase order is still pending")

# Generate recommendation
if len(risk_factors) >= 2:
    recommendation = "🚨 Escalate"
    risk_level = "High Risk"

elif len(risk_factors) == 1:
    recommendation = "⚠️ Review"
    risk_level = "Medium Risk"

else:
    recommendation = "✅ Approve"
    risk_level = "Low Risk"

# Display recommendation
st.success(f"### Recommendation: {recommendation}")

st.write(f"**Risk Level:** {risk_level}")

# Display factors
st.write("### 🔎 Decision Factors")

for factor in risk_factors:
    st.write(f"• {factor}")

if not risk_factors:
    st.write("• No major risk factors identified.")

# Explain the decision
st.info(
    "The recommendation is generated using the selected "
    "purchase order's priority, procurement value and status."
)
# -------------------------------
# Purchase Order Actions
# -------------------------------
st.markdown("---")
st.subheader("⚡ Purchase Order Actions")

action1, action2, action3 = st.columns(3)

with action1:
    if st.button(
        "✅ Approve Purchase Order",
        use_container_width=True
    ):
        st.success(
            f"{selected_po} has been approved successfully."
        )

with action2:
    if st.button(
        "❌ Reject Purchase Order",
        use_container_width=True
    ):
        st.error(
            f"{selected_po} has been rejected."
        )

with action3:
    if st.button(
        "🚨 Escalate Purchase Order",
        use_container_width=True
    ):
        st.warning(
            f"{selected_po} has been escalated to the Procurement Head."
        )