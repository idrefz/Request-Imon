import streamlit as st
import pandas as pd
from io import StringIO

# Inisialisasi session state
if "data" not in st.session_state:
    st.session_state.data = []

st.title("Form Input Proyek Telkom")

with st.form("form_proyek"):
       tahun = datetime.now().year  # Tahun otomatis    
    unit_bisnis = st.selectbox("UNIT BISNIS", ["SUBDIT CONSUMER FULFILLMENT", "DIVISI PLANNING & DEPLOYMENY", "TELKOM REGIONAL II"
    ])
    task = st.selectbox("TASK", ["HLD", "HLD Non-SW"])
    
    no_kontrak = st.text_input("NO KONTRAK", "")
    additional_project = st.selectbox("ADDITIONAL PROJECT NAME", [
        "BGES 2024 SERANG",
        "OLO(DWS) 2025",
        "OSP FEEDER, PT3",
        "NODE-B 2025",
        "QE UTILITAS 2025",
        "Microdemand 2025",
        "ODP PT2 LOP GABUNGAN 2025",
        "QE AKSES",
        "PT2 TSEL",
        "HARTA KARUN",
        "NIQE"
    ])
    vendor = st.selectbox("VENDOR NAME", ["TELKOM AKSES"])    
    sub_program = st.selectbox("SUB PROGRAM", 
    "HEM BGES", "LME OLO", "NODE B", "QE", "Microdemand", "PT2", "PT3", "NIQE"])    
    id_referensi = st.text_input("ID REFERENSI", "(isi manual)")
    lop_telkom = st.text_input("LOP TELKOM", "(isi manual)")
    detail_lokasi = st.text_input("DETAIL LOKASI", "(isi manual)")

    region = st.selectbox("REGION", ["REGIONAL II"])
    witel = st.selectbox("WITEL", [
        "SERANG", "TANGERANG", "BOGOR", "BEKASI", "BANDUNG", "CIREBON", "SUBANG", "DLL"
    ])
    sto = st.selectbox("STO", [
        "BLJ", "CKA", "CSK", "KRS", "SAG", "TGR", "TJO", "BJO", "CLG", "CWN", "GRL",
        "MER", "PBN", "PSU", "SAM", "BAY", "LBU", "LWD", "MEN", "MLP", "PDG", "RKS",
        "SKE", "BJT", "BRS", "CKD", "CRS", "KMT", "SEG"
    ])
    
    potensi_tematik = st.selectbox("POTENSI TEMATIK", ["FTTH PT 2", "FTTH PT 3", "Node B", "BACKBONE", "OLO", ""])
    capex = st.selectbox("CAPEX", ["Consumer", "Wibs", "Ebis", ""])

    submit = st.form_submit_button("Submit")

if submit:
    new_entry = {
        "TAHUN": tahun,
        "UNIT BISNIS": unit_bisnis,
        "TASK": task,
        "NO KONTRAK": no_kontrak,
        "ADDITIONAL PROJECT NAME": additional_project,
        "VENDOR NAME": vendor,
        "SUB PROGRAM": sub_program,
        "ID REFERENSI": id_referensi,
        "LOP TELKOM": lop_telkom,
        "DETAIL LOKASI": detail_lokasi,
        "REGION": region,
        "WITEL": witel,
        "STO": sto,
        "POTENSI TEMATIK": potensi_tematik,
        "CAPEX": capex
    }
    st.session_state.data.append(new_entry)
    st.success("Data berhasil ditambahkan!")

if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.subheader("Data Input:")
    st.dataframe(df, use_container_width=True)

    # Download CSV
    csv = df.to_csv(index=False)
    st.download_button("Download CSV", data=csv, file_name="data_proyek.csv", mime="text/csv")
