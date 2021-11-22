*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page 

** Test Cases **
Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set Password-Confirmation  testi123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  testi123
    Set Password-Confirmation  testi123
    Submit Credentials
    Registration Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  aa123
    Set Password-Confirmation  aa123
    Submit Credentials
    Registration Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi123
    Set Password-Confirmation  testi123456
    Submit Credentials
    Registration Should Fail With Message  Passwords not matching

Login After Successful Registration
    Set Username  testii
    Set Password  testi123
    Set Password-Confirmation  testi123
    Submit Credentials
    Registration Should Succeed
    Go To Login Page
    Set Username  testii
    Set Password  testi123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  aa
    Set Password  testi123
    Set Password-Confirmation  testi123
    Submit Credentials
    Registration Should Fail With Message  Invalid username
    Go To Login Page
    Set Username  aa
    Set Password  testi123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

** Keywords **
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password-Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}