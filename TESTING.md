Testing was done using the (IDE) Visual Studio on Windows 10 using a _**Surface Pro 6**_ That contain the following specs.

-   [**Specifications**](readme-files/pc-specs.jpg)

 Debugging was done using Visual Studio. Here are the final results for the dubugging.

 ### Error Message

- [**Results**](readme-files/debug-results.jpg)

The message that I keep coming across here is: 
#### (**libpng warning: iCCP: known incorrect sRGB profile**)

A google search for what I perceived to be an error message takes me to [Stack Overflow](https://stackoverflow.com/) with this response and solution from the community.

- [**Fix Link**](https://stackoverflow.com/questions/22745076/libpng-warning-iccp-known-incorrect-srgb-profile)
- [**Fix Image**](readme-files/warning-ms.jpg)

### Bugs

* When I wrote the project the game kept running into negative lives and continuing in a endless loop. This was because I I forgot to add '=' sign with less than for the end when it hits 0 lives.

### Remaining Bug

* When the player's health hits 0% the game ends even though the player has remaining lives when they aren't zero. Prior to sending the project this is the fix I was trying to work on.

### Validator testing


