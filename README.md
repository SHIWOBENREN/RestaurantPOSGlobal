# Restaurant POS Global

**Local-first restaurant ordering and kitchen management for macOS and Windows.**  
[简体中文](README.zh-CN.md) · [Product features](docs/FEATURES.md) · [Release status](docs/RELEASE_STATUS.md) · [Security](SECURITY.md)

> **Development / release-preparation status (updated 2026-11-05).** No consumer-ready public installer is available in this repository today. Do not treat an unsigned QA build as an official commercial release.

Restaurant POS Global is a commercial, closed-source point-of-sale **order-management** application designed for smaller restaurants. It uses a local desktop host and a browser-based interface for staff and other devices on a trusted private network.

## Main capabilities

- Front desk: create and manage orders and menu items.
- Kitchen: view orders and mark them complete.
- Reporting: review sales and channel/payment summaries.
- Local-first storage: restaurant information is kept in a local SQLite data directory.
- Offline license activation: installation-bound signed licenses, issued separately by the seller.
- Private LAN access: a phone or tablet can connect to the desktop host on the **same trusted network**, while the host remains running.
- Configurable language, regional and currency options. Availability and translation quality may differ by build.

## Platform status

| Platform | Verified so far | Public release |
|---|---|---|
| macOS (Apple Silicon, V1.2.5) | Owner's functional acceptance: desktop UI, POS/kitchen/report, LAN phone ordering, backup/restart persistence | **Not yet**: Developer ID signing, notarization and clean-machine distribution checks remain |
| Windows x64 (V1.2.6 QA) | Windows CI build, backend HTTP start, ZIP hashes, desktop process and main-window creation | **Not yet**: interactive WebView2, offline-license flow, clean Windows 10/11 installs and signing remain |
| iPhone/iPad | Browser access to a running desktop host on a trusted LAN, tested with the macOS host | Not a native App Store application |

See [verified vs. unverified claims](docs/RELEASE_STATUS.md) before making purchase decisions.

## What this product does *not* currently promise

Restaurant POS Global is **not** certified fiscal cash-register software, a tax-invoice issuer, or an integrated payment processor. Order entry and third-party delivery channels are managed manually; do not assume automatic delivery-platform API integrations, receipt-printer certification, or compliance with specific local fiscalization rules. LAN traffic in the tested configuration uses unencrypted HTTP; never expose it directly to the public Internet.

## Downloads and licensing

There is **no public production installer yet**. When a release passes the published [release gate](docs/RELEASE_STATUS.md), vetted distribution links and checksums will appear under GitHub **Releases** or be delivered privately to licensed customers. If a paid installer is supplied privately, a GitHub release may contain only product information and change notes.

A commercial license, where offered, will be provided by the seller; do not interpret these documentation pages as a grant of a software license or a confirmed price, refund policy or support term. See [license notice](LICENSE_NOTICE.md).

## Documentation

- [Features and limitations](docs/FEATURES.md)
- [Windows installation — only after signed release](docs/INSTALL_WINDOWS.md)
- [Mac installation — only after notarized release](docs/INSTALL_MAC.md)
- [LAN and data security](docs/LAN_SECURITY.md)
- [Local data and privacy notes](docs/DATA_AND_PRIVACY.md)
- [FAQ](docs/FAQ.md)
- [Support](SUPPORT.md) and [Security reporting](SECURITY.md)

**Repository policy:** This public repository contains product documents only. Application source code, license-signing private keys, customer databases, QA artifacts and unsigned executables stay outside it.
