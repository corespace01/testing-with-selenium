import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

s = Service(r"C:\Users\HP\PycharmProjects\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get("https://www.thesparksfoundationsingapore.org/")

print("\nTesting............\n")

########################## Home Page ################################

print("TestCase - 1: Title")
if driver.title == "The Sparks Foundation | Home":
    print("Title  matches ! Verification Successful")
else:
    print("Title Verification Failed!")
time.sleep(2)
print("\n")


print("TestCase - 2: Logo")
try:
    driver.find_element(By.XPATH, '//*[@id="home"]/div/div[1]/h1/a/img')
    print("Logo Exists!")
except NoSuchElementException:
    print("Logo does not exists!")
time.sleep(2)
print("\n")


print("TestCase - 3: Home Link")
try:
    driver.find_element(By.PARTIAL_LINK_TEXT, "The Sparks Foundation").click()
    print("Home link works! SUCCESS")
except NoSuchElementException:
    print("Home Link Doesn't Work! FAILED")
time.sleep(2)
print("\n")


print("TestCase - 4: Navbar")
try:
    driver.find_element(By.CLASS_NAME, "navbar-brand")
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")
time.sleep(2)


print("TestCase - 5: Slide Links")

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div/ol/li[2]/a").click()
print(" clicked 2 Internships ")
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div/ol/li[3]/a").click()
print(" clicked 3 Mentorship ")
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div/ol/li[4]/a").click()
print(" clicked 4 Support ")
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div/ol/li[5]/a").click()
print(" clicked 5 Scholarships ")
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div/ol/li[6]/a").click()
print(" clicked 6 Community \n")
time.sleep(6)

# driver.execute_script("window.scrollTo(0, 500)")
# time.sleep(2)
# print("scrolled 500px")


print("TestCase - 6: YouTube Iframe")
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)
print("scrolled 500px")

required_frame = driver.find_element(By.XPATH, "//iframe[contains(@src,'https://www.youtube.com/embed/kgj_0E_urK0?autoplay=0&theme=light&loop=1&disablekb=1&modestbranding=1&hd=1&autohide=0&color=white&controls=0&showinfo=0&showsearch=0&cc_load_policy=1&rel=0')]")
driver.switch_to.frame(required_frame)

element = driver.find_element(By.XPATH, "//button[@aria-label='Play']")
element.click()

print("YouTube video played")

time.sleep(10)
stop = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/video").click()
print("Pause Video\n")
time.sleep(1.5)

driver.refresh()
time.sleep(2)
driver.find_element(By.ID, "toTopHover").click()
time.sleep(1)
print("scrolling Up \n")
print("page refreshed \n")
time.sleep(5)


print("TestCase - 7: Know More Link/Button")
try:
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "hvr-rectangle-out").click()
    print("Know More link of mission & vision statement is Working! SUCCESS\n")
except NoSuchElementException:
    print("Know More Link does not exist! FAILED\n")

time.sleep(3)
for i in range(0, 1500, 250):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)
time.sleep(1)
driver.find_element(By.ID, "toTopHover").click()
time.sleep(1)
print("scrolling Down -> Up")

time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "The Sparks Foundation").click()
print("Back to main page\n")
time.sleep(5)


print("TestCase - 8: Learn More Link/Button")
try:
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/a').click()
    print("Learn more Link is working! SUCCESS\n")
except NoSuchElementException:
    print("Learn more link does not! FAILED\n")
time.sleep(3)

for i in range(0, 1500, 250):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)
time.sleep(1)
driver.find_element(By.ID, "toTopHover").click()
time.sleep(1)
print("scrolling Down -> Up")

time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "The Sparks Foundation").click()
print("Back to main page\n")


################################  About us Page  ##################################


time.sleep(3)
print("TestCase - 9: News Link")
time.sleep(2)
try:
    driver.find_element(By.CLASS_NAME, "menu__link").click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[1]/ul/li[7]/a').click()
    time.sleep(1)
    print("About Us and News link is working! SUCCESS\n")
except NoSuchElementException:
    print("About us and News link is not working! FAILED\n")

time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "The Sparks Foundation").click()
print("Back to main page\n")


##########################  Policies & Code Page #################################


time.sleep(4)
print('TestCase - 10: Policies Link')
try:
    driver.find_element(By.LINK_TEXT, 'Policies and Code').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Policies").click()
    time.sleep(2)
    print('Policy page is working! SUCCESS\n')
