from logging import LogRecord
from flask import Flask,request,has_request_context
import logging
from logging.handlers import RotatingFileHandler


mylogs = logging.getLogger(__name__)
mylogs.setLevel(logging.DEBUG)

stream = logging.StreamHandler()
stream.setLevel(logging.INFO)
streamformat = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
stream.setFormatter(streamformat)
mylogs.addHandler(stream)


# class NewFormatter(logging.Formatter):
#     def format(self, record):
#         if has_request_context:
#             record.url=request.url
#             record.remote=request.remote_addr
#             return super().format(record)
#         else:
#             record.url=None
#             record.remote=None

# logFormatter=NewFormatter("%(asctime)s - %(url)s - %(remote)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H-%M:%S")

# # DEBUG, INFO , WARNING , ERROR, CRITICAL
# log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format=log_format)

app=Flask(__name__)



@app.route('/')
def index():
    mylogs.info("User visited the index page")
    return "Helllooo"


if __name__=='__main__':
    app.run(debug=True)