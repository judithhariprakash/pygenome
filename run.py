import sys

project_home = u'/home/parashar/pygenome_project/'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from pygenome import app

if __name__== "__main__":
    app.run()