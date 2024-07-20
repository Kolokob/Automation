Feature: Delivery Test Cases

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
    And tips are <tips>
    And signature is <signature>

  Examples:
    | pick_up_address_amount | extra_service | extra_service_details | drop_off_address_amount | parcel_size | vehicle_type | declared_value | pick_up_time | days_or_date | time | start_date | tips | signature |
    | 1 | White gloves service | 60 minutes | 1 | medium | None | 1310 | scheduled | 13/08/2024 | 05:39 | None | 100 | True |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Cargo Van | 8367 | urgent | None | None | None | 10 | True |
    | 1 | Ladder | 5 | 1 | heavy_load | 10ft Box Truck | 9551 | repeated | Sunday, Wednesday, Thursday | 02:06, 12:06, 10:04 | 25/08/2024 | 10 | True |
    | 1 | Blankets | 5 | 1 | large | Car | 9573 | scheduled | 25/08/2024 | 18:36 | None | 0 | False |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 6873 | urgent | None | None | None | 10 | False |
    | 1 | Blankets | 5 | 1 | custom size | SUV | 9941 | scheduled | 25/08/2024 | 18:50 | None | 10 | False |
    | 1 | Blankets | 5 | 1 | medium | None | 6912 | repeated | Saturday, Friday, Sunday | 03:56, 05:55, 23:27 | 04/09/2024 | 10 | False |
    | 1 | White gloves service | 60 minutes | 1 | heavy_load | 9ft Ref Van | 1101 | repeated | Sunday, Thursday | 00:53, 11:43 | 04/09/2024 | 50 | False |
    | 1 | Ladder | 5 | 1 | custom size | 10ft Box Truck | 2943 | repeated | Wednesday, Tuesday | 19:09, 07:49 | 17/08/2024 | 10 | True |
    | 1 | White gloves service | 60 minutes | 1 | medium | None | 7820 | scheduled | 19/09/2024 | 16:58 | None | 100 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | heavy_load | 10ft Box Truck | 4646 | urgent | None | None | None | 100 | False |
    | 1 | None |  | 1 | small | None | 1525 | repeated | Tuesday | 12:37 | 28/07/2024 | 50 | True |
    | 1 | Ladder | 5 | 1 | large | Car | 3585 | repeated | Tuesday | 02:46 | 16/08/2024 | 20 | True |
    | 1 | Ladder | 5 | 1 | medium | None | 3510 | repeated | Sunday, Saturday | 12:34, 12:34 | 23/07/2024 | 20 | True |
    | 1 | None |  | 1 | heavy_load | Pickup Truck | 6470 | repeated | Wednesday, Monday, Sunday | 02:18, 16:03, 16:50 | 24/07/2024 | 10 | True |
    | 1 | White gloves service | 60 minutes | 1 | large | Car | 5587 | repeated | Tuesday, Thursday | 20:41, 16:12 | 11/09/2024 | 0 | False |
    | 1 | None |  | 1 | small | None | 9743 | repeated | Sunday, Saturday, Monday | 19:44, 10:21, 18:15 | 08/09/2024 | 50 | False |
    | 1 | Ladder | 5 | 1 | medium | None | 250 | scheduled | 29/09/2024 | 21:31 | None | 50 | False |
    | 1 | Ladder | 5 | 1 | large | SUV | 348 | repeated | Sunday, Monday, Friday | 06:54, 22:32, 02:21 | 10/09/2024 | 50 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | small | None | 3417 | urgent | None | None | None | 20 | False |
    | 1 | Ladder | 5 | 1 | custom size | 15ft Box Truck | 9813 | scheduled | 25/08/2024 | 14:12 | None | 0 | True |
    | 1 | Blankets | 5 | 1 | custom size | Car | 7133 | scheduled | 15/09/2024 | 10:29 | None | 0 | True |
    | 1 | None |  | 1 | medium | None | 2823 | scheduled | 06/08/2024 | 13:51 | None | 10 | True |
    | 1 | None |  | 1 | medium | None | 7749 | urgent | None | None | None | 0 | False |
    | 1 | Blankets | 5 | 1 | medium | None | 1029 | repeated | Wednesday | 10:29 | 22/08/2024 | 0 | True |
    | 1 | Blankets | 5 | 1 | custom size | Car | 3956 | scheduled | 27/07/2024 | 11:50 | None | 100 | True |
    | 1 | White gloves service | 60 minutes | 1 | heavy_load | 9ft Ref Van | 4151 | urgent | None | None | None | 50 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | SUV | 219 | urgent | None | None | None | 0 | True |
    | 1 | White gloves service | 60 minutes | 1 | large | Pickup Truck | 1724 | repeated | Sunday, Monday | 20:05, 01:48 | 12/08/2024 | 0 | True |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Pickup Truck | 593 | urgent | None | None | None | 10 | True |
    | 1 | None |  | 1 | large | SUV | 8640 | urgent | None | None | None | 100 | False |
    | 1 | None |  | 1 | custom size | 15ft Box Truck | 7627 | urgent | None | None | None | 10 | False |
    | 1 | None |  | 1 | heavy_load | 9ft Cargo Van | 1177 | urgent | None | None | None | 50 | False |
    | 1 | None |  | 1 | heavy_load | 9ft Ref Van | 1892 | urgent | None | None | None | 50 | True |
    | 1 | Blankets | 5 | 1 | custom size | Car | 4497 | scheduled | 26/07/2024 | 19:24 | None | 100 | True |
    | 1 | Blankets | 5 | 1 | large | Car | 5264 | repeated | Saturday, Monday | 06:42, 18:21 | 26/08/2024 | 100 | False |
    | 1 | None |  | 1 | custom size | Car | 1650 | repeated | Monday, Sunday | 16:03, 23:34 | 18/09/2024 | 0 | True |
    | 1 | Ladder | 5 | 1 | medium | None | 7019 | scheduled | 11/08/2024 | 06:57 | None | 10 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | heavy_load | 10ft Box Truck | 663 | repeated | Sunday | 17:39 | 21/07/2024 | 100 | True |
    | 1 | None |  | 1 | large | SUV | 6182 | scheduled | 05/09/2024 | 01:05 | None | 50 | True |
    | 1 | Blankets | 5 | 1 | small | None | 2473 | repeated | Thursday | 13:25 | 26/07/2024 | 0 | False |
    | 1 | None |  | 1 | large | Pickup Truck | 7696 | urgent | None | None | None | 50 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 9710 | urgent | None | None | None | 50 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | heavy_load | 10ft Box Truck | 3636 | repeated | Thursday | 20:18 | 25/08/2024 | 100 | False |
    | 1 | None |  | 1 | small | None | 7585 | scheduled | 31/07/2024 | 05:38 | None | 20 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | large | SUV | 5445 | scheduled | 21/07/2024 | 18:37 | None | 100 | True |
    | 1 | None |  | 1 | large | Pickup Truck | 524 | urgent | None | None | None | 0 | True |
    | 1 | Ladder | 5 | 1 | medium | None | 2728 | scheduled | 21/07/2024 | 19:21 | None | 20 | False |
    | 1 | Blankets | 5 | 1 | large | Car | 8343 | urgent | None | None | None | 20 | True |
    | 1 | Blankets | 5 | 1 | custom size | SUV | 4100 | scheduled | 17/08/2024 | 06:45 | None | 50 | False |
    | 1 | White gloves service | 60 minutes | 1 | heavy_load | 9ft Ref Van | 4673 | repeated | Saturday, Thursday, Tuesday | 12:17, 05:30, 13:32 | 08/09/2024 | 20 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | Pickup Truck | 5256 | repeated | Sunday | 02:38 | 19/09/2024 | 50 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | small | None | 3051 | repeated | Friday | 09:25 | 27/07/2024 | 10 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | large | Pickup Truck | 2600 | urgent | None | None | None | 20 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 1350 | scheduled | 25/08/2024 | 00:36 | None | 0 | False |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 4912 | urgent | None | None | None | 50 | True |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 4351 | repeated | Thursday, Saturday, Sunday | 13:58, 17:32, 18:52 | 08/08/2024 | 50 | True |
    | 1 | Ladder | 5 | 1 | heavy_load | 10ft Box Truck | 7030 | urgent | None | None | None | 0 | True |
    | 1 | Ladder | 5 | 1 | small | None | 3191 | repeated | Sunday | 22:35 | 17/09/2024 | 100 | True |
    | 1 | None |  | 1 | small | None | 3561 | urgent | None | None | None | 100 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | small | None | 9610 | urgent | None | None | None | 50 | True |
    | 1 | Blankets | 5 | 1 | small | None | 821 | scheduled | 11/08/2024 | 01:30 | None | 100 | False |
    | 1 | None |  | 1 | custom size | Pickup Truck | 2720 | repeated | Wednesday, Thursday, Tuesday | 17:10, 19:23, 04:40 | 09/08/2024 | 0 | True |
    | 1 | None |  | 1 | small | None | 161 | repeated | Wednesday, Tuesday | 04:14, 18:47 | 21/09/2024 | 50 | True |
    | 1 | None |  | 1 | large | SUV | 3658 | urgent | None | None | None | 100 | False |
    | 1 | Blankets | 5 | 1 | large | Pickup Truck | 1221 | scheduled | 18/09/2024 | 14:56 | None | 100 | False |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 6673 | repeated | Tuesday, Wednesday, Thursday | 14:22, 15:05, 23:29 | 06/09/2024 | 0 | False |
    | 1 | None |  | 1 | large | SUV | 5123 | urgent | None | None | None | 0 | True |
    | 1 | None |  | 1 | heavy_load | 15ft Box Truck | 384 | urgent | None | None | None | 0 | True |
    | 1 | Ladder | 5 | 1 | heavy_load | 9ft Cargo Van | 7588 | urgent | None | None | None | 100 | False |
    | 1 | White gloves service | 60 minutes | 1 | small | None | 5483 | repeated | Tuesday, Monday, Saturday | 09:09, 06:28, 20:28 | 28/09/2024 | 100 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | SUV | 2220 | scheduled | 17/08/2024 | 19:50 | None | 0 | False |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Pickup Truck | 4279 | urgent | None | None | None | 20 | True |
    | 1 | Blankets | 5 | 1 | custom size | 10ft Box Truck | 5897 | scheduled | 16/08/2024 | 13:19 | None | 10 | False |
    | 1 | None |  | 1 | heavy_load | 15ft Box Truck | 7413 | scheduled | 18/09/2024 | 09:20 | None | 10 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 5340 | scheduled | 04/09/2024 | 22:46 | None | 50 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | SUV | 1256 | repeated | Monday | 16:28 | 16/09/2024 | 10 | False |
    | 1 | White gloves service | 60 minutes | 1 | small | None | 3446 | scheduled | 27/09/2024 | 12:34 | None | 20 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | small | None | 1411 | repeated | Saturday, Tuesday, Wednesday | 00:18, 02:05, 17:46 | 17/08/2024 | 0 | False |
    | 1 | Ladder | 5 | 1 | heavy_load | 10ft Box Truck | 2515 | urgent | None | None | None | 50 | False |
    | 1 | Blankets | 5 | 1 | medium | None | 2147 | scheduled | 26/08/2024 | 18:28 | None | 10 | False |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Cargo Van | 5196 | urgent | None | None | None | 0 | True |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 10ft Box Truck | 1932 | repeated | Sunday | 04:31 | 25/08/2024 | 0 | True |
    | 1 | Blankets | 5 | 1 | medium | None | 1536 | repeated | Tuesday, Wednesday, Thursday | 04:01, 17:38, 09:14 | 08/08/2024 | 10 | False |
    | 1 | None |  | 1 | medium | None | 4667 | repeated | Thursday | 00:19 | 21/09/2024 | 10 | False |
    | 1 | Blankets | 5 | 1 | heavy_load | 9ft Ref Van | 4672 | urgent | None | None | None | 100 | False |
    | 1 | Ladder | 5 | 1 | custom size | 10ft Box Truck | 9972 | urgent | None | None | None | 50 | True |
    | 1 | White gloves service | 60 minutes | 1 | heavy_load | Pickup Truck | 2371 | scheduled | 13/09/2024 | 16:36 | None | 100 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 15ft Box Truck | 5464 | repeated | Friday | 09:15 | 09/09/2024 | 10 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Ref Van | 6474 | scheduled | 20/08/2024 | 18:34 | None | 0 | False |
    | 1 | Blankets | 5 | 1 | small | None | 402 | scheduled | 18/07/2024 | 06:41 | None | 10 | True |
    | 1 | Blankets | 5 | 1 | large | Pickup Truck | 8127 | repeated | Saturday | 22:51 | 17/08/2024 | 20 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 934 | scheduled | 04/09/2024 | 02:34 | None | 20 | True |
    | 1 | Ladder | 5 | 1 | medium | None | 3296 | repeated | Sunday, Wednesday | 10:28, 03:52 | 06/09/2024 | 0 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 8043 | urgent | None | None | None | 100 | False |
    | 1 | None |  | 1 | heavy_load | 10ft Box Truck | 9231 | urgent | None | None | None | 0 | False |
    | 1 | Ladder | 5 | 1 | medium | None | 9851 | scheduled | 08/08/2024 | 09:05 | None | 10 | True |
    | 1 | Ladder | 5 | 1 | heavy_load | 9ft Cargo Van | 1004 | repeated | Monday, Tuesday, Friday | 19:38, 09:46, 19:17 | 26/07/2024 | 100 | True |
    | 1 | Ladder | 5 | 1 | custom size | 15ft Box Truck | 3105 | repeated | Sunday, Friday | 19:31, 11:13 | 06/09/2024 | 20 | False |
    | 1 | White gloves service | 60 minutes | 1 | medium | None | 6365 | repeated | Friday, Thursday | 12:14, 22:45 | 29/09/2024 | 100 | False |
    | 1 | None |  | 1 | heavy_load | 10ft Box Truck | 9550 | scheduled | 06/08/2024 | 03:10 | None | 10 | True |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 10ft Box Truck | 3547 | repeated | Saturday, Sunday | 12:38, 03:36 | 28/08/2024 | 50 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 10ft Box Truck | 668 | scheduled | 19/07/2024 | 08:14 | None | 10 | True |
    | 1 | White gloves service | 60 minutes | 1 | heavy_load | 9ft Cargo Van | 6528 | scheduled | 12/08/2024 | 06:12 | None | 10 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | small | None | 6398 | scheduled | 06/08/2024 | 06:57 | None | 0 | True |
    | 1 | Ladder | 5 | 1 | custom size | Pickup Truck | 2591 | scheduled | 25/08/2024 | 21:21 | None | 20 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | large | SUV | 8655 | repeated | Saturday | 11:56 | 11/08/2024 | 10 | True |
    | 1 | None |  | 1 | heavy_load | 9ft Cargo Van | 3917 | repeated | Saturday, Sunday | 07:17, 00:33 | 25/08/2024 | 10 | True |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 6823 | scheduled | 06/08/2024 | 06:19 | None | 10 | False |
    | 1 | None |  | 1 | small | None | 6120 | repeated | Saturday, Thursday | 01:53, 10:19 | 22/07/2024 | 100 | False |
    | 1 | Blankets | 5 | 1 | small | None | 8761 | repeated | Monday | 17:05 | 11/09/2024 | 20 | True |
    | 1 | Blankets | 5 | 1 | heavy_load | 10ft Box Truck | 1460 | scheduled | 19/09/2024 | 04:46 | None | 100 | False |
    | 1 | None |  | 1 | small | None | 5598 | scheduled | 08/09/2024 | 15:56 | None | 100 | False |
    | 1 | Blankets | 5 | 1 | large | Pickup Truck | 724 | repeated | Thursday | 21:59 | 26/08/2024 | 10 | False |
    | 1 | Ladder | 5 | 1 | medium | None | 2432 | repeated | Saturday | 12:19 | 26/07/2024 | 10 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | small | None | 4667 | urgent | None | None | None | 100 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | heavy_load | 10ft Box Truck | 6377 | urgent | None | None | None | 50 | False |
    | 1 | Blankets | 5 | 1 | custom size | Car | 9746 | repeated | Thursday, Friday | 10:56, 11:37 | 11/09/2024 | 100 | True |
    | 1 | White gloves service | 60 minutes | 1 | large | Car | 361 | scheduled | 13/08/2024 | 23:33 | None | 50 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | small | None | 3804 | urgent | None | None | None | 20 | False |
    | 1 | Blankets | 5 | 1 | large | Car | 5774 | repeated | Thursday | 18:51 | 05/09/2024 | 100 | True |
    | 1 | White gloves service | 60 minutes | 1 | large | Pickup Truck | 195 | scheduled | 22/08/2024 | 19:06 | None | 20 | False |
    | 1 | Blankets | 5 | 1 | heavy_load | 9ft Ref Van | 9172 | scheduled | 06/08/2024 | 10:12 | None | 10 | False |
    | 1 | None |  | 1 | custom size | Car | 7987 | scheduled | 06/08/2024 | 16:11 | None | 0 | True |
    | 1 | None |  | 1 | custom size | 9ft Cargo Van | 7930 | scheduled | 19/09/2024 | 15:47 | None | 50 | False |
    | 1 | Blankets | 5 | 1 | custom size | Car | 2813 | repeated | Thursday | 18:00 | 17/08/2024 | 100 | True |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Cargo Van | 5277 | scheduled | 10/09/2024 | 09:45 | None | 100 | True |
    | 1 | None |  | 1 | large | Pickup Truck | 1263 | urgent | None | None | None | 100 | False |
    | 1 | Blankets | 5 | 1 | custom size | 9ft Cargo Van | 2410 | repeated | Wednesday, Tuesday | 01:25, 22:15 | 20/08/2024 | 0 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 5650 | scheduled | 18/08/2024 | 22:15 | None | 50 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | SUV | 5831 | repeated | Thursday, Tuesday, Friday | 18:28, 02:29, 01:23 | 12/08/2024 | 0 | True |
    | 1 | None |  | 1 | small | None | 3995 | repeated | Thursday, Tuesday, Wednesday | 02:12, 21:59, 05:53 | 20/08/2024 | 50 | False |
    | 1 | Blankets | 5 | 1 | small | None | 329 | urgent | None | None | None | 10 | True |
    | 1 | Ladder | 5 | 1 | large | Pickup Truck | 4396 | scheduled | 18/07/2024 | 13:14 | None | 10 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | small | None | 8629 | scheduled | 23/08/2024 | 02:14 | None | 0 | True |
    | 1 | Ladder | 5 | 1 | small | None | 5069 | repeated | Thursday, Monday, Friday | 11:41, 23:30, 11:45 | 13/08/2024 | 0 | True |
    | 1 | Ladder | 5 | 1 | small | None | 8978 | repeated | Friday, Sunday | 19:16, 06:47 | 16/09/2024 | 100 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | large | Car | 7583 | urgent | None | None | None | 10 | True |
    | 1 | Blankets | 5 | 1 | medium | None | 9017 | urgent | None | None | None | 0 | False |
    | 1 | Ladder | 5 | 1 | small | None | 6000 | scheduled | 23/09/2024 | 23:11 | None | 10 | True |
    | 1 | None |  | 1 | medium | None | 5698 | urgent | None | None | None | 10 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 10ft Box Truck | 510 | repeated | Friday | 20:32 | 17/08/2024 | 100 | True |
    | 1 | Ladder | 5 | 1 | heavy_load | 10ft Box Truck | 2010 | repeated | Tuesday, Saturday | 20:35, 10:33 | 06/09/2024 | 20 | True |
    | 1 | Ladder | 5 | 1 | heavy_load | 10ft Box Truck | 4362 | repeated | Sunday, Wednesday | 21:37, 04:25 | 18/08/2024 | 20 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | heavy_load | 9ft Cargo Van | 5000 | scheduled | 07/09/2024 | 00:10 | None | 50 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | large | Car | 823 | repeated | Tuesday | 12:39 | 05/08/2024 | 10 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | small | None | 4262 | scheduled | 16/08/2024 | 05:28 | None | 10 | False |
    | 1 | None |  | 1 | medium | None | 3509 | urgent | None | None | None | 10 | True |
    | 1 | None |  | 1 | medium | None | 5161 | scheduled | 22/08/2024 | 06:38 | None | 50 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | heavy_load | 9ft Ref Van | 4947 | urgent | None | None | None | 0 | True |
    | 1 | Ladder | 5 | 1 | heavy_load | 9ft Ref Van | 5353 | scheduled | 28/08/2024 | 18:36 | None | 100 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Ref Van | 860 | repeated | Monday, Wednesday, Sunday | 23:47, 21:02, 05:55 | 25/08/2024 | 20 | False |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 15ft Box Truck | 8619 | scheduled | 22/09/2024 | 11:57 | None | 20 | False |
    | 1 | White gloves service | 60 minutes | 1 | medium | None | 8469 | repeated | Wednesday | 23:16 | 25/08/2024 | 10 | False |
    | 1 | Blankets | 5 | 1 | small | None | 1057 | scheduled | 12/08/2024 | 03:57 | None | 10 | True |
    | 1 | Blankets | 5 | 1 | custom size | 15ft Box Truck | 9010 | urgent | None | None | None | 20 | False |
    | 1 | Blankets | 5 | 1 | large | Car | 4736 | scheduled | 25/09/2024 | 19:16 | None | 50 | True |
    | 1 | White gloves service | 60 minutes | 1 | medium | None | 1692 | scheduled | 14/09/2024 | 00:53 | None | 50 | False |
    | 1 | Blankets | 5 | 1 | small | None | 9105 | scheduled | 07/09/2024 | 23:29 | None | 50 | True |
    | 1 | Ladder | 5 | 1 | medium | None | 8376 | repeated | Tuesday | 00:23 | 14/09/2024 | 20 | False |
    | 1 | Ladder | 5 | 1 | medium | None | 8929 | urgent | None | None | None | 50 | True |
    | 1 | White gloves service | 60 minutes | 1 | heavy_load | 9ft Cargo Van | 2715 | urgent | None | None | None | 20 | True |
    | 1 | Ladder | 5 | 1 | medium | None | 6888 | scheduled | 23/08/2024 | 20:30 | None | 0 | False |
    | 1 | Blankets | 5 | 1 | large | Car | 3540 | urgent | None | None | None | 0 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | small | None | 4218 | repeated | Friday, Thursday | 14:43, 03:41 | 13/09/2024 | 20 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 15ft Box Truck | 2475 | repeated | Sunday, Friday, Tuesday | 07:20, 15:10, 23:56 | 06/08/2024 | 100 | True |
    | 1 | Ladder | 5 | 1 | heavy_load | Pickup Truck | 5424 | urgent | None | None | None | 0 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 3549 | scheduled | 23/08/2024 | 22:20 | None | 10 | True |
    | 1 | Ladder | 5 | 1 | heavy_load | 15ft Box Truck | 7786 | repeated | Wednesday | 03:29 | 19/08/2024 | 50 | False |
    | 1 | Ladder | 5 | 1 | small | None | 379 | scheduled | 22/09/2024 | 23:17 | None | 0 | True |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Cargo Van | 3580 | urgent | None | None | None | 50 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | large | Pickup Truck | 240 | repeated | Thursday | 11:32 | 26/07/2024 | 10 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | small | None | 7219 | urgent | None | None | None | 50 | False |
    | 1 | White gloves service | 60 minutes | 1 | large | Car | 2962 | urgent | None | None | None | 50 | True |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 5589 | repeated | Sunday, Wednesday, Tuesday | 06:07, 04:44, 21:22 | 18/08/2024 | 100 | True |
    | 1 | Ladder | 5 | 1 | large | SUV | 6221 | urgent | None | None | None | 20 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 0 | scheduled | 28/07/2024 | 04:35 | None | 50 | True |
    | 1 | White gloves service | 60 minutes | 1 | small | None | 4024 | urgent | None | None | None | 10 | False |
    | 1 | Ladder | 5 | 1 | small | None | 5097 | repeated | Friday, Tuesday | 22:23, 10:59 | 06/09/2024 | 20 | False |
    | 1 | Ladder | 5 | 1 | small | None | 1366 | repeated | Saturday, Friday, Monday | 19:05, 22:54, 20:14 | 23/09/2024 | 0 | True |
    | 1 | Blankets | 5 | 1 | medium | None | 4384 | urgent | None | None | None | 50 | False |
    | 1 | Ladder | 5 | 1 | custom size | SUV | 8219 | repeated | Friday, Monday | 22:53, 20:29 | 09/09/2024 | 0 | True |
    | 1 | None |  | 1 | heavy_load | 9ft Cargo Van | 7491 | urgent | None | None | None | 50 | True |
    | 1 | Blankets | 5 | 1 | medium | None | 7265 | scheduled | 30/08/2024 | 23:50 | None | 100 | False |
    | 1 | White gloves service | 60 minutes | 1 | small | None | 6595 | urgent | None | None | None | 100 | False |
    | 1 | White gloves service | 60 minutes | 1 | heavy_load | Pickup Truck | 209 | urgent | None | None | None | 20 | True |
    | 1 | None |  | 1 | medium | None | 278 | scheduled | 31/07/2024 | 03:47 | None | 20 | False |
    | 1 | Blankets | 5 | 1 | heavy_load | 15ft Box Truck | 1477 | urgent | None | None | None | 20 | True |
    | 1 | Blankets | 5 | 1 | heavy_load | 15ft Box Truck | 1178 | scheduled | 30/08/2024 | 10:38 | None | 100 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 9076 | scheduled | 22/09/2024 | 17:53 | None | 50 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | large | Car | 7018 | scheduled | 25/08/2024 | 05:00 | None | 10 | False |
    | 1 | None |  | 1 | small | None | 446 | scheduled | 24/08/2024 | 07:15 | None | 50 | True |
    | 1 | Ladder | 5 | 1 | custom size | 10ft Box Truck | 6394 | urgent | None | None | None | 50 | False |
    | 1 | White gloves service | 60 minutes | 1 | medium | None | 7671 | repeated | Tuesday, Saturday | 15:40, 02:26 | 24/08/2024 | 100 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | heavy_load | 9ft Cargo Van | 3147 | urgent | None | None | None | 0 | True |
    | 1 | White gloves service | 60 minutes | 1 | large | SUV | 8967 | scheduled | 21/08/2024 | 20:43 | None | 10 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | small | None | 9945 | repeated | Monday, Friday, Thursday | 07:00, 08:56, 12:30 | 28/07/2024 | 10 | False |
    | 1 | Ladder | 5 | 1 | heavy_load | 15ft Box Truck | 3738 | scheduled | 27/09/2024 | 19:30 | None | 20 | False |
    | 1 | Blankets | 5 | 1 | large | SUV | 8695 | urgent | None | None | None | 10 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 7038 | scheduled | 06/08/2024 | 05:23 | None | 100 | True |
    | 1 | White gloves service | 60 minutes | 1 | heavy_load | 10ft Box Truck | 7891 | scheduled | 26/08/2024 | 14:51 | None | 10 | True |
    | 1 | None |  | 1 | small | None | 6392 | scheduled | 17/09/2024 | 17:23 | None | 20 | True |
    | 1 | Ladder | 5 | 1 | custom size | 10ft Box Truck | 9094 | scheduled | 07/09/2024 | 02:33 | None | 0 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Ref Van | 9072 | urgent | None | None | None | 10 | False |
    | 1 | Blankets | 5 | 1 | large | Pickup Truck | 4631 | scheduled | 16/09/2024 | 21:04 | None | 0 | False |
    | 1 | White gloves service | 60 minutes | 1 | medium | None | 9626 | urgent | None | None | None | 50 | False |
    | 1 | Ladder | 5 | 1 | large | Pickup Truck | 251 | scheduled | 25/08/2024 | 15:51 | None | 20 | False |
    | 1 | Blankets | 5 | 1 | medium | None | 9763 | urgent | None | None | None | 20 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 3717 | repeated | Wednesday, Thursday, Sunday | 07:45, 10:53, 22:34 | 23/07/2024 | 10 | True |
    | 1 | Ladder | 5 | 1 | small | None | 6906 | scheduled | 23/07/2024 | 11:45 | None | 0 | True |
    | 1 | None |  | 1 | heavy_load | 10ft Box Truck | 7252 | scheduled | 22/07/2024 | 08:12 | None | 20 | True |
    | 1 | Blankets | 5 | 1 | large | SUV | 1043 | urgent | None | None | None | 10 | False |
    | 1 | White gloves service | 60 minutes | 1 | medium | None | 7264 | repeated | Wednesday, Tuesday, Friday | 11:44, 01:53, 02:25 | 09/08/2024 | 20 | False |
    | 1 | Blankets | 5 | 1 | medium | None | 9214 | scheduled | 17/09/2024 | 08:32 | None | 50 | False |
    | 1 | Blankets | 5 | 1 | heavy_load | 10ft Box Truck | 9872 | repeated | Thursday | 17:57 | 22/07/2024 | 0 | False |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Ref Van | 3519 | repeated | Monday | 10:26 | 28/07/2024 | 20 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 5034 | repeated | Wednesday | 04:23 | 21/08/2024 | 50 | False |
    | 1 | White gloves service | 60 minutes | 1 | medium | None | 5981 | urgent | None | None | None | 0 | False |
    | 1 | Ladder | 5 | 1 | custom size | Car | 5179 | repeated | Sunday, Thursday, Wednesday | 17:43, 21:34, 11:44 | 08/08/2024 | 0 | True |
    | 1 | None |  | 1 | heavy_load | 9ft Ref Van | 6237 | scheduled | 10/08/2024 | 22:38 | None | 0 | False |
    | 1 | None |  | 1 | heavy_load | 15ft Box Truck | 1435 | urgent | None | None | None | 10 | True |
    | 1 | None |  | 1 | heavy_load | 9ft Cargo Van | 3409 | repeated | Wednesday, Tuesday | 05:34, 00:04 | 28/07/2024 | 100 | False |
    | 1 | None |  | 1 | small | None | 2134 | scheduled | 22/07/2024 | 05:16 | None | 10 | True |
    | 1 | Ladder | 5 | 1 | heavy_load | 15ft Box Truck | 4586 | scheduled | 12/08/2024 | 13:03 | None | 100 | True |
    | 1 | None |  | 1 | small | None | 8503 | scheduled | 19/09/2024 | 20:53 | None | 50 | True |
    | 1 | White gloves service | 60 minutes | 1 | custom size | SUV | 1817 | urgent | None | None | None | 50 | False |
    | 1 | Blankets | 5 | 1 | heavy_load | Pickup Truck | 1296 | repeated | Tuesday, Wednesday, Saturday | 12:41, 09:01, 21:57 | 22/08/2024 | 0 | True |
    | 1 | Blankets | 5 | 1 | large | Car | 8343 | urgent | None | None | None | 20 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | large | SUV | 2105 | scheduled | 12/08/2024 | 19:24 | None | 10 | True |
    | 1 | Blankets | 5 | 1 | heavy_load | 9ft Ref Van | 8631 | scheduled | 16/08/2024 | 00:13 | None | 20 | False |
    | 1 | Blankets | 5 | 1 | medium | None | 6418 | urgent | None | None | None | 20 | True |
    | 1 | Ladder | 5 | 1 | small | None | 5583 | repeated | Sunday, Friday, Saturday | 23:31, 16:32, 05:46 | 14/09/2024 | 100 | True |
    | 1 | None |  | 1 | small | None | 2620 | urgent | None | None | None | 10 | False |
    | 1 | White gloves service | 60 minutes | 1 | large | Car | 2352 | urgent | None | None | None | 10 | True |
    | 1 | Ladder | 5 | 1 | medium | None | 975 | scheduled | 19/08/2024 | 13:50 | None | 20 | False |
    | 1 | None |  | 1 | heavy_load | 9ft Ref Van | 5549 | repeated | Sunday, Saturday, Tuesday | 08:23, 14:44, 01:59 | 10/08/2024 | 50 | True |
    | 1 | White gloves service | 60 minutes | 1 | heavy_load | 9ft Ref Van | 269 | repeated | Sunday, Friday, Tuesday | 14:52, 01:10, 00:01 | 10/08/2024 | 0 | False |
    | 1 | Ladder | 5 | 1 | large | SUV | 1730 | repeated | Thursday, Monday, Saturday | 23:47, 14:26, 14:09 | 06/08/2024 | 20 | False |
    | 1 | Ladder | 5 | 1 | custom size | 15ft Box Truck | 2397 | repeated | Thursday, Sunday, Tuesday | 18:06, 02:23, 13:29 | 28/08/2024 | 0 | True |
    | 1 | Ladder | 5 | 1 | heavy_load | 9ft Ref Van | 1295 | urgent | None | None | None | 20 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | large | Pickup Truck | 6695 | repeated | Tuesday, Sunday, Friday | 21:20, 22:16, 08:09 | 04/09/2024 | 100 | False |
    | 1 | Blankets | 5 | 1 | heavy_load | 9ft Cargo Van | 2355 | scheduled | 21/09/2024 | 06:42 | None | 100 | False |
    | 1 | Blankets | 5 | 1 | large | Pickup Truck | 1255 | urgent | None | None | None | 10 | False |
    | 1 | Blankets | 5 | 1 | small | None | 5457 | scheduled | 26/07/2024 | 16:32 | None | 20 | False |
    | 1 | Ladder | 5 | 1 | heavy_load | 9ft Cargo Van | 5267 | urgent | None | None | None | 0 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | SUV | 9985 | scheduled | 21/07/2024 | 10:34 | None | 20 | False |
    | 1 | Blankets | 5 | 1 | custom size | Car | 4612 | repeated | Saturday | 05:47 | 08/09/2024 | 50 | True |
    | 1 | None |  | 1 | medium | None | 9517 | repeated | Thursday, Sunday, Saturday | 13:33, 19:29, 02:07 | 21/07/2024 | 10 | False |
    | 1 | None |  | 1 | large | Pickup Truck | 4844 | urgent | None | None | None | 20 | True |
    | 1 | White gloves service | 60 minutes | 1 | heavy_load | 15ft Box Truck | 3925 | urgent | None | None | None | 0 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | medium | None | 5793 | urgent | None | None | None | 50 | True |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Cargo Van | 1577 | scheduled | 24/08/2024 | 07:56 | None | 20 | True |
    | 1 | None |  | 1 | medium | None | 5187 | repeated | Tuesday, Thursday | 04:19, 10:06 | 04/09/2024 | 100 | False |
    | 1 | White gloves service | 60 minutes | 1 | small | None | 3407 | urgent | None | None | None | 0 | False |
    | 1 | White gloves service | 60 minutes | 1 | small | None | 7125 | urgent | None | None | None | 100 | True |
    | 1 | None |  | 1 | custom size | 9ft Cargo Van | 9903 | repeated | Wednesday, Sunday, Saturday | 08:44, 16:39, 03:20 | 13/09/2024 | 10 | False |
    | 1 | None |  | 1 | custom size | 10ft Box Truck | 4279 | urgent | None | None | None | 10 | False |
    | 1 | Ladder | 5 | 1 | custom size | 15ft Box Truck | 7131 | urgent | None | None | None | 50 | True |
    | 1 | White gloves service | 60 minutes | 1 | medium | None | 2497 | repeated | Sunday, Friday | 18:08, 15:54 | 04/09/2024 | 0 | True |
    | 1 | None |  | 1 | custom size | Pickup Truck | 6795 | repeated | Tuesday | 11:26 | 29/09/2024 | 20 | True |
    | 1 | White gloves service | 60 minutes | 1 | large | Car | 415 | scheduled | 23/09/2024 | 04:27 | None | 0 | False |
    | 1 | Ladder | 5 | 1 | heavy_load | 15ft Box Truck | 424 | repeated | Wednesday, Saturday, Thursday | 02:17, 05:53, 18:50 | 30/08/2024 | 50 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | large | Pickup Truck | 7243 | repeated | Tuesday | 08:29 | 22/07/2024 | 10 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Cargo Van | 5012 | scheduled | 05/08/2024 | 02:05 | None | 50 | True |
    | 1 | Ladder | 5 | 1 | medium | None | 7836 | urgent | None | None | None | 100 | False |
    | 1 | White gloves service | 60 minutes | 1 | large | Car | 3460 | scheduled | 23/07/2024 | 16:58 | None | 10 | False |
    | 1 | Ladder | 5 | 1 | medium | None | 5593 | repeated | Monday, Sunday | 14:36, 10:27 | 10/08/2024 | 20 | True |
    | 1 | Blankets | 5 | 1 | small | None | 7502 | repeated | Tuesday | 11:46 | 13/09/2024 | 10 | True |
    | 1 | Blankets | 5 | 1 | custom size | SUV | 3357 | repeated | Saturday, Monday | 07:11, 00:53 | 27/07/2024 | 50 | True |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Ref Van | 2246 | scheduled | 19/09/2024 | 12:56 | None | 10 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | heavy_load | 9ft Cargo Van | 2989 | scheduled | 20/08/2024 | 04:26 | None | 20 | True |
    | 1 | None |  | 1 | medium | None | 3745 | repeated | Sunday | 11:07 | 09/09/2024 | 10 | False |
    | 1 | None |  | 1 | large | Car | 6387 | urgent | None | None | None | 100 | False |
    | 1 | None |  | 1 | heavy_load | Pickup Truck | 1958 | repeated | Wednesday | 23:41 | 07/09/2024 | 20 | False |
    | 1 | Ladder | 5 | 1 | small | None | 4839 | scheduled | 27/09/2024 | 05:29 | None | 20 | True |
    | 1 | None |  | 1 | large | SUV | 7373 | repeated | Thursday | 01:29 | 14/09/2024 | 100 | False |
    | 1 | Ladder | 5 | 1 | large | Pickup Truck | 878 | urgent | None | None | None | 100 | True |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 10ft Box Truck | 855 | scheduled | 06/08/2024 | 15:37 | None | 0 | False |
    | 1 | None |  | 1 | custom size | 9ft Cargo Van | 6085 | scheduled | 13/09/2024 | 06:42 | None | 0 | True |
    | 1 | Blankets | 5 | 1 | heavy_load | 9ft Ref Van | 3960 | urgent | None | None | None | 50 | True |
    | 1 | White gloves service | 60 minutes | 1 | large | Pickup Truck | 5796 | repeated | Thursday, Saturday | 01:55, 22:56 | 26/07/2024 | 100 | False |
    | 1 | Blankets | 5 | 1 | small | None | 8304 | repeated | Monday, Tuesday | 20:05, 06:35 | 18/09/2024 | 20 | False |
    | 1 | White gloves service | 60 minutes | 1 | custom size | 9ft Ref Van | 3292 | repeated | Tuesday | 06:09 | 14/09/2024 | 20 | True |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Ref Van | 1205 | repeated | Friday, Tuesday | 22:47, 01:45 | 09/08/2024 | 20 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | large | SUV | 6528 | repeated | Saturday, Monday | 17:30, 19:47 | 24/07/2024 | 20 | True |
    | 1 | None |  | 1 | custom size | 15ft Box Truck | 213 | urgent | None | None | None | 50 | True |
    | 1 | White gloves service | 60 minutes | 1 | custom size | Car | 7012 | repeated | Monday | 04:41 | 24/07/2024 | 50 | True |
    | 1 | Ladder | 5 | 1 | custom size | 15ft Box Truck | 1051 | scheduled | 17/08/2024 | 12:28 | None | 50 | False |
    | 1 | Blankets | 5 | 1 | small | None | 4705 | scheduled | 22/08/2024 | 14:59 | None | 100 | False |
    | 1 | Food Catering Setup | 3 hours | 1 | custom size | 9ft Ref Van | 7764 | repeated | Tuesday, Sunday | 20:39, 21:54 | 19/07/2024 | 100 | True |
    | 1 | Ladder | 5 | 1 | custom size | 9ft Ref Van | 124 | urgent | None | None | None | 0 | False |
    | 1 | White gloves service | 60 minutes | 1 | small | None | 6030 | repeated | Thursday, Tuesday, Saturday | 02:16, 22:06, 08:34 | 18/08/2024 | 100 | False |
    | 1 | Ladder | 5 | 1 | small | None | 9259 | scheduled | 06/09/2024 | 00:00 | None | 10 | False |
    | 1 | White gloves service | 60 minutes | 1 | heavy_load | Pickup Truck | 304 | scheduled | 26/08/2024 | 12:40 | None | 0 | False |
    | 1 | White gloves service | 60 minutes | 1 | small | None | 1465 | urgent | None | None | None | 10 | True |
    | 1 | Ladder | 5 | 1 | large | SUV | 7052 | urgent | None | None | None | 10 | True |
    | 1 | Food Catering Setup | 3 hours | 1 | large | Car | 3380 | scheduled | 13/08/2024 | 08:54 | None | 0 | True |
    | 1 | None |  | 1 | large | SUV | 171 | repeated | Tuesday | 17:44 | 25/08/2024 | 10 | True |
    | 1 | Blankets | 5 | 1 | custom size | SUV | 7926 | scheduled | 12/08/2024 | 14:09 | None | 0 | True |
    | 1 | Blankets | 5 | 1 | small | None | 7737 | repeated | Saturday, Sunday, Friday | 03:27, 01:05, 13:54 | 23/07/2024 | 100 | False |
