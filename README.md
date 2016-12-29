# file_logger
This repository defines a set of helper functions used to speed up the tedius process of configuring logging the way I like.  

The first function provided determines the OS being used and checks whether a folder already exists in root for storing log-files.  If it does not yet exist, it creates it.  It also defines filenames based on the module name for two files, a low-level (debug and all) log file and a higher-level (info and up) log file.

The second function sets up the root logger with three handlers and logging levels.  All log messages will be sent to the debug log file, while only info and up messages will be sent to the info log-file.  A stream handler is also configured for info-level and higher messages although this can easily be re-configured for warning and up if desired.

The third function is provided for lazy users (most of us) to call both of the previously described functions in the necessary order to fully configure logging in one step