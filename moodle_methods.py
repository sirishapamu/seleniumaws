import sys
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import moodle_locators as locators


driver = webdriver.Chrome('C:/Users/Sirisha/PycharmProjects/pythonProject/chromedriver.exe')


# Fixture method - to open web browser
def setUp():

# Make a full screen
    driver.maximize_window()

# Let's wait for the browser response in general
    driver.implicitly_wait(30)

# Navigate to the Moodle app website
    driver.get(locators.moodle_url)

# checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.moodle_url and driver.title == 'Software Quality Assurance Testing':
        print(f'We are at Moodle homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- "Software Quality Assurance Testing"')
    else:
        print(f'We are not at the Moodle homepage. Check your code!')
        driver.close()
        driver.quit()


# Log In method with custom (dynamic) username and password
def log_in(username, password):
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_url:
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url == locators.moodle_dashboard_url:
                assert driver.current_url == locators.moodle_dashboard_url
                print(f'Log in successful. Dashboard id present. \n'
                f'We logged in with Username: {username} and Password: {password}')
            else:
                print(f'We\re not at the Dashboard. Try again')


# Fixture method - to close web browser
def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()
        sleep(1)
        # Make a log file with dynamic fake values
        old_instance = sys.stdout
        log_file = open('message.log', 'w')
        sys.stdout = log_file
        print(f'Email: {locators.email} \nUsername: {locators.new_username} \nPassword: {locators.new_password} \nFull name: {locators.full_name}')
        sys.stdout = old_instance
        log_file.close()


# Log out method to log our from the Moodle app
def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//span[contains(., "Log out")]').click()
    sleep(0.5)
    if driver.current_url == locators.moodle_url:
        print(f'Log out successful and completed at: {datetime.datetime.now()}')


# Create new user with fake data
def create_new_user():
    # driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/nav/div/button/i').click()
    driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    # Enter fake data into username open field
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(0.25)
    # Click by the password open field and enter fake password
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    print(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    print(locators.last_name)
    sleep(0.50)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    print(locators.email)
    sleep(0.25)
    # Select 'Allow everyone to see my email address'
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.5)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text('Canada')
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    sleep(0.25)
    assert driver.find_element(By.ID, 'id_lang').is_displayed()
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.25)

    # Upload picture to the user picture section
    # Click by 'You can drag and drop files here to add them.' section
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(0.25)
    # driver.find_element(By.XPATH, '//span[contains(., "Server files")]').click()
    # driver.find_element(By.PARTIAL_LINK_TEXT, 'Server files').click()
    driver.find_element(By.LINK_TEXT, 'Server files').click()
    driver.find_element(By.LINK_TEXT, 'Cosmetics').click()
    driver.find_element(By.LINK_TEXT, 'Biotherm 2021 fall school').click()
    driver.find_element(By.LINK_TEXT, 'Course image').click()
    driver.find_element(By.LINK_TEXT, 'BT2021fall.png').click()
    # Click by 'Select this file' button
    driver.find_element(By.XPATH, '//button[contains(., "Select this file")]').click()
    sleep(0.25)
    # Enter value to the 'Picture description' open field
    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)
    # Click by Additional names dropdown menu
    driver.find_element(By.XPATH, '//a[contains(., "Additional names")]').click()
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.phonetic_name)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.phonetic_name)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.phonetic_name)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.phonetic_name)
    sleep(0.5)
    # Click by Interest dropdown menu
    driver.find_element(By.XPATH, '//a[contains(., "Interests")]').click()
    sleep(0.50)
    # Using for loop, take all items from the list and populate data
    for tag in locators.list_of_interests:
        driver.find_element(By.XPATH, '//div[3]/input').click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//div[3]/input').send_keys(tag)
        driver.find_element(By.XPATH, '//div[3]/input').send_keys(Keys.ENTER)
    sleep(0.25)
    # Click by Optional dropdown menu and fill the section
    # driver.find_element(By.XPATH, '//a[contains(., "Optional")]').click() - another approach
    driver.find_element(By.XPATH, "//a[text() = 'Optional']").click()
    sleep(0.25)
    # Fill out the Web page input field
    driver.find_element(By.CSS_SELECTOR, "input#id_url").send_keys(locators.web_page_url)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_icq").send_keys(locators.icq_number)
    driver.find_element(By.CSS_SELECTOR, "input#id_skype").send_keys(locators.new_username)
    driver.find_element(By.CSS_SELECTOR, "input#id_aim").send_keys(locators.new_username)
    driver.find_element(By.CSS_SELECTOR, "input#id_yahoo").send_keys(locators.new_username)
    driver.find_element(By.CSS_SELECTOR, "input#id_msn").send_keys(locators.new_username)
    driver.find_element(By.CSS_SELECTOR, "input#id_idnumber").send_keys(locators.icq_number)
    sleep(0.5)
    # Fill out Institution open field
    driver.find_element(By.CSS_SELECTOR, "input#id_institution").send_keys(locators.institution)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_department").send_keys(locators.department)
    driver.find_element(By.CSS_SELECTOR, "input#id_phone1").send_keys(locators.phone)
    driver.find_element(By.CSS_SELECTOR, "input#id_phone2").send_keys(locators.mobile_phone)
    driver.find_element(By.CSS_SELECTOR, "input#id_address").send_keys(locators.address)
    sleep(0.5)
    # Click by Create User button
    driver.find_element(By.ID, "id_submitbutton").click()
    sleep(0.25)
    print(f'New user {locators.new_username} created. Test passed.')


