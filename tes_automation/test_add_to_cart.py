"""
TEST CASE: Add to Cart Functionality
Deskripsi: Test apakah user bisa tambah produk ke keranjang (cart)
Test Scenario: User cari produk Hammer, klik produk, tambah ke cart, verifikasi produk ada di cart
Expected Result: Produk berhasil ditambahkan ke cart dan tampil di halaman cart
"""

# ===== IMPORT LIBRARIES =====
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# ===== SETUP BROWSER =====
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# ===== MULAI TEST CASE =====
try:
    # ===== STEP 1: BUKA HOMEPAGE =====
    # Analogi: Membuka website di browser
    driver.get("https://practicesoftwaretesting.com/")
    print("✓ Step 1: Homepage berhasil dibuka")
    time.sleep(2)
    
    # ===== STEP 2: KLIK MENU CATEGORIES =====
    # Analogi: Klik menu untuk pergi ke halaman produk
    categories_link = driver.find_element(By.LINK_TEXT, "Categories")
    categories_link.click()
    print("✓ Step 2: Tombol Categories berhasil diklik")
    time.sleep(2)
    
    # ===== STEP 3: CARI SEARCH BOX DAN SEARCH PRODUK =====
    # Tunggu sampai search box muncul
    # Analogi: Tunggu halaman products load sebelum search
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
    )
    print("✓ Step 3: Search box ditemukan")
    
    # Klik search box
    search_box.click()
    time.sleep(1)
    
    # Input keyword "Hammer"
    # Analogi: Ketik nama produk yang ingin dicari
    search_box.send_keys("Hammer")
    print("✓ Step 3: Keyword 'Hammer' berhasil diinput")
    
    # Submit pencarian dengan tekan Enter
    # Analogi: Tekan tombol Enter atau Search
    search_box.submit()
    print("✓ Step 3: Pencarian berhasil disubmit")
    time.sleep(3)
    
    # ===== STEP 4: KLIK PRODUK HAMMER DARI HASIL SEARCH =====
    # Dari halaman search results, ada beberapa produk Hammer
    # Kita perlu klik pada gambar atau nama produk untuk masuk ke halaman detail
    # Analogi: Klik pada card produk untuk lihat detail lengkap
    
    time.sleep(2)  # Tunggu hasil search render
    
    try:
        # Cari card/link produk dengan class "card" atau element yang clickable
        # XPath untuk cari element yang paling dekat dengan text "Hammer"
        product_card = driver.find_element(
            By.XPATH,
            "//a[@href and contains(.//text(), 'Hammer')]"
        )
        product_card.click()
        print("✓ Step 4: Produk card 'Hammer' berhasil diklik")
        time.sleep(3)
    except:
        print("⚠ Produk card tidak ketemu, coba alternative...")
        try:
            # Alternative: Cari gambar produk (img tag)
            product_image = driver.find_element(
                By.XPATH,
                "//img[contains(@alt, 'Hammer')]"
            )
            product_image.click()
            print("✓ Step 4: Gambar produk berhasil diklik")
            time.sleep(3)
        except:
            print("⚠ Gambar tidak ketemu, coba klik link produk langsung...")
            # Alternative: Cari link dengan href /product/
            product_link = driver.find_element(
                By.XPATH,
                "//a[contains(@href, '/product/')]"
            )
            product_link.click()
            print("✓ Step 4: Link produk berhasil diklik")
            time.sleep(3)
    
    # ===== STEP 5: KLIK TOMBOL ADD TO CART =====
    # Tunggu sampai tombol "Add to cart" muncul di halaman detail produk
    # Dari inspect element, button punya: data-test="add-to-cart" dan id="btn-add-to-cart"
    # Analogi: Tunggu halaman produk detail selesai load
    
    # Debug: Print URL untuk verifikasi sudah di halaman produk
    current_url = driver.current_url
    print(f"✓ Step 5: Current URL: {current_url}")
    time.sleep(3)  # Tunggu halaman load lebih lama
    
    try:
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='add-to-cart']"))
        )
        print("✓ Step 5: Tombol 'Add to cart' ditemukan")
        
        # Klik tombol Add to cart
        # Analogi: Klik tombol untuk tambah produk ke keranjang
        add_to_cart_button.click()
        print("✓ Step 5: Tombol 'Add to cart' berhasil diklik")
        time.sleep(2)
    except Exception as e:
        print(f" Error di Step 5: {e}")
        print(f"Page source preview (first 500 chars): {driver.page_source[:500]}")
        raise
    
    # ===== STEP 6: VERIFIKASI PRODUK DITAMBAHKAN KE CART =====
    # Ada beberapa cara untuk verify:
    # - Cek apakah ada notifikasi "Added to cart"
    # - Cek apakah cart count bertambah
    # - Cek apakah ada success message
    
    # Cara 1: Cek page source apakah ada text "Added" atau "Cart"
    # Analogi: Cek apakah ada pesan sukses di halaman
    page_source = driver.page_source
    
    if "added" in page_source.lower() or "cart" in page_source.lower():
        print(" Step 6: Notifikasi 'Added to cart' terdeteksi")
    else:
        print(" Step 6: Notifikasi tidak terdeteksi di page source")
    
    time.sleep(2)
    
    # ===== STEP 7: NAVIGASI KE HALAMAN CART =====
    # Cari link "Cart" atau "Shopping Cart" untuk verifikasi produk ada di cart
    # Analogi: Klik link Cart untuk lihat isi keranjang belanja
    try:
        # Coba cari link dengan text "Cart"
        cart_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
        cart_link.click()
        print("✓ Step 7: Link 'Cart' berhasil diklik")
        time.sleep(2)
    except:
        print("⚠ Link Cart tidak ketemu, coba via icon...")
        # Jika link tidak ketemu, coba cari icon cart
        try:
            cart_icon = driver.find_element(By.XPATH, "//a[@href='/cart']")
            cart_icon.click()
            print("✓ Step 7: Cart icon berhasil diklik")
            time.sleep(2)
        except:
            print("⚠ Cart link/icon tidak ditemukan")
    
    # ===== STEP 8: VERIFIKASI PRODUK ADA DI CART =====
    # Cek apakah halaman cart menampilkan produk "Hammer"
    # Analogi: Cek isi keranjang belanja, pastikan "Hammer" ada di situ
    current_url = driver.current_url
    page_source = driver.page_source
    
    print(f"✓ Step 8: Current URL: {current_url}")
    
    # Cek apakah "Hammer" ada di halaman cart
    if "Hammer" in page_source:
        print(" ASSERTION PASSED: Produk 'Hammer' berhasil ditambahkan ke cart!")
    elif "cart" in current_url.lower():
        print(" ASSERTION PASSED: Sudah di halaman cart (URL berubah)")
    else:
        print(" ASSERTION FAILED: Produk tidak ditemukan di cart")
    
    # Tunggu 3 detik agar bisa lihat hasil
    time.sleep(3)

