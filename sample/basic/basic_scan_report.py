import os
import sys

from dxlbootstrap.util import MessageUtils
from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient

root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_dir + "/../..")
sys.path.append(root_dir + "/..")

from dxlnmapclient.client import NmapClient
from dxlnmapclient.constants import DxlNmapOptions

# Import common logging and configuration
from common import *

# Configure local logger
logging.getLogger().setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

# Create DXL configuration from file
config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE)

# Define elements to be analysed
target_1 = 'host_1'
target_2 = 'host_2'
target_list = [target_1, target_2]

# Define options to execute the tool
option = DxlNmapOptions.AGGRESSIVE_SCAN_OP_SYSTEM

# Create the client
with DxlClient(config) as dxl_client:
    # Connect to the fabric
    dxl_client.connect()

    logger.info("Connected to DXL fabric.")

    # Create client wrapper
    client = NmapClient(dxl_client)

    # Invoke the scan report method
    resp_dict = client.scan_report(target_list, option)

    # Print out the response (convert dictionary to JSON for pretty
    # printing)
    print "Response:\n{0}".format(
        MessageUtils.dict_to_json(resp_dict, pretty_print=True))
