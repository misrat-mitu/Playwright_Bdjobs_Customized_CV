from playwright.sync_api import sync_playwright

# Your credentials
USERNAME = "jenoge4512@simerm.com"
PASSWORD = "12123456"

def run():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)

        # Open new page
        page = browser.new_page()

        # Open Bdjobs login page
        page.goto("https://mybdjobs.bdjobs.com/jobseeker-panel/signin?tp=default&lang=en")

        # Wait for page load
        page.wait_for_load_state("networkidle")

        # Enter username/email/mobile no
        page.fill('input[placeholder="Type username email or mobile no"]', USERNAME)
        page.wait_for_timeout(3000)
        # Click Continue button
        page.click("button:has-text('Continue')")

        # Wait for password field to appear
        page.wait_for_selector('input[type="password"]')

        # Enter password
        page.fill('input[type="password"]', PASSWORD)

        # Click Sign in/Login button
        page.click("button:has-text('Sign in')")

        # Wait after login
        page.wait_for_load_state("networkidle")

        # Print title after login
        print("Logged in successfully!")
        print("Page Title:", page.title())

        # Keep browser open for a few seconds
        page.wait_for_timeout(5000)
        
         
    # Close popup if it appears
        try:
            popup_close_selector = (
                "button.close, "
                "button[aria-label='Close'], "
                ".modal .close, "
                ".popup-close"
            )

            page.wait_for_selector(popup_close_selector, timeout=5000)
            page.click(popup_close_selector)
            #page.wait_for_timeout(2000)

            print("Popup closed!")

        except Exception:
            print("No popup found, continuing...")
        
        # Wait some time
            page.wait_for_timeout(2000)

        # Click My bdjobs logo and handle new tab
        with page.expect_popup() as popup_info:
            page.locator("img[alt='mybdjobs']").click()

            new_page = popup_info.value

        # Wait for new tab load
            new_page.wait_for_load_state("domcontentloaded", timeout=2000)

            print("New tab opened:", new_page.url)
            print("New URL:", new_page.url)

            new_page.wait_for_timeout(5000)
            
                 
# ================================
# CLICK MANAGE PROFILE
# ================================
        new_page.wait_for_selector("//span[normalize-space()='Manage Profile']")

        new_page.locator("//span[normalize-space()='Manage Profile']").click()

        print("Clicked Manage Profile")
        
        # Keep browser open
        new_page.wait_for_timeout(5000)

# ========================================
# # CLICK CUSTOMIZED CV
# ========================================
        new_page.wait_for_selector("//span[normalize-space()='Customized CV']")

        new_page.locator("//span[normalize-space()='Customized CV']").click()

        # Wait for page load
        new_page.wait_for_load_state("networkidle")

        print("Customized CV page opened!")
        print("Current URL:", new_page.url)

        # Keep browser open
        new_page.wait_for_timeout(5000)
        
        
# ========================================
# CLICK "ADD CUSTOMIZED CV"
# ========================================
        new_page.wait_for_selector("//span[contains(text(),'Add Customized CV')]")

        new_page.locator("//span[contains(text(),'Add Customized CV')]").click()

        print("Clicked Add Customized CV")

        # WAIT FOR BROWSE FILE BUTTON
        new_page.wait_for_timeout(2000)

      
# ========================================
# UPLOAD FILE USING FILE CHOOSER
# ========================================

        file_path = r"H:\juairia.pdf"

        with new_page.expect_file_chooser() as fc_info:

        # Click Browse File button
            new_page.locator("//button[contains(.,'Browse File')]").click()

        # Get file chooser
        file_chooser = fc_info.value

        # Upload file
        file_chooser.set_files(file_path)

        print("File uploaded successfully!")

        # Wait after upload
        new_page.wait_for_load_state("networkidle")

        new_page.wait_for_timeout(5000)

        print("Upload completed successfully!")
        
        browser.close()
        
'''        
        # ========================================
        # CLICK DELETE BUTTON
        # ========================================
        new_page.wait_for_selector("//span[normalize-space()='Delete']")

        new_page.locator("//span[normalize-space()='Delete']").click()

        print("Clicked Delete Button")

        # WAIT FOR POPUP
        new_page.wait_for_timeout(3000)


        # CLICK YES, CONTINUE BUTTON
        new_page.locator("text=Yes, Continue").click()

        print("Clicked Yes, Continue")

        # Wait after delete
        new_page.wait_for_load_state("networkidle")

        print("CV Deleted Successfully")

        browser.close()
'''        
        
if __name__ == "__main__":
    run()       
               
