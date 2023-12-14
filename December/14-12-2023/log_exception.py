import logging
logging.basicConfig(filename='logexcept.log', format='%(asctime)s,%(name)s:%(levelname)s:%(message)s:%(process)s:%(lineno)s')

# try:
#     age=int(input("Enter your age"))

# except Exception as obj:
#     # print(obj)
#     # logging.error(obj) 
#     # logging.error("Exception Information",exc_info=True) #This will enter the entire traceback for the error or do bellow

#     logging.exception("Exception Information:")


class AccessDenied(Exception):
    pass

try:
    age = int(input("Enter your age"))
    if age<18:
        raise AccessDenied("Acess Denied")
    logging.info(f"User of age {age} has logged in")

except Exception as obj:
    logging.exception("Exception Occurred")
