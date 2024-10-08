# Created by kolokob at 6/27/24
Feature: I go through test cases from https://docs.google.com/spreadsheets/d/1bG28ygPm0nvvZmaYDYxxHTO9JurJgrjl-LbyfRbu0g8/edit?pli=1&gid=0#gid=0

  @android
  Scenario Outline: Order creation and completion as instant order
    Given I select country as "Canada" android
    Given I click on "Get a Quote" android
    Then I select "Last-mile delivery" service android
    Then I add "<pick_up_address_amount>" pick-up's addresses and "<drop_off_address_amount>" drop-off addresses android
    Then I click Continue android
    Then I add parcel size as "<parcel_size>" and "<vehicle_type>" android
    Then I make a "medium" "down" swipe android
    Then I add declared value "<declared_value>" android
    Then I click Continue android
    Then I add pick-up time as "<pick_up_time>" with days "<days_or_date>" and time "<time>" for each and start date as "<start_date>" android
    Then I add extra services "<extra_service>" and service "<extra_service_details>" android
    Then I click Continue android
    Then I add tips as "<tips>" android
    Then I click Continue android
    Then I add name of the order as "Cockroaches" android
    Then I add signature "<signature>" android
    Then I add description to the order as "Describe your shipment" android
    Then I add receiver's and sender's all info in all required fields android
    Then I click Continue android
    Then I click Continue android
    Then I add credit card info as "4242 4242 4242 4242" for credit card number, "0429" for expiration date and "123" for CVV android
    Then I make a "long" "down" swipe android
    Then I make a "long" "down" swipe android
    Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number android
    Then I click Continue android
    Then I click on "Track Order" android
    Then I retrieve the login password
    Then I click on button2 (I have no idea what it is, but it is necessary) android
    Given I login as new user with new credentials that were got from the email
    Then I navigate the latest order android
    Examples:
      | pick_up_address_amount | extra_service | extra_service_details | drop_off_address_amount | parcel_size | vehicle_type   | declared_value | pick_up_time | days_or_date               | time                         | start_date | tips | signature |  |
      | 3                      | Ladder        | 5                     | 3                       | small       | None           | 1000           | urgent       | None                       | None                         | None       | 20   | True      |  |
      | 2                      |               |                       | 2                       | medium      | None           | 5000           | urgent       | None                       | None                         | None       | None | False     |  |
      | 1                      |               |                       | 4                       | large       | SUV            | 2000           | scheduled    | 29/06/2024                 | 04:23 PM                     | None       | 10   | False     |  |
      | 1                      |               |                       | 5                       | heavy_load  | 9ft Cargo Van  | 0              | scheduled    | 30/06/2024                 | 09:10 PM                     | None       | 100  | True      |  |
      | 10                     |               |                       | 10                      | custom size | 17ft Box Truck | 5              | repeated     | Thursday, Saturday, Sunday | 10:32 PM, 06:18 PM, 11:08 AM | 15/07/2024 | 1    | False     |  |


  @android
  Scenario Outline: Order creation and completion as existing user
    Given I login as client with username "test_base@gmail.com" and password "123456"
    Then I select "Last-mile delivery" service
    Then I add "<pick_up_address_amount>" pick-up's addresses and "<drop_off_address_amount>" drop-off addresses
    Then I click Continue
    Then I add parcel size as "<parcel_size>" and "<vehicle_type>"
    Then I make a "medium" "down" swipe
    Then I add declared value "<declared_value>"
    Then I click Continue
    Then I add pick-up time as "<pick_up_time>" with days "<days_or_date>" and time "<time>" for each and start date as "<start_date>"
    Then I add extra services "<extra_service>" and service "<extra_service_details>"
    Then I click Continue
    Then I add tips as "<tips>"
    Then I click Continue
    Then I add name of the order as "Cockroaches"
    Then I add signature "<signature>"
    Then I add description to the order as "Describe your shipment"
    Then I add receiver's and sender's all info in all required fields
    Then I click Continue
    Then I click Continue
    Then I select saved credit card
    Then I make a "long" "down" swipe
    Then I click Continue
    Then I click on "Track Order"
    Examples:
      | pick_up_address_amount | drop_off_address_amount | parcel_size | vehicle_type   | declared_value | pick_up_time | days_or_date               | time                         | start_date | tips | signature | extra_service | extra_service_details |
      | 1                      | 1                       | small       | None           | 1000           | urgent       | None                       | None                         | None       | 20   | True      | Ladder        | 5                     |
      | 2                      | 2                       | medium      | None           | 5000           | urgent       | None                       | None                         | None       | None | False     |               |                       |
      | 1                      | 4                       | large       | SUV            | 2000           | scheduled    | 29/06/2024                 | 04:23 PM                     | None       | 10   | False     |               |                       |
      | 1                      | 5                       | heavy_load  | 9ft Cargo Van  | 0              | scheduled    | 30/06/2024                 | 09:10 PM                     | None       | 100  | True      |               |                       |
      | 10                     | 10                      | custom size | 17ft Box Truck | 5              | repeated     | Thursday, Saturday, Sunday | 10:32 PM, 06:18 PM, 11:08 AM | 15/07/2024 | 1    | False     |               |                       |
