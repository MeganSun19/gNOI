# gNOI OS Install — Reference Client

A minimal Python reference client that performs **gNOI OS service**
`Install` + `Activate` against a network device — gRPC over TLS, with
OpenConfig `.proto` files compiled to Python stubs.

## About this release

This codebase was extracted, sanitized, and re-released in 2026 from
work originally done in **2024** as part of a 100+ engineer
multi-country backbone-engineering program. Within that program, this
script was used as a building block for device-lifecycle automation
and Ixia traffic-regression harnesses. The implementation has not
been refreshed since; treat it as a focused 2024 snapshot, not a
full-featured production client.

## What this is — and what it isn't

**Is**:
- A working reference for invoking the gNOI `OS.Install` streaming RPC
  from Python, including TLS channel setup, metadata-based auth, and
  chunked file transfer.
- A pre-compiled OpenConfig proto stub set so you can extend the same
  pattern to other gNOI / gNMI / bootz / gNSI RPCs without re-running
  `grpc_tools.protoc` from scratch.

**Isn't**:
- A general-purpose multi-RPC gNOI client.
- A managed orchestration layer (no retries, no resumability, no
  pre/post state assertions baked in).

## Repository contents

```
.
├── os_install.py               # Reference client: OS Install + Activate
└── protos/
    └── github.com/openconfig/  # Compiled stubs for:
        ├── gnoi/{os, file, bootconfig, common, types}
        ├── gnmi/{proto/gnmi, proto/gnmi_ext}
        ├── bootz/proto
        └── gnsi/{authz, certz, credentialz, pathz}
```

## What `os_install.py` does

1. Builds a gRPC secure channel: TLS root CA + per-request username /
   password metadata via `AuthMetadataPlugin`.
2. Streams a local firmware image (e.g. `.iso`) to the device's
   `OS.Install` RPC in 64 KB chunks, framed by `TransferRequest` →
   `TransferContent` (n chunks) → `TransferEnd`.
3. Iterates the response stream and prints progress; surfaces gRPC
   error code + debug string on failure.

## Prerequisites

- Python 3.9+
- `grpcio`, `grpcio-tools`, `protobuf`
- A reachable device with the gNOI service enabled
- Root CA certificate (`CA.cer`) trusted for the device's gNOI port
- Device hostname matching the cert CN (or override via
  `grpc.ssl_target_name_override`)

## Quick Start

```bash
pip install grpcio grpcio-tools protobuf

# Edit os_install.py with your target IP, port, version, package path,
# and credentials, then:
python os_install.py
```

The pre-compiled stubs live under `protos/`, so no `protoc` step is
needed unless you regenerate from upstream `.proto` files.

## Extending to other RPCs

The pattern is identical for any other gNOI / gNMI service. For
example, to add `File.Get`:

```python
from github.com.openconfig.gnoi.file import file_pb2, file_pb2_grpc

stub = file_pb2_grpc.FileStub(channel)
for chunk in stub.Get(file_pb2.GetRequest(remote_file="/disk0:/show_tech.tgz")):
    ...
```

The corresponding stubs are already shipped under `protos/` for
`file`, `bootconfig`, `gnmi`, `bootz`, and the `gnsi` services
(`authz`, `certz`, `credentialz`, `pathz`).

## Production considerations

When wiring this into a real lifecycle pipeline:

- **Cert lifecycle** — gNOI on most platforms requires per-device cert
  provisioning; pair with the gNOI `Cert` flow (or whichever PKI you
  run) before driving Install.
- **Backpressure** — streaming uploads can saturate the management
  plane; pace chunks and watch for queue buildup on the receiver.
- **Idempotency** — wrap mutating operations (`Install`, `Activate`,
  `Reboot`) with pre/post state checks so retries are safe.
- **Auth** — the example uses TLS + username/password metadata; some
  platforms additionally require AAA gating on the gRPC layer.

## Limitations

- Single-RPC reference; no batching, retry, or circuit-breaker.
- Streaming flow has no resumability or per-chunk checksum.
- Hard-coded variables in `__main__` for clarity — wire your own
  config layer when embedding.

## References

- [OpenConfig gNOI](https://github.com/openconfig/gnoi)
- [OpenConfig gNMI](https://github.com/openconfig/gnmi)
- [gRPC Python](https://grpc.io/docs/languages/python/)
- [Cisco IOS-XR Programmability Configuration Guide](https://www.cisco.com/c/en/us/support/ios-nx-os-software/ios-xr-software/products-installation-and-configuration-guides-list.html)

## License

[MIT](LICENSE)
