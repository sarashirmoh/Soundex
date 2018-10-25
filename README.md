# Soundex
* Constructed an FST that implements the Soundex algorithm (Soundex Algorith creates an output format of "Letter Digit Digit Digit", given any input string)
* The 1st transducer, retains the firstrst letter, removes letters and replaces letters with numbers.
* The 2nd tansducer truncates extra digits.
* The 3rd transducer pads the output with zeros if required.
