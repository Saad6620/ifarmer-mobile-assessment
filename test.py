import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


desired_cap = {
    "appium:automationName": "UiAutomator2",
    "appium:platformName": "Android",
    "appium:platformVersion": "15",
    "appium:deviceName": "S4J7WO8LJJTKAUA6",
    "appium:app": "Downloads/Android-SauceDemoApp.1.3.0.build-244.apk"
}
options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote('http://localhost:4723', options=options)
time.sleep(2)


try:
    # Login
    menu = "//android.view.ViewGroup[@content-desc='open menu']/android.widget.ImageView"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=menu,
    )
    element.click()
    time.sleep(2)

    login = '(//android.view.ViewGroup[@content-desc="store item"])[3]/android.view.ViewGroup[' \
            '1]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=login,
    )
    element.click()
    time.sleep(2)

    username = '//android.widget.EditText[@content-desc="Username input field"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=username,
    )
    element.send_keys('bob@example.com')
    time.sleep(2)

    password = '//android.widget.EditText[@content-desc="Password input field"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=password,
    )
    element.send_keys('10203040')
    time.sleep(5)

    # Clicking login button
    loginBtn = '//android.view.ViewGroup[@content-desc="Login button"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=loginBtn,
    )
    element.click()
    time.sleep(2)

    # Go to catalog
    menu1 = "//android.view.ViewGroup[@content-desc='open menu']/android.widget.ImageView"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=menu1,
    )
    element.click()
    time.sleep(2)

    catalog = '//android.view.ViewGroup[@content-desc="longpress reset app"]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=catalog,
    )
    element.click()
    time.sleep(2)

    sortByName = '//android.view.ViewGroup[@content-desc="sort button"]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=sortByName,
    )
    element.click()
    time.sleep(2)

    sortN = '//android.view.ViewGroup[@content-desc="nameDesc"]/android.widget.TextView[2]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=sortN,
    )
    element.click()
    time.sleep(2)

    sortByPrice = '//android.view.ViewGroup[@content-desc="sort button"]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=sortByPrice,
    )
    element.click()
    time.sleep(2)

    sortP = '//android.view.ViewGroup[@content-desc="priceAsc"]/android.widget.TextView[2]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=sortP,
    )
    element.click()
    time.sleep(2)

    addSecProduct = '(//android.view.ViewGroup[@content-desc="store item"])[2]/android.view.ViewGroup[' \
                    '1]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=addSecProduct,
    )
    element.click()
    time.sleep(2)

    qty1 = '//android.view.ViewGroup[@content-desc="counter plus button"]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=qty1,
    )
    element.click()
    time.sleep(2)

    qty2 = '//android.view.ViewGroup[@content-desc="counter plus button"]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=qty2,
    )
    element.click()
    time.sleep(2)

    cart1 = '//android.view.ViewGroup[@content-desc="Add To Cart button"]/android.widget.TextView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=cart1,
    )
    element.click()
    time.sleep(2)

    menu2 = "//android.view.ViewGroup[@content-desc='open menu']/android.widget.ImageView"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=menu2,
    )
    element.click()
    time.sleep(2)

    catalog1 = '//android.view.ViewGroup[@content-desc="longpress reset app"]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=catalog1,
    )
    element.click()
    time.sleep(2)

    add3rdProduct = '(//android.view.ViewGroup[@content-desc="store item"])[3]/android.view.ViewGroup[' \
                    '1]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=add3rdProduct,
    )
    element.click()
    time.sleep(2)

    qty3 = '//android.view.ViewGroup[@content-desc="counter plus button"]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=qty3,
    )
    element.click()
    time.sleep(2)

    cart2 = '//android.view.ViewGroup[@content-desc="Add To Cart button"]/android.widget.TextView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=cart2,
    )
    element.click()
    time.sleep(2)

    menu3 = "//android.view.ViewGroup[@content-desc='open menu']/android.widget.ImageView"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=menu3,
    )
    element.click()
    time.sleep(2)

    catalog2 = '//android.view.ViewGroup[@content-desc="longpress reset app"]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=catalog2,
    )
    element.click()
    time.sleep(2)

    """
    # Scroll down
    img = '//android.view.ViewGroup[@content-desc="products screen"]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
    imgElement = driver.find_element(
        by=AppiumBy.XPATH,
        value=img,
    )
    action = TouchAction(driver)
    action.long_press(imgElement, duration=10000).move_to(x=0, y=0).release().perform()
    time.sleep(3)
    """
    add5thProduct = '(//android.view.ViewGroup[@content-desc="store item"])[5]/android.view.ViewGroup[' \
                    '1]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=add5thProduct,
    )
    element.click()
    time.sleep(2)

    cart3 = '//android.view.ViewGroup[@content-desc="Add To Cart button"]/android.widget.TextView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=cart3,
    )
    element.click()
    time.sleep(2)

    goCart = '//android.view.ViewGroup[@content-desc="cart badge"]/android.widget.TextView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=goCart,
    )
    element.click()
    time.sleep(2)

    dec1stPro = '(//android.view.ViewGroup[@content-desc="counter minus button"])[1]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=dec1stPro,
    )
    element.click()
    time.sleep(3)

    """
    # Scroll down
    img1 = '//android.widget.ScrollView[@content-desc="cart screen"]/android.view.ViewGroup/android.widget.ImageView[1]'
    imgElement = driver.find_element(
        by=AppiumBy.XPATH,
        value=img1,
    )
    action = TouchAction(driver)
    action.long_press(imgElement, duration=1000).move_to(x=0, y=0).release().perform()
    time.sleep(3)
    """
    inc3rdPro = '(//android.view.ViewGroup[@content-desc="counter plus button"])[2]/android.widget.ImageView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=inc3rdPro,
    )
    element.click()
    time.sleep(2)

    rmvSecPro = '(//android.view.ViewGroup[@content-desc="remove item"])[1]/android.widget.TextView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=rmvSecPro,
    )
    element.click()
    time.sleep(2)

    checkout = '//android.view.ViewGroup[@content-desc="Proceed To Checkout button"]/android.widget.TextView'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=checkout,
    )
    element.click()
    time.sleep(2)

    # Complete checkout process
    fullName = '//android.widget.EditText[@content-desc="Full Name* input field"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=fullName,
    )
    element.send_keys('Bob')
    time.sleep(2)

    add = '//android.widget.EditText[@content-desc="Address Line 1* input field"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=add,
    )
    element.send_keys('Kuril Chowrasta')
    time.sleep(2)

    city = '//android.widget.EditText[@content-desc="City* input field"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=city,
    )
    element.send_keys('Dhaka')
    time.sleep(2)

    zipC = '//android.widget.EditText[@content-desc="Zip Code* input field"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=zipC,
    )
    element.send_keys('1234')
    time.sleep(2)

    country = '//android.widget.EditText[@content-desc="Country* input field"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=country,
    )
    element.send_keys('Bangladesh')
    time.sleep(2)

    pay = '//android.view.ViewGroup[@content-desc="To Payment button"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=pay,
    )
    element.click()
    time.sleep(2)

    # Review Order
    fName = '//android.widget.EditText[@content-desc="Full Name* input field"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=fName,
    )
    element.send_keys('Bob Canary')
    time.sleep(2)

    card = '//android.widget.EditText[@content-desc="Card Number* input field"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=card,
    )
    element.send_keys('123456789101112')
    time.sleep(2)

    date = '//android.widget.EditText[@content-desc="Expiration Date* input field"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=date,
    )
    element.send_keys('0425')
    time.sleep(2)

    code = '//android.widget.EditText[@content-desc="Security Code* input field"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=code,
    )
    element.send_keys('123')
    time.sleep(2)

    orderBtn = '//android.view.ViewGroup[@content-desc="Review Order button"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=orderBtn,
    )
    element.click()
    time.sleep(2)

    orderBtn1 = '//android.view.ViewGroup[@content-desc="Review Order button"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=orderBtn1,
    )
    element.click()
    time.sleep(2)

    placeOdr = '//android.view.ViewGroup[@content-desc="Place Order button"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=placeOdr,
    )
    element.click()
    time.sleep(2)

    cont = '//android.view.ViewGroup[@content-desc="Continue Shopping button"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=cont,
    )
    element.click()
    time.sleep(2)

    menu4 = "//android.view.ViewGroup[@content-desc='open menu']/android.widget.ImageView"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=menu4,
    )
    element.click()
    time.sleep(2)

    logoutBtn = '(//android.widget.TextView[@content-desc="store item text"])[3]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=logoutBtn,
    )
    element.click()
    time.sleep(2)

    logout = 'android:id/button1'
    element = driver.find_element(
        by=AppiumBy.ID,
        value=logout,
    )
    element.click()
    time.sleep(2)

    okay = 'android:id/button1'
    element = driver.find_element(
        by=AppiumBy.ID,
        value=okay,
    )
    element.click()
    time.sleep(2)

    print('Test: Successful ✔')
except Exception as e:
    print('Test: Failed! 👎')
    print(f"Error when Test: {e}")

    driver.close()
