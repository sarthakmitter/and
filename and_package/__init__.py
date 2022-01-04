from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import discord_webhook
from discord_webhook import DiscordWebhook,DiscordEmbed

hookurl = "https://discord.com/api/webhooks/867473440049987594/nj5p8_ennwxQjxlVeA3aP-ee9XMXjmq58ZkgLHM7HJpNLLuGDU5ezZJJi8u0nG-TbQ9a"
#Generate a Discord Webhook URL and paste the same above
run_time = input("How many iterations do you want:")  #number of times you want the bot to scan for seats
j = int(run_time)
print("Make sure that you have set your registration number in login function")   #Or else you may add your credentials in the login function to skip prompts
print("")
password = input("Enter your password:")
reg_no = input("Enter your Registration Number:")

driver = webdriver.Chrome("D:\\chromedriver.exe")           #Download the selenium webdriver according to your Chrome version and specify the path of the webdriver exe file
driver.implicitly_wait(5)
driver.get("https://vtopreg.vit.ac.in/adddrop/")

def discord_online():
    hook = DiscordWebhook(hookurl,content= "@everyone")
    embed = DiscordEmbed(title='Activation Successful', description=f"Iterations remaining- {run_time}", color='03b2f8')
    hook.add_embed(embed)
    response = hook.execute()

def discord_normal_ping(status):

    hook = DiscordWebhook(hookurl,content= status).execute()

def discord_important_ping(important_status):

    hook = DiscordWebhook(hookurl,content= "@everyone")
    embed = DiscordEmbed(title='Updates', description= important_status, color='03b2f8')
    hook.add_embed(embed)
    response = hook.execute()

def login():
    driver.implicitly_wait(5)
    agree_button = driver.find_element_by_xpath("//button[contains(text(),'Agree')]")
    driver.execute_script("arguments[0].scrollIntoView();", agree_button)
    agree_button.click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[@id='userName']").send_keys(reg_no)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
    time.sleep(15)

def sign_out():
    driver.implicitly_wait(5)
    print("Initiating Sign Out")
    discord_important_ping("Initiating Sign Out")
    signout_button = driver.find_element_by_xpath("//button[contains(text(),'Sign out')]")
    driver.execute_script("arguments[0].scrollIntoView();", signout_button)
    signout_button.click()
def back_home():
    driver.implicitly_wait(5)
    time.sleep(1)
    home_button = driver.find_element_by_xpath("//button[contains(text(),'Home')]")
    driver.execute_script("arguments[0].scrollIntoView();", home_button)
    home_button.click()
    time.sleep(2)
def course_type(rb,pg_num):                 #Enter the respective page number to visit in the course type
    driver.implicitly_wait(5)
    radio_button = driver.find_element_by_xpath(f"//input[@id='registrationOption{rb}']")  #Values of rb can be given as PC = 0 ; PE = 1 ; UC = 2 ; UE = 3
    driver.execute_script("arguments[0].scrollIntoView();", radio_button)
    radio_button.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
    pg_id = f"//body/div[@id='page-wrapper']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/ul[1]/li[{int(pg_num) + 1}]/a[1]"
    driver.find_element_by_xpath(pg_id).click()
    time.sleep(2)
def course_reg(name,pg,n):
    #n is the serial number of course on respective page
    #pg is the respective page number to visit
    #For name- Enter the name of the course(Any name you want to enter)
    print()
    print(f" {name}:-")
    discord_normal_ping(f" {name}:-")
    driver.implicitly_wait(5)
    reg_button_number = (((int(pg)*5)-1) - (5-int(n)))
    button_id = (f"//button[@id='registerbtn_{reg_button_number}']")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element_by_xpath(button_id).click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    try:
        faculty_reg(4)

    except NoSuchElementException:

        try:
            faculty_reg(4)

        except NoSuchElementException:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element_by_xpath("//button[contains(text(),'Go Back')]").click()
        pass
def course_view(name,pg,n):
    # n is the serial number of course on respective page
    # pg is the respective page number to visit
    # For name- Enter the name of the course(Any name you want to enter)
    print()
    print(f" {name}:-")
    discord_normal_ping(f" {name}:-")
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(f"//body[1]/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/div[{int(pg)+1}]/table[1]/tbody[1]/tr[{n}]/td[12]/button[1]").click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    try:
        faculty_view(4)

    except NoSuchElementException:

        try:
            faculty_view(4)

        except NoSuchElementException:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element_by_xpath("//button[contains(text(),'Go Back')]").click()
        pass
def faculty_reg(m):     #m =  selected faculty serial number on the page
    driver.implicitly_wait(10)
    a = f"//thead/tr[{int(m)+3}]/td[5]"
    seats1 = driver.find_element_by_xpath(a)
    fcname= f"//thead/tr[{int(m)+3}]/td[3]"
    faculty_name = driver.find_element_by_xpath(fcname).text
    sltname = f"//thead/tr[{int(m)+3}]/td[1]"
    slot = driver.find_element_by_xpath(sltname).text
    normal_update = f"{slot}, {faculty_name} =  {seats1.text}"
    print(normal_update)
    discord_normal_ping(normal_update)
    if (seats1.text) != "Full" :
        for _ in range(5):discord_important_ping("Vacant Seats Alert!")
        driver.get_screenshot_as_file(f"{slot}_available.png")
    b = a + '/input[1]'
    verify = driver.find_element_by_xpath(b)
    verify.click()
    time.sleep(2)
    course_option_button= driver.find_element_by_xpath("//thead/tr[8]/td[2]/div[2]/div[1]/input[1]")
    driver.execute_script("arguments[0].scrollIntoView();", course_option_button)
    course_option_button.click()
    time.sleep(2)
    reg_button_xapth ="//body[1]/div[3]/div[1]/div[1]/div[1]/form[1]/div[2]/table[1]/thead[1]/tr[9]/td[1]/div[1]/button[1]"
    driver.find_element_by_xpath(reg_button_xapth).click()
    time.sleep(2)
    print(f"Course Registration Successful: {slot}")
    for _ in range(5): discord_important_ping(f"Course Registration Successful: {slot}")
    driver.get_screenshot_as_file(f"course_reg_ger_{slot}.png")
def faculty_view(n):    #n =  selected faculty serial number on the page
    driver.implicitly_wait(10)
    a = f"//thead/tr[{int(n) + 1}]/td[8]"
    fcname = f"//thead/tr[{int(n) + 1}]/td[4]"
    faculty_name = driver.find_element_by_xpath(fcname).text
    sltname = f"//thead/tr[{int(n) + 1}]/td[2]"
    slot = driver.find_element_by_xpath(sltname).text

    verify = driver.find_element_by_xpath(a)
    driver.execute_script("arguments[0].scrollIntoView();", verify)
    live_seats = f" {slot},{faculty_name} = {verify.text}"
    print(live_seats)
    discord_normal_ping(live_seats)
    if int(verify.text) > 0:
            for _ in range(5): discord_important_ping(f"Seats Available In {slot},{faculty_name}:{verify.text}")
            driver.get_screenshot_as_file(f"{slot}_available.png")
            back_button = driver.find_element_by_xpath("//button[contains(text(),'Go Back')]")
            driver.execute_script("arguments[0].scrollIntoView();", back_button)
            time.sleep(1)
            back_button.click()
    else:
        error_button = driver.find_element_by_xpath("//button[contains(text(),'xyz')]")
        error_button.click()


def process_flow():
    course_reg("LESM",2,3)


#Initial Setup
login()
discord_online()
driver.maximize_window()
course_type(1,2)

i=1
try:
    while i < j+1:

        Itr_update = f"    >>ITERATION NUMBER:{i}<< "
        print()
        print(Itr_update)
        discord_normal_ping(Itr_update)

        process_flow()
        i = i + 1
        if i == j + 1:
            print('Process Completed:Course could not be registered')
            for _ in range(5): discord_important_ping('Process Completed:Course could not be registered')
            sign_out()
        else:
            continue

except:
    for _ in range(10): discord_important_ping('Process Failed due to some error:Aborted')
    sign_out()






