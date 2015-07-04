import sys
import os

project_home = os.path.dirname(os.getcwd())
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from pygenome import app

if __name__== "__main__":
    app.run(debug=True)