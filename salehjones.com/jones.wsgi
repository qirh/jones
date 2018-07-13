#!/var/www/jones/salehjones.com/venv/bin/python
import sys
import os
import logging

PROJECT_DIR = "/var/www/jones/salehjones.com"

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, PROJECT_DIR)

activate_this = os.path.join(PROJECT_DIR, 'venv', 'bin', 'activate_this.py')
exec(open(activate_this, "rb").read(), dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from downing import app as application
application.secret_key = "NonJeNelxxxxxadihfihasasflhfkaaaaaalsaklfshaRegretteRien"
