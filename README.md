# libbark

## Functions

`version()`                 - Returns the current version\
`check()`                   - If no `logFile` is found, one is created\
`log(logLevel, logMessage)` - Logs a message with a specific level\
`clear()`                   - Clears the log\

## Log levels

*NOTE: logLevel must be a string (ex. "0")*\
`"-1"` - Ok\
`"0"`  - Info\
`"1"`  - Debug\
`"2"`  - Warn\
`"3"`  - Error

## Reading logs

Use the `bark` binary provided in [SrFluff/bark](https://www.github.com/SrFluff/bark)
