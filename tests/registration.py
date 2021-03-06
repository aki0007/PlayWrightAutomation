from src.page import CustomPage


def test_registration(page: CustomPage) -> None:
    # Leave the test like this to show how codegen creates code
    # Go to http://0.0.0.0:3000/register
    page.original.goto("http://0.0.0.0:3000/register")
    # Go to http://0.0.0.0:3000/register#/
    page.original.goto("http://0.0.0.0:3000/register#/")
    # Click [aria-label="Close Welcome Banner"]
    page.original.locator('[aria-label="Close Welcome Banner"]').click()
    # Click [aria-label="Show\/hide account menu"]
    page.original.locator('[aria-label="Show\\/hide account menu"]').click()
    # Click button[role="menuitem"]:has-text("exit_to_app Login")
    page.original.locator(
        'button[role="menuitem"]:has-text("exit_to_app Login")'
    ).click()
    # expect(page).to_have_url("http://0.0.0.0:3000/register#/login")
    # Click text=Not yet a customer?
    page.original.locator("text=Not yet a customer?").click()
    # expect(page).to_have_url("http://0.0.0.0:3000/register#/register")
    # Click [aria-label="Email address field"]
    page.original.locator('[aria-label="Email address field"]').click()
    # Fill [aria-label="Email address field"]
    page.original.locator('[aria-label="Email address field"]').fill(
        "jaksa.milanovic007@gmail.com"
    )
    # Click [aria-label="Field for the password"]
    page.original.locator('[aria-label="Field for the password"]').click()
    # Fill [aria-label="Field for the password"]
    page.original.locator('[aria-label="Field for the password"]').fill("Test123*")
    # Click [aria-label="Field to confirm the password"]
    page.original.locator('[aria-label="Field to confirm the password"]').click()
    # Fill [aria-label="Field to confirm the password"]
    page.original.locator('[aria-label="Field to confirm the password"]').fill(
        "Test123*"
    )
    # Click #registration-form div:has-text("Security Question *") >> nth=3
    page.original.locator('#registration-form div:has-text("Security Question *")').nth(
        3
    ).click()
    # Click text=Your eldest siblings middle name?
    page.original.locator("text=Your eldest siblings middle name?").click()
    # Click #registration-form div:has-text("Answer *") >> nth=3
    page.original.locator('#registration-form div:has-text("Answer *")').nth(3).click()
    # Fill [placeholder="Answer to your security question"]
    page.original.locator('[placeholder="Answer to your security question"]').fill(
        "Aki"
    )
    # Click [aria-label="Button to complete the registration"]
    # with page.expect_navigation(url="http://0.0.0.0:3000/register#/login"):
    with page.original.expect_navigation():
        page.original.locator(
            '[aria-label="Button to complete the registration"]'
        ).click()
