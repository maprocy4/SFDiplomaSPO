#!/usr/bin/python

from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    ## Основные элементы страницы

    # Логотип в левом верхнем углу страницы (в левой части "шапки" страницы)
    header_logo = WebElement(xpath='//*[@id="app-header"]/div[1]/div[1]/svg[1]')

    # Левая часть страницы
    # Логотип в левой части страницы
    left_side_logo = WebElement(css_selector='svg.rt_logo.what-is-container__logo-container')
    # Заголовок "Личный кабинет" в левой части страницы
    left_side_title = WebElement(css_selector='h2.what-is__title')
    # Текст в левой части страницы
    # left_side_caption = WebElement(xpath='//section[contains(.,"Личный кабинетПерсональный помощник в цифровом мире Ростелекома")]')
    left_side_caption = WebElement(css_selector='p.what-is__desc')

    # Правая часть страницы
    # Заголовок формы авторизации
    right_side_auth_form_title = WebElement(css_selector='h1.card-container__title')
    # Табы методов авторизации
    right_side_auth_form_tabs = WebElement(css_selector='div.rt-tabs.rt-tabs--orange.rt-tabs--small.tabs-input-container__tabs')
    # Поле ввода мобильного телефона
    right_side_auth_form_cellphone = WebElement(css_selector='input#username.rt-input__input.rt-input__input--rounded.rt-input__input--orange')
    # Поле ввода пароля
    right_side_auth_form_password = WebElement(css_selector='input#password.rt-input__input.rt-input__input--rounded.rt-input__input--orange')
    # Кнопка отправки формы
    right_side_auth_form_submit_btn = WebElement(css_selector='button#kc-login.rt-btn.rt-btn--orange.rt-btn--medium.rt-btn--rounded.login-form__login-btn')

    # "Подвал" страницы
    # Copyright в левой части "подвала"
    footer_copyright = WebElement(css_selector='div.rt-footer-left__item.rt-footer-copyright.rt-footer-side-item')
    # Текст в центре "подвала"
    footer_message = WebElement(css_selector='div.rt-foote-left__item')
    # Телефон техподдержки в правой части "подвала"
    footer_ts = WebElement(css_selector='div.rt-footer-right.rt-footer-side-item')
