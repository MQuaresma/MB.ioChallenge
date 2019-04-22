#!/usr/bin/env python3

""" Mercedes Workflow Automator

This script allows the user to automate the workflow of purchasing an item of merchandise on the Mercedes-Benz online shop.

The tool searches for items matching the term "cap" and randomly selects, from the listed items, one item to add to the 
shopping basket. It then proceed to filling in the details form and stops when a payment method is requested.

"""
import time
from selenium import webdriver
from random import randint



def setup_driver():
    ''' Loads the Webdriver and fetches the initial page, bypassing the cookie warning
    '''

    base_url = 'https://shop.mercedes-benz.com/en-gb/collection/'
    driver = webdriver.Safari()
    driver.get(base_url)
    driver.implicitly_wait(8);
    #Locate the cookie accept button
    cookie_accept = driver.find_elements_by_xpath("//*[@id=\"button-text\"]")[0] 
    cookie_accept.click()
    return driver


def search_product(driver):
    '''Randomly selects a product matching the search term "cap"
    '''

    # Find the search button to trigger the search field DOM element
    search = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/header-grid/div/div/div[2]/div[2]/div/div[1]/div/header-search/div/div[1]")[0]
    search.click()
    search_form = driver.find_elements_by_xpath("//*[@id=\"searchTerm\"]")[0]
    search_form.send_keys("cap")
    search_form.submit()
    prod_count = len(driver.find_elements_by_class_name("utils-product-tile-link"))
    prod_index = randint(1, prod_count)
    product = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/pg-grid/div/div/div[4]/div[" + str(prod_index) + "]/utils-product-tile-large/div")[0]
    product.click()

def add_to_basket(driver):
    '''Adds a previously selected item to the basket
    '''

    add_to_basket = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/pdp-grid/div[1]/div[2]/utils-sticky-bar/ng-transclude/div/div/pdp-buy-box-add-to-basket/div/div/div/div[2]/button")[0]
    # wait for the action to load
    time.sleep(2)
    add_to_basket.click()
    driver.switch_to.active_element
    driver.switch_to.default_content
    shop_basket = driver.find_elements_by_xpath("/html/body/div[7]/div/div/div/div[2]/div[2]/div/div[2]/button[1]")[0]
    shop_basket.click()

def checkout(driver):
    ''' Fill the details in checkout
    '''

    proceed = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div/co-func-header/div/div[2]/button")[0]
    proceed.click()
    email_input = driver.find_element_by_id("dcp-login-guest-user-email")
    email_input.send_keys("dummy@gmail.com")
    place_order = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/div/co-grid-tunnel/div/div/co-order-process-login/div/div/div[3]/ng-include/div/form/button")[0]
    place_order.click()
    salutation_mr = driver.find_elements_by_xpath("//*[@id=\"co-address-payment\"]/div[1]/utils-dynamic-form/div/form/div[1]/div[1]")[0]
    salutation_mr.click()
    fst_name = driver.find_element_by_id("co_payment_address-firstName") 
    fst_name.send_keys("teste")
    lst_name = driver.find_element_by_id("co_payment_address-lastName")
    lst_name.send_keys("teste")
    no = driver.find_element_by_id("co_payment_address-line2")
    no.send_keys("teste")
    st = driver.find_element_by_id("co_payment_address-line1")
    st.send_keys("teste")
    town = driver.find_element_by_id("co_payment_address-town")
    town.send_keys("teste")
    pcode = driver.find_element_by_id("co_payment_address-postalCode")
    pcode.send_keys("SP2 0FL")

def main():
    driver = setup_driver()
    search_product(driver)
    add_to_basket(driver)
    checkout(driver)
    last_step = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div/co-func-header/div/div[2]/button")[0]
    # wait for the action to load
    time.sleep(2)
    last_step.click()
    dummy_check = driver.find_element_by_id("dcp-co-payment-modes_options-CREDITCARD") #dummy DOM action to force page to load
    # keep browser from quitting immediately
    time.sleep(5)

if __name__ == "__main__":
    main()
