# main_app.py
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Pusat Belajar Agraria",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- App Content (Functions for each page) ---

def home_page():
    """Displays the home page of the application."""
    st.title("🌿 Pembelajaran Agraria Digital")
    st.markdown("---")
    st.header("Selamat Datang di Platform Edukasi Agraria Indonesia")
    
    st.write(
        """
        Aplikasi ini dirancang untuk menjadi sumber informasi utama Anda mengenai seluk-beluk pertanahan dan agraria di Indonesia. 
        Baik Anda seorang mahasiswa, praktisi hukum, pemilik tanah, atau masyarakat umum yang ingin tahu, kami menyediakan materi yang mudah dipahami.
        """
    )
    
    st.image("https://www.shutterstock.com/id/image-vector/vector-sketch-green-grass-field-on-2476632733",
             caption="Agraria adalah tentang hubungan manusia dengan tanah, air, dan sumber daya alam.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Apa yang Anda Temukan di Sini?")
        st.info(
            """
            - **Konsep Dasar:** Pengertian fundamental agraria dan jenis-jenis hak atas tanah.
            - **Sejarah:** Perjalanan hukum agraria dari masa kolonial hingga reformasi.
            - **Pendaftaran Tanah:** Panduan langkah demi langkah untuk mendaftarkan tanah Anda.
            - **Kuis Interaktif:** Uji pemahaman Anda tentang materi yang telah dipelajari.
            """
        )
    with col2:
        st.subheader("Mengapa Belajar Agraria Penting?")
        st.warning(
            """
            Memahami agraria berarti memahami hak dan kewajiban atas tanah yang kita pijak. Ini adalah kunci untuk kepastian hukum, menghindari sengketa, 
            dan berpartisipasi dalam pembangunan nasional yang berkeadilan.
            """
        )
    
    st.markdown("---")
    st.write("Gunakan menu di sebelah kiri untuk mulai menjelajahi topik yang Anda minati.")


def basic_concepts_page():
    """Displays the page for basic agrarian concepts."""
    st.header("Konsep Dasar Agraria")
    st.markdown("Memahami fondasi hukum pertanahan di Indonesia.")
    st.markdown("---")

    st.subheader("Apa itu Hukum Agraria?")
    st.write(
        """
        Hukum Agraria adalah keseluruhan kaidah hukum, baik yang tertulis maupun tidak tertulis, yang mengatur hubungan antara manusia dengan bumi, air, ruang angkasa, 
        dan kekayaan alam yang terkandung di dalamnya. Landasan utamanya adalah **Undang-Undang Pokok Agraria (UUPA) No. 5 Tahun 1960**.
        """
    )

    st.subheader("Jenis-Jenis Hak Atas Tanah")
    st.write("UUPA mengklasifikasikan beberapa jenis hak atas tanah yang utama, antara lain:")
    
    # Using expanders to keep the UI clean
    with st.expander("1. Hak Milik (HM)"):
        st.markdown(
            """
            - **Definisi:** Hak terkuat dan terpenuh yang dapat dipunyai orang atas tanah.
            - **Sifat:** Dapat diwariskan, dapat dialihkan (dijual, dihibahkan), dan dapat dijadikan jaminan utang (hak tanggungan).
            - **Subjek:** Hanya Warga Negara Indonesia (WNI) tunggal. Badan hukum tidak dapat memiliki Hak Milik.
            """
        )
    
    with st.expander("2. Hak Guna Usaha (HGU)"):
        st.markdown(
            """
            - **Definisi:** Hak untuk mengusahakan tanah yang dikuasai langsung oleh Negara.
            - **Tujuan:** Untuk usaha pertanian, perikanan, atau peternakan.
            - **Jangka Waktu:** Maksimal 25 atau 35 tahun dan dapat diperpanjang.
            - **Subjek:** WNI dan badan hukum yang didirikan menurut hukum Indonesia.
            """
        )

    with st.expander("3. Hak Guna Bangunan (HGB)"):
        st.markdown(
            """
            - **Definisi:** Hak untuk mendirikan dan mempunyai bangunan di atas tanah yang bukan miliknya sendiri.
            - **Tanah Objek:** Tanah Negara atau Tanah Hak Milik.
            - **Jangka Waktu:** Maksimal 30 tahun dan dapat diperpanjang.
            - **Subjek:** WNI dan badan hukum yang didirikan menurut hukum Indonesia.
            """
        )

    with st.expander("4. Hak Pakai"):
        st.markdown(
            """
            - **Definisi:** Hak untuk menggunakan dan/atau memungut hasil dari tanah yang dikuasai langsung oleh Negara atau tanah milik orang lain.
            - **Sifat:** Lebih fleksibel dibandingkan hak lain, bisa diberikan untuk jangka waktu tertentu atau selama tanahnya dipergunakan untuk tujuan tertentu.
            - **Subjek:** WNI, orang asing yang berkedudukan di Indonesia, badan hukum Indonesia, dan badan hukum asing yang punya perwakilan di Indonesia.
            """
        )

def history_page():
    """Displays the page for Indonesian agrarian history."""
    st.header("Sejarah Singkat Hukum Agraria Indonesia")
    st.markdown("Dari dualisme hukum kolonial menuju unifikasi hukum nasional.")
    st.markdown("---")

    st.subheader("1. Masa Kolonial Belanda (Sebelum 1960)")
    st.write(
        """
        Pada masa ini, hukum pertanahan bersifat **dualisme**. Artinya, ada dua sistem hukum yang berjalan bersamaan:
        - **Hukum Adat:** Berlaku bagi penduduk pribumi (Indonesia Asli). Bersifat komunal dan tidak tertulis.
        - **Hukum Barat:** Berdasarkan *Burgerlijk Wetboek* (BW) dan *Agrarische Wet 1870*. Berlaku bagi orang Eropa, Tionghoa, dan Timur Asing lainnya. Ini menciptakan ketidakpastian dan ketidakadilan hukum.
        """
    )

    st.subheader("2. Lahirnya UUPA (24 September 1960)")
    st.write(
        """
        Tanggal 24 September diperingati sebagai Hari Tani Nasional. Pada tanggal ini, UUPA No. 5 Tahun 1960 diundangkan.
        Tujuan utama UUPA adalah:
        - **Unifikasi Hukum:** Mengakhiri dualisme hukum dengan menciptakan satu sistem hukum agraria nasional yang berdasarkan hukum adat.
        - **Kepastian Hukum:** Memberikan jaminan kepastian hukum mengenai hak-hak atas tanah bagi seluruh rakyat Indonesia.
        - **Fungsi Sosial Tanah:** Menegaskan bahwa setiap hak atas tanah memiliki fungsi sosial, artinya penggunaannya harus disesuaikan dengan kepentingan masyarakat.
        """
    )
    st.success("Prinsip utama UUPA adalah 'Tanah untuk Kesejahteraan Rakyat'.")

    st.subheader("3. Masa Reformasi dan Reforma Agraria")
    st.write(
        """
        Setelah era reformasi 1998, agenda **Reforma Agraria** kembali menguat. Tujuannya adalah untuk menata ulang struktur kepemilikan, penguasaan, dan penggunaan tanah agar lebih berkeadilan.
        Program utamanya meliputi:
        - **Legalisasi Aset:** Pendaftaran tanah secara massal (misalnya melalui program PTSL).
        - **Redistribusi Tanah:** Pembagian tanah-tanah negara kepada petani penggarap.
        """
    )


def registration_page():
    """Displays the page for the land registration process."""
    st.header("Panduan Pendaftaran Tanah Pertama Kali")
    st.markdown("Langkah demi langkah untuk mendapatkan Sertipikat Hak Atas Tanah.")
    st.markdown("---")
    
    st.info("Proses ini dilakukan di Kantor Pertanahan (BPN/ATR) sesuai lokasi tanah.")

    st.subheader("Langkah 1: Persiapan Dokumen")
    st.write("Siapkan dokumen-dokumen berikut:")
    st.code(
        """
        - Formulir permohonan yang sudah diisi dan ditandatangani.
        - Surat Kuasa (jika dikuasakan).
        - Fotokopi identitas (KTP, KK) pemohon.
        - Dokumen bukti kepemilikan tanah (alas hak), bisa berupa:
          - Girik / Letter C
          - Akta Jual Beli (AJB)
          - Surat Waris
          - Putusan Pengadilan
        - Dokumen perpajakan terkait (SPPT PBB tahun berjalan).
        """, language='text'
    )

    st.subheader("Langkah 2: Mengajukan Permohonan di Kantor Pertanahan")
    st.write("Datang ke loket pendaftaran, serahkan semua dokumen. Anda akan mendapatkan bukti penerimaan berkas dan rincian biaya yang harus dibayar.")

    st.subheader("Langkah 3: Pengukuran Tanah")
    st.write("Petugas dari Kantor Pertanahan akan datang ke lokasi untuk melakukan pengukuran dan pemetaan tanah. Pastikan Anda atau perwakilan Anda hadir dan menunjukkan batas-batas tanah.")

    st.subheader("Langkah 4: Pengumuman (Publikasi Data Yuridis)")
    st.write("Data permohonan Anda (nama, luas, lokasi, status tanah) akan diumumkan di Kantor Pertanahan dan/atau kantor desa/kelurahan selama 60 hari. Tujuannya adalah memberi kesempatan jika ada pihak lain yang merasa berkeberatan.")

    st.subheader("Langkah 5: Penerbitan Sertipikat")
    st.write("Jika tidak ada sanggahan atau keberatan selama masa pengumuman, Kantor Pertanahan akan menerbitkan Sertipikat Hak Atas Tanah atas nama Anda.")
    st.success("Selamat! Tanah Anda kini telah terdaftar secara resmi dan memiliki kepastian hukum.")


