# Created by kolokob at 6/27/24

Feature: I go through test cases from https://docs.google.com/spreadsheets/d/1bG28ygPm0nvvZmaYDYxxHTO9JurJgrjl-LbyfRbu0g8/edit?pli=1&gid=0#gid=0

  @ios
  @client
  Scenario: Order creation and completion as instant order
    Given I select country as "Canada" ios
    Given I click on "Get a Quote" ios
    Then I click on "Last-mile delivery" service ios
    Then I add "1" pick-up's addresses and "1" drop-off addresses ios
    Then I click on button "Continue" ios
    Then I add parcel size as "heavy_load" and "15ft Box Truck" ios
    Then I click on "Confirm shipment details" ios
    Then I click on "Calculate Price" ios
    Then I click on button "Continue" ios
    Then I add order name as "Obviously test" ios



