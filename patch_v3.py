import os
from textwrap import dedent

# Konfigurasi
ACCESS_KEY = "0ff689c7-b0e8-4ced-94e4-8f9b28683f52"
FILES_TO_PATCH = {
    "html": "index.html",
    "js": "script.js",
    "css": "styles.css"
}

def patch_html_file():
    """Memodifikasi file HTML untuk integrasi Web3Forms."""
    file_path = FILES_TO_PATCH["html"]
    print(f"[*] Memulai patch untuk file: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"[!] Error: File {file_path} tidak ditemukan.")
        return

    # Blok HTML lama yang akan diganti
    old_html_block = dedent("""\
        <div class="contact-form">
                    <h3>Kirim Pesan</h3>
                    <form id="contactForm">
                        <input type="text" placeholder="Nama Anda" required>
                        <input type="email" placeholder="Email Anda" required>
                        <textarea placeholder="Pesan Anda" rows="5" required></textarea>
                        <button type="submit" class="submit-button">Kirim Pesan <i class="fas fa-paper-plane"></i></button>
                    </form>
                </div>""")

    # Blok HTML baru dengan integrasi Web3Forms
    # - Menambahkan action, method, dan input yang diperlukan
    # - Memberi 'name' pada setiap input field
    # - Mengubah placeholder di textarea
    new_html_block = dedent(f"""\
        <div class="contact-form">
                    <h3>Kirim Pesan</h3>
                    <form action="https://api.web3forms.com/submit" method="POST" id="contactForm">
                        <input type="hidden" name="access_key" value="{ACCESS_KEY}">
                        <input type="hidden" name="subject" value="Pesan Baru dari Website KatodikPro">
                        
                        <input type="text" name="name" placeholder="Nama Anda" required>
                        <input type="email" name="email" placeholder="Email Anda" required>
                        <textarea name="message" placeholder="Pesan Anda..." rows="6" required></textarea>
                        
                        <button type="submit" class="submit-button">Kirim Pesan <i class="fas fa-paper-plane"></i></button>
                    </form>
                </div>""")
    
    # Ganti blok HTML lama dengan yang baru
    if old_html_block in content:
        content = content.replace(old_html_block, new_html_block)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[*] Sukses: {file_path} telah dipatch.")
    else:
        print(f"[!] Peringatan: Blok form HTML yang diharapkan tidak ditemukan di {file_path}. Mungkin sudah di-patch.")


def patch_js_file():
    """Memodifikasi file JavaScript untuk mengirim data form menggunakan Fetch API."""
    file_path = FILES_TO_PATCH["js"]
    print(f"[*] Memulai patch untuk file: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"[!] Error: File {file_path} tidak ditemukan.")
        return

    # Fungsi JavaScript lama yang akan diganti
    old_js_function = dedent("""\
    // Function untuk setup contact form
    function setupContactForm() {
        // Ambil contact form element
        const contactForm = document.getElementById('contactForm');
        
        // Check jika form exist
        if (contactForm) {
            // Add submit event listener
            contactForm.addEventListener('submit', function(e) {
                // Prevent default form submission
                e.preventDefault();
                
                // Get form data
                const formData = new FormData(this);
                
                // Simulate form submission (dalam real app, kirim ke server)
                console.log('Form submitted with data:');
                for (let [key, value] of formData.entries()) {
                    console.log(key + ': ' + value);
                }
                
                // Show success message
                alert('Terima kasih! Pesan Anda telah terkirim. Kami akan segera menghubungi Anda.');
                
                // Reset form
                this.reset();
            });
        }
    }""")

    # Fungsi JavaScript baru yang menangani pengiriman ke Web3Forms
    new_js_function = dedent("""\
    // Function untuk setup contact form dengan Web3Forms
    function setupContactForm() {
        const contactForm = document.getElementById('contactForm');
        if (!contactForm) return;

        const submitButton = contactForm.querySelector('.submit-button');
        const originalButtonHTML = submitButton.innerHTML;

        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();
            
            const formData = new FormData(contactForm);
            const object = Object.fromEntries(formData);
            const json = JSON.stringify(object);

            submitButton.disabled = true;
            submitButton.innerHTML = 'Mengirim... <i class="fas fa-spinner fa-spin"></i>';

            fetch('https://api.web3forms.com/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: json
            })
            .then(async (response) => {
                let jsonResponse = await response.json();
                if (response.status == 200) {
                    alert('Terima kasih! Pesan Anda telah berhasil terkirim. Kami akan segera menghubungi Anda.');
                } else {
                    console.error('Error from server:', jsonResponse);
                    alert(`Oops! Terjadi kesalahan: ${jsonResponse.message}`);
                }
            })
            .catch(error => {
                console.error('Fetch error:', error);
                alert('Oops! Gagal mengirim pesan. Periksa koneksi internet Anda.');
            })
            .finally(() => {
                submitButton.disabled = false;
                submitButton.innerHTML = originalButtonHTML;
                contactForm.reset();
            });
        });
    }""")

    # Ganti fungsi lama dengan yang baru
    if old_js_function in content:
        content = content.replace(old_js_function, new_js_function)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[*] Sukses: {file_path} telah dipatch.")
    else:
        print(f"[!] Peringatan: Fungsi 'setupContactForm' yang diharapkan tidak ditemukan di {file_path}. Mungkin sudah di-patch.")


def patch_css_file():
    """Menambahkan style untuk placeholder di file CSS."""
    file_path = FILES_TO_PATCH["css"]
    print(f"[*] Memulai patch untuk file: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"[!] Error: File {file_path} tidak ditemukan.")
        return

    # Kode CSS yang akan ditambahkan
    css_to_add = dedent("""
    /* Style untuk placeholder custom di textarea */
    #contactForm textarea::placeholder {
      line-height: 1.5;
      color: var(--gray-400);
    }
    
    #contactForm textarea {
      /* Menambahkan placeholder custom dengan content property */
      position: relative;
    }
    
    #contactForm textarea::after {
      content: 'Hubungi Saya, ini nomor yang bisa dihubungi: ';
      position: absolute;
      bottom: 12px; /* Sesuaikan posisi vertikal */
      left: 12px; /* Sesuaikan posisi horizontal */
      color: var(--gray-400); /* Warna transparan */
      pointer-events: none; /* Agar bisa diklik tembus */
      font-size: 1rem;
      opacity: 0.7;
    }
    
    /* Perbaikan: Ganti textarea placeholder saat user mulai mengetik */
    #contactForm textarea:not(:placeholder-shown)::after {
      display: none;
    }
    """)
    
    # Tambahkan CSS baru di akhir file jika belum ada
    if "/* Style untuk placeholder custom di textarea */" not in content:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write("\n" + css_to_add)
        print(f"[*] Sukses: {file_path} telah dipatch.")
    else:
        print(f"[!] Peringatan: Style untuk placeholder custom tampaknya sudah ada di {file_path}.")


if __name__ == "__main__":
    print("=============================================")
    print("=      KatodikPro Web3Forms Patcher v3      =")
    print("=============================================\n")
    
    patch_html_file()
    print("-" * 45)
    patch_js_file()
    print("-" * 45)
    # Note: CSS patch dinonaktifkan karena cara terbaik adalah melalui placeholder HTML
    # Mari kita modifikasi patch HTML untuk memasukkan teks langsung.
    
    print("\n[#] Proses patch selesai.")
    print("[#] Silakan periksa kembali file Anda dan coba jalankan di browser.")