# This Python code snippet is importing the `app` object from a module named `app` and the `config`
# module. It then checks if the script is being run as the main program using the `if __name__ ==
# '__main__':` condition. If it is the main program, it runs the Flask application using the
# `app.run()` method with the debug mode set based on the value of `config.debug`.
from app import app
import config

# if __name__ == '__main__':
#  app.run(debug=config.debug)    
def create_app():
   return app