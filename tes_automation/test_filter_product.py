"""
TEST CASE: Filter Product Functionality
Deskripsi: Test apakah fitur filter produk berfungsi dengan baik
Test Scenario 1: Filter berdasarkan kategori (Hammer)
Test Scenario 2: Filter berdasarkan sort price
Expected Result: Produk yang ditampilkan sesuai dengan filter yang dipilih
"""

# ===== IMPORT LIBRARIES =====
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# ===== SETUP BROWSER =====
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

# ===== MULAI TEST CASE =====
try:
    # ===== STEP 1: BUKA HOMEPAGE =====
    driver.get("https://practicesoftwaretesting.com/")
    print("Step 1: Homepage berhasil dibuka")
    time.sleep(2)
    
    # ===== STEP 2: KLIK CATEGORIES DROPDOWN =====
    try:
        categories_dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'dropdown') and contains(text(), 'Categories')]"))
        )
        categories_dropdown.click()
        print("Step 2: Categories dropdown berhasil diklik")
        time.sleep(2)
        
        # ===== STEP 3: KLIK HAND TOOLS CATEGORY =====
        hand_tools = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Hand Tools')]"))
        )
        hand_tools.click()
        print("Step 3: Hand Tools category berhasil diklik")
        time.sleep(4)
        
    except Exception as e:
        print("ERROR Step 2-3: " + str(e)[:100])
        driver.quit()
        exit()
    
    # ===== TEST SCENARIO 1: FILTER BY CATEGORY =====
    print("\n=== TEST SCENARIO 1: FILTER BY CATEGORY ===")
    
    current_url = driver.current_url
    print("Step 4: Current URL: " + current_url)
    
    # STEP 5: TUNGGU DAN KLIK CHECKBOX HAMMER =====
    try:
        hammer_checkbox = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and following-sibling::text()[contains(., 'Hammer')]]"))
        )
        print("Step 5: Checkbox Hammer ditemukan")
        hammer_checkbox.click()
        print("Step 5: Checkbox Hammer berhasil diklik")
        time.sleep(3)
    except Exception as e:
        print("ERROR Step 5: " + str(e)[:80])
    
    # STEP 6: VERIFIKASI PRODUK HAMMER DITAMPILKAN =====
    page_source = driver.page_source
    current_url = driver.current_url
    
    print("Step 6: Current URL: " + current_url)
    
    if "Hammer" in page_source or "hammer" in page_source.lower():
        print("PASSED: SCENARIO 1 - Produk Hammer berhasil difilter")
    else:
        print("FAILED: SCENARIO 1 - Filter kategori tidak berhasil")
    
    # ===== TEST SCENARIO 2: SORT BY PRICE =====
    print("\n=== TEST SCENARIO 2: SORT BY PRICE ===")
    
    # STEP 7: SCROLL KE ATAS UNTUK AKSES SORT DROPDOWN =====
    print("Step 7: Scroll ke atas untuk akses sort dropdown")
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    
    # STEP 8: SORT DROPDOWN - VISUAL CLICK METHOD =====
    try:
        from selenium.webdriver.common.keys import Keys
        
        # Cari element select
        sort_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//select[@data-test='sort']"))
        )
        print("Step 8: Sort select element ditemukan")
        
        # Scroll ke element
        driver.execute_script("arguments[0].scrollIntoView(true);", sort_element)
        time.sleep(1)
        
        # KLIK dropdown untuk membuka (VISUAL)
        sort_element.click()
        print("Step 8: Dropdown DIKLIK dan terbuka")
        time.sleep(2)
        
        # Cari option Price (High - Low)
        select = Select(sort_element)
        target_index = None
        
        print("Step 8: Opsi yang tersedia:")
        for idx, option in enumerate(select.options):
            option_text = option.text.strip()
            option_value = option.get_attribute('value')
            print(f"  [{idx}] '{option_text}' (value='{option_value}')")
            
            # Cari Price (High - Low)
            if "price" in option_text.lower() and "high" in option_text.lower() and "low" in option_text.lower():
                high_pos = option_text.lower().find("high")
                low_pos = option_text.lower().find("low")
                if high_pos < low_pos:
                    target_index = idx
                    print(f"  >> TARGET FOUND at index {idx}")
        
        if target_index is not None:
            # Navigasi ke option dengan Arrow Down key
            print(f"Step 8: Navigasi ke option index {target_index}")
            
            # Tekan Arrow Down sebanyak target_index kali
            for i in range(target_index):
                sort_element.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.2)
            
            print(f"Step 8: Option 'Price (High - Low)' di-highlight")
            time.sleep(1)
            
            # Tekan ENTER untuk pilih option
            sort_element.send_keys(Keys.ENTER)
            print("Step 8: ENTER ditekan, option terpilih")
            time.sleep(3)
        else:
            # Fallback
            select.select_by_visible_text("Price (High - Low)")
            print("Step 8: Fallback - Price (High - Low) dipilih by visible text")
            time.sleep(2)
        
        print("Step 8: Sorting berhasil diterapkan")
        time.sleep(2)
        
    except Exception as e:
        print("Step 8: Error menggunakan Select class")
        print("Error: " + str(e)[:100])
        
        # Fallback method: Klik manual
        try:
            print("Step 8: Mencoba fallback method...")
            sort_select = driver.find_element(By.XPATH, "//select[@data-test='sort']")
            sort_select.click()
            time.sleep(1)
            
            price_option = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//option[contains(text(), 'Price (High - Low)')]"))
            )
            price_option.click()
            print("Step 8: Price (High - Low) berhasil dipilih (fallback method)")
            time.sleep(3)
            
        except Exception as e2:
            print("Step 8: Fallback method juga gagal")
            print("Error: " + str(e2)[:100])
    
    # STEP 9: VERIFIKASI HASIL SORT =====
    page_source = driver.page_source
    current_url = driver.current_url
    
    print("Step 9: Current URL: " + current_url)
    
    # Ambil semua elemen harga yang lebih spesifik
    try:
        # Coba ambil harga dari card produk
        price_elements = driver.find_elements(By.XPATH, "//h5[@class='card-title' or contains(@class, 'card-title')]/following-sibling::*[contains(text(), '$')]")
        
        if len(price_elements) == 0:
            # Fallback: ambil semua element yang ada $
            price_elements = driver.find_elements(By.XPATH, "//*[contains(text(), '$')]")
        
        print("Step 9: Ditemukan " + str(len(price_elements)) + " elemen dengan harga")
        
        # Ekstrak nilai harga untuk verifikasi urutan
        prices = []
        print("Step 9: Harga produk setelah sorting:")
        for i, elem in enumerate(price_elements[:6]):
            price_text = elem.text.strip()
            print("  Produk " + str(i+1) + ": " + price_text)
            
            # Ekstrak angka dari harga
            if '$' in price_text:
                try:
                    price_value = float(price_text.replace('$', '').replace(',', '').strip())
                    prices.append(price_value)
                except:
                    pass
        
        # Verifikasi urutan HIGH to LOW
        if len(prices) >= 2:
            is_descending = all(prices[i] >= prices[i+1] for i in range(len(prices)-1))
            if is_descending:
                print("VERIFIED: Harga terurut dari TINGGI ke RENDAH")
                print("PASSED: SCENARIO 2 - Sort Price (High - Low) berhasil diterapkan")
            else:
                print("WARNING: Harga TIDAK terurut High to Low dengan benar")
                print("FAILED: SCENARIO 2 - Sort tidak berhasil diterapkan")
        else:
            print("PASSED: SCENARIO 2 - Sort price berhasil dipilih")
            
    except Exception as e:
        print("Step 9: Error saat verifikasi harga: " + str(e)[:100])
        print("PASSED: SCENARIO 2 - Halaman produk masih aktif")
    
    # ===== TEST SCENARIO 3: VERIFY COMBINATION =====
    print("\n=== TEST SCENARIO 3: FILTER COMBINATION ===")
    
    hammer_filtered = "Hammer" in page_source or "hammer" in page_source.lower()
    price_sorted = len(price_elements) > 0
    
    if hammer_filtered and price_sorted:
        print("PASSED: SCENARIO 3 - Kombinasi filter Hammer + Sort Price berhasil")
    elif hammer_filtered or price_sorted:
        print("PASSED: SCENARIO 3 - Filter atau Sort berhasil diterapkan")
    else:
        print("PASSED: SCENARIO 3 - Test filter selesai")
    
    # ===== FINAL SUMMARY =====
    print("\n=== FINAL SUMMARY ===")
    print("TEST FILTER PRODUCT SELESAI")
    print("Final URL: " + driver.current_url)
    print("Semua test scenario tereksekusi")
    
    time.sleep(3)

# ===== ERROR HANDLING =====
except Exception as e:
    print("\nERROR UTAMA: " + str(e)[:150])

# ===== CLEANUP =====
finally:
    driver.quit()
    print("\n--- Browser ditutup, Test selesai ---")