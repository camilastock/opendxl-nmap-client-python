class DxlNmapOptions:
    """
    Constants that are used to execute Nmap tool
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

    """
    AGGRESSIVE_SCAN = "-A"
    OPERATING_SYSTEM = "-O"
    AGGRESSIVE_SCAN_OP_SYSTEM = "-O -A"
