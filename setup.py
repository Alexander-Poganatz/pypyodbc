try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='snekodbc',
    version="0.5.0",
    description='A Pure Python ctypes ODBC module.',
    author='Alexander-Poganatz',
    author_email='alex.poga@outlook.com',
    url='https://github.com/Alexander-Poganatz/snekodbc',
    py_modules=['snekodbc'],
    long_description="A Pure Python ctypes ODBC module compatible with PyPy",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
    ],
    keywords='Python, Database, Interface, ODBC, PyPy',
    license='MIT',
)
