# Changelog / 更新日志

This document reports engineering milestones. **A version mentioned here is not necessarily a published consumer release.**

## 2026-11-05 — Windows 1.2.6 (internal QA, NOT a public release)

- Windows x64 CI build completed successfully.
- Packaged Python backend served a local HTTP endpoint in Windows CI.
- Archive CRC, 817 file hashes and x64 PE format validated for the original candidate ZIP.
- Native Windows desktop process started and a main window was detected.
- Subsequent internal QA copy removed the `.pdb` debug-symbol file without changing executable bytes.
- Interactive WebView2 operations, licensed transactions, clean install and signing **remain unverified**.

## 2026-11-04 — macOS 1.2.5 (owner-accepted QA, NOT a notarized public release)

- Owner verified desktop launch, preserved license/data, front/kitchen/reports, LAN iPhone synchronization, consistent backups and restart persistence.
- Developer ID signing, notarization and independent second-Mac install checks remain outstanding.

See [release readiness](docs/RELEASE_STATUS.md).
