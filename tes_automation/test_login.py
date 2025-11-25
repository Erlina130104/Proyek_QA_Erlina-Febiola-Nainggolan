"""
TEST CASE: Login Functionality
Deskripsi: Test apakah user bisa login dengan email dan password yang benar
Expected Result: User berhasil login dan dialihkan ke dashboard
"""

# ===== IMPORT LIBRARIES =====
# Import webdriver untuk kontrol browser otomatis
from selenium import webdriver

# Import By untuk menemukan elemen di website (seperti "cari" di Find & Replace)
from selenium.webdriver.common.by import By

# Import WebDriverWait untuk tunggu elemen muncul sebelum klik
from selenium.webdriver.support.ui import WebDriverWait

# Import expected_conditions untuk set kondisi tunggu yang spesifik
from selenium.webdriver.support import expected_conditions as EC

# Import ChromeDriverManager untuk auto download ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

# Import Service untuk setup ChromeDriver
from selenium.webdriver.chrome.service import Service

# Import time untuk pause (delay) antar action
import time

# ===== SETUP BROWSER =====
# Buat object Service dengan ChromeDriver yang sudah didownload otomatis
# Analogi: Service = instruktur yang akan mengontrol robot (browser)
service = Service(ChromeDriverManager().install())

# Buka browser Chrome kosong
# Analogi: Membuka jendela browser baru seperti Anda klik ikon Chrome
driver = webdriver.Chrome(service=service)

# ===== MULAI TEST CASE =====
try:
    # STEP 1: Buka website
    # Analogi: Ketik URL di address bar dan tekan Enter
    driver.get("https://practicesoftwaretesting.com/")
    print("✓ Step 1: Website berhasil dibuka")
    
    # Tunggu 2 detik agar website selesai load semua elemen
    # Analogi: Tunggu loading bar di website selesai sebelum mulai klik
    time.sleep(2)
    
    # ===== STEP 2: KLIK BUTTON LOGIN =====
    # Cari element/tombol dengan text "Sign in"
    # By.LINK_TEXT = cari berdasarkan text link (tombol yang bisa diklik)
    # Analogi: Cari tombol login di halaman menggunakan "Find" kemudian klik
    sign_in_link = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in_link.click()
    print("✓ Step 2: Tombol Sign in berhasil diklik")
    
    # Tunggu halaman login load sebelum lanjut
    time.sleep(2)
    
    # ===== STEP 3: INPUT EMAIL =====
    # Cari textbox email berdasarkan ID attribute
    # By.ID = cari berdasarkan ID (identitas unik element di HTML)
    # Analogi: Cari textbox email menggunakan "inspect element" dan liat ID-nya
    email_input = driver.find_element(By.ID, "email")
    
    # Klik textbox untuk fokus (opsional, tapi praktik baik)
    email_input.click()
    
    # Ketik email ke dalam textbox
    # send_keys() = simulates mengetik di keyboard
    # Analogi: Klik textbox email lalu ketik email address
    email_input.send_keys("customer@practicesoftwaretesting.com")
    print("✓ Step 3: Email berhasil diinput")
    
    # ===== STEP 4: INPUT PASSWORD =====
    # Cari textbox password berdasarkan ID
    password_input = driver.find_element(By.ID, "password")
    
    # Klik textbox untuk fokus
    password_input.click()
    
    # Ketik password
    # Analogi: Klik textbox password lalu ketik password
    password_input.send_keys("welcome01")
    print("✓ Step 4: Password berhasil diinput")
    
    # ===== STEP 5: KLIK TOMBOL LOGIN =====
    # Cari button submit/login berdasarkan data-test attribute
    # By.CSS_SELECTOR = cari berdasarkan CSS selector (bisa pakai attribute apapun)
    # Analogi: Cari element menggunakan "Find & Replace" dengan pattern khusus
    login_button = driver.find_element(By.CSS_SELECTOR, "[data-test='login-submit']")
    
    # Klik button login
    # Analogi: Klik tombol "Masuk" setelah input email dan password
    login_button.click()
    print("✓ Step 5: Tombol Login berhasil diklik")
    
    # Tunggu halaman redirect setelah login
    time.sleep(3)
    
    # ===== STEP 6: VERIFY LOGIN BERHASIL =====
    # Tunggu halaman selesai load setelah login (max 10 detik)
    time.sleep(3)
    
    # Print current page URL dan title untuk debug
    current_url = driver.current_url
    page_title = driver.title
    print(f"✓ Step 6: Current URL: {current_url}")
    print(f"✓ Step 6: Page Title: {page_title}")
    
    # ===== ASSERTION (VERIFIKASI HASIL) =====
    # Cek apakah URL berubah (redirect ke dashboard/account page)
    # Jika URL berubah dari /auth/login ke /account atau lainnya = login berhasil
    if "/auth/login" not in current_url:
        print("✅ TEST PASSED: Login berhasil! URL berubah ke:", current_url)
    else:
        print("❌ TEST FAILED: Login gagal, masih di halaman login")
    
    # Tunggu 3 detik agar bisa lihat hasil sebelum browser tutup
    time.sleep(3)

# ===== ERROR HANDLING =====
# Jika ada error saat menjalankan test, tampilkan error message
except Exception as e:
    print(f"❌ ERROR: {e}")
    print("Test gagal karena error di atas")

# ===== CLEANUP =====
# Tutup browser setelah test selesai
# Analogi: Tutup jendela browser seperti klik tombol X
finally:
    driver.quit()
    print("\n--- Browser ditutup, Test selesai ---")


# ===== PENJELASAN SINGKAT SETIAP KONSEP =====
"""
1. FIND ELEMENT (Mencari Element)
   - By.ID: Cari berdasarkan ID unik (paling akurat)
   - By.NAME: Cari berdasarkan nama attribute
   - By.LINK_TEXT: Cari berdasarkan text link
   - By.CLASS_NAME: Cari berdasarkan CSS class
   - By.XPATH: Cari berdasarkan path (paling kompleks tapi fleksibel)

2. SEND_KEYS (Ketik Text)
   - send_keys("text") = ketik text ke textbox
   - Analogi: Seperti Anda ketik di keyboard

3. CLICK (Klik Element)
   - click() = klik element (button, link, checkbox, dll)
   - Analogi: Seperti Anda klik mouse

4. WEBDRIVERWAIT (Tunggu Element)
   - WebDriverWait(driver, 10) = tunggu maksimal 10 detik
   - EC.presence_of_elements_located = tunggu sampai element muncul
   - Analogi: Jangan langsung klik sebelum page selesai load

5. ASSERTION (Verifikasi)
   - if condition: test PASS
   - else: test FAIL
   - Analogi: Verifikasi apakah hasil sesuai dengan yang diharapkan
"""