except NoSuchElementException:
    print('Policy Page Does not exist! FAILED\n')
    time.sleep(2)

for i in range(0, 1500, 250):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)
time.sleep(1)
driver.find_element(By.ID, "toTopHover").click()
time.sleep(1)
print("scrolling Down -> Up")

time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "The Sparks Foundation").click()
print("Back to main page\n")


#################################  Programs Page  #########################################


time.sleep(3)
print('TestCase - 11: Workshop Page & Link')
try:
    driver.find_element(By.LINK_TEXT, 'Programs').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Workshops").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'LEARN MORE').click()
    time.sleep(2)
    print('Workshop and LEARN MORE Link is working! SUCCESS\n')
except NoSuchElementException:
    print('No New Tab opened link is not working! FAILED\n')

driver.switch_to.window(driver.window_handles[1])

for i in range(0, 1500, 250):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)

driver.find_element(By.ID, "toTopHover").click()
time.sleep(1)
print("scrolling Down -> Up")

time.sleep(1)
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "The Sparks Foundation").click()
print("Back to main page\n")
time.sleep(1)


#################################### Links Page ################################################


time.sleep(3)
print("TestCase - 12: Links")
try:
    driver.find_element(By.LINK_TEXT, 'LINKS').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'Software & App').click()
    time.sleep(2)
    print('LINKS Verification successful!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")

for i in range(0, 1500, 250):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)

driver.find_element(By.ID, "toTopHover").click()
time.sleep(1)
print("scrolling Down -> Up")


time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "The Sparks Foundation").click()
print("Back to main page\n")


###################################### Join Us Page ##########################################

time.sleep(3)
print("TestCase - 13: Join Us")
try:
    driver.find_element(By.LINK_TEXT, 'Join Us').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'Why Join Us').click()
    time.sleep(3)
    driver.find_element(By.NAME, 'Name').send_keys('Sara')
    time.sleep(3)
    driver.find_element(By.NAME, 'Email').send_keys('sara03@gmail.com')
    time.sleep(3)
    select = Select(driver.find_element(By.CLASS_NAME, 'form-control'))
    time.sleep(3)
    select.select_by_visible_text('Student')
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'button-w3layouts').click()
    time.sleep(3)
    print("Form Verification Successful!\n")
    time.sleep(2)
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)

driver.find_element(By.ID, "toTopHover").click()
time.sleep(1)

time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "The Sparks Foundation").click()
print("Back to main page\n")


#######################################  Contact Us Page #######################################


time.sleep(3)
print("TestCase - 14: Contact Us")
try:
    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    time.sleep(1)
    info = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(1)

    if info.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print('contact Information Correct!')
    else:
        print('Contact Information Incorrect!')

    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification unsuccessful!")

time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "The Sparks Foundation").click()
print("Back to main page\n")


################################# FOOTER lINKS ##################################


time.sleep(3)
print("TestCase - 15: Jobs at Angel.co Portal")
time.sleep(2)
for i in range(0, 1500, 250):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)
time.sleep(3)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div[2]/ul/li[2]/a").click()
    print("Jobs at Angel.co Portal page is working! SUCCESS\n")
except NoSuchElementException:
    print("Jobs at Angel.co Portal page is not working! FAILED\n")
time.sleep(5)

driver.switch_to.window(driver.window_handles[0])
time.sleep(5)


print("TestCase - 16: Jobs at Tech in Asia Portal")
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div[2]/ul/li[3]/a").click()
    print("Jobs at Tech in Asia Portal page is working! SUCCESS\n")
except NoSuchElementException:
    print("Jobs at Tech in Asia Portal page is not working! FAILED\n")

time.sleep(10)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)


print("TestCase - 17: Code for India page")
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div[1]/ul/li[3]/a").click()
    print("Code for India page is working! SUCCESS\n")
except NoSuchElementException:
    print("Code for India page is not working! FAILED\n")

time.sleep(10)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)


print("TestCase - 18: Internships at Internshala")
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div[3]/ul/li/a").click()
    print("Internships at Internshala page is working! SUCCESS\n")
except NoSuchElementException:
    print("Internships at Internshala page is not working! FAILED\n")

time.sleep(10)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)

driver.find_element(By.ID, "toTopHover").click()
time.sleep(1)
print("scrolling Up\n")


print(" ********** Testing of sparkfoundation.sg Website Completed *********** ")
