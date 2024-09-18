Feature: Delivery Test Cases with Custom Dimensions

  Scenario Outline: Delivery scenario
    Given pick up address amount is <pick_up_address_amount>
    And extra service is <extra_service>
    And extra service details are <extra_service_details>
    And drop off address amount is <drop_off_address_amount>
    And parcel size is <parcel_size>
    And vehicle type is <vehicle_type>
    And declared value is <declared_value>
    And pick up time is <pick_up_time>
    And days or date are <days_or_date>
    And time is <time>
    And start date is <start_date>
    And custom dimensions are <custom_dimensions>
    And tips are <tips>
    And signature is <signature>

  Examples:
    | pick_up_address_amount | extra_service | extra_service_details | drop_off_address_amount | parcel_size | vehicle_type | declared_value | pick_up_time | days_or_date | time | start_date | custom_dimensions | tips | signature |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Ref Van | 269 | repeated | Sunday, Tuesday | 04:14, 20:03 | 31/07/2024 | {'length': 139, 'width': 91, 'height': 188} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 15ft Box Truck | 7451 | urgent | None | None | None | {'length': 280, 'width': 76, 'height': 90} | 50 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | Pickup Truck | 2086 | scheduled | 04/09/2024 | 19:37 | None | {'length': 150, 'width': 148, 'height': 99} | 0 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | SUV | 9926 | urgent | None | None | None | {'length': 79, 'width': 20, 'height': 113} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | Car | 6784 | repeated | Saturday, Wednesday | 22:53, 15:42 | 07/08/2024 | {'length': 212, 'width': 105, 'height': 293} | 20 |
    | 1 | Blankets | 5 | 1 | custom size | Car | 9747 | repeated | Sunday, Saturday, Monday | 07:37, 12:33, 13:47 | 02/09/2024 | {'length': 11, 'width': 171, 'height': 168} | 20 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 4578 | urgent | None | None | None | {'length': 145, 'width': 35, 'height': 288} | 20 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 2105 | urgent | None | None | None | {'length': 147, 'width': 205, 'height': 282} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Pickup Truck | 141 | scheduled | 26/09/2024 | 04:26 | None | {'length': 69, 'width': 175, 'height': 204} | 50 |
    | 1 | None |  | 1 | custom size | 15ft Box Truck | 3613 | scheduled | 01/08/2024 | 21:14 | None | {'length': 176, 'width': 182, 'height': 228} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Ref Van | 1955 | repeated | Tuesday, Wednesday, Sunday | 12:59, 17:08, 17:23 | 29/08/2024 | {'length': 29, 'width': 188, 'height': 251} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Pickup Truck | 9297 | repeated | Sunday, Thursday, Saturday | 02:24, 17:17, 08:58 | 27/09/2024 | {'length': 194, 'width': 142, 'height': 115} | 50 |
    | 1 | None |  | 1 | custom size | SUV | 6519 | scheduled | 24/08/2024 | 13:56 | None | {'length': 228, 'width': 178, 'height': 35} | 100 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | Car | 9105 | repeated | Thursday | 19:10 | 29/09/2024 | {'length': 188, 'width': 183, 'height': 116} | 10 |
    | 1 | Ladder | 5 | 1 | custom size | Car | 7042 | scheduled | 18/09/2024 | 23:28 | None | {'length': 9, 'width': 300, 'height': 156} | 50 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Ref Van | 2094 | repeated | Wednesday, Tuesday | 12:21, 07:27 | 02/09/2024 | {'length': 219, 'width': 266, 'height': 261} | 50 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 15ft Box Truck | 9354 | urgent | None | None | None | {'length': 7, 'width': 274, 'height': 207} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Cargo Van | 6333 | scheduled | 18/09/2024 | 23:20 | None | {'length': 189, 'width': 196, 'height': 2} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Ref Van | 8741 | scheduled | 26/08/2024 | 15:13 | None | {'length': 69, 'width': 255, 'height': 210} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 1089 | scheduled | 26/08/2024 | 13:34 | None | {'length': 54, 'width': 273, 'height': 12} | 20 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 8258 | scheduled | 24/09/2024 | 01:22 | None | {'length': 154, 'width': 197, 'height': 54} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 15ft Box Truck | 1151 | repeated | Monday, Sunday | 08:04, 09:46 | 07/08/2024 | {'length': 174, 'width': 147, 'height': 207} | 100 |
    | 1 | Ladder | 5 | 1 | custom size | 15ft Box Truck | 6508 | urgent | None | None | None | {'length': 76, 'width': 78, 'height': 173} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Cargo Van | 6813 | repeated | Saturday, Sunday | 20:06, 20:08 | 21/07/2024 | {'length': 203, 'width': 230, 'height': 56} | 50 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | Car | 4428 | repeated | Friday, Monday | 16:43, 19:37 | 15/09/2024 | {'length': 141, 'width': 59, 'height': 63} | 50 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 4047 | urgent | None | None | None | {'length': 201, 'width': 4, 'height': 269} | 0 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 2249 | scheduled | 18/07/2024 | 06:59 | None | {'length': 132, 'width': 300, 'height': 103} | 20 |
    | 1 | None |  | 1 | custom size | 9ft Cargo Van | 8954 | repeated | Saturday, Thursday, Sunday | 19:44, 04:39, 04:33 | 16/08/2024 | {'length': 211, 'width': 130, 'height': 298} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 9838 | scheduled | 18/08/2024 | 16:53 | None | {'length': 47, 'width': 37, 'height': 211} | 0 |
    | 1 | Blankets | 5 | 1 | custom size | Pickup Truck | 2312 | scheduled | 17/09/2024 | 09:17 | None | {'length': 17, 'width': 95, 'height': 166} | 0 |
    | 1 | None |  | 1 | custom size | 15ft Box Truck | 6537 | scheduled | 06/08/2024 | 13:10 | None | {'length': 243, 'width': 119, 'height': 105} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Pickup Truck | 2930 | repeated | Monday, Tuesday | 21:00, 13:45 | 16/08/2024 | {'length': 12, 'width': 31, 'height': 61} | 20 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 5828 | urgent | None | None | None | {'length': 233, 'width': 263, 'height': 38} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 9432 | repeated | Tuesday, Saturday, Wednesday | 03:51, 22:57, 16:37 | 18/08/2024 | {'length': 195, 'width': 86, 'height': 148} | 100 |
    | 1 | None |  | 1 | custom size | Car | 2238 | scheduled | 16/08/2024 | 14:32 | None | {'length': 27, 'width': 300, 'height': 50} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 2277 | repeated | Sunday, Saturday, Thursday | 22:53, 21:29, 09:16 | 19/09/2024 | {'length': 59, 'width': 100, 'height': 152} | 50 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 8485 | repeated | Friday | 15:35 | 29/09/2024 | {'length': 221, 'width': 261, 'height': 204} | 100 |
    | 1 | None |  | 1 | custom size | 15ft Box Truck | 9755 | urgent | None | None | None | {'length': 110, 'width': 229, 'height': 164} | 50 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 7020 | scheduled | 29/09/2024 | 03:17 | None | {'length': 38, 'width': 5, 'height': 220} | 50 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 2832 | urgent | None | None | None | {'length': 42, 'width': 19, 'height': 149} | 10 |
    | 1 | None |  | 1 | custom size | 15ft Box Truck | 9793 | urgent | None | None | None | {'length': 25, 'width': 14, 'height': 187} | 20 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 10ft Box Truck | 5247 | repeated | Wednesday, Sunday, Saturday | 03:44, 18:34, 18:02 | 08/08/2024 | {'length': 227, 'width': 88, 'height': 96} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 3805 | scheduled | 17/08/2024 | 21:15 | None | {'length': 4, 'width': 4, 'height': 296} | 100 |
    | 1 | Ladder | 5 | 1 | custom size | Car | 4428 | scheduled | 26/08/2024 | 05:26 | None | {'length': 28, 'width': 112, 'height': 262} | 0 |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 5822 | scheduled | 29/09/2024 | 09:02 | None | {'length': 190, 'width': 85, 'height': 185} | 0 |
    | 1 | None |  | 1 | custom size | Car | 4504 | repeated | Saturday, Tuesday | 13:48, 03:07 | 15/08/2024 | {'length': 112, 'width': 7, 'height': 195} | 20 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 10ft Box Truck | 8501 | scheduled | 31/08/2024 | 03:59 | None | {'length': 185, 'width': 158, 'height': 155} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 2290 | urgent | None | None | None | {'length': 80, 'width': 240, 'height': 98} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 4513 | scheduled | 23/08/2024 | 20:56 | None | {'length': 280, 'width': 118, 'height': 263} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 6036 | scheduled | 08/08/2024 | 20:53 | None | {'length': 39, 'width': 114, 'height': 128} | 50 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 2561 | scheduled | 04/09/2024 | 23:31 | None | {'length': 241, 'width': 163, 'height': 22} | 10 |
    | 1 | None |  | 1 | custom size | Car | 6304 | urgent | None | None | None | {'length': 138, 'width': 228, 'height': 41} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 4714 | scheduled | 08/08/2024 | 07:47 | None | {'length': 163, 'width': 65, 'height': 179} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 8153 | repeated | Thursday | 19:51 | 30/08/2024 | {'length': 250, 'width': 214, 'height': 39} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 7671 | repeated | Monday | 21:59 | 25/08/2024 | {'length': 31, 'width': 200, 'height': 54} | 100 |
    | 1 | None |  | 1 | custom size | 10ft Box Truck | 8797 | scheduled | 17/09/2024 | 01:26 | None | {'length': 31, 'width': 98, 'height': 48} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 4961 | scheduled | 04/09/2024 | 00:32 | None | {'length': 93, 'width': 297, 'height': 86} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 9207 | repeated | Friday | 23:46 | 18/08/2024 | {'length': 290, 'width': 190, 'height': 199} | 50 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 6435 | scheduled | 28/08/2024 | 08:50 | None | {'length': 222, 'width': 67, 'height': 20} | 100 |
    | 1 | None |  | 1 | custom size | Car | 1082 | scheduled | 22/08/2024 | 00:11 | None | {'length': 32, 'width': 47, 'height': 284} | 10 |
    | 1 | None |  | 1 | custom size | Car | 3461 | repeated | Monday, Friday, Saturday | 20:32, 02:05, 13:32 | 29/09/2024 | {'length': 155, 'width': 298, 'height': 271} | 0 |
    | 1 | None |  | 1 | custom size | 10ft Box Truck | 2568 | urgent | None | None | None | {'length': 28, 'width': 29, 'height': 239} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 7168 | repeated | Sunday | 03:36 | 15/09/2024 | {'length': 215, 'width': 53, 'height': 109} | 0 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 10ft Box Truck | 9142 | scheduled | 29/09/2024 | 13:13 | None | {'length': 116, 'width': 11, 'height': 158} | 100 |
    | 1 | Ladder | 5 | 1 | custom size | 10ft Box Truck | 117 | repeated | Saturday, Monday, Wednesday | 21:18, 10:15, 15:56 | 15/09/2024 | {'length': 140, 'width': 50, 'height': 248} | 50 |
    | 1 | None |  | 1 | custom size | 9ft Ref Van | 9605 | repeated | Saturday | 10:50 | 29/08/2024 | {'length': 160, 'width': 290, 'height': 93} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | SUV | 3536 | urgent | None | None | None | {'length': 45, 'width': 46, 'height': 66} | 50 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 10ft Box Truck | 3672 | urgent | None | None | None | {'length': 58, 'width': 282, 'height': 176} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 10ft Box Truck | 8430 | urgent | None | None | None | {'length': 285, 'width': 115, 'height': 86} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | Pickup Truck | 2307 | repeated | Tuesday, Monday | 07:04, 00:42 | 30/08/2024 | {'length': 233, 'width': 300, 'height': 68} | 0 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 6213 | urgent | None | None | None | {'length': 8, 'width': 204, 'height': 44} | 50 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 5727 | repeated | Friday, Saturday | 07:51, 11:59 | 15/09/2024 | {'length': 168, 'width': 38, 'height': 278} | 0 |
    | 1 | Blankets | 5 | 1 | custom size | Car | 1253 | urgent | None | None | None | {'length': 33, 'width': 44, 'height': 210} | 0 |
    | 1 | Ladder | 5 | 1 | custom size | SUV | 2862 | scheduled | 23/08/2024 | 14:04 | None | {'length': 130, 'width': 84, 'height': 228} | 0 |
    | 1 | Blankets | 5 | 1 | custom size | SUV | 9444 | urgent | None | None | None | {'length': 134, 'width': 120, 'height': 13} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Cargo Van | 8336 | urgent | None | None | None | {'length': 262, 'width': 294, 'height': 178} | 20 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 9552 | scheduled | 05/09/2024 | 16:12 | None | {'length': 175, 'width': 213, 'height': 259} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 1713 | urgent | None | None | None | {'length': 259, 'width': 242, 'height': 185} | 10 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Ref Van | 3564 | scheduled | 09/08/2024 | 01:39 | None | {'length': 28, 'width': 148, 'height': 103} | 10 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 1161 | urgent | None | None | None | {'length': 91, 'width': 147, 'height': 184} | 10 |
    | 1 | Ladder | 5 | 1 | custom size | SUV | 477 | scheduled | 26/07/2024 | 00:18 | None | {'length': 138, 'width': 73, 'height': 273} | 100 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | Car | 6865 | urgent | None | None | None | {'length': 82, 'width': 261, 'height': 140} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 4835 | repeated | Tuesday | 05:17 | 07/08/2024 | {'length': 287, 'width': 268, 'height': 240} | 10 |
    | 1 | None |  | 1 | custom size | Car | 1842 | scheduled | 25/07/2024 | 00:30 | None | {'length': 21, 'width': 39, 'height': 281} | 50 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 1341 | urgent | None | None | None | {'length': 176, 'width': 150, 'height': 95} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 8962 | repeated | Friday, Saturday, Monday | 06:16, 15:18, 22:58 | 18/08/2024 | {'length': 64, 'width': 178, 'height': 243} | 100 |
    | 1 | None |  | 1 | custom size | 9ft Cargo Van | 1653 | scheduled | 19/09/2024 | 13:44 | None | {'length': 257, 'width': 131, 'height': 120} | 50 |
    | 1 | Ladder | 5 | 1 | custom size | Pickup Truck | 6295 | urgent | None | None | None | {'length': 184, 'width': 276, 'height': 8} | 10 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Ref Van | 6685 | urgent | None | None | None | {'length': 107, 'width': 183, 'height': 2} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | 15ft Box Truck | 8631 | repeated | Thursday, Monday, Saturday | 18:27, 08:50, 01:47 | 15/09/2024 | {'length': 15, 'width': 225, 'height': 102} | 20 |
    | 1 | Blankets | 5 | 1 | custom size | Car | 4713 | scheduled | 09/09/2024 | 13:06 | None | {'length': 91, 'width': 112, 'height': 104} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 10ft Box Truck | 8566 | repeated | Saturday, Friday, Thursday | 12:12, 21:55, 22:09 | 15/08/2024 | {'length': 277, 'width': 193, 'height': 199} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 482 | urgent | None | None | None | {'length': 237, 'width': 57, 'height': 162} | 50 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Ref Van | 8553 | scheduled | 31/08/2024 | 05:26 | None | {'length': 96, 'width': 236, 'height': 60} | 20 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 712 | urgent | None | None | None | {'length': 51, 'width': 29, 'height': 8} | 0 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 8436 | scheduled | 12/09/2024 | 00:55 | None | {'length': 211, 'width': 146, 'height': 253} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 1689 | scheduled | 24/08/2024 | 20:10 | None | {'length': 250, 'width': 158, 'height': 180} | 0 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 15ft Box Truck | 3298 | urgent | None | None | None | {'length': 43, 'width': 161, 'height': 21} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 8213 | scheduled | 27/09/2024 | 22:52 | None | {'length': 32, 'width': 175, 'height': 109} | 0 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 5852 | scheduled | 04/09/2024 | 16:02 | None | {'length': 207, 'width': 201, 'height': 113} | 0 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | Pickup Truck | 6889 | urgent | None | None | None | {'length': 89, 'width': 193, 'height': 135} | 50 |
    | 1 | None |  | 1 | custom size | Car | 9688 | urgent | None | None | None | {'length': 227, 'width': 81, 'height': 197} | 100 |
    | 1 | None |  | 1 | custom size | 15ft Box Truck | 9897 | urgent | None | None | None | {'length': 88, 'width': 10, 'height': 257} | 100 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 5124 | repeated | Friday | 17:06 | 28/07/2024 | {'length': 178, 'width': 80, 'height': 200} | 0 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Ref Van | 1477 | repeated | Tuesday | 20:21 | 30/08/2024 | {'length': 173, 'width': 10, 'height': 200} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | 15ft Box Truck | 454 | repeated | Friday, Saturday, Wednesday | 15:21, 11:03, 09:11 | 15/09/2024 | {'length': 139, 'width': 200, 'height': 55} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 179 | urgent | None | None | None | {'length': 83, 'width': 210, 'height': 279} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 4003 | urgent | None | None | None | {'length': 243, 'width': 158, 'height': 91} | 0 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 10ft Box Truck | 3756 | scheduled | 11/09/2024 | 21:40 | None | {'length': 199, 'width': 133, 'height': 190} | 10 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 10ft Box Truck | 7998 | urgent | None | None | None | {'length': 284, 'width': 70, 'height': 141} | 20 |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 1759 | repeated | Saturday | 08:01 | 05/09/2024 | {'length': 130, 'width': 101, 'height': 239} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 387 | urgent | None | None | None | {'length': 115, 'width': 180, 'height': 300} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Cargo Van | 8694 | scheduled | 14/09/2024 | 07:40 | None | {'length': 42, 'width': 65, 'height': 136} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 5541 | repeated | Wednesday | 07:27 | 08/08/2024 | {'length': 267, 'width': 228, 'height': 287} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Cargo Van | 7196 | repeated | Monday, Thursday | 09:59, 06:28 | 17/09/2024 | {'length': 37, 'width': 162, 'height': 79} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | Pickup Truck | 5812 | urgent | None | None | None | {'length': 249, 'width': 213, 'height': 29} | 50 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Ref Van | 9888 | scheduled | 17/09/2024 | 00:25 | None | {'length': 214, 'width': 103, 'height': 241} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Ref Van | 7918 | scheduled | 18/08/2024 | 00:57 | None | {'length': 96, 'width': 254, 'height': 87} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Cargo Van | 1008 | scheduled | 21/08/2024 | 18:30 | None | {'length': 142, 'width': 25, 'height': 182} | 20 |
    | 1 | None |  | 1 | custom size | 9ft Cargo Van | 7785 | urgent | None | None | None | {'length': 288, 'width': 145, 'height': 136} | 10 |
    | 1 | Ladder | 5 | 1 | custom size | SUV | 4109 | repeated | Thursday, Monday | 05:12, 16:30 | 18/09/2024 | {'length': 254, 'width': 300, 'height': 197} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Cargo Van | 3035 | scheduled | 22/09/2024 | 12:39 | None | {'length': 189, 'width': 63, 'height': 217} | 10 |
    | 1 | None |  | 1 | custom size | 9ft Ref Van | 4645 | scheduled | 21/07/2024 | 17:20 | None | {'length': 77, 'width': 211, 'height': 185} | 0 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Ref Van | 6485 | urgent | None | None | None | {'length': 62, 'width': 274, 'height': 130} | 10 |
    | 1 | None |  | 1 | custom size | 15ft Box Truck | 5506 | repeated | Thursday, Monday, Wednesday | 16:23, 18:20, 17:53 | 20/09/2024 | {'length': 111, 'width': 197, 'height': 35} | 10 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | SUV | 5757 | scheduled | 08/09/2024 | 15:50 | None | {'length': 146, 'width': 168, 'height': 174} | 50 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 9228 | scheduled | 19/09/2024 | 14:10 | None | {'length': 214, 'width': 134, 'height': 14} | 50 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Cargo Van | 1087 | urgent | None | None | None | {'length': 18, 'width': 137, 'height': 238} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Ref Van | 9346 | scheduled | 18/09/2024 | 23:04 | None | {'length': 290, 'width': 280, 'height': 242} | 0 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Pickup Truck | 9646 | scheduled | 08/08/2024 | 06:35 | None | {'length': 17, 'width': 10, 'height': 98} | 20 |
    | 1 | Blankets | 5 | 1 | custom size | Car | 8626 | repeated | Thursday, Friday | 23:40, 00:24 | 26/09/2024 | {'length': 273, 'width': 169, 'height': 193} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 9007 | urgent | None | None | None | {'length': 31, 'width': 251, 'height': 193} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Cargo Van | 8593 | urgent | None | None | None | {'length': 264, 'width': 127, 'height': 229} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | Pickup Truck | 1801 | repeated | Tuesday, Wednesday, Saturday | 18:55, 15:37, 20:51 | 28/08/2024 | {'length': 298, 'width': 173, 'height': 4} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 9801 | urgent | None | None | None | {'length': 294, 'width': 88, 'height': 181} | 100 |
    | 1 | None |  | 1 | custom size | 9ft Ref Van | 2069 | urgent | None | None | None | {'length': 207, 'width': 219, 'height': 205} | 20 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 10ft Box Truck | 3665 | urgent | None | None | None | {'length': 175, 'width': 221, 'height': 90} | 0 |
    | 1 | None |  | 1 | custom size | Car | 933 | scheduled | 18/08/2024 | 09:37 | None | {'length': 102, 'width': 252, 'height': 77} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 4395 | repeated | Saturday | 07:54 | 27/09/2024 | {'length': 196, 'width': 31, 'height': 291} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 3724 | urgent | None | None | None | {'length': 152, 'width': 229, 'height': 26} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 9639 | repeated | Monday, Tuesday | 12:35, 12:17 | 18/08/2024 | {'length': 57, 'width': 184, 'height': 172} | 0 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 9916 | urgent | None | None | None | {'length': 57, 'width': 300, 'height': 240} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Cargo Van | 5188 | urgent | None | None | None | {'length': 131, 'width': 66, 'height': 223} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | Car | 740 | scheduled | 16/08/2024 | 10:40 | None | {'length': 67, 'width': 268, 'height': 79} | 100 |
    | 1 | Ladder | 5 | 1 | custom size | Pickup Truck | 7777 | repeated | Thursday, Saturday | 04:28, 19:42 | 08/09/2024 | {'length': 59, 'width': 125, 'height': 257} | 50 |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 7303 | scheduled | 06/08/2024 | 07:24 | None | {'length': 74, 'width': 292, 'height': 52} | 20 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 6525 | urgent | None | None | None | {'length': 129, 'width': 76, 'height': 13} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Cargo Van | 3885 | repeated | Thursday, Friday, Saturday | 08:53, 01:02, 14:10 | 02/09/2024 | {'length': 61, 'width': 40, 'height': 9} | 0 |
    | 1 | None |  | 1 | custom size | Car | 4878 | scheduled | 26/07/2024 | 18:55 | None | {'length': 34, 'width': 67, 'height': 26} | 20 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 4309 | urgent | None | None | None | {'length': 28, 'width': 147, 'height': 123} | 10 |
    | 1 | Ladder | 5 | 1 | custom size | 10ft Box Truck | 4867 | scheduled | 20/09/2024 | 07:07 | None | {'length': 40, 'width': 235, 'height': 240} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Ref Van | 9408 | repeated | Monday, Friday, Wednesday | 00:30, 08:35, 06:26 | 26/07/2024 | {'length': 162, 'width': 66, 'height': 198} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | SUV | 1990 | repeated | Thursday | 01:29 | 08/08/2024 | {'length': 241, 'width': 283, 'height': 9} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 6940 | scheduled | 26/08/2024 | 22:51 | None | {'length': 120, 'width': 128, 'height': 274} | 20 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Cargo Van | 5698 | urgent | None | None | None | {'length': 299, 'width': 291, 'height': 232} | 10 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 6838 | scheduled | 15/08/2024 | 07:33 | None | {'length': 42, 'width': 158, 'height': 234} | 100 |
    | 1 | None |  | 1 | custom size | 9ft Ref Van | 8540 | scheduled | 21/07/2024 | 04:14 | None | {'length': 274, 'width': 277, 'height': 35} | 20 |
    | 1 | None |  | 1 | custom size | 9ft Ref Van | 5312 | urgent | None | None | None | {'length': 257, 'width': 83, 'height': 47} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 4370 | repeated | Monday | 15:05 | 23/07/2024 | {'length': 282, 'width': 101, 'height': 207} | 20 |
    | 1 | None |  | 1 | custom size | 9ft Ref Van | 9638 | repeated | Sunday, Friday | 01:28, 18:31 | 02/08/2024 | {'length': 27, 'width': 279, 'height': 32} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | Pickup Truck | 3201 | scheduled | 08/08/2024 | 20:15 | None | {'length': 104, 'width': 262, 'height': 58} | 50 |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 4985 | repeated | Sunday, Saturday, Tuesday | 10:03, 18:40, 20:08 | 28/08/2024 | {'length': 258, 'width': 58, 'height': 299} | 100 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 10ft Box Truck | 1136 | urgent | None | None | None | {'length': 140, 'width': 100, 'height': 16} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | 10ft Box Truck | 573 | repeated | Wednesday, Saturday, Monday | 09:28, 13:52, 11:02 | 16/08/2024 | {'length': 251, 'width': 195, 'height': 79} | 10 |
    | 1 | Ladder | 5 | 1 | custom size | 15ft Box Truck | 5695 | urgent | None | None | None | {'length': 137, 'width': 243, 'height': 80} | 50 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Cargo Van | 3058 | urgent | None | None | None | {'length': 187, 'width': 292, 'height': 123} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 1471 | urgent | None | None | None | {'length': 94, 'width': 225, 'height': 76} | 0 |
    | 1 | None |  | 1 | custom size | 9ft Ref Van | 9233 | urgent | None | None | None | {'length': 156, 'width': 226, 'height': 35} | 0 |
    | 1 | Blankets | 5 | 1 | custom size | SUV | 2261 | repeated | Tuesday, Sunday, Saturday | 21:56, 13:01, 09:50 | 09/08/2024 | {'length': 149, 'width': 32, 'height': 126} | 20 |
    | 1 | None |  | 1 | custom size | Car | 7224 | scheduled | 29/09/2024 | 13:03 | None | {'length': 173, 'width': 216, 'height': 298} | 0 |
    | 1 | None |  | 1 | custom size | 15ft Box Truck | 5470 | repeated | Thursday | 00:02 | 17/08/2024 | {'length': 243, 'width': 118, 'height': 244} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 640 | scheduled | 07/08/2024 | 13:39 | None | {'length': 217, 'width': 40, 'height': 257} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 7026 | scheduled | 02/08/2024 | 05:03 | None | {'length': 194, 'width': 156, 'height': 23} | 100 |
    | 1 | None |  | 1 | custom size | Car | 4964 | repeated | Thursday, Sunday, Tuesday | 23:52, 03:34, 21:05 | 24/09/2024 | {'length': 50, 'width': 143, 'height': 107} | 50 |
    | 1 | None |  | 1 | custom size | 9ft Ref Van | 6459 | repeated | Wednesday, Friday, Thursday | 06:32, 16:26, 22:01 | 17/08/2024 | {'length': 21, 'width': 79, 'height': 156} | 0 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 9752 | scheduled | 16/08/2024 | 21:03 | None | {'length': 216, 'width': 15, 'height': 185} | 100 |
    | 1 | None |  | 1 | custom size | Car | 5410 | urgent | None | None | None | {'length': 192, 'width': 187, 'height': 235} | 0 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Ref Van | 282 | scheduled | 18/08/2024 | 10:14 | None | {'length': 251, 'width': 281, 'height': 162} | 100 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Cargo Van | 2849 | repeated | Monday | 20:36 | 05/09/2024 | {'length': 163, 'width': 50, 'height': 279} | 10 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 223 | repeated | Sunday | 19:37 | 21/07/2024 | {'length': 226, 'width': 288, 'height': 242} | 10 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 2591 | urgent | None | None | None | {'length': 103, 'width': 87, 'height': 278} | 100 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Ref Van | 6633 | urgent | None | None | None | {'length': 197, 'width': 169, 'height': 292} | 20 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 3074 | urgent | None | None | None | {'length': 137, 'width': 175, 'height': 165} | 50 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Ref Van | 2106 | scheduled | 04/09/2024 | 20:26 | None | {'length': 252, 'width': 146, 'height': 243} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 2523 | urgent | None | None | None | {'length': 269, 'width': 282, 'height': 262} | 20 |
    | 1 | None |  | 1 | custom size | 9ft Ref Van | 6767 | repeated | Saturday, Sunday, Tuesday | 11:46, 14:47, 14:14 | 28/08/2024 | {'length': 138, 'width': 187, 'height': 33} | 10 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | Car | 6143 | urgent | None | None | None | {'length': 75, 'width': 19, 'height': 52} | 50 |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 6694 | urgent | None | None | None | {'length': 147, 'width': 34, 'height': 265} | 0 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 5424 | urgent | None | None | None | {'length': 97, 'width': 14, 'height': 248} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 3607 | repeated | Tuesday, Friday, Sunday | 17:23, 11:03, 07:19 | 25/07/2024 | {'length': 229, 'width': 76, 'height': 186} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 2550 | scheduled | 05/09/2024 | 23:12 | None | {'length': 1, 'width': 135, 'height': 149} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Pickup Truck | 4100 | urgent | None | None | None | {'length': 214, 'width': 261, 'height': 74} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | SUV | 1037 | repeated | Monday, Wednesday | 03:54, 01:30 | 31/07/2024 | {'length': 62, 'width': 149, 'height': 136} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 7671 | repeated | Tuesday, Sunday | 20:17, 00:45 | 08/08/2024 | {'length': 111, 'width': 201, 'height': 276} | 50 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | SUV | 4911 | scheduled | 18/07/2024 | 14:04 | None | {'length': 280, 'width': 259, 'height': 198} | 0 |
    | 1 | Ladder | 5 | 1 | custom size | 10ft Box Truck | 740 | scheduled | 24/08/2024 | 05:52 | None | {'length': 235, 'width': 23, 'height': 195} | 100 |
    | 1 | None |  | 1 | custom size | 9ft Ref Van | 2870 | scheduled | 22/08/2024 | 03:12 | None | {'length': 13, 'width': 10, 'height': 13} | 50 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | Car | 4715 | repeated | Thursday | 21:18 | 04/09/2024 | {'length': 296, 'width': 22, 'height': 223} | 10 |
    | 1 | Ladder | 5 | 1 | custom size | 15ft Box Truck | 4825 | scheduled | 18/08/2024 | 16:14 | None | {'length': 258, 'width': 266, 'height': 95} | 50 |
    | 1 | Ladder | 5 | 1 | custom size | 10ft Box Truck | 5141 | repeated | Tuesday, Thursday, Monday | 17:19, 00:12, 11:03 | 11/08/2024 | {'length': 205, 'width': 258, 'height': 121} | 10 |
    | 1 | None |  | 1 | custom size | 15ft Box Truck | 3103 | repeated | Wednesday, Thursday | 07:54, 11:24 | 19/09/2024 | {'length': 98, 'width': 34, 'height': 60} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | SUV | 748 | urgent | None | None | None | {'length': 74, 'width': 89, 'height': 17} | 100 |
    | 1 | Ladder | 5 | 1 | custom size | 10ft Box Truck | 8011 | scheduled | 16/07/2024 | 15:18 | None | {'length': 97, 'width': 102, 'height': 228} | 0 |
    | 1 | Ladder | 5 | 1 | custom size | 15ft Box Truck | 5064 | repeated | Sunday, Monday | 06:22, 01:46 | 24/09/2024 | {'length': 48, 'width': 157, 'height': 80} | 20 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Ref Van | 2470 | scheduled | 17/09/2024 | 23:09 | None | {'length': 7, 'width': 132, 'height': 182} | 10 |
    | 1 | Ladder | 5 | 1 | custom size | Car | 2469 | repeated | Monday, Friday | 17:32, 17:13 | 26/07/2024 | {'length': 84, 'width': 225, 'height': 299} | 10 |
    | 1 | Ladder | 5 | 1 | custom size | Pickup Truck | 2671 | urgent | None | None | None | {'length': 213, 'width': 192, 'height': 181} | 50 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Cargo Van | 3031 | urgent | None | None | None | {'length': 278, 'width': 62, 'height': 171} | 50 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 1992 | scheduled | 29/09/2024 | 15:51 | None | {'length': 21, 'width': 54, 'height': 84} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 6515 | scheduled | 29/09/2024 | 14:56 | None | {'length': 92, 'width': 48, 'height': 285} | 50 |
    | 1 | None |  | 1 | custom size | Car | 4156 | urgent | None | None | None | {'length': 16, 'width': 235, 'height': 40} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Ref Van | 3083 | repeated | Monday, Friday, Tuesday | 07:22, 10:32, 14:33 | 22/09/2024 | {'length': 292, 'width': 238, 'height': 121} | 20 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Pickup Truck | 1561 | scheduled | 15/09/2024 | 03:30 | None | {'length': 160, 'width': 297, 'height': 173} | 0 |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 348 | scheduled | 23/07/2024 | 04:43 | None | {'length': 154, 'width': 227, 'height': 107} | 50 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 290 | urgent | None | None | None | {'length': 249, 'width': 112, 'height': 195} | 50 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 635 | repeated | Thursday, Monday, Friday | 01:20, 18:04, 17:46 | 23/09/2024 | {'length': 229, 'width': 49, 'height': 178} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 6521 | scheduled | 25/07/2024 | 12:11 | None | {'length': 133, 'width': 137, 'height': 273} | 50 |
    | 1 | Ladder | 5 | 1 | custom size | Pickup Truck | 6476 | repeated | Friday | 08:47 | 07/08/2024 | {'length': 224, 'width': 151, 'height': 34} | 100 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Cargo Van | 1540 | scheduled | 26/09/2024 | 13:43 | None | {'length': 87, 'width': 114, 'height': 240} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 321 | repeated | Sunday | 09:01 | 31/07/2024 | {'length': 98, 'width': 97, 'height': 35} | 100 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | SUV | 3658 | urgent | None | None | None | {'length': 64, 'width': 83, 'height': 136} | 10 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 1297 | repeated | Saturday, Friday, Monday | 07:04, 19:40, 18:43 | 23/08/2024 | {'length': 176, 'width': 233, 'height': 248} | 20 |
    | 1 | None |  | 1 | custom size | 10ft Box Truck | 1240 | urgent | None | None | None | {'length': 184, 'width': 146, 'height': 25} | 50 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Ref Van | 5448 | repeated | Thursday, Tuesday | 21:55, 14:20 | 18/08/2024 | {'length': 248, 'width': 71, 'height': 253} | 10 |
    | 1 | None |  | 1 | custom size | 9ft Cargo Van | 8795 | scheduled | 24/08/2024 | 19:33 | None | {'length': 281, 'width': 65, 'height': 193} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Ref Van | 7429 | repeated | Saturday, Monday | 05:32, 02:10 | 21/07/2024 | {'length': 292, 'width': 150, 'height': 33} | 100 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 15ft Box Truck | 9893 | repeated | Thursday, Saturday | 04:51, 02:13 | 23/07/2024 | {'length': 8, 'width': 213, 'height': 144} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | Pickup Truck | 1211 | repeated | Tuesday, Monday | 13:33, 19:47 | 25/07/2024 | {'length': 131, 'width': 197, 'height': 10} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | Pickup Truck | 143 | repeated | Sunday, Monday | 18:54, 15:07 | 30/08/2024 | {'length': 114, 'width': 44, 'height': 137} | 20 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 6221 | urgent | None | None | None | {'length': 133, 'width': 228, 'height': 271} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 9778 | repeated | Monday | 02:19 | 08/08/2024 | {'length': 85, 'width': 73, 'height': 208} | 10 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Cargo Van | 5290 | repeated | Monday | 16:14 | 31/08/2024 | {'length': 61, 'width': 143, 'height': 57} | 100 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Cargo Van | 1196 | repeated | Tuesday, Saturday, Monday | 07:50, 01:35, 18:55 | 30/08/2024 | {'length': 260, 'width': 225, 'height': 26} | 0 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 10ft Box Truck | 7513 | repeated | Saturday | 21:11 | 09/08/2024 | {'length': 8, 'width': 139, 'height': 93} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | Pickup Truck | 3145 | scheduled | 29/08/2024 | 23:25 | None | {'length': 111, 'width': 256, 'height': 62} | 20 |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 3564 | scheduled | 12/08/2024 | 12:46 | None | {'length': 230, 'width': 108, 'height': 250} | 0 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 6786 | repeated | Friday, Saturday | 05:23, 11:12 | 04/09/2024 | {'length': 59, 'width': 34, 'height': 47} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 15ft Box Truck | 2606 | urgent | None | None | None | {'length': 33, 'width': 204, 'height': 189} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | Pickup Truck | 5810 | urgent | None | None | None | {'length': 269, 'width': 66, 'height': 227} | 50 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 2047 | repeated | Thursday, Friday, Tuesday | 03:12, 15:54, 02:55 | 18/08/2024 | {'length': 196, 'width': 257, 'height': 195} | 0 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 9852 | scheduled | 16/08/2024 | 17:12 | None | {'length': 116, 'width': 17, 'height': 298} | 50 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 15ft Box Truck | 6892 | scheduled | 21/08/2024 | 04:35 | None | {'length': 257, 'width': 201, 'height': 138} | 100 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Ref Van | 124 | repeated | Thursday, Monday, Friday | 13:26, 07:09, 04:40 | 22/08/2024 | {'length': 281, 'width': 101, 'height': 62} | 10 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Cargo Van | 1231 | scheduled | 29/09/2024 | 06:45 | None | {'length': 178, 'width': 115, 'height': 299} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | Pickup Truck | 1530 | repeated | Friday | 00:42 | 29/08/2024 | {'length': 100, 'width': 256, 'height': 13} | 20 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 3262 | urgent | None | None | None | {'length': 227, 'width': 264, 'height': 67} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | Car | 858 | urgent | None | None | None | {'length': 72, 'width': 150, 'height': 169} | 20 |
    | 1 | Blankets | 5 | 1 | custom size | SUV | 6846 | repeated | Thursday, Wednesday, Monday | 02:53, 18:14, 04:38 | 21/07/2024 | {'length': 57, 'width': 217, 'height': 116} | 50 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 5554 | scheduled | 31/08/2024 | 23:02 | None | {'length': 295, 'width': 41, 'height': 117} | 50 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 10ft Box Truck | 8376 | repeated | Tuesday | 14:33 | 09/08/2024 | {'length': 245, 'width': 45, 'height': 266} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | SUV | 5744 | scheduled | 15/08/2024 | 17:34 | None | {'length': 24, 'width': 280, 'height': 256} | 0 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Ref Van | 3158 | urgent | None | None | None | {'length': 140, 'width': 254, 'height': 158} | 0 |
    | 1 | None |  | 1 | custom size | 10ft Box Truck | 7715 | repeated | Wednesday | 17:36 | 30/07/2024 | {'length': 129, 'width': 11, 'height': 46} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | Pickup Truck | 1539 | repeated | Thursday | 23:14 | 18/09/2024 | {'length': 21, 'width': 14, 'height': 158} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 2171 | scheduled | 18/08/2024 | 11:09 | None | {'length': 156, 'width': 96, 'height': 85} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Pickup Truck | 5232 | repeated | Monday | 01:19 | 23/07/2024 | {'length': 95, 'width': 49, 'height': 19} | 50 |
    | 1 | None |  | 1 | custom size | SUV | 8011 | repeated | Thursday, Sunday | 07:26, 09:58 | 12/08/2024 | {'length': 220, 'width': 203, 'height': 56} | 100 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 1015 | repeated | Monday, Wednesday | 14:11, 08:18 | 11/08/2024 | {'length': 64, 'width': 192, 'height': 36} | 10 |
    | 1 | Ladder | 5 | 1 | custom size | Car | 5893 | scheduled | 21/08/2024 | 23:44 | None | {'length': 210, 'width': 70, 'height': 33} | 50 |
    | 1 | Ladder | 5 | 1 | custom size | 15ft Box Truck | 5586 | urgent | None | None | None | {'length': 283, 'width': 18, 'height': 190} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 9704 | scheduled | 26/09/2024 | 13:18 | None | {'length': 166, 'width': 233, 'height': 20} | 50 |
    | 1 | None |  | 1 | custom size | 9ft Cargo Van | 8705 | urgent | None | None | None | {'length': 66, 'width': 155, 'height': 284} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | Pickup Truck | 3440 | repeated | Sunday, Saturday, Tuesday | 23:55, 03:14, 08:01 | 30/07/2024 | {'length': 263, 'width': 23, 'height': 37} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | Pickup Truck | 8504 | repeated | Monday, Sunday, Friday | 05:52, 02:08, 15:56 | 18/08/2024 | {'length': 184, 'width': 143, 'height': 218} | 100 |
    | 1 | Ladder | 5 | 1 | custom size | 10ft Box Truck | 8293 | scheduled | 29/08/2024 | 15:48 | None | {'length': 157, 'width': 82, 'height': 3} | 20 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 380 | repeated | Friday | 18:31 | 18/08/2024 | {'length': 12, 'width': 158, 'height': 201} | 10 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | Car | 2894 | urgent | None | None | None | {'length': 264, 'width': 93, 'height': 289} | 100 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 564 | repeated | Wednesday, Saturday, Friday | 05:32, 00:29, 04:11 | 25/07/2024 | {'length': 78, 'width': 254, 'height': 89} | 50 |
    | 1 | Blankets | 5 | 1 | custom size | Car | 6945 | repeated | Wednesday, Monday, Thursday | 10:14, 19:17, 22:05 | 06/09/2024 | {'length': 112, 'width': 224, 'height': 82} | 10 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 154 | urgent | None | None | None | {'length': 132, 'width': 255, 'height': 65} | 100 |
    | 1 | None |  | 1 | custom size | 10ft Box Truck | 1279 | repeated | Tuesday, Sunday, Thursday | 12:20, 10:49, 02:16 | 26/09/2024 | {'length': 150, 'width': 175, 'height': 253} | 50 |
    | 1 | Ladder | 5 | 1 | custom size | SUV | 4859 | scheduled | 11/09/2024 | 07:52 | None | {'length': 237, 'width': 277, 'height': 281} | 50 |
    | 1 | None |  | 1 | custom size | Car | 649 | repeated | Sunday, Thursday, Saturday | 11:50, 17:37, 05:13 | 19/09/2024 | {'length': 48, 'width': 119, 'height': 243} | 0 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 15ft Box Truck | 3595 | repeated | Monday, Sunday, Saturday | 19:08, 10:37, 09:19 | 21/08/2024 | {'length': 105, 'width': 38, 'height': 88} | 100 |
    | 1 | None |  | 1 | custom size | 10ft Box Truck | 9582 | scheduled | 21/08/2024 | 21:48 | None | {'length': 85, 'width': 135, 'height': 33} | 100 |
    | 1 | Ladder | 5 | 1 | custom size | Pickup Truck | 9096 | scheduled | 05/08/2024 | 09:17 | None | {'length': 136, 'width': 86, 'height': 261} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | Car | 6614 | repeated | Sunday, Monday | 18:47, 19:18 | 25/08/2024 | {'length': 186, 'width': 187, 'height': 291} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Cargo Van | 2611 | scheduled | 08/09/2024 | 21:57 | None | {'length': 73, 'width': 212, 'height': 222} | 100 |
    | 1 | None |  | 1 | custom size | 15ft Box Truck | 8997 | urgent | None | None | None | {'length': 75, 'width': 225, 'height': 285} | 0 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 3847 | repeated | Thursday, Monday, Wednesday | 01:16, 18:58, 12:39 | 07/09/2024 | {'length': 166, 'width': 298, 'height': 85} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | 10ft Box Truck | 7070 | scheduled | 24/08/2024 | 02:48 | None | {'length': 33, 'width': 66, 'height': 271} | 100 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 10ft Box Truck | 6917 | scheduled | 02/08/2024 | 12:37 | None | {'length': 258, 'width': 3, 'height': 44} | 10 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 6851 | urgent | None | None | None | {'length': 228, 'width': 50, 'height': 157} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | Pickup Truck | 2466 | scheduled | 29/09/2024 | 13:02 | None | {'length': 255, 'width': 52, 'height': 97} | 0 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 9381 | urgent | None | None | None | {'length': 11, 'width': 118, 'height': 242} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Pickup Truck | 7674 | scheduled | 25/07/2024 | 16:46 | None | {'length': 221, 'width': 203, 'height': 94} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 8597 | repeated | Tuesday, Thursday, Saturday | 16:36, 18:31, 06:11 | 18/08/2024 | {'length': 108, 'width': 272, 'height': 228} | 10 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 6477 | urgent | None | None | None | {'length': 221, 'width': 25, 'height': 136} | 0 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 1160 | repeated | Monday, Friday, Tuesday | 00:48, 10:17, 08:32 | 18/08/2024 | {'length': 174, 'width': 206, 'height': 181} | 0 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 3184 | urgent | None | None | None | {'length': 138, 'width': 22, 'height': 280} | 50 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 2195 | repeated | Sunday, Tuesday | 06:40, 02:08 | 19/09/2024 | {'length': 287, 'width': 196, 'height': 293} | 10 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 8144 | repeated | Friday, Monday | 12:41, 17:50 | 24/08/2024 | {'length': 28, 'width': 236, 'height': 195} | 20 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 3662 | urgent | None | None | None | {'length': 105, 'width': 122, 'height': 123} | 100 |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 10ft Box Truck | 3661 | scheduled | 31/08/2024 | 03:55 | None | {'length': 53, 'width': 189, 'height': 225} | 20 |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Ref Van | 488 | scheduled | 29/08/2024 | 16:49 | None | {'length': 173, 'width': 146, 'height': 128} | 20 |
    | 1 | None |  | 1 | custom size | Pickup Truck | 7802 | scheduled | 05/09/2024 | 23:36 | None | {'length': 67, 'width': 251, 'height': 30} | 20 |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Ref Van | 8681 | urgent | None | None | None | {'length': 211, 'width': 273, 'height': 106} | 100 |
    | 1 | Blankets | 5 | 1 | custom size | Car | 1764 | urgent | None | None | None | {'length': 275, 'width': 211, 'height': 43} | 0 |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 5387 | scheduled | 12/09/2024 | 10:01 | None | {'length': 168, 'width': 242, 'height': 4} | 0 |
    | 1 | None |  | 1 | custom size | 10ft Box Truck | 3417 | scheduled | 08/09/2024 | 09:20 | None | {'length': 63, 'width': 231, 'height': 144} | 50 |