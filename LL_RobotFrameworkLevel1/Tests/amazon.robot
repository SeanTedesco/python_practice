*** Settings ***
Documentation  Test suite to implement Amazon checkout feature.
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
User must sign in to check out
    [Documentation]  amazon test
    [Tags]  Smoke
    open browser  http://www.amazon.com  chrome
    wait until page contains  Today's Deals
    input text  id=twotabsearchtextbox  Ferrari 458
    click button  id=nav-search-submit-button
    wait until page contains  results for "Ferrari 458"
    click link  xpath=/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div[2]/h2/a
    wait until page contains  Back to results
    click button  id=add-to-cart-button
    wait until page contains  Added to Cart
    click button  xpath=iv/div/span[2]/span/a
    page should contain  ap_signin1a_pagelet_title
    element text should be  ap_signin1a_pagelet_title Sign input text
    close browser

*** Keywords ***