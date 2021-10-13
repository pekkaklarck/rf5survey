# Robot Framework 5.0 survey results

We had a [survey](https://forms.gle/E9CKhYLxvY4uKQR46) asking what features
[Robot Framework](http://robotframework.org) community members would like to
see in the forthcoming Robot Framework 5.0 release. In addition to that,
respondents could give free comments to the Robot Framework development team
and to the [Robot Framework Foundation](https://robotframework.org/foundation/)
that sponsors Robot Framework development.

Voted issues are listed by priority in the section below and all responses to
the survey are after them. Also [raw data](responses.csv) is available with
all personal information removed.

Two online tickets to [RoboCon 2022](https://robocon.io) were raffled among
the respondents who left their contact information. The lucky winners,
selected by the [random](https://docs.python.org/3/library/random.html) module,
are Anton Pääkkönen and Veijo Yli-Kätkä. Congratulations to them and thanks
for everyone who participated the survey!

## Issues by priority

Voted issues are listed below by priority with comments explaining why they
were considered important. Issues were voted in three priorities and higher
priority issues had a higher weight. Comments are got only from the highest
priority issues.

<!-- start issues (generated) -->
- [#3075](https://github.com/robotframework/robotframework/issues/3075) Native support for `TRY/EXCEPT` functionality (weighted priority: 86)
    - "Errors" are part of the business when working in process automation. Exceptions are ok and require handling. Which is rather difficult in RF right now.
    - Native TRY / EXCEPT is important for implementing RPA error handling workflows. Other control structures, such as WHILE, are also highly requested among RPA users (who wants to use FOR in range 0..999?) but out of everything other TRY / EXCEPT is difficult to implement with current constructs. Basically every RPA bot will benefit from this.
    - The current way to handle errors is really clunky. Try/except is a well-known pattern in many languages.
    - In RPA cases exceptions are common and need to be handled with proper code paths
    - Many operations in RF can raise exceptions and try/except enables much better syntax for handling those than what is currently available.
    - This brings large part of funcionality higher, to robot 
    - Native support for try except can help to handle exceptions well and prevent unwanted failures.
    - handle exceptions is a must during automation developing
    - Better error control for actions we know that may fail, and then run a workaround or repeat attempt.
    - Having the ability to use a try catch code block would help clean up a lot of code, along with solve a number of problems
    - This would simplify keywords where we want to do the same thing with both error inducing test data and successful test data
- [#4084](https://github.com/robotframework/robotframework/issues/4084) `WHILE` loop (weighted priority: 85)
    - While loop support is probably one of the most common questions I get from our engineers as they start with Robot.
    - Make polling solutions more readable
    - Because of a variety of use cases to build around a WHILE-loop.
    - It's missing at the moment and for loop has to be used as a workaround
    - I have multiple cases where I need to execute my API operation tests with an 'infinite' loop which is only supposed to be terminated in case there is a change in e.g. a variable's value etc. <br><br>Since 'real' While loops are not available, I use a For loop as a workaround. Nevertheless, due to its nature, this loop is finite and will terminate once the iteration counter has reached its maximum value.
    - Have got  a lot of cases when it would be more useful instead WUKS
    - More flexible code! And we have many polling situations in our product so it will be very helpful!
    - It'll be quite handy and useful in certain situations instead of using WUKS.
- [#4078](https://github.com/robotframework/robotframework/issues/4078) New `RETURN` statement for returning from a user keyword (weighted priority: 60)
    - I really like to use the output from a keyword as an argument in another keyword. Without hassling with scopes like test/suite or global. 
    - [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support") is the most important, however, it will surely be there. :) [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword") adds a construction known from other language, which makes it possible to remove one configuration option and 4 keywords. Great!
    - Sometimes I want to keep IF-return-ELSE-return logic in robot-file instead of "hiding" it away in a python-file. This would really simplify tests and make them readable to more people.
    - There has been many times a situation in my work where returning value inside IF..ELSE could have been very useful. 
- [#4093](https://github.com/robotframework/robotframework/issues/4093) Inline `IF` support (weighted priority: 43)
    - There have been times where I would have preferred a ternary type operation. With some work the Set Variable If keyword can be used to determine keyword execution, but with an in-line IF with an ELSE would definitely eliminate the work around.
- [#4079](https://github.com/robotframework/robotframework/issues/4079) New `BREAK` and `CONTINUE` statemens for `FOR` loop control (weighted priority: 43)
- [#3187](https://github.com/robotframework/robotframework/issues/3187) Inline keyword call syntax (weighted priority: 30)
    - because the test will be more readable, less variables "spamming"
- [#3423](https://github.com/robotframework/robotframework/issues/3423) Possibility to use output.json in addition to output.xml (weighted priority: 27)
    - It would help in customization of reports
    - managing results is bit tedious job
    - I believe that implementing this feature greatly reduces the weight of the outputs by speeding up their processing
- [#3761](https://github.com/robotframework/robotframework/issues/3761) Native syntax to create local variables (weighted priority: 25)
    - This is one of the most weird things when writing Robot tests. Would be great to have this supported natively. 
- [#3278](https://github.com/robotframework/robotframework/issues/3278) Variable type conversion in test data (weighted priority: 15)
- [#4088](https://github.com/robotframework/robotframework/issues/4088) Ability to register custom converters for keyword arguments (weighted priority: 14)
- [#3625](https://github.com/robotframework/robotframework/issues/3625) Support custom statuses (weighted priority: 14)
- [#3993](https://github.com/robotframework/robotframework/issues/3993) Provide API to get the variables from a Python file (weighted priority: 12)
    - Most probably not the only person who uses RF with Python. So the tighter the integration we have the better. Would love to help out, however I am by know means a developer.
    - This would open interesting doors in robot test automation.
- [#2581](https://github.com/robotframework/robotframework/issues/2581) Scope of keywords called in resource files is globally reinterpreted when resource file is imported (weighted priority: 12)
    - It is missed thing for RF to be a good language.<br>Keyword support in large projects becomes real headache, name conflicts, unexpected keyword usage, mess of imports 
- [#3457](https://github.com/robotframework/robotframework/issues/3457) Remove Python 2 and Python 3.5 support (weighted priority: 11)
    - The original sunset target of 2015 was announced back in 2008. That's a _decade_ and then some. Good riddance, Python 2! Hello f-strings, path-like objects, and other cool kids!
    - I want asyncio support which requires dropping python 2 support :)
- [#3017](https://github.com/robotframework/robotframework/issues/3017) Add return type to libdoc output (weighted priority: 10)
- [#4096](https://github.com/robotframework/robotframework/issues/4096) Multilanguage support for markers used in data (weighted priority: 9)
    - This will help for sharing information
- [#4020](https://github.com/robotframework/robotframework/issues/4020) Remove built-in Tidy tool in favor of external Robotidy (weighted priority: 9)
- [#4095](https://github.com/robotframework/robotframework/issues/4095) Add type formatter to Log keyword (weighted priority: 7)
- [#2970](https://github.com/robotframework/robotframework/issues/2970) Imported resource files variables not isolated (weighted priority: 6)
- [#519](https://github.com/robotframework/robotframework/issues/519) Given/When/Then should support other languages than English (weighted priority: 5)
- [#4039](https://github.com/robotframework/robotframework/issues/4039) Incomplete Exception Trace in log.html (Exception Chaining) (weighted priority: 5)
- [#2982](https://github.com/robotframework/robotframework/issues/2982) xUnit outputs: Add separate `<testsuite>` entries for each suite (weighted priority: 3)
- [#3410](https://github.com/robotframework/robotframework/issues/3410) Add `--maxassignlength` to control how much to automatically log when assigning variables (weighted priority: 3)
- [#3902](https://github.com/robotframework/robotframework/issues/3902) Support serializing executable test suite into JSON (weighted priority: 3)
- [#4089](https://github.com/robotframework/robotframework/issues/4089) support async keywords (weighted priority: 1)
- [#4068](https://github.com/robotframework/robotframework/issues/4068) Make test and suite messages available as plain text and HTML separately (weighted priority: 1)
<!-- end issues (generated) -->


## All responses

Hover mouse over the issue id to see its title.

<!-- start responses (generated) -->

### What is the single most important feature for you? Why?

| Issue | Comment |
|-------|---------|
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | "Errors" are part of the business when working in process automation. Exceptions are ok and require handling. Which is rather difficult in RF right now. |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | Native TRY / EXCEPT is important for implementing RPA error handling workflows. Other control structures, such as WHILE, are also highly requested among RPA users (who wants to use FOR in range 0..999?) but out of everything other TRY / EXCEPT is difficult to implement with current constructs. Basically every RPA bot will benefit from this. |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | The current way to handle errors is really clunky. Try/except is a well-known pattern in many languages. |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | In RPA cases exceptions are common and need to be handled with proper code paths |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | Many operations in RF can raise exceptions and try/except enables much better syntax for handling those than what is currently available. |
| [#2457](https://github.com/robotframework/robotframework/issues/2457 "Robot Process library incorrectly buffers file pipe output") | Dummy |
| [#3423](https://github.com/robotframework/robotframework/issues/3423 "Possibility to use output.json in addition to output.xml") | It would help in customization of reports |
| [#3993](https://github.com/robotframework/robotframework/issues/3993 "Provide API to get the variables from a Python file") | Most probably not the only person who uses RF with Python. So the tighter the integration we have the better. Would love to help out, however I am by know means a developer. |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop") | While loop support is probably one of the most common questions I get from our engineers as they start with Robot. |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop") | Make polling solutions more readable |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | This brings large part of funcionality higher, to robot  |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | Native support for try except can help to handle exceptions well and prevent unwanted failures. |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | handle exceptions is a must during automation developing |
| [#3820](https://github.com/robotframework/robotframework/issues/3820 "New setting for test parametrization") | People struggle with running same tests with different configs. |
| [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support") | There have been times where I would have preferred a ternary type operation. With some work the Set Variable If keyword can be used to determine keyword execution, but with an in-line IF with an ELSE would definitely eliminate the work around. |
| [#3761](https://github.com/robotframework/robotframework/issues/3761 "Native syntax to create local variables") | This is one of the most weird things when writing Robot tests. Would be great to have this supported natively.  |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop") | Because of a variety of use cases to build around a WHILE-loop. |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | Better error control for actions we know that may fail, and then run a workaround or repeat attempt. |
| [#3423](https://github.com/robotframework/robotframework/issues/3423 "Possibility to use output.json in addition to output.xml") | managing results is bit tedious job |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop") | It's missing at the moment and for loop has to be used as a workaround |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop") | I have multiple cases where I need to execute my API operation tests with an 'infinite' loop which is only supposed to be terminated in case there is a change in e.g. a variable's value etc. <br><br>Since 'real' While loops are not available, I use a For loop as a workaround. Nevertheless, due to its nature, this loop is finite and will terminate once the iteration counter has reached its maximum value. |
| [#4110](https://github.com/robotframework/robotframework/issues/4110 "Robotframework doesn't have any parallel test execution feature in built") | This would really optimize the number of hours a big test cycle takes. |
| [#2581](https://github.com/robotframework/robotframework/issues/2581 "Scope of keywords called in resource files is globally reinterpreted when resource file is imported") | It is missed thing for RF to be a good language.<br>Keyword support in large projects becomes real headache, name conflicts, unexpected keyword usage, mess of imports  |
| [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword") | I really like to use the output from a keyword as an argument in another keyword. Without hassling with scopes like test/suite or global.  |
| [#3457](https://github.com/robotframework/robotframework/issues/3457 "Remove Python 2 and Python 3.5 support") | The original sunset target of 2015 was announced back in 2008. That's a _decade_ and then some. Good riddance, Python 2! Hello f-strings, path-like objects, and other cool kids! |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop") | Have got  a lot of cases when it would be more useful instead WUKS |
| [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword") | [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support") is the most important, however, it will surely be there. :) [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword") adds a construction known from other language, which makes it possible to remove one configuration option and 4 keywords. Great! |
| [#3993](https://github.com/robotframework/robotframework/issues/3993 "Provide API to get the variables from a Python file") | This would open interesting doors in robot test automation. |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | Having the ability to use a try catch code block would help clean up a lot of code, along with solve a number of problems |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | This would simplify keywords where we want to do the same thing with both error inducing test data and successful test data |
| [#3457](https://github.com/robotframework/robotframework/issues/3457 "Remove Python 2 and Python 3.5 support") | I want asyncio support which requires dropping python 2 support :) |
| [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword") | Sometimes I want to keep IF-return-ELSE-return logic in robot-file instead of "hiding" it away in a python-file. This would really simplify tests and make them readable to more people. |
| [#3423](https://github.com/robotframework/robotframework/issues/3423 "Possibility to use output.json in addition to output.xml") | I believe that implementing this feature greatly reduces the weight of the outputs by speeding up their processing |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") |  |
| [#4096](https://github.com/robotframework/robotframework/issues/4096 "Multilanguage support for markers used in data") | This will help for sharing information |
| [#4088](https://github.com/robotframework/robotframework/issues/4088 "Ability to register custom converters for keyword arguments") |  |
| [#2581](https://github.com/robotframework/robotframework/issues/2581 "Scope of keywords called in resource files is globally reinterpreted when resource file is imported") |  |
| [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax") | because the test will be more readable, less variables "spamming" |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop") | More flexible code! And we have many polling situations in our product so it will be very helpful! |
| [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword") | There has been many times a situation in my work where returning value inside IF..ELSE could have been very useful.  |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop") | It'll be quite handy and useful in certain situations instead of using WUKS. |

### Which three issues have second-highest priority? Why?

| Issue | Comment |
|-------|---------|
| [#2982](https://github.com/robotframework/robotframework/issues/2982 "xUnit outputs: Add separate `<testsuite>` entries for each suite"), [#3761](https://github.com/robotframework/robotframework/issues/3761 "Native syntax to create local variables"), [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax") | They would resolve a big amount of extra-steps I am find myself too comfortable with. |
| [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword"), [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop"), [#3423](https://github.com/robotframework/robotframework/issues/3423 "Possibility to use output.json in addition to output.xml") | Better support for RETURN will simplify tasks a lot and allow for common coding patterns. Something that people just expect to work. Although inline keyword call ([#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax") ) is also to be expected to just work, but that's another topic.<br><br>Native WHILE will eliminate the need for ugly hacks around FOR. This is something that's not obvious for many users and it's kind of embarrassing to explain the workaround.<br><br>Native support for JSON output is way overdue. XML based formats are a thing of the past and while it's easy to post process the output to JSON instead of XML, not having the support in RF core prevents the ecosystem from growing on top of a common schema. |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop"), [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword"), [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control") | Having constructs that are familiar with "normal" programming languages makes Robot Framework easier to learn and use (since things are somewhat familiar). |
| [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword"), [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop"), [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control") | All the above provide elegant and natural changes into RF syntax ([#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax") and [#3761](https://github.com/robotframework/robotframework/issues/3761 "Native syntax to create local variables") are not yet ready for implementation. Their syntax proposals are still not good enough and might cause more confusion than clarify things) |
| [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax"), [#3278](https://github.com/robotframework/robotframework/issues/3278 "Variable type conversion in test data"), [#3017](https://github.com/robotframework/robotframework/issues/3017 "Add return type to libdoc output") | Robot Framework code is often at it's most clearest when types are handled automatically and user does not need to use seemingly obscure syntax like ${1} just to give a number. |
| [#4088](https://github.com/robotframework/robotframework/issues/4088 "Ability to register custom converters for keyword arguments") | Dummy |
| [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword"), [#3017](https://github.com/robotframework/robotframework/issues/3017 "Add return type to libdoc output") | This would help in customization of robot framework based on the need, I have also raised [#3017](https://github.com/robotframework/robotframework/issues/3017 "Add return type to libdoc output") sometime back |
| [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword"), [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop"), [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control") | Syntax and the ability to make it easier to read and learn when coming from or to other languages. |
| [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support"), [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control"), [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | These issues extend Robotframework functionality that would be used by more traditional programmers. This would help drive adoption of engineers that are looking for this kind of functionality. |
| [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control"), [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support"), [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword") | Making the code more readable |
| [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword"), [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop"), [#4020](https://github.com/robotframework/robotframework/issues/4020 "Remove built-in Tidy tool in favor of external Robotidy") | These two bring some flow control funcionalities to robot. Robotidy is important for me as I find it very useful and with that change it might get wider audience and community support for further development.  |
| [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax"), [#4088](https://github.com/robotframework/robotframework/issues/4088 "Ability to register custom converters for keyword arguments"), [#3423](https://github.com/robotframework/robotframework/issues/3423 "Possibility to use output.json in addition to output.xml") | Inline keyword call would be very handy feature as it would help to reduce some steps from the code. Custom convertors would be very useful since its about data type/format. Data is the key thing for any test case so would be benefit all. Output.json would be easy to parse and use in custom dashboards. |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop"), [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control"), [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword") | overal semantic |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop"), [#4020](https://github.com/robotframework/robotframework/issues/4020 "Remove built-in Tidy tool in favor of external Robotidy"), [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax") | Adding WHILE seems like the next logical item after adding the IF/ELSE, the external tidy tool is superior to the built in- I wish the external tool could be brought into the standard RF package. The ability to chain keywords could potentially be abused (limit the number of chained keywords?)- I could remove so many unnecessary local variables if I could chain some of the keywords. Super useful if you are manipulating variable values. |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | Same as #1 :-) |
| [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control"), [#4020](https://github.com/robotframework/robotframework/issues/4020 "Remove built-in Tidy tool in favor of external Robotidy"), [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support") | Inline IF feels like something I'd want to use with IFs already now, and I'd like to have it in before I feel like there's a lot to refactor in the future where I'd favor that design. Tidy is outdated, so fragmenting the tool selection is not good for the ecosystem. Break and Continue are good tools to have in the box, but not critical. I also like Try/Except and understand the RPA-importance, but I don't work with RPA so won't favor that over Break/Continue. |
| [#519](https://github.com/robotframework/robotframework/issues/519 "Given/When/Then should support other languages than English"), [#4096](https://github.com/robotframework/robotframework/issues/4096 "Multilanguage support for markers used in data") | Better internationalization, and simplification of some steps with inline support. |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality"), [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support"), [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax") | Inline keywords actually saves time and code |
| [#3625](https://github.com/robotframework/robotframework/issues/3625 "Support custom statuses"), [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support"), [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | They impact the general ease of use, code readability and integration  |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality"), [#3410](https://github.com/robotframework/robotframework/issues/3410 "Add `--maxassignlength` to control how much to automatically log when assigning variables"), [#3761](https://github.com/robotframework/robotframework/issues/3761 "Native syntax to create local variables") |  |
| [#3625](https://github.com/robotframework/robotframework/issues/3625 "Support custom statuses") | It would be really convenient and flexible. |
| [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support"), [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality"), [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control") | Aligned the code with python at least, makes easy to develop tests for programmers |
| [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support"), [#3278](https://github.com/robotframework/robotframework/issues/3278 "Variable type conversion in test data"), [#3017](https://github.com/robotframework/robotframework/issues/3017 "Add return type to libdoc output") | [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support") :The inline IF removes the END<br>[#3278](https://github.com/robotframework/robotframework/issues/3278 "Variable type conversion in test data") : we made a keyword to see what type of variable we get.  With this one we can assign the type<br>[#3017](https://github.com/robotframework/robotframework/issues/3017 "Add return type to libdoc output") : It is nice to see what is returned. |
| [#3902](https://github.com/robotframework/robotframework/issues/3902 "Support serializing executable test suite into JSON"), [#4039](https://github.com/robotframework/robotframework/issues/4039 "Incomplete Exception Trace in log.html (Exception Chaining)"), [#3278](https://github.com/robotframework/robotframework/issues/3278 "Variable type conversion in test data") |  |
| [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control"), [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword"), [#3423](https://github.com/robotframework/robotframework/issues/3423 "Possibility to use output.json in addition to output.xml") |  |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop"), [#3761](https://github.com/robotframework/robotframework/issues/3761 "Native syntax to create local variables"), [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control") | They simplifies common constructions and/or makes them more pretty |
| [#4077](https://github.com/robotframework/robotframework/issues/4077 "Prematurely abort 'Wait Until Keyword Succeeds' in a programmatic way with a negative response") |  |
| [#3423](https://github.com/robotframework/robotframework/issues/3423 "Possibility to use output.json in addition to output.xml"), [#3278](https://github.com/robotframework/robotframework/issues/3278 "Variable type conversion in test data"), [#3761](https://github.com/robotframework/robotframework/issues/3761 "Native syntax to create local variables") | Json as the output would help with parsing the output file. The other two, in my opinion, can help greatly with making the tests/keywords more readable  |
| [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword"), [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control"), [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop") | They provide support for common syntax patterns applicable to a wide range of use cases |
| [#3278](https://github.com/robotframework/robotframework/issues/3278 "Variable type conversion in test data"), [#4088](https://github.com/robotframework/robotframework/issues/4088 "Ability to register custom converters for keyword arguments"), [#3761](https://github.com/robotframework/robotframework/issues/3761 "Native syntax to create local variables") | These would help make tests more readable and make it more clear what kind of variables should and will be moving between keywords. All these would also make tests more compact and reduce redundant ${} and other expressions |
| [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support"), [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control"), [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop") | They allow you to manage conditions more easily by making the writing process faster and the reading process easier |
| [#3625](https://github.com/robotframework/robotframework/issues/3625 "Support custom statuses"), [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop"), [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax") |  |
| [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support"), [#4095](https://github.com/robotframework/robotframework/issues/4095 "Add type formatter to Log keyword"), [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop") | Some of these are needed to improve testing |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality"), [#4095](https://github.com/robotframework/robotframework/issues/4095 "Add type formatter to Log keyword"), [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop") |  |
| [#2970](https://github.com/robotframework/robotframework/issues/2970 "Imported resource files variables not isolated"), [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support"), [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword") |  |
| [#3761](https://github.com/robotframework/robotframework/issues/3761 "Native syntax to create local variables"), [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop"), [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support") | to have test more readable and avoid variables "spamming" |
| [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax"), [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword"), [#3625](https://github.com/robotframework/robotframework/issues/3625 "Support custom statuses") | More readable code, return status will be more generic and clear now with the if-else, and custom statuses will help a lot to distinguish failures and skipped tests! |
| [#4084](https://github.com/robotframework/robotframework/issues/4084 "`WHILE` loop"), [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control"), [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality") | They move RF closer to native coding conventions which is good. |
| [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control"), [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword"), [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support") |  |

### Which other issues you would like to see included? Why?

| Issue | Comment |
|-------|---------|
| [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax") | This is something that a new user would expect to "just work" but the syntax proposals in that issue are not great. Still worth exploring more. |
| [#519](https://github.com/robotframework/robotframework/issues/519 "Given/When/Then should support other languages than English") | I see more and more non-English speakers working with Robot Framework and this may help the barrier of entry for them. |
| [#4079](https://github.com/robotframework/robotframework/issues/4079 "New `BREAK` and `CONTINUE` statemens for `FOR` loop control"), [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax") |  |
| [#4095](https://github.com/robotframework/robotframework/issues/4095 "Add type formatter to Log keyword"), [#519](https://github.com/robotframework/robotframework/issues/519 "Given/When/Then should support other languages than English"), [#3625](https://github.com/robotframework/robotframework/issues/3625 "Support custom statuses") | [#4095](https://github.com/robotframework/robotframework/issues/4095 "Add type formatter to Log keyword") - helpful for debugging <br>[#519](https://github.com/robotframework/robotframework/issues/519 "Given/When/Then should support other languages than English") - Would tempt cucumber users to migrate on Robot Framework.<br>[#3625](https://github.com/robotframework/robotframework/issues/3625 "Support custom statuses") - May help some users to follow organisations standards for test case status. |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality"), [#3457](https://github.com/robotframework/robotframework/issues/3457 "Remove Python 2 and Python 3.5 support") | Good for the framework itself in gaining more userbase who respect modern support. |
| [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax"), [#3993](https://github.com/robotframework/robotframework/issues/3993 "Provide API to get the variables from a Python file"), [#4078](https://github.com/robotframework/robotframework/issues/4078 "New `RETURN` statement for returning from a user keyword") | Good to have |
| [#2970](https://github.com/robotframework/robotframework/issues/2970 "Imported resource files variables not isolated") | This issue is pretty similar with the most important for me, scope of resource keywords |
| [#3761](https://github.com/robotframework/robotframework/issues/3761 "Native syntax to create local variables"), [#3993](https://github.com/robotframework/robotframework/issues/3993 "Provide API to get the variables from a Python file") |  |
| [#2581](https://github.com/robotframework/robotframework/issues/2581 "Scope of keywords called in resource files is globally reinterpreted when resource file is imported"), [#2970](https://github.com/robotframework/robotframework/issues/2970 "Imported resource files variables not isolated") |  |
| [#3075](https://github.com/robotframework/robotframework/issues/3075 "Native support for `TRY/EXCEPT` functionality"), [#4096](https://github.com/robotframework/robotframework/issues/4096 "Multilanguage support for markers used in data") | I am a fan of writing tests in my language. |
| [#3761](https://github.com/robotframework/robotframework/issues/3761 "Native syntax to create local variables") | Just so common that it would be nice to have |
| [#4089](https://github.com/robotframework/robotframework/issues/4089 "support async keywords") | async is increasingly important! |
| [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support") | Whatever makes RF more compact. |
| [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax") | It would be great to use keywords in places where you would normally only have simple strings (or variables). |
| [#4068](https://github.com/robotframework/robotframework/issues/4068 "Make test and suite messages available as plain text and HTML separately") | To improve reports |
| [#2581](https://github.com/robotframework/robotframework/issues/2581 "Scope of keywords called in resource files is globally reinterpreted when resource file is imported"), [#2970](https://github.com/robotframework/robotframework/issues/2970 "Imported resource files variables not isolated") |  |
| [#3017](https://github.com/robotframework/robotframework/issues/3017 "Add return type to libdoc output"), [#4039](https://github.com/robotframework/robotframework/issues/4039 "Incomplete Exception Trace in log.html (Exception Chaining)") | [#3017](https://github.com/robotframework/robotframework/issues/3017 "Add return type to libdoc output") to get easily the signature of a kwd, [#4039](https://github.com/robotframework/robotframework/issues/4039 "Incomplete Exception Trace in log.html (Exception Chaining)") to improve analysis |
| [#4093](https://github.com/robotframework/robotframework/issues/4093 "Inline `IF` support") | More readable code and reduce of testcase body length. of course sometimes having a clear block of if-else keywords is better, but especially for one liners its very good.  |
| [#4039](https://github.com/robotframework/robotframework/issues/4039 "Incomplete Exception Trace in log.html (Exception Chaining)"), [#3625](https://github.com/robotframework/robotframework/issues/3625 "Support custom statuses") | More detailed log is always useful. Custom status could be very practical and informative for other co-workers also. |
## Free comments to the development team
- [#3187](https://github.com/robotframework/robotframework/issues/3187 "Inline keyword call syntax") and [#3761](https://github.com/robotframework/robotframework/issues/3761 "Native syntax to create local variables") are excellent ideas, but not yet ready for implementation. Proposed syntaxes might still cause too much confusion.
- Awesome tool, keep up the good work
- Keep up the great work!
- Praiseworthy efforts on the project. Thanks for this open source automation tool
- GL. These votes are great for the community, as otherwise many of us may not have the opportunity to join the development work.
- First of all, Thank you for creating this great tool. Hats off to you guys (y)<br><br>Need below functionality as well:<br>All assertions should have option to return True/False instead of marking test as Pass/Fail (Should be, Should not be)<br>
- You're doing great job guys :)
- Continue to make the RF future releases more solid and strong
- Godspeed with this new release. I am very gratefull for yout hard work.
- Good luck! :)
- Thank you for your request of feedback!
- This was a good effort!
- Thank you! Keeping an eye on this process and hoping to contribute in the future
- Thanks for your good work!
- Keep doing the good work!
- Thanks for the work you do!
- Thanks for the hard work
- Keep up the good work! You are always there to help out in slack and mailing list. Hope this year i can dedicate some work time as well to help out. 
## Free comments to Robot Framework Foundation
- Thank you for making this available to all and 7keeping it updated on a regular basis. 
- Keep up the great work!
- Thanks a lot for supporting and funding this awesome automation tool.
- Has there been any thought to developing an official style guide?
- Thanks for releasing this as open source, please continue to do so :P
- very useful and perfect ATDD
- You are on the right side
- Keep up the good work!
- Good luck! :)
- Thanks for all the fish.
- Thanks for robot framework!
- It will be good to have some students (College) activities
- I am sure the foundation will grow year by year and it definitely deserves it! Really good work with the conferences, well done! 
- Foundation could arrange more trainings and workshops than just once/twice a year.
<!-- end responses (generated) -->
