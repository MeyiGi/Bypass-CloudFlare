import time
from DrissionPage import ChromiumPage, ChromiumOptions

start_time = time.time()

options = ChromiumOptions().headless(False)
driver = ChromiumPage(options)

try:
    print("getting url")
    driver.get("https://paperpapers.com/")
    
    print("Bypassing cloudflare it will take 120-150 sec")
    
    # Once you've launched code, you can remove this part
    time.sleep(120)
    
    # Attempt to handle Cloudflare protection
    i = driver.get_frame("@src^https://challenges.cloudflare.com/cdn-cgi")
    if i:
        e = i(".mark")
        e.click()
    time.sleep(20)
    driver.quit()
except:
    driver.quit