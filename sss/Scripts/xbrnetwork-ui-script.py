#!C:\WebD\Django\eg\sss\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'autobahn==22.7.1','console_scripts','xbrnetwork-ui'
__requires__ = 'autobahn==22.7.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('autobahn==22.7.1', 'console_scripts', 'xbrnetwork-ui')()
    )
