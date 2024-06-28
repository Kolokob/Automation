# Created by kolokob at 6/27/24
Feature: I go through test cases from https://docs.google.com/spreadsheets/d/1bG28ygPm0nvvZmaYDYxxHTO9JurJgrjl-LbyfRbu0g8/edit?pli=1&gid=0#gid=0

  @android
  Scenario Outline: Order creation and completion as instant order
    Given I click on "Get a Quote"
    Then I select "Moving" service
    Then I select categories "<category>" with "<add_info>"
    Then I choose vehicle type as "<vehicle_type>" in "<service>"
    Then I select "<helpers_amount>" helpers
    Then I add extra services "<extra_service>" and service "<extra_service_details>"
    Then I make a "medium" "down" swipe
    Then I add declared value "1000"
    Then I click Continue
    Then I add "<pick_up_address_amount>" pick-up's addresses and "<drop_off_address_amount>" drop-off addresses
    Then I click Continue
    Then I add pick-up time as "<pick_up_time>" with days "<days_or_date>" and time "<time>" for each and start date as "<start_date>"
    Then I add promo code as "<promo>%"
    Then I click Continue
    Then I add tips as "<tips>"
    Then I click Continue
    Then I add name of the order as "Cockroaches"
    Then I add description to the order as "Describe your shipment"
    Then I add signature "<signature>"
    Then I add receiver's and sender's all info in all required fields
    Then I click Continue
    Then I click Continue
    Then I add credit card info as "<card_number>" for credit card number, "<exp_date>" for expiration date and "<cvv>" for CVV
    Then I make a "long" "down" swipe
    Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number
    Then I click Continue
    Then I click on "Track Order"
    Then I retrieve the login password
    Then I click on button2 (I have no idea what it is, but it is necessary)
    Given I login as new user with new credentials that were got from the email
    Then I navigate the latest order
  Examples:
    | helpers_amount | vehicle_type   | service | category                     | add_info                                    | extra_service                                   | extra_service_details  | pick_up_address_amount | drop_off_address_amount | pick_up_time | days_or_date | time     | start_date | promo     | tips | signature | card_number         | exp_date | cvv |  |
    | only driver    | Pickup Truck   | Moving  | Commercial Moving            | 3000 - 4000 sqft                            | Ladder, Packing and Unpacking, Special Handling | 5, 2 hours, 60 minutes | 1                      | 1                       | scheduled    | 06/30/2024   | 08:30 AM | None       | Ave Maria | 30   | Yes       | 4242 4242 4242 4242 | 0430     | 123 |  |
#    | 1              | 9ft Cargo Van  | Moving  | Warehouse/Storage Relocation | 4000 - 5000 sqft                            | Packing and Unpacking, Ladder, Hand Truck       | 45 minutes, 5, 2       |                        |                         |              |              |          |            |           |      |           |                     |          |     |  |
#    | 2              | 10ft Box Truck | Moving  | Home/Apartment Moving        | 2-bedroom                                   |                                                 |                        |                        |                         |              |              |          |            |           |      |           |                     |          |     |  |
#    | 3              | 15ft Box Truck | Moving  | Pallets                      | 7 Pallets                                   |                                                 |                        |                        |                         |              |              |          |            |           |      |           |                     |          |     |  |
#    | 1              | 17ft Box Truck | Moving  | Piano                        | Baby Grand Piano                            |                                                 |                        |                        |                         |              |              |          |            |           |      |           |                     |          |     |  |
#    | 2              | 9ft Cargo Van  | Moving  | Bike                         | Electric Bike                               |                                                 |                        |                        |                         |              |              |          |            |           |      |           |                     |          |     |  |
#    | 3              | 10ft Box Truck | Moving  | Server Racks                 | 5+ server racks                             |                                                 |                        |                        |                         |              |              |          |            |           |      |           |                     |          |     |  |
#    | 1              | 15ft Box Truck | Moving  | Electronics                  | TVs                                         |                                                 |                        |                        |                         |              |              |          |            |           |      |           |                     |          |     |  |
#    | 2              | 17ft Box Truck | Moving  | Sport Equipment              | Sports Equipment Transport                  |                                                 |                        |                        |                         |              |              |          |            |           |      |           |                     |          |     |  |
#    | 3              | 9ft Cargo Van  | Moving  | Furniture                    | Furniture Rearrangement and Placement       |                                                 |                        |                        |                         |              |              |          |            |           |      |           |                     |          |     |  |
#    | 1              | 10ft Box Truck | Moving  | Laboratory Equipment         | Laboratory Equipment Disposal and Recycling |                                                 |                        |                        |                         |              |              |          |            |           |      |           |                     |          |     |  |

