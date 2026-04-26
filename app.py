import streamlit as st
from data.gejala import gejala_list
from core.inference import forward_chaining

def show_home_page():
    st.title("Dr. Betta Fisher", text_alignment="center")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("img/cupang.webp", use_container_width=True)
        
    st.markdown("""
    Dr. Betta Fisher, sebuah Sistem Pakar untuk mendeteksi penyakit yang dialami ikan Cupang kesayangan Anda! Hanya dengan **Klik** gejala-gejala yang muncul pada ikan Cupang, Anda langsung mengetahui diagnosis dan solusi penanganan untuk ikan Cupang Anda!
    """, text_alignment='center')

    st.write("")

    st.subheader("Segera Deteksi, Sebelum Terlambat!!!", text_alignment='center')
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Mulai Deteksi", type="primary", use_container_width=True):
            st.session_state.page = 'detection'
            st.rerun()

def show_detection_page():
    st.header("Diagnosa Penyakit", text_alignment='center')
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Kembali ke Beranda", use_container_width=True):
            st.session_state.page = 'home'
            st.rerun()
            
    st.divider()
    st.write("Centang gejala-gejala yang Anda amati pada ikan cupang:")
    
    selected_gejala = []
    
    col1, col2 = st.columns(2)
    half_idx = len(gejala_list) // 2
    
    for i, g in enumerate(gejala_list):
        kode = list(g.keys())[0]
        nama_gejala = g[kode]
        
        if i <= half_idx:
            with col1:
                if st.checkbox(f"{nama_gejala}", key=kode):
                    selected_gejala.append(kode)
        else:
            with col2:
                if st.checkbox(f"{nama_gejala}", key=kode):
                    selected_gejala.append(kode)
                    
    st.divider()
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        deteksi_clicked = st.button("Deteksi Penyakit", type="primary", use_container_width=True)
        
    if deteksi_clicked:
        if len(selected_gejala) == 0:
            st.warning("Silakan pilih minimal satu gejala.")
        else:
            st.subheader("Hasil Deteksi")
            detected_diseases = forward_chaining(selected_gejala)
            
            if detected_diseases:
                st.success(f"Ditemukan {len(detected_diseases)} kemungkinan penyakit.")
                
                for p in detected_diseases:
                    with st.expander(f"Penyakit: {p['nama']}", expanded=True):
                        st.write("**Deskripsi:**")
                        st.info(p['deskripsi'])
                        
                        st.write("**Solusi Penanganan:**")
                        st.success(p['solusi'])
            else:
                st.error("Tidak ada penyakit yang cocok dengan kombinasi gejala tersebut.")

def main():
    st.set_page_config(page_title="Sistem Pakar Ikan Cupang", layout="centered")
    
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    if st.session_state.page == 'home':
        show_home_page()
    elif st.session_state.page == 'detection':
        show_detection_page()

if __name__ == "__main__":
    main()