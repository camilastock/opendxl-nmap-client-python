Overview
========

The OpenDXL Nmap Client Python exposes access to the `Nmap Security Scanner <https://nmap.org/docs.html/>`_
via the `Data Exchange Layer <http://www.mcafee.com/us/solutions/data-exchange-layer.aspx>`_ (DXL) fabric.

The purpose of this library is to allow users to access the Nmap tool utility for network discovery and
security auditing without having to focus on lower-level details such as Nmap-specific DXL topics and
message formats.

The :class:`dxlnmapclient.client.DxlNmapClient` class wraps the connection to the DXL fabric and is used to
access the Nmap tool integration.

This client requires an OpenDXL Nmap service to be running and available on the DXL fabric.

A Python-based implementation of an OpenDXL Nmap service is available here:
* `OpenDXL Nmap Python Service <https://github-lvs.corpzone.internalzone.com/detect/opendxl-nmap-service-python>`_

