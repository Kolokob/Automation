# Created by kolokob at 6/27/24

Feature: I go through test cases from https://docs.google.com/spreadsheets/d/1bG28ygPm0nvvZmaYDYxxHTO9JurJgrjl-LbyfRbu0g8/edit?pli=1&gid=0#gid=0

  @ios
  @client
  Scenario: Order creation and completion as instant order
    Given I click on "Get a Quote"
    Then I click on "Last-mile delivery" service
    Then I add "1" pick-up's addresses and "1" drop-off addresses
    Then I click on button "Continue"
    Then I add parcel size as "heavy_load" and "15ft Box Truck"


