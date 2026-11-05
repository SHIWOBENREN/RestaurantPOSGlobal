# Data and privacy information / 数据与隐私说明

This page describes the observed local-first architecture, **not a completed GDPR/privacy-law compliance certification or a comprehensive legal privacy notice**.

- Restaurant order/menu/administrator records are stored in a local database belonging to the operator, separate from the application package.
- Backups can contain sensitive business information and license state; they should be encrypted or stored securely, not shared publicly.
- LAN-connected devices communicate with the local host. The current tested HTTP mode is unencrypted and should only be used on trusted Wi-Fi.
- GitHub is used for product information and developer CI, **not** as the production store for restaurant/customer databases.
- Deletion and retention, telemetry (if any), payment-related data, legal data-controller duties and end-user rights must be audited and documented by the distributor and restaurant operator before a consumer release.

Never attach real database contents, order exports, passwords, installation IDs or licenses in public GitHub Issues.
