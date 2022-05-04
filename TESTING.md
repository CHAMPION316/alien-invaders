# Testing

Testing was done using the (IDE) Visual Studio on Windows 10 using a _**Surface Pro 6**_ That contain the following specs.

-   [**Specifications**](readme-files/pc-specs.jpg)

 Debugging was done using Visual Studio. Here are the final results for the dubugging.

 ## Error Message: Command Line

- [**Results**](readme-files/debug-results.jpg)

The message that I keep coming across here is: 
### (**libpng warning: iCCP: known incorrect sRGB profile**)

A google search for what I perceived to be an error message takes me to [Stack Overflow](https://stackoverflow.com/) with this response and solution from the community.

- [**Fix Link**](https://stackoverflow.com/questions/22745076/libpng-warning-iccp-known-incorrect-srgb-profile)
- [**Fix Image**](readme-files/warning-ms.jpg)

## Bugs

* When I wrote the project the game kept running into negative lives and continuing in a endless loop. This was because I I forgot to add '=' sign with less than for the end when it hits 0 lives.

## Remaining Bug (not anymore)

* When the player's health hits 0% the game ends even though the player has remaining lives when they aren't zero. Prior to sending the project this is the fix I was trying to work on. (_**At the time of updating this I finally fixed this bug that has haunted me on the final day.**_)
    * [**Fixed Bug Code**](readme-files/fixed-health-bug.jpg)

## Code validators testing

[**PEP8 Validator Results**](readme-files/PEP8_results.jpg): 

All errors were fixed using PEP8 except for two lines of code:
- Code E501 (line too long > 79 characters)
    - These lines of code are in a if statment which if idented crashes the program from running. I tried varies ways to make the identation work in order for it to clear PEP8 validation but had no success. In order to avoid crashing the program it was best to keep the errors. 

## PROBLEMS

[**run.py problem image**](docs/img/problems_image.jpg):

Within the terminal in the problems column I currently have 27 problems, which are as follows:
- 13 total: pylint(no-member) [**pylint(no-member)**](https://www.lesinskis.com/pylint-false-positives.html)
    - ***However since Python is so dynamic there's a whole bunch of ways in which you can dynamically define members of a class, and Pylint won't always catch these.***
    - For this reason I decided to ignore pylint due to the many changes I would have to make to my code which could result in it crashing.

- 5 total: pylint(arguments-renamed)
    - I avoided this problem after reading how complicated it would be to fix it to my understanding.
    - [**Example of W0237**](https://pylint.pycqa.org/en/latest/messages/warning/arguments-renamed.html)

- 4 total: Missing function or method docstring ***pylint(missing-function-docstring)***
    - A docstring was issued above these 4 functions in it's parent Laser class which is line 36.

- 5 total: Argument name "x" doesn't conform to snake_case naming style ***pylint(invalid-name)***
    - At the time of writing it was more difficult to change the code to meet this standard so I left it as is. 

## (URGENT) Issues with HEROKU

* I had sent this project but provided the wrong email so I was allowed to send it again. I again tried to fix the issue of having the program run on HEROKU but was not successfuly. I even went as far as creating a new repository and importing the code on there. That at least opened the window for the game but was still gettting a video "No available video device" error.


## Update on sending project

* Due to pygame not working on heroku I was allowed by student care to upload it through [**replit**](https://replit.com/) instead where it would be reviewed and graded. 