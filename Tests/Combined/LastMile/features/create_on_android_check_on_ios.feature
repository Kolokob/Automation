# Created by kolokob at 6/17/24
Feature: Create an instant order on Android check as a driver on IOS

  @android
  Scenario: I create an instant order in Android
    Given I click on "Get a Quote"
    Then I select "Last-mile delivery" service
    Then I add pick-up address as "S"
    Then I add location details as "Crater"
    Then I click Continue
    Then I add drop-off address as "Q"
    Then I add location details as "Sun"
    Then I click Continue
    Then I click Continue
    Then I add parcel size as "small"
    Then I make a "medium" "down" swipe
    Then I add declared value "1000"
    Then I click Continue
    Then I add pick-up time as "urgent"
    Then I add extra services: "{'Ladder':['Be careful', '5'], "Packing and Unpacking":["ARA", '2 hours']}"
    Then I add promo code as "50%"
    Then I click Continue
    Then I add tips as "50"
    Then I click Continue
    Then I add name of the order as "Cockroaches"
    Then I add description to the order as "Describe your shipment"
    Then I make a "medium" "down" swipe
    Then I add sender full name as "Dart Wader"
    Then I add sender phone number as "5104029083"
    Then I make a "long" "down" swipe
    Then I make a "short" "down" swipe
    Then I make a "short" "down" swipe
    Then I add receiver full name as "John Marston"
    Then I add receiver phone number as "5104029083"
    Then I click Continue
    Then I click Continue
    Then I add credit card info as "4242 4242 4242 4242" for credit card number, "0429" for expiration date and "123" for CVV
    Then I make a "long" "down" swipe
    Then I make a "long" "down" swipe
    Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number
    Then I click Continue
    Then I click on "Track Order"
    Then I click on button2 (I have no idea what it is, but it is necessary)
    Given I login as new user with new credentials that were got from the email
    Then I navigate to orders
    Then I extract data to json file

#  @ios
#  Scenario Outline: I check as a driver on IOS
##    Given I login as a driver with username "unicornM99@mail.com" and password "123456"
#    Given I search for the order ID "<order_id>" and click on it
#    Then I as driver ios app extract all data to json file
#    Examples:
#      | order_id |
#      | 724155   |
#      | 724140   |
#      | 724139   |
#      | 724138   |
#      | 724135   |


  @ios
  Scenario:  I check as a driver on IOS recently created an order
    Given I click on the latest available order
    Then I as driver ios app extract all data to json file

  Scenario: I compare two JSON files from client and driver
    Given I compare two JSON files from client and driver
    Then I enjoy my work






