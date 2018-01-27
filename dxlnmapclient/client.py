import logging

from dxlclient.message import Request
from dxlbootstrap.util import MessageUtils
from dxlbootstrap.client import Client
from constants import DxlNmapOptions

# Configure local logger
logging.getLogger().setLevel(logging.ERROR)
logger = logging.getLogger(__name__)


class NmapClient(Client):
    """
    The Nmap DXL Client provides a high level wrapper for invoking the Nmap
    tool via (DXL) fabric.
    """

    #: The DXL Nmap service type for the Nmap tool
    SERVICE_TYPE = "/opendxl-nmap/service"

    #: Scan report request
    _REQ_SCAN = "{0}/scan/report".format(SERVICE_TYPE)

    #: The target IP required
    _TARGET = "target"

    #: The required option to execute Nmap
    _OPTION = "option"

    #: The default timeout value related to the DXL sync requests
    _DEFAULT_SYNC_REQUEST_TIMEOUT = 300

    def __init__(self, dxl_client):
        """
        Constructor parameters:

        :param dxl_client: The DXL client to use for communication with the
        fabric
        """
        super(NmapClient, self).__init__(dxl_client)

    @staticmethod
    def _add_target_param(req_dict, param_value):
        """
        Adds the specified target parameter to the dictionary

        :param req_dict: The dictionary
        :param param_value: The value for the parameter
        """
        if isinstance(param_value, list):
            req_dict[NmapClient._TARGET] = param_value
        else:
            logger.warning("Type invalid in target parameter")

    @staticmethod
    def _add_option_param(req_dict, option_value):
        """
        Adds the specified option parameter to the dictionary

        :param req_dict: The dictionary
        :param option_value: Option to execute Nmap tool
        """
        if option_value != str:
            new_op_value = str(option_value)
            req_dict[NmapClient._OPTION] = new_op_value
        else:
            logger.warning("Type invalid in option parameter")

    def _invoke_service(self, req_dict, topic):
        """
        Invokes the DXL Nmap service.

        :param req_dict: Dictionary containing request information
        :param topic: The Nmap DXL topic to invoke
        :return: A dictionary containing the response
        """
        # Create the DXL request message
        request = Request(topic)

        # Set the payload on the request message (Python dictionary to JSON
        # payload)
        MessageUtils.dict_to_json_payload(request, req_dict)

        # Perform a synchronous DXL request
        response = self._dxl_sync_request(request)

        # Convert the JSON payload in the DXL response message to a Python
        # dictionary and return it.
        return MessageUtils.json_payload_to_dict(response)

    def scan_report(self, target_list, option_value, timeout=_DEFAULT_SYNC_REQUEST_TIMEOUT):
        """
        Invokes the service "/opendxl-nmap/service" that expose the
        "/opendxl-nmap/service/scan/report" topic

        :param target_list: Elements to be analysed
        :param option_value: Nmap tool option
        :param timeout: DXL sync request timeout
        :return: service response
        """

        req_dict = {}

        # Adding targets parameters into a dictionary
        if target_list:
            self._add_target_param(req_dict, target_list)
        else:
            logging.warning("Targets list is empty")

        # Adding options parameters into a dictionary
        if option_value:
            self._add_option_param(req_dict, option_value)
        else:
            self._add_option_param(req_dict, DxlNmapOptions.AGGRESSIVE_SCAN_OP_SYSTEM)

        # Update the response timeout
        self.response_timeout = timeout

        return self._invoke_service(req_dict, self._REQ_SCAN)

