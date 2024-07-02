# Created by kolokob at 6/17/24
Feature: Create an order and check all payment methods

  @android
  Scenario: I create an instant order and pay with credit card
    Given I click on "Get a Quote"
    Then I select "Moving" service
    Then I select categories "Commercial Moving" with "3000 - 4000 sqft"
    Then I choose vehicle type as "Pickup Truck" in "Moving"
    Then I select "only driver" helpers
    Then I make a "medium" "down" swipe
    Then I click Continue
    Then I add "1" pick-up's addresses and "1" drop-off addresses
    Then I click Continue
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None"
    Then I click Continue
    Then I click Continue
    Then I add name of the order as "Cockroaches"
    Then I add description to the order as "Describe your shipment"
    Then I add receiver's and sender's all info in all required fields
    Then I click Continue
    Then I click Continue
    Then I add credit card info as "4242 4242 4242 4242" for credit card number, "0429" for expiration date and "123" for CVV
    Then I make a "long" "down" swipe
    Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number
    Then I click Continue
    Then I click on "Track Order"
    Then I retrieve the login password
    Then I click on button2 (I have no idea what it is, but it is necessary)
    Given I login as new user with new credentials that were got from the email
    Then I navigate the latest order

  @android
  Scenario Outline: I create an instant order and pay with a wrong credit card
    Given I click on "Get a Quote"
    Then I select "Moving" service
    Then I select categories "Commercial Moving" with "3000 - 4000 sqft"
    Then I choose vehicle type as "Pickup Truck" in "Moving"
    Then I select "only driver" helpers
    Then I make a "medium" "down" swipe
    Then I click Continue
    Then I add "1" pick-up's addresses and "1" drop-off addresses
    Then I click Continue
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None"
    Then I click Continue
    Then I click Continue
    Then I add name of the order as "Cockroaches"
    Then I add description to the order as "Describe your shipment"
    Then I add receiver's and sender's all info in all required fields
    Then I click Continue
    Then I click Continue
    Then I add credit card info as "<card_number>" for credit card number, "0429" for expiration date and "123" for CVV
    Then I should see an error message
    Examples:
      | card_number      |
      | 4000000000000002 |
      | 4000000000009987 |
      | 4000000000009995 |
      | 4000000000009979 |
      | 4000000000000069 |
      | 4000000000000127 |
      | 4000000000000119 |
      | 4242424242424241 |
      | 4000000000006975 |


  @android
  Scenario: I create an instant order with payment link but don't pay for it
    Given I click on "Get a Quote"
    Then I select "Moving" service
    Then I select categories "Commercial Moving" with "3000 - 4000 sqft"
    Then I choose vehicle type as "Pickup Truck" in "Moving"
    Then I select "only driver" helpers
    Then I make a "medium" "down" swipe
    Then I click Continue
    Then I add "1" pick-up's addresses and "1" drop-off addresses
    Then I click Continue
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None"
    Then I click Continue
    Then I click Continue
    Then I add name of the order as "Cockroaches"
    Then I add description to the order as "Describe your shipment"
    Then I add receiver's and sender's all info in all required fields
    Then I click Continue
    Then I click Continue
    Then I select payment type as payment link
    Then I add payer's phone number "5104029033" and email "automation.senpex@outlook.com"
    Then I make a "medium" "down" swipe
    Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number
    Then I click Continue
    Then I click on "Track Order"
    Then I retrieve the login password
    Then I click on button2 (I have no idea what it is, but it is necessary)
    Given I login as new user with new credentials that were got from the email
    Then I navigate the latest order

  @android
  Scenario: I create an instant order with payment link and pay for it
    Given I click on "Get a Quote"
    Then I select "Moving" service
    Then I select categories "Commercial Moving" with "3000 - 4000 sqft"
    Then I choose vehicle type as "Pickup Truck" in "Moving"
    Then I select "only driver" helpers
    Then I make a "medium" "down" swipe
    Then I click Continue
    Then I add "1" pick-up's addresses and "1" drop-off addresses
    Then I click Continue
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None"
    Then I click Continue
    Then I click Continue
    Then I add name of the order as "Cockroaches"
    Then I add description to the order as "Describe your shipment"
    Then I add receiver's and sender's all info in all required fields
    Then I click Continue
    Then I click Continue
    Then I select payment type as payment link
    Then I add payer's phone number "5104029033" and email "automation.senpex@outlook.com"
    Then I make a "medium" "down" swipe
    Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number
    Then I click Continue
    Then I click on "Track Order"
    Then I open retrieved payment link and pay for it "4242424242424242", "0429", "123"
    Then I open "customer" app
    Then I retrieve the login password
    Given I login as new user with new credentials that were got from the email
    Then I navigate the latest order
    Then I should see order status as "Paid order"

  @android
  Scenario: I create an order as a user with account and pay with a new credit card
    Given I login as client with username "gihala5645@picdv.com" and password "123456"
    Then I select "Last-mile delivery" service
    Then I add pick-up address as "S"
    Then I add location details as "Crater"
    Then I click Continue
    Then I add drop-off address as "Q"
    Then I add location details as "Sun"
    Then I click Continue
    Then I click Continue
    Then I add parcel size as "small" and "None"
    Then I make a "medium" "down" swipe
    Then I add declared value "1000"
    Then I click Continue
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None"
    Then I add extra services "Ladder" and service "5"
    Then I add promo code as "50%"
    Then I click Continue
    Then I add tips as "50"
    Then I click Continue
    Then I add name of the order as "Cockroaches"
    Then I add description to the order as "Describe your shipment"
    Then I make a "medium" "down" swipe
    Then I make a "long" "down" swipe
    Then I make a "short" "down" swipe
    Then I make a "short" "down" swipe
    Then I add receiver full name as "John Marston"
    Then I add receiver phone number as "5104029083"
    Then I click Continue
    Then I click Continue
    Then I add a new card as "4242 4242 4242 4242" for credit card number, "0429" for expiration date and "123" for CVV
    Then I select recently created credit card
    Then I click Continue
    Then I click on "Track Order"

  @android
  Scenario Outline: I create an order as a user with account and pay with a wrong credit card
    Given I login as client with username "gihala5645@picdv.com" and password "123456"
    Then I select "Moving" service
    Then I select categories "Commercial Moving" with "3000 - 4000 sqft"
    Then I choose vehicle type as "Pickup Truck" in "Moving"
    Then I select "only driver" helpers
    Then I make a "medium" "down" swipe
    Then I click Continue
    Then I add "1" pick-up's addresses and "1" drop-off addresses
    Then I click Continue
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None"
    Then I click Continue
    Then I click Continue
    Then I add name of the order as "Cockroaches"
    Then I add description to the order as "Describe your shipment"
    Then I add receiver's and sender's all info in all required fields
    Then I click Continue
    Then I click Continue
    Then I add a new card as "<card_number>" expecting it to fail
    Then I should see an error message
    Examples:
      | card_number      |
      | 4000000000000002 |
      | 4000000000009987 |
      | 4000000000009995 |
      | 4000000000009979 |
      | 4000000000000069 |
      | 4000000000000127 |
      | 4000000000000119 |
      | 4242424242424241 |
      | 4000000000006975 |

  @android
  Scenario: I create an order as a user with account and pay with a saved credit card
    Given I login as client with username "gihala5645@picdv.com" and password "123456"
    Then I select "Last-mile delivery" service
    Then I add pick-up address as "S"
    Then I add location details as "Crater"
    Then I click Continue
    Then I add drop-off address as "Q"
    Then I add location details as "Sun"
    Then I click Continue
    Then I click Continue
    Then I add parcel size as "small" and "None"
    Then I make a "medium" "down" swipe
    Then I add declared value "1000"
    Then I click Continue
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None"
    Then I add extra services "Ladder" and service "5"
    Then I add promo code as "50%"
    Then I click Continue
    Then I add tips as "50"
    Then I click Continue
    Then I add name of the order as "Cockroaches"
    Then I add description to the order as "Describe your shipment"
    Then I make a "medium" "down" swipe
    Then I make a "long" "down" swipe
    Then I make a "short" "down" swipe
    Then I make a "short" "down" swipe
    Then I add receiver full name as "John Marston"
    Then I add receiver phone number as "5104029083"
    Then I click Continue
    Then I click Continue
    Then I select saved credit card
    Then I click Continue
    Then I click on "Track Order"

  @android
  Scenario: I create an order as a user with account and pay by payment link
    Given I login as client with username "gihala5645@picdv.com" and password "123456"
    Then I select "Last-mile delivery" service
    Then I add "1" pick-up's addresses and "1" drop-off addresses
    Then I click Continue
    Then I add parcel size as "small" and "None"
    Then I make a "medium" "down" swipe
    Then I add declared value "1000"
    Then I click Continue
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None"
    Then I add extra services "Ladder" and service "5"
    Then I add promo code as "50%"
    Then I click Continue
    Then I add tips as "50"
    Then I click Continue
    Then I add name of the order as "Cockroaches"
    Then I add description to the order as "Describe your shipment"
    Then I add receiver's and sender's all info in all required fields
    Then I click Continue
    Then I click Continue
    Then I select payment type as payment link
    Then I add payer's phone number "5104029033" and email "<>"
    Then I click Continue
    Then I open retrieved payment link and pay for it "4242424242424242", "0429", "123"
    Then I open "customer" app
    Then I retrieve the login password
    Given I login as new user with new credentials that were got from the email
    Then I navigate the latest order
    Then I should see order status as "Paid order"

