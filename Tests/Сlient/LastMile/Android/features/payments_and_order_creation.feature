# Created by kolokob at 6/17/24
Feature: Create an order and check all payment methods

  @android
  Scenario: I create an instant order and pay with credit card
    Given I click on "Get a Quote" android
    Then I select "Last-mile delivery" service android
    Then I add "1" pick-up's addresses and "1" drop-off addresses android
    Then I click Continue android
    Then I click Continue android
    Then I add parcel size as "small" and "None" android
    Then I make a "medium" "down" swipe android
    Then I click Continue android
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None" android
    Then I click Continue android
    Then I click Continue android
    Then I add name of the order as "Cockroaches" android
    Then I add description to the order as "Describe your shipment" android
    Then I make a "medium" "down" swipe android
    Then I add receiver's and sender's all info in all required fields android
    Then I click Continue android
    Then I click Continue android
    Then I add credit card info as "4242 4242 4242 4242" for credit card number, "0429" for expiration date and "123" for CVV android
    Then I make a "long" "down" swipe android
    Then I make a "long" "down" swipe android
    Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number android
    Then I click Continue android
    Then I click on "Track Order" android
    Then I retrieve the login password android
    Then I click on button2 (I have no idea what it is, but it is necessary) android
    Given I login as new user with new credentials that were got from the email android
    Then I navigate the latest order android

  @android
  Scenario Outline: I create an instant order and pay with a wrong credit card
    Given I click on "Get a Quote"
    Then I select "Last-mile delivery" service android
    Then I add pick-up address as "S" android
    Then I add location details as "Crater" android
    Then I click Continue android
    Then I add drop-off address as "Q" android
    Then I add location details as "Sun" android
    Then I click Continue android
    Then I click Continue android
    Then I click Continue android
    Then I click Continue android
    Then I click Continue android
    Then I add name of the order as "Cockroaches" android
    Then I add description to the order as "Describe your shipment" android
    Then I make a "medium" "down" swipe android
    Then I add sender full name as "Dart Wader" android
    Then I add sender phone number as "5104029083" android
    Then I make a "long" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I add receiver full name as "John Marston" android
    Then I add receiver phone number as "5104029083" android
    Then I click Continue android
    Then I click Continue android
    Then I add credit card info as "<card_number>" for credit card number, "0429" for expiration date and "123" for CVV android
    Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number android
    Then I make a "long" "down" swipe android
    Then I click Continue android
    Then I should see an error message android
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
    Given I click on "Get a Quote" android
    Then I select "Last-mile delivery" service android
    Then I add pick-up address as "S" android
    Then I add location details as "Crater" android
    Then I click Continue android
    Then I add drop-off address as "Q" android
    Then I add location details as "Sun" android
    Then I click Continue android
    Then I click Continue android
    Then I add parcel size as "small" and "None" android
    Then I make a "medium" "down" swipe android
    Then I add declared value "1000" android
    Then I click Continue android
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None" android
    Then I add extra services "Ladder" and service "5" android
    Then I add promo code as "50%" android
    Then I click Continue android
    Then I add tips as "50" android
    Then I click Continue android
    Then I add name of the order as "Cockroaches" android
    Then I add description to the order as "Describe your shipment" android
    Then I make a "medium" "down" swipe android
    Then I add sender full name as "Dart Wader" android
    Then I add sender phone number as "5104029083" android
    Then I make a "long" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I add receiver full name as "John Marston" android
    Then I add receiver phone number as "5104029083" android
    Then I click Continue android
    Then I click Continue android
    Then I select payment type as payment link android
    Then I add payer's phone number "5104029033" and email "<>" android
    Then I make a "long" "down" swipe android
    Then I make a "long" "down" swipe android
    Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number android
    Then I click Continue android
    Then I click on "Track Order" android
    Then I retrieve the login password android
    Then I click on button2 (I have no idea what it is, but it is necessary) android
    Given I login as new user with new credentials that were got from the email android
    Then I navigate the latest order android
    Then I extract data to json file android

  @android
  Scenario: I create an instant order with payment link and pay for it
    Given I click on "Get a Quote" android
    Then I select "Last-mile delivery" service android
    Then I add pick-up address as "S" android
    Then I add location details as "Crater" android
    Then I click Continue android
    Then I add drop-off address as "Q" android
    Then I add location details as "Sun" android
    Then I click Continue android
    Then I click Continue android
    Then I add parcel size as "small" and "None" android
    Then I make a "medium" "down" swipe android
    Then I add declared value "1000" android
    Then I click Continue android
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None" android
    Then I add extra services "Ladder" and service "5" android
    Then I add promo code as "50%" android
    Then I click Continue android
    Then I add tips as "50" android
    Then I click Continue android
    Then I add name of the order as "Cockroaches" android
    Then I add description to the order as "Describe your shipment" android
    Then I make a "medium" "down" swipe android
    Then I add sender full name as "Dart Wader" android
    Then I add sender phone number as "5104029083" android
    Then I make a "long" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I add receiver full name as "John Marston" android
    Then I add receiver phone number as "5104029083" android
    Then I click Continue android
    Then I click Continue android
    Then I select payment type as payment link android
    Then I add payer's phone number "5104029033" and email "<>" android
    Then I make a "long" "down" swipe android
    Then I make a "long" "down" swipe android
    Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number android
    Then I click Continue android
    Then I click on "Track Order" android
    Then I click on button2 (I have no idea what it is, but it is necessary) android
    Then I open retrieved payment link and pay for it "4242424242424242", "0429", "123" android
    Then I open "customer" app android
    Then I retrieve the login password android
    Given I login as new user with new credentials that were got from the email android
    Then I navigate the latest order android
    Then I extract data to json file android


  @android
  Scenario: I create an order as a user with account and pay with a new credit card
    Given I login as client with username "gihala5645@picdv.com" and password "123456" android
    Then I select "Last-mile delivery" service android
    Then I add pick-up address as "S" android
    Then I add location details as "Crater" android
    Then I click Continue android
    Then I add drop-off address as "Q" android
    Then I add location details as "Sun" android
    Then I click Continue android
    Then I click Continue android
    Then I add parcel size as "small" and "None" android
    Then I make a "medium" "down" swipe android
    Then I add declared value "1000" android
    Then I click Continue android
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None" android
    Then I add extra services "Ladder" and service "5" android
    Then I add promo code as "50%" android
    Then I click Continue android
    Then I add tips as "50" android
    Then I click Continue android
    Then I add name of the order as "Cockroaches" android
    Then I add description to the order as "Describe your shipment" android
    Then I make a "medium" "down" swipe android
    Then I make a "long" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I add receiver full name as "John Marston" android
    Then I add receiver phone number as "5104029083" android
    Then I click Continue android
    Then I click Continue android
    Then I add a new card as "4242 4242 4242 4242" for credit card number, "0429" for expiration date and "123" for CVV android
    Then I select recently created credit card android
    Then I click Continue android
    Then I click on "Track Order" android

  @android
  Scenario Outline: I create an order as a user with account and pay with a wrong credit card
    Given I login as client with username "gihala5645@picdv.com" and password "123456" android
    Then I select "Last-mile delivery" service android
    Then I add pick-up address as "S" android
    Then I add location details as "Crater" android
    Then I click Continue android
    Then I add drop-off address as "Q" android
    Then I add location details as "Sun" android
    Then I click Continue android
    Then I click Continue android
    Then I add parcel size as "small" and "None" android
    Then I make a "medium" "down" swipe android
    Then I add declared value "1000" android
    Then I click Continue android
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None" android
    Then I add extra services "Ladder" and service "5" android
    Then I add promo code as "50%" android
    Then I click Continue android
    Then I add tips as "50" android
    Then I click Continue android
    Then I add name of the order as "Cockroaches" android
    Then I add description to the order as "Describe your shipment" android
    Then I make a "medium" "down" swipe android
    Then I make a "long" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I add receiver full name as "John Marston" android
    Then I add receiver phone number as "5104029083" android
    Then I click Continue android
    Then I click Continue android
    Then I add a new card as "<card_number>" for credit card number, "0429" for expiration date and "123" for CVV android
    Then I select recently created credit card android
    Then I click Continue android
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
    Given I login as client with username "gihala5645@picdv.com" and password "123456" android
    Then I select "Last-mile delivery" service android
    Then I add pick-up address as "S" android
    Then I add location details as "Crater" android
    Then I click Continue android
    Then I add drop-off address as "Q" android
    Then I add location details as "Sun" android
    Then I click Continue android
    Then I click Continue android
    Then I add parcel size as "small" and "None" android
    Then I make a "medium" "down" swipe android
    Then I add declared value "1000" android
    Then I click Continue android
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None" android
    Then I add extra services "Ladder" and service "5" android
    Then I add promo code as "50%" android
    Then I click Continue android
    Then I add tips as "50" android
    Then I click Continue android
    Then I add name of the order as "Cockroaches" android
    Then I add description to the order as "Describe your shipment" android
    Then I make a "medium" "down" swipe android
    Then I make a "long" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I add receiver full name as "John Marston" android
    Then I add receiver phone number as "5104029083" android
    Then I click Continue android
    Then I click Continue android
    Then I select saved credit card android
    Then I click Continue android
    Then I click on "Track Order" android

  @android
  Scenario: I create an order as a user with account and pay by payment link
    Given I login as client with username "gihala5645@picdv.com" and password "123456" android
    Then I select "Last-mile delivery" service android
    Then I add pick-up address as "S" android
    Then I add location details as "Crater" android
    Then I click Continue android
    Then I add drop-off address as "Q" android
    Then I add location details as "Sun" android
    Then I click Continue android
    Then I click Continue android
    Then I add parcel size as "small" and "None" android
    Then I make a "medium" "down" swipe android
    Then I add declared value "1000" android
    Then I click Continue android
    Then I add pick-up time as "urgent" with days "None" and time "None" for each and start date as "None" android
    Then I add extra services "Ladder" and service "5" android
    Then I add promo code as "50%" android
    Then I click Continue android
    Then I add tips as "50" android
    Then I click Continue android
    Then I add name of the order as "Cockroaches" android
    Then I add description to the order as "Describe your shipment" android
    Then I make a "medium" "down" swipe android
    Then I make a "long" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I make a "short" "down" swipe android
    Then I add receiver full name as "John Marston" android
    Then I add receiver phone number as "5104029083" android
    Then I click Continue android
    Then I click Continue android
    Then I select payment type as payment link android
    Then I add payer's phone number "5104029033" and email "<>" android
    Then I click Continue android
    Then I open retrieved payment link and pay for it "4242424242424242", "0429", "123" android
    Then I open "customer" app android
    Given I login as client with username "gihala5645@picdv.com" and password "123456" android
    Then I navigate the latest order android