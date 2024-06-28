# Created by kolokob at 6/27/24
Feature: I go through test cases from https://docs.google.com/spreadsheets/d/1bG28ygPm0nvvZmaYDYxxHTO9JurJgrjl-LbyfRbu0g8/edit?pli=1&gid=0#gid=0

  @android
  Scenario Outline: Order creation and completion as instant order
    Given I click on "Get a Quote"
    Then I select "Last-mile delivery" service
    Then I add "<pick_up_address_amount>" pick-up's addresses and "<pick_up_address_amount>" drop-off addresses
    Then I click Continue
    Then I add parcel size as "<parcel_size>" and "<vehicle_type>"
    Then I make a "medium" "down" swipe
    Then I add declared value "1000"
    Then I click Continue
    Then I add pick-up time as "<pick_up_time>" with days "<days_or_date>" and time "<time>" for each and start date as "<start_date>"
    Then I click Continue
    Then I add tips as "<tips>"
    Then I click Continue
    Then I add name of the order as "Cockroaches"
    Then I add signature "<signature>"
    Then I add description to the order as "Describe your shipment"
    Then I add receiver's and sender's all info in all required fields
    Then I click Continue
    Then I click Continue
    Then I add credit card info as "4242 4242 4242 4242" for credit card number, "0429" for expiration date and "123" for CVV
    Then I make a "long" "down" swipe
    Then I make a "long" "down" swipe
    Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number
    Then I click Continue
    Then I click on "Track Order"
    Then I retrieve the login password
    Then I click on button2 (I have no idea what it is, but it is necessary)
    Given I login as new user with new credentials that were got from the email
    Then I navigate the latest order
#    Then I extract data to json file
    Examples:
      | pick_up_address_amount |  | pick_up_address_amount | parcel_size | vehicle_type   | pick_up_time | days_or_date               | time                         | start_date | tips | signature |  |
      | 3                      |  | 3                      | small       | None           | urgent       | None                       | None                         | None       | 20   | True      |  |
      | 2                      |  | 2                      | medium      | None           | urgent       | None                       | None                         | None       | None | False     |  |
      | 1                      |  | 4                      | large       | SUV            | scheduled    | 29/06/2024                 | 04:23 PM                     | None       | 10   | False     |  |
      | 1                      |  | 5                      | heavy_load  | 9ft Cargo Van  | scheduled    | 30/06/2024                 | 09:10 PM                     | None       | 100  | True      |  |
      | 10                     |  | 10                     | custom size | 17ft Box Truck | repeated     | Thursday, Saturday, Sunday | 10:32 PM, 06:18 PM, 11:08 AM | 15/07/2024 | 1    | False     |  |
