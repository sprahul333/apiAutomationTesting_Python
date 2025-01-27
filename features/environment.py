from selenium import webdriver

def before_scenario(context, scenario):
    # Start browser before scenario is executed
    context.browser = webdriver.Chrome()

def before_step(context, step):
    print("Before step")
    print(step)

def after_step(context, step):
    print("After step")
    print(step)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        # Take screenshot if scenario failed
        context.browser.save_screenshot("screenshot.png")