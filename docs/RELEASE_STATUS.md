# Public release gate / 正式公开发布条件

**As of 2026-11-05: NOT RELEASE READY.** No consumer ZIP/DMG/EXE should be called an official production version yet.

## Windows x64 V1.2.6

- [x] CI compiler and packaging pipeline succeeded on Windows Server 2022.
- [x] Packaged backend responded over local HTTP.
- [x] ZIP hashes and file inventory checked.
- [x] Desktop process started and main window existed.
- [ ] WebView2 UI visibly renders and supports interaction on real consumer Windows 10/11.
- [ ] Legitimate offline activation, menu/order/kitchen/report/backup end-to-end acceptance.
- [ ] Install/upgrade/uninstall/restart on clean and non-admin Windows accounts.
- [ ] Windows private-LAN/firewall behavior and disconnected-device handling.
- [ ] Code signing and verification; no test/customer data or unnecessary debug symbols.
- [ ] Third-party licenses, commercial EULA, privacy and support terms finalized.

## macOS V1.2.5

- [x] Owner's functional acceptance on one Apple Silicon Mac, including LAN and data persistence.
- [ ] Final Developer ID code signing, hardened runtime and Apple notarization/stapling.
- [ ] Independent clean installation and Gatekeeper verification on another supported Mac.
- [ ] Commercial EULA, third-party notices, privacy and support terms finalized.

**Note:** GitHub Releases may be used for vetted binary assets, or only for release notes with a private licensed download flow. An unsigned QA asset must never be marked production/stable.
