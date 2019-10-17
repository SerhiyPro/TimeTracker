import sys
from app.osfactory import OsFactory


if __name__ == '__main__':
    os_f = OsFactory()
    try:
        os_f.run()
    except KeyboardInterrupt:
        sys.exit()

