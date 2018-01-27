class DxlNmapOptions:
    """
    Constants that are used to execute Nmap tool
    +------------+---------+----------------------------------------------------------+
    | Option     | Command | Description                                              |
    +============+=========+==========================================================+
    | Aggressive  |  -A     | Aggressive Scan                                          |
    | scan       |         |                                                          |
    +------------+---------+----------------------------------------------------------+
    | Operating  |  -O     | Operating system in the current host                     |
    | system     |         |                                                          |
    +------------+---------+----------------------------------------------------------+
    |Agress Scan | -O - A  | Both options                                             |
    |Operat sys  |         |                                                          |
    +------------+---------+----------------------------------------------------------+

    """
    AGGRESSIVE_SCAN = "-A"
    OPERATING_SYSTEM = "-O"
    AGGRESSIVE_SCAN_OP_SYSTEM = "-O -A"
