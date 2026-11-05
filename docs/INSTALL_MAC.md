# macOS installation (future Developer ID + notarized build)

> **No notarized public macOS build is available yet.** Owner functional acceptance on a development Mac is not equivalent to a distributable production release.

1. Obtain the signed and notarized official DMG/ZIP from the authorized distributor and verify its checksum.
2. Open the DMG or extract the ZIP, install the complete App in Applications, then launch it. Do not extract embedded executables out of the App bundle.
3. Complete offline activation and first-time administrator setup on the host Mac. Keep setup codes and license JSON private.
4. Explicitly enable trusted LAN access when needed; connect phones/tablets on the same private Wi-Fi. Do not expose this HTTP service to the Internet.
5. Back up from within the POS; quit the service before upgrading and verify data/authorization persist after relaunch.

The application and its SQLite data are separate. Some builds use `~/RestaurantPOSData`, while earlier testing used an isolated sandbox directory; do **not** rename or manually merge data directories without a verified migration/restore procedure.
