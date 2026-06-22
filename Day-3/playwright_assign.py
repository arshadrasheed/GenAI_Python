import pandas as pd
import time
import random
import json
import os
from playwright.sync_api import sync_playwright

def ReadExcel(path="contacts.xlsx"):
    df = pd.read_excel(path)
    subset_df = df[['Name', 'Phone', 'Message']]
    return subset_df.to_dict(orient='records')

def human_delay(min_sec=2, max_sec=4):
    time.sleep(random.uniform(min_sec, max_sec))

def run_automation():
    contacts = ReadExcel("contacts.xlsx")
    report_data = []
    
    os.makedirs("screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="./whatsapp_session",
            headless=False
        )
        page = browser.new_page()
        
        print("Loading WhatsApp Web...")
        page.goto("https://web.whatsapp.com/")
        page.wait_for_selector("#side", timeout=120000)
        print("Login verified. Starting automation...\n")

        for contact in contacts:
            name = str(contact['Name'])
            phone = str(contact['Phone']).strip()
            
            raw_message = contact['Message']
            if pd.isna(raw_message):
                raw_message = ""
            else:
                raw_message = str(raw_message)
                
            personalized_msg = raw_message.replace('{name}', name)
            
            print(f"\nProcessing: {name} ({phone})")
            
            contact_report = {
                "Name": name,
                "Phone": phone,
                "Sent_Status": "Failed",
                "Extracted_Messages": []
            }

            try:
                # 1. RESET THE UI: Press Escape to close any open searches/menus
                page.keyboard.press("Escape")
                time.sleep(1)

                # 2. SEARCH PROCESS
                search_box = page.get_by_placeholder("Search", exact=False).first
                search_box.click()
                search_box.fill("") 
                time.sleep(1)
                
                page.keyboard.type(phone, delay=50) 
                
                time.sleep(3)
                page.keyboard.press("Enter")
                time.sleep(2)

                # 3. MESSAGE PROCESS (Targeting the chat footer strictly)
                message_box = page.locator('footer div[contenteditable="true"]').first
                message_box.wait_for(state="visible", timeout=5000)
                message_box.click()
                
                page.keyboard.type(personalized_msg, delay=30)
                time.sleep(1)
                page.keyboard.press("Enter")
                
                # 4. WRAP UP
                time.sleep(3) 
                safe_phone = phone.replace('+', '')
                screenshot_path = f"screenshots/sent_{name}_{safe_phone}.png"
                page.screenshot(path=screenshot_path)
                
                contact_report["Sent_Status"] = "Success"
                print("✅ Message sent and screenshot captured.")

                # 5. DATA EXTRACTION
                human_delay(2, 3)
                chat_rows = page.locator('div[role="row"]').all()
                extracted_texts = []
                
                for row in chat_rows[-5:]: 
                    text_span = row.locator('span.selectable-text')
                    if text_span.count() > 0:
                        extracted_texts.append(text_span.first.inner_text())
                
                contact_report["Extracted_Messages"] = extracted_texts[-3:]
                print(f"🔍 Extracted {len(contact_report['Extracted_Messages'])} recent messages.")

            except Exception as e:
                print(f"❌ Failed to process {name}. Reason: Contact not found or timeout.")
                # We do not print the full 'e' here so it doesn't clutter your terminal with huge red error blocks

            report_data.append(contact_report)
            human_delay(2, 4) 

        browser.close()

    print("\nGenerating reports...")
    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4)
    
    for row in report_data:
        row["Extracted_Messages"] = " | ".join(row["Extracted_Messages"])
        
    pd.DataFrame(report_data).to_excel("report.xlsx", index=False)
    
    print("✅ Run complete! Check report.json, report.xlsx, and screenshots.")

    
    
run_automation()