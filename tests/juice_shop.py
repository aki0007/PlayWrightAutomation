from src.page import CustomPage
from src.pom.add_apple_juice import AddAppleJuicePage
from src.pom.add_apple_pomice import AddApplePomicePage


def test_add_apple_juice(turn_on_trace, page: CustomPage, successful_login) -> None:
    add_apple_juice: AddAppleJuicePage = AddAppleJuicePage(page)

    add_apple_juice.add_apple_juice_to_basket()
    add_apple_juice.validate_apple_juice_in_basket()


def test_validate_banana_description(page: CustomPage, successful_login):
    # Click text=Banana Juice (1000ml)
    page.get_element("text=Banana Juice (1000ml)").click()
    # Click text=Monkeys love it the most
    assert page.get_element("text=Monkeys love it the most.")
    # Click [aria-label="Close\\ Dialog"
    page.get_element('[aria-label="Close\\ Dialog"]').click()


def test_add_apple_pomace(page: CustomPage, successful_login):
    apple_pomice_page: AddApplePomicePage = AddApplePomicePage(page)
    apple_pomice_page.add_apple_pomice_to_basket()
    apple_pomice_page.validate_apple_pomice()


# def test_fail_on_purpose(page: Page, successful_login):
#     # Click text=Monkeys love it the most.
#     @allure.step
#     def fail_test() -> None:
#         assert page.get_element(
#             "text=Moose love it the most."
#         ).is_visible(), "Element not visible on page"
#
#         assert page.get_element(
#             "text=Moose love it the most."
#         ).is_visible(), "Element not visible on page"
#
#     fail_test()
