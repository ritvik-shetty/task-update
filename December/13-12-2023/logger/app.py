from flask import Flask
import logging

app=Flask(__name__)

# DEBUG, INFO , WARNING , ERROR, CRITICAL

log_level=logging.DEBUG
log_file='app.log'
log_file_mode='a'
log_format='%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=log_level, filename=log_file, filemode=log_file_mode, format=log_format)


@app.route('/')
def index():
    app.logger.info("User visited the index page")
    app.logger.error("Error Found")
    return "Helllooo"




if __name__=='__main__':
    app.run(debug=True)