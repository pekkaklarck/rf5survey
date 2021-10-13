Survey results
==============

Voting
------

Issues were voted in three priorities with limits for how many issues could
get higher priorities. In the final priority all votes are combined so that
higher priority issues have a higher weight. Maximum number of issues per
priority and their weights are shown in the table below.

| Priority | Max issues | Weight |
|----------|------------|--------|
| Critical | 1          | 5      |
| High     | 3          | 3      |
| Medium   | unlimited  | 1      |

Issues by priority
------------------

Voted issues are listed below by priority with comments explaining why they
were considered important. Comments are got only from issues with the highest
priority.

<!-- insert issues below -->
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
    - 4093 is the most important, however, it will surely be there. :) 4078 adds a construction known from other language, which makes it possible to remove one configuration option and 4 keywords. Great!
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
