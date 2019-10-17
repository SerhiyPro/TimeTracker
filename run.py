import sys
from app.os_factory import OsFactory


if __name__ == '__main__':
    os_f = OsFactory()
    try:
        os_f.run()
    except KeyboardInterrupt:
        sys.exit()

