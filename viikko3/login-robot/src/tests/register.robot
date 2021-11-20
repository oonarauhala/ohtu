*** Settings ***
Resource  resource.robot
#Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Validate Username And Password  testi  testi123
    Input New Command
    Input Credentials  testi  testi 123

Register With Already Taken Username And Valid Password
    Create User And Input New Command
    Input Credentials  testi  testi1234
    Output Should Contain  User with username testi already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  a  testi123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  testi  ab123
    Output Should Contain  Invalid password
    
Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  testi  testitesti

*** Keywords ***
Create User And Input New Command
    Create User  testi  testi123
    Input New Command
