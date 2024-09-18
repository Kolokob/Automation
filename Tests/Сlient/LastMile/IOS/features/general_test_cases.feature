# Created by kolokob at 6/27/24

Feature: I go through test cases from https://docs.google.com/spreadsheets/d/1bG28ygPm0nvvZmaYDYxxHTO9JurJgrjl-LbyfRbu0g8/edit?pli=1&gid=0#gid=0

  @ios
  @client
  Scenario: Order creation and completion as instant order
    Given I select country as "Canada" ios
    Given I click on "Get a Quote" ios
    Then I click on "Last-mile delivery" service ios
    Then I add "2" pick-up's addresses and "2" drop-off addresses ios
    Then I click on button "Continue" ios
    Then I add parcel size as "heavy_load" and "15ft Box Truck" ios
    Then I click on "Confirm shipment details" ios
    Then I click on "Calculate Price" ios
    Then I click on button "Continue" ios
    Then I add order name as "Obviously test" ios
    Then I fill all info for sender and receiver ios
    Then I click on button "Continue" ios
    Then I click "Confirm order" ios
    Then I add credit card info as "4242 4242 4242 4242" for credit card number, "0429" for expiration date and "123" for CVV ios
    Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number ios
    Then I click pay for the order ios
#    TODO: Check methods from line 19 to line 23; they may not work



