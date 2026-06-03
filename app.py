import streamlit as st

st.set_page_config(
    page_title = "Perhitungan  Matematika",
    page_icon = ":fire:"
)

with st.sidebar:
    col1, col2, col3, col4, col5 = st.columns([1,2,2,2,1])
    with col2:
        st.image("logo.png")
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilihan Bangun Datar", ["Persegi", "Persegi Panjang", "Lingkaran", "Segitiga", "Trapesium"])
    st.caption("Dibuat dengan :fire: oleh **Cristian Tisya**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung `luas` dan `keliling` persegi")
        sisi = st.number_input("Masukkan Sisi")
        if st.button("Hitung"):
            luas = sisi * sisi
            keliling = 4 * sisi
            #st.success(f"Luas persegi adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2 :
                st.metric("Keliling", value=keliling, border=True)
            st.balloons()


    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung `luas` dan `keliling` persegi panjang")
        panjang = st.number_input("Masukkan Panjang")
        lebar = st.number_input("Masukkan Lebar")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang * lebar)
          #st.success(f"Luas persegi panjang adalah {luas:.2f} dan keliling adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2 :
                st.metric("Keliling", value=keliling, border=True)
            st.balloons()


    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `luas` dan `keliling` lingkaran")
        jarijari = st.number_input("Masukkan Jari-Jari")
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jarijari * jarijari
            keliling = 2 * 3.14 * jarijari
            #st.success(f"Luas lingkaran adalah {luas:.2f} dan kelilinya adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2 :
                st.metric("Keliling", value=keliling, border=True)
            st.balloons()

    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung `luas` dan `keliling` segitiga")

        alas = st.number_input("Masukkan Alas")
        tinggi = st.number_input("Masukkan Tinggi")
        sisi1 = st.number_input("Masukkan Sisi 1")
        sisi2 = st.number_input("Masukkan Sisi 2")
        sisi3 = st.number_input("Masukkan Sisi 3")

        if st.button("Hitung", type="primary"):
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3

        #st.success(f"Luas segitiga adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
        col1, col2, col3, col4, col5 = st.columns([2,2,2,2,2])
        with col1:
                st.metric("Luas", value=luas, border=True)
        with col2 :
                st.metric("Keliling", value=keliling, border=True)
        st.balloons()


    case "Trapesium":
        st.title("Trapesium")
        st.markdown("Menghitung `luas` dan `keliling` trapesium")

        sisi_atas = st.number_input("Masukkan Sisi Atas")
        sisi_bawah = st.number_input("Masukkan Sisi Bawah")
        tinggi = st.number_input("Masukkan Tinggi")
        sisi_miring1 = st.number_input("Masukkan Sisi Miring 1")
        sisi_miring2 = st.number_input("Masukkan Sisi Miring 2")

        if st.button("Hitung", type="primary"):
            luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
            keliling = sisi_atas + sisi_bawah + sisi_miring1 + sisi_miring2

        #st.success(f"Luas trapesium adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
        col1, col2 = st.columns([2,2])
        with col1:
                st.metric("Luas", value=luas, border=True)
        with col2 :
                st.metric("Keliling", value=keliling, border=True)
        st.balloons()
    case _:
        st.error("Terjadi kesalahan")