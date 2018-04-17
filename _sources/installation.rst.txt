Library Installation
====================

Prerequisites
*************

* OpenDXL Python Client library installed
   `<https://github.com/opendxl/opendxl-client-python>`_

* The OpenDXL Python Client prerequisites must be satisfied
   `<https://opendxl.github.io/opendxl-client-python/pydoc/installation.html>`_

* Python 2.7.9 or higher installed within a Windows or Linux environment
    (Python 3 is not supported at this time)

* Python-libnmap installed within a Windows or Linux environment
    .. parsed-literal::

        pip install python-libnmap

   You can look for more information in `<https://pypi.python.org/pypi/python-libnmap>_`

Installation
************

Use ``pip`` to automatically install the library:

    .. parsed-literal::

        pip install dxlnmapclient-\ |version|\-py2.7-none-any.whl

Or with:

    .. parsed-literal::

        pip install dxlnmapclient-\ |version|\.zip

As an alternative (without PIP), unpack the dxlnmapclient-\ |version|\.zip (located in the lib folder) and run the setup
script:

    .. parsed-literal::

        python setup.py install
