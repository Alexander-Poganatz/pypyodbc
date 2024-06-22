
import os, sys, platform
from os.path import join, dirname, abspath, basename
import unittest


def print_library_info(cnxn):
    import snekodbc as pypyodbc
    print('python:  %s' % sys.version)
    print('pypyodbc:  %s %s' % (pypyodbc.version, os.path.abspath(pypyodbc.__file__)))
    print('odbc:    %s' % cnxn.getinfo(pypyodbc.SQL_ODBC_VER))
    print('driver:  %s %s' % (cnxn.getinfo(pypyodbc.SQL_DRIVER_NAME), cnxn.getinfo(pypyodbc.SQL_DRIVER_VER)))
    print('         supports ODBC version %s' % cnxn.getinfo(pypyodbc.SQL_DRIVER_ODBC_VER))
    print('os:      %s' % platform.system())
    print('unicode: Py_Unicode=%s SQLWCHAR=%s' % (pypyodbc.UNICODE_SIZE, pypyodbc.SQLWCHAR_SIZE))

    if platform.system() == 'Windows':
        print('         %s' % ' '.join([s for s in platform.win32_ver() if s]))



def load_tests(testclass, name, *args):
    """
    Returns a TestSuite for tests in `testclass`.

    name
      Optional test name if you only want to run 1 test.  If not provided all tests in `testclass` will be loaded.

    args
      Arguments for the test class constructor.  These will be passed after the test method name.
    """
    if name:
        if not name.startswith('test_'):
            name = 'test_%s' % name
        names = [ name ]

    else:
        names = [ method for method in dir(testclass) if method.startswith('test_') ]

    return unittest.TestSuite([ testclass(name, *args) for name in names ])


def load_setup_connection_string(section):
    """
    Attempts to read the default connection string from the setup.cfg file.

    If the file does not exist or if it exists but does not contain the connection string, None is returned.  If the
    file exists but cannot be parsed, an exception is raised.
    """
    from os.path import exists, join, dirname, splitext, basename
    from ConfigParser import SafeConfigParser
    
    FILENAME = 'setup.cfg'
    KEY      = 'connection-string'

    path = join(dirname(dirname(abspath(__file__))), 'tmp', FILENAME)

    if exists(path):
        try:
            p = SafeConfigParser()
            p.read(path)
        except:
            raise SystemExit('Unable to parse %s: %s' % (path, sys.exc_info()[1]))

        if p.has_option(section, KEY):
            return p.get(section, KEY)

    return None
