Basic Scan Host Report Example
==============================

This sample invokes and displays the results of an aggressive Nmap scan with the corresponding operating system where this execution is being performed
by invoking the Nmap service via DXL

For more information see:
    https://nmap.org

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The OpenDXL Nmap service is running and available on the DXL fabric (see `OpenDXL Nmap Service Python <https://github.com/camilastock/opendxl-nmap-service-python>`_)

Setup
*****

Modify the example to include the targets and options in the file you want to scan.

For example:

    .. code-block:: python

        # Define elements to be analysed
        target_1 = '200.17.2.2'
        target_2 = '200.17.2.3'
        target_list = [target_1, target_2]

        # Define options to execute the tool
        option = NmapOptions.AGGRESSIVE_SCAN_OP_SYSTEM

Where `"target_#"` parameter represent the element to be analysed and `"option"`is the parameter to
execute Nmap tool
There are different options:

    +-------------+---------+----------------------------------------------------------+
    | Option      | Command | Description                                              |
    +=============+=========+==========================================================+
    | Aggressive  | -A      | Aggressive Scan                                          |
    | Scan        |         |                                                          |
    +-------------+---------+----------------------------------------------------------+
    | Operating   | -O      | Operating system in the current host                     |
    | System      |         |                                                          |
    +-------------+---------+----------------------------------------------------------+
    | Aggressive  | -O - A  | Both options                                             |
    | Scan        |         |                                                          |
    | +           |         |                                                          |
    | Operating   |         |                                                          |
    | System      |         |                                                          |
    +-------------+---------+----------------------------------------------------------+

You can look for more information about Nmap tool in `Nmap page <https://nmap.org/book/man-briefoptions.html>`_

Running
*******

To run this sample execute the ``sample/basic/basic_scan_report.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_scan_report.py

The output should be similar to the following:

    .. code-block:: python

        Response for nmapservice_requesthandler:

        Response:
        {
            "100": "------------------------------------------",
            "101": "Nmap scan report for 10.87.242.195. Host is up",
            "102": "Operative System: Linux",
            "103": "PORT:    22/tcp STATE: open SERVICE: ssh",
            "104": "------------------------------------------"
        }


Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

            # Create the client
            with DxlClient(config) as dxl_client:

                # Connect to the fabric
                dxl_client.connect()

                logger.info("Connected to DXL fabric.")

                # Create client wrapper
                client = DXLNmapClient(dxl_client)

                # Invoke the aggressive scan method
                resp_dict = client.scan_report(option)

                # Print out the response (convert dictionary to JSON for pretty
                # printing)
                print "Response:\n{0}".format(
                    MessageUtils.dict_to_json(resp_dict, pretty_print=True))

Once a connection is established to the DXL fabric, a :class:`dxlnmapclient.client.DXLNmapClient` instance is
created which will be used to invoke remote commands on the OpenDXL Nmap Service.

Next, the :func:`dxlnmapclient.client.DXLNmapClient.scan_report` method is invoked with the target to
be scanned and report it.

The final step is to display the contents of the returned dictionary (``dict``) which contains the results of the scan report.
