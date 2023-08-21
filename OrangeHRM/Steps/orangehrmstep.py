from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.common.keys import Keys

"""
All Required Path"""
paths = {
    'admin_username': "//*[@name='username']",
    'admin_password': "//*[@name='password']",
    'submit': "//*[@type='submit']",
    'pim_button': "(//*[@class='oxd-main-menu-item-wrapper']/child::a)[2]",
    'add_button': "//*[@class='orangehrm-header-container']/child::button",
    'first_name': '//input[@name="firstName"]',
    'middle_name': '//input[@name="middleName"]',
    'last_name': '//input[@name="lastName"]',
    'emp_id': "(//*[text()='Employee Id']/following::input)[1]",
    'login_button': "//div[@class='oxd-switch-wrapper']/descendant::span",
    'new_username': "(//*[text()='Username']/following::input)[1]",
    'enabled_button': "(//input[@type='radio'])[1]",
    'password': "(//*[text()='Password']/following::input)[1]",
    'confirm_password': "(//*[text()='Confirm Password']/following::input)[1]",
    'save_button': "//button[@type='submit']",
    'profile_name': "//h6[@class='oxd-text oxd-text--h6 --strong']",
    'emp_list': "//*[@class='oxd-icon bi-check oxd-checkbox-input-icon']",
    'number_of_records': "(//span[@class='oxd-text oxd-text--span'])[1]",
    'delete_records': "(//*[@class='oxd-text oxd-text--span'])[1]/following-sibling::button",
    'confiraming_delete': "(//div[@class='orangehrm-modal-footer']/child::button)[2]",

}


@given(u'Opening Login_Page of OrangeHRM')
def opening_chrome_browser(context):
    """
    I am Opening the OrangeHrm Admin Login
    """
    context.driver = webdriver.Chrome()
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)


@when('Login By Using Username "{username}" and Password "{password}"')
def Login_into_the_page(context, username, password):
    """
    :param Username: Holds User Name Value in str format
    :param Password: Holds Password in str format
    """

    context.driver.find_element(By.XPATH, paths['admin_username']).send_keys(username)

    context.driver.find_element(By.XPATH, paths['admin_password']).send_keys(password)

    context.driver.find_element(By.XPATH, paths['submit']).click()


@when(u'Entering In PIM')
def Entering_To_PIM_Form(context):
    """
    Opening The Page To Create New Account For New Employee
    """
    PIM_Button = context.driver.find_element(By.XPATH, paths['pim_button'])
    PIM_Button.click()
    Add_Button = context.driver.find_element(By.XPATH, paths['add_button'])
    Add_Button.click()


@when('Enter First_Name "{first_name}" Middle_Name "{middle_name}" and Last_Name "{last_name}"')
def Filling_Details_of_New_Employee(context, first_name, middle_name, last_name):
    """
    Filling Employee Details
    :param FirstName: Holds First Name of Employee in str format
    :param MiddleName: Holds Middle Name of Employee in str fromat
    :param LastName: Holds Last Name of Employee in str fromat

    """

    context.name = first_name + ' ' + last_name
    First_name = context.driver.find_element(By.XPATH, paths['first_name'])
    First_name.send_keys(first_name)

    Middle_name = context.driver.find_element(By.XPATH, paths['middle_name'])
    Middle_name.send_keys(middle_name)

    Last_name = context.driver.find_element(By.XPATH, paths['last_name'])
    Last_name.send_keys(last_name)

    EMP_ID = context.driver.find_element(By.XPATH, paths['emp_id'])
    if EMP_ID.get_attribute('value') == False:
        raise Exception('Not Generating Automatic Id')



@when('Enter UserName "{user_Name}" Password "{password}" and Confirm Password "{confirm_password}"')
def creating_login_details(context, user_Name, password, confirm_password):
    """
    Filling Login Credential For New Employee
    :param user_Name: Holds New Employee User_Name in str format
    :param password: Holds Password of New Employee in str format
    :param confirm_password: Holds Confirm Password Value of New Employee in str format

    """
    create_login_radio_button = context.driver.find_element(By.XPATH, paths['login_button'])
    create_login_radio_button.click()
    User_Name = context.driver.find_element(By.XPATH, paths['new_username'])
    User_Name.send_keys(user_Name)
    if context.driver.find_element(By.XPATH, paths['enabled_button']).is_selected()==False:
        context.driver.find_element(By.XPATH, paths['enabled_button']).click()
    else:
        raise Exception('Enabled Button Is Not Automatically Selected')

    Password = context.driver.find_element(By.XPATH, paths['password'])
    Password.send_keys(password)
    Confirm_Password = context.driver.find_element(By.XPATH, paths['confirm_password'])
    Confirm_Password.send_keys(confirm_password)
    saving_details = context.driver.find_element(By.XPATH, paths['save_button'])
    saving_details.click()
    time.sleep(10)
    """Checking Records Saved Or Not"""
    wait = WebDriverWait(context.driver, 30)

    if wait.until(ec.presence_of_element_located((By.XPATH, paths['profile_name']))).text != context.name:
        raise Exception('Not Saved')
    


@then(u'Deleting Records')
def deleting_records(context):
    """
    Deleting Multiple Records from the List
    """

    context.driver.back()
    context.driver.back()
    records_details = context.driver.find_element(By.XPATH, paths['number_of_records'])
    records_details.screenshot('records_delete_before_screenshot2'
                               '.png')
    employee_list = context.driver.find_elements(By.XPATH, paths['emp_list'])
    for i in range(1, 9):
        employee_list[i].click()
    context.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.UP)
    delete_button = context.driver.find_element(By.XPATH, paths['delete_records'])
    delete_button.click()

    accepting_delete = context.driver.find_element(By.XPATH, paths['confiraming_delete'])
    accepting_delete.click()
    context.driver.find_element(By.XPATH, "(//*[@class='oxd-main-menu-item-wrapper']/child::a)[2]").click()
    records_details = context.driver.find_element(By.XPATH, paths['number_of_records'])
    records_details.screenshot('records_delete_after_screenshot2.png')


