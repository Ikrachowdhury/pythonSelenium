 
# Selenium Automation on Open Source phptravels.com

 This is an Automation project on  open source website
 [phptravels.net](https://phptravels.net) with      Selenium, Python unittest.


#### **Automated sections**
---
* [Admin Page](https://phptravels.net/admin/login.php)
    - Flights
    - Flights Airports
    - Flights Airlines
    - Flights Featured
    - Flights Suggestions

* [Agent Page](https://phptravels.net/login)
    - DashBoard
    - Search for Best Flights
    - Featured Flights
    - Flights Booking
---







## Technologies Used
 * python
 * Selenium
 * unittest
 ---

## Flow Of Automation
* *Admin Side*
    1. Visit [Admin Login Page ](https://phptravels.net/admin/login.php) and Login
    2. Visit module page and toggle on Fligts
    3. Visit Flights Airports and assert All Fligts Airports page's features
    4. Visit Flights Airlines and assert All Fligts Airlines page's features
    5. Visit Flights Featureds and assert All Fligts Featureds page's features
    6. Visit Flights  and assert All Fligts page's features
    7. Visit Flights Suggestions and assert All Fligts Suggestions page's features
    8. Add 2 Fligts Airport, 1 Airline, Featured Fligh,
Flight Suggestion ,1 Flight

* *Agent Side*
  1. Visit [Agent Login Page](https://phptravels.net/login) and Login
  2. Assert Flights page
  3. Searcch For The Flight that has been added before in Admin Page
  4. Book the Flight
  5. Assert the Flight booking
  6. Select Flight From Featured Flights that has beed added before in Admin Page
  7. Book the Featured Flight
  8. Assert the Flight booking


## Test Cases For Automation
* [Test Cases Sheet -Google Drive](https://docs.google.com/spreadsheets/d/1hajuFhTIyi4jKHoYCHmUdvyngu5ql8nAZtCWSsjYv-g/edit?usp=sharing)
## Requirements
* python needs to be installed
* Selenium needs to be installed 
## Video Result
* Coming