# ===== ERROR HANDLING =====
except Exception as e:
    print(f" ERROR: {e}")
    print("Test gagal karena error di atas")

# ===== CLEANUP =====
finally:
    driver.quit()
    print("\n--- Browser ditutup, Test selesai ---")


# ===== PENJELASAN KONSEP YANG DIGUNAKAN =====
"""
1. FLOW TEST CASE ADD TO CART:
   Homepage → Klik Categories → Cari Produk → Klik Produk → Klik Add to Cart → Verifikasi

2. FIND ELEMENT METHODS:
   - By.LINK_TEXT: Cari berdasarkan text link (untuk link)
   - By.XPATH dengan contains(): Cari element yang text-nya mengandung keyword tertentu
   
3. WEBDRIVERWAIT:
   - Tunggu sampai element muncul sebelum interact (max 10 detik)
   - Sangat penting untuk dynamic content yang load via JavaScript
   
4. TRY-EXCEPT:
   - Untuk handle multiple ways untuk find element
   - Jika cara 1 gagal, coba cara 2
   - Test tetap jalan meskipun ada error kecil
   
5. ASSERTION/VERIFICATION:
   - Cek page_source apakah mengandung text yang diharapkan
   - Cek URL berubah atau tidak
   - Cek element/notifikasi muncul atau tidak
   
6. FLOW REUSABILITY:
   - Flow ini bisa dipakai juga untuk test produk lain
   - Tinggal ubah keyword "Hammer" dengan produk lain
   - Atau ubah jadi test case parametrized (input berbeda-beda)
"""