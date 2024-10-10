import inspect
import logging
import pytest


@pytest.mark.Usefixtures("setup")
class BaseClass:

    def getLogger(self):

        #Step 6: This method gives name of the method from which this getLogger utility called
        loggerName = inspect.stack()[1][3]

        # step 1: Create object for logging, loggerName is to catch file name from which test case is running
        logger = logging.getLogger(loggerName)

        # Step2: filehandler gives file location
        filehandler = logging.FileHandler('logfile.log')

        # step 4: How to print format customized
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        # Step 3: Need to pass filehandler object into addHandler
        # In what file, what format log should print is sent in addHandler method
        logger.addHandler(filehandler)

        # Step 5: Set level from which log will print
        logger.setLevel(logging.DEBUG)
        return logger

