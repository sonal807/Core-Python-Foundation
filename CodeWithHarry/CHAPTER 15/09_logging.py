#Logging: Logging is the process of recording information about what a program is doing,
# including normal operations, warnings, errors, and important events.
#In pyhton logging is a built-in python module, we just simple import it.

#Basic example:
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Apllication started")
logging.warning("This is warning")
logging.error("Something went wrong")

#Logging has commonly used level
# DEBUG → detailed information for debugging
# INFO → normal application activity
# WARNING → something unexpected, but application can continue
# ERROR → an operation failed
# CRITICAL → very serious failure

#Example:
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Chatbot started")
logging.info("User query received")
logging.warning("Response is taking longer")
logging.error("API request failed")

#Example
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logging.info("User logged in")
logging.info("Balance checked")
logging.info("₹5,000 transfer initiated")
logging.info("Transaction successful")
logging.warning("Wrong OTP entered")
logging.warning("Wrong OTP entered")
logging.error("Account temporarily locked")

#File logging
import logging

logging.basicConfig(
    filename="bank.log",    #it will create a file named bank.log in same folder
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logging.info("User logged in")
logging.info("Balance checked")
logging.info("₹5,000 transfer initiated")
logging.info("Transaction successful")
logging.warning("Wrong OTP entered")
logging.error("Account temporarily locked")