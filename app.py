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

selected_po = st.selectbox(
    "Select Purchase Order",
    filtered_df["PO ID"]
)