# Check for new user created with Email as a filter
def check_user_created():
    # Check that we are on the User's Main Page
    if driver.current_url == locators.moodle_users_main_page:
        assert driver.find_element(By.XPATH, "//h1[text() = 'Software Quality Assurance Testing']").is_displayed()
        if driver.find_element(By.ID, 'fgroup_id_email_grp_label') and\
                driver.find_element(By.NAME, 'email'):
            driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
            sleep(0.5)
            driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
            sleep(0.5)
            if driver.find_element(By.XPATH, f'//td[contains(., "{locators.email}")]'):
                print(f'Username {locators.new_username} with Email {locators.email} created and checked. Test passed.')
                # Logout
                log_out()


# Log In method with new username and password created
def check_we_logged_in_with_new_cred():
    if driver.current_url == locators.moodle_dashboard_url:
        if driver.find_element(By.XPATH, f'//span[contains(., "{locators.full_name}")]').is_displayed():
            print(f'User with the name {locators.full_name} is displayed. Test passed')


# Delete new user created
def delete_new_user_created():
    if driver.title == 'Dashboard' and driver.current_url == locators.moodle_dashboard_url:
        assert driver.current_url == locators.moodle_dashboard_url
        driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
        assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
        driver.find_element(By.LINK_TEXT, 'Users').click()
        assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed()
        driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
        if driver.current_url == locators.moodle_users_main_page:
            assert driver.find_element(By.XPATH, "//h1[text() = 'Software Quality Assurance Testing']").is_displayed()
            print('You are on User list page')
        if driver.find_element(By.ID, 'fgroup_id_email_grp_label').is_displayed() and \
                driver.find_element(By.NAME, 'email').is_displayed():
            driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
            sleep(0.5)
            driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
            sleep(0.5)
        if driver.find_element(By.XPATH, f'//td[contains(., "{locators.email}")]').is_displayed() and \
            driver.find_element(By.XPATH, '//*[@title = "Delete"]').is_displayed():
            print(f'"{locators.email}" email confirmed to delete')
            driver.find_element(By.XPATH, '//i[@title = "Delete"]').click()
            sleep(0.5)
            driver.find_element(By.XPATH, '//button[contains(., "Delete")]').click()
            print(f'New user "{locators.new_username}" that is created is deleted by "{locators.moodle_username}"')
            sleep(0.5)
        else:
            print(f'User with "{locators.email}" not deleted. Test failed')
