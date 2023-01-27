import pytest

from .pages.login_page import LoginPage, login_and_password_generator
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

main_page_link = 'http://selenium1py.pythonanywhere.com'
item_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason="I'm failed and I know it"))
                          for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    url = f"{item_link}?promo=offer{promo_offer}"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.should_be_product_page()
    product_page.click_button_add_to_basket()
    product_page.should_be_correct_answer()
    product_page.should_be_correct_page_data()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = main_page_link
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.go_to_basket()
    basket_page = BasketPage(browser, url)
    basket_page.should_be_no_items_in_basket()
    basket_page.should_be_empty_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = item_link
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, url)
    basket_page.should_be_no_items_in_basket()
    basket_page.should_be_empty_basket()


@pytest.mark.xfail(reason='fix it later')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = item_link
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.click_button_add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    url = item_link
    product_page = ProductPage(browser, url, 0)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = item_link
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_url()
    page.should_be_login_link()
    page.go_to_login_page()
    page.should_be_login_page()


def test_guest_should_see_login_link_on_product_page(browser):
    link = item_link
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason='fix it later')
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = item_link
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.click_button_add_to_basket()
    product_page.should_success_message_disappear()


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        url = main_page_link
        main_page = MainPage(browser, url)
        main_page.open()
        main_page.should_be_login_link()
        main_page.go_to_login_page()
        product_page = ProductPage(browser, url)
        product_page.should_be_login_page()  # have to move to own file for login page

    def test_guest_should_see_login_link(self, browser):
        url = main_page_link
        main_page = MainPage(browser, url)
        main_page.open()
        main_page.should_be_login_link()


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = main_page_link
        main_page = MainPage(browser, url)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, url)
        login_page.register_new_user(*login_and_password_generator())
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        url = item_link
        product_page = ProductPage(browser, url, 0)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = item_link
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.should_be_product_page()
        product_page.click_button_add_to_basket()