def quiz_page():
    """Displays a simple quiz page."""
    st.header("📝 Kuis Cepat Agraria")
    st.markdown("Uji sejauh mana pemahaman Anda!")
    st.markdown("---")

    # Questions and answers data structure
    quiz_data = [
        {
            "question": "Apa landasan hukum utama agraria di Indonesia?",
            "options": ["Burgerlijk Wetboek (BW)", "Undang-Undang Pokok Agraria (UUPA) 1960", "KUHP", "UU Cipta Kerja"],
            "answer": "Undang-Undang Pokok Agraria (UUPA) 1960"
        },
        {
            "question": "Hak atas tanah yang terkuat dan terpenuh adalah...",
            "options": ["Hak Guna Bangunan (HGB)", "Hak Pakai", "Hak Milik (HM)", "Hak Guna Usaha (HGU)"],
            "answer": "Hak Milik (HM)"
        },
        {
            "question": "Instansi pemerintah yang berwenang mengurus pendaftaran tanah adalah...",
            "options": ["Kantor Pajak", "Kantor Kecamatan", "Kantor Pertanahan (BPN/ATR)", "Kantor Notaris"],
            "answer": "Kantor Pertanahan (BPN/ATR)"
        },
        {
            "question": "Tujuan utama dari UUPA adalah mengakhiri... hukum di bidang pertanahan.",
            "options": ["Monopoli", "Pluralisme", "Dualisme", "Sentralisme"],
            "answer": "Dualisme"
        }
    ]

    # Using a form to submit all answers at once
    with st.form("quiz_form"):
        user_answers = []
        for i, item in enumerate(quiz_data):
            st.subheader(f"Pertanyaan {i+1}:")
            st.write(item["question"])
            answer = st.radio(
                "Pilih jawaban Anda:",
                item["options"],
                key=f"q{i}"
            )
            user_answers.append(answer)
        
        submitted = st.form_submit_button("Kirim Jawaban")

    if submitted:
        score = 0
        for i, item in enumerate(quiz_data):
            if user_answers[i] == item["answer"]:
                score += 1
        
        st.markdown("---")
        st.header("Hasil Kuis Anda")
        st.write(f"Anda menjawab benar {score} dari {len(quiz_data)} pertanyaan.")
        
        percentage = (score / len(quiz_data)) * 100
        if percentage == 100:
            st.balloons()
            st.success(f"Luar biasa! Skor Anda {percentage:.0f}%. Anda sangat paham materi dasar agraria!")
        elif percentage >= 75:
            st.info(f"Bagus! Skor Anda {percentage:.0f}%. Pemahaman Anda sudah baik.")
        else:
            st.warning(f"Skor Anda {percentage:.0f}%. Coba pelajari lagi materinya dan ulangi kuisnya!")


# --- Sidebar Navigation ---
st.sidebar.title("Menu Navigasi")
page_options = {
    "🏠 Beranda": home_page,
    "📖 Konsep Dasar": basic_concepts_page,
    "📜 Sejarah Agraria": history_page,
    "✒️ Pendaftaran Tanah": registration_page,
    "✒️ Survey dan Pengukuran Tanah": registration_page,
    "✒️ Penataan dan Pemberdayaan Pertanahan": registration_page,
    "✒️ Pengadaan Tanah": registration_page,
    "✒️ Sengketa dan Konflik Tanah": registration_page,
    "📝 Kuis Cepat": quiz_page
}

selection = st.sidebar.radio("Pilih Halaman:", list(page_options.keys()))

# --- Display the selected page ---
page_function = page_options[selection]
page_function()

# --- Footer in Sidebar ---
st.sidebar.markdown("---")
st.sidebar.info(
    "Aplikasi ini dibuat untuk tujuan edukasi. "
    "Untuk kasus hukum spesifik, konsultasikan dengan profesional."
)
st.sidebar.markdown("Dibuat dengan ❤️ menggunakan **Streamlit**.")
