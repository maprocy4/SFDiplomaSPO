#!/usr/bin/python

import pytest
from pages.auth_page import AuthPage

def test_smoke_test(web_browser):

    page = AuthPage(web_browser)

    result_state = False

    result_state = bool(page.header_logo)
    
    print(result_state)
