# os_install.py

A Python script for installing and activating OS packages on network devices using gRPC and gNOI OS services.

## Prerequisites

1. **Install Python and Required Libraries**  
   - Ensure Python 3.6 or later is installed.
   - Install the required libraries:
     pip install grpcio grpcio-tools protobuf

2. **Download the Required `.proto` Files**
   https://github.com/openconfig/gnoi/blob/main/os/os.proto#L408
   
   - Download the necessary `.proto` files, including `os.proto` and any dependencies (e.g., `common.proto`).
   - Ensure they match the version of gNOI implemented on your target device.

4. **Compile the `.proto` Files**  
   - Use `grpcio-tools` to generate Python gRPC and message classes:
     ```bash
     python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. os.proto
     ```
   - Repeat this step for all required `.proto` files.

5. **Set Up Credentials** (Optional, if using secure gRPC)  
   - Obtain the root CA certificate for the device and save it (e.g., `CA.cer`).
   - Update the `cert_cn` and certificate paths in the script as needed.
