from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.common.keys import Keys


@given(u'Opening Login_Page of OrangeHRM')
def opening_chrome_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)


@when(u'Enter Username "{Username}" and Password "{Password}"')
def Login_into_the_page(context, Username, Password):
    try:
        context.driver.find_element(By.XPATH, "//*[@name='username']").send_keys(Username)
    except:
        raise Exception('Not Able to Take UserName')
    try:
        context.driver.find_element(By.XPATH, "//*[@name='password']").send_keys(Password)
    except:
        raise Exception('Not Able To Fill Password Block')
    try:
        context.driver.find_element(By.XPATH, "//*[@type='submit']").click()
    except:
        raise Exception('Submit Button Is Not Working Properly')


@when(u'Entering In PIM')
def Entering_To_PIM_Form(context):
    PIM_Button = context.driver.find_element(By.XPATH, "(//*[@class='oxd-main-menu-item']/descendant::span)[2]")
    PIM_Button.click()
    Add_Button = context.driver.find_element(By.XPATH, "//*[@class='orangehrm-header-container']/child::button")
    Add_Button.click()


@when(u'Enter FirstName "{FirstName}" MiddleName "{MiddleName}" LastName "{LastName}"')
def Filling_Details_of_New_Employee(context, FirstName, MiddleName, LastName):
    context.name=FirstName+' '+LastName
    First_Name = context.driver.find_element(By.XPATH, '//input[@name="firstName"]')
    First_Name.send_keys(FirstName)
    Middle_Name = context.driver.find_element(By.XPATH, '//input[@name="middleName"]')
    Middle_Name.send_keys(MiddleName)
    Last_Name = context.driver.find_element(By.XPATH, '//input[@name="lastName"]')
    Last_Name.send_keys(LastName)
    EMP_ID=context.driver.find_element(By.XPATH,"(//*[text()='Employee Id']/following::input)[1]")
    if EMP_ID.get_attribute('value')==False:
        raise Exception('Not Generating Automatic Id')
    error_msg=context.driver.find_element(By.XPATH,"(//*[text()='Employee Id']/following::input)[1]")
    if error_msg.text=='Employee Id already exists':
        EMP_ID.send_keys('0000000001')





@when('Enter UserName "{user_Name}" Password "{password}" and Confirm Password "{confirm_password}"')
def creating_login_details(context, user_Name, password, confirm_password):
    create_login_radio_button = context.driver.find_element(By.XPATH,
                                                            "//div[@class='oxd-switch-wrapper']/descendant::span")
    create_login_radio_button.click()
    User_Name = context.driver.find_element(By.XPATH, "(//*[text()='Username']/following::input)[1]")
    User_Name.send_keys(user_Name)
    if context.driver.find_element(By.XPATH, "(//input[@type='radio'])[1]").is_selected() == False:
        context.driver.find_element(By.XPATH, "(//input[@type='radio'])[1]").click()
    Password = context.driver.find_element(By.XPATH, "(//*[text()='Password']/following::input)[1]")
    Password.send_keys(password)
    Confirm_Password = context.driver.find_element(By.XPATH, "(//*[text()='Confirm Password']/following::input)[1]")
    Confirm_Password.send_keys(confirm_password)
    saving_details = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    saving_details.click()
    time.sleep(10)


@then(u'Verifying Information Saved Or Not')
def verifying_information_saved_or_not(context):
    wait = WebDriverWait(context.driver, 100)
    time.sleep(5)

    if wait.until(ec.presence_of_element_located(
            (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 --strong']"))).text != context.name:
        raise Exception('Not Saved')


@then(u'Deleting Records')
def deleting_records(context):

    context.driver.back()
    context.driver.back()

    employee_list=context.driver.find_elements(By.XPATH,"//*[@class='oxd-icon bi-check oxd-checkbox-input-icon']")
    for i in range(1, 3):
        employee_list[i].click()
    context.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.UP)
    records_details=context.driver.find_element(By.XPATH,"(//span[@class='oxd-text oxd-text--span'])[1]")
    record_before_delete=records_details.text

    delete_button=context.driver.find_element(By.XPATH,"(//*[@class='oxd-text oxd-text--span'])[1]/following-sibling::button")
    delete_button.click()

    accepting_delete=context.driver.find_element(By.XPATH, "(//div[@class='orangehrm-modal-footer']/child::button)[2]")
    accepting_delete.click()
    context.driver.find_element(By.XPATH, "(//*[@class='oxd-main-menu-item']/descendant::span)[2]").click()
    time.sleep(5)
    records_after_delete=records_details.text
    if record_before_delete==records_after_delete:
        raise Exception('Record Not Deleted Properly')
    time.sleep(2)


