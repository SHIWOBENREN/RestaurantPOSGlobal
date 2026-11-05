# Features and limitations / 功能与限制

| Category | Intended behavior | Validation note |
|---|---|---|
| Front desk | Manual order entry, menu and category management | Owner-accepted on macOS V1.2.5 |
| Kitchen | Order queue and completion updates | Owner-accepted on macOS V1.2.5 |
| Reports | Sales, channels and payment summaries | Owner-accepted on macOS V1.2.5 |
| LAN | iPhone/iPad browser connects to running desktop host | Tested on trusted LAN with Mac host; use HTTP privately only |
| Data | Local SQLite database and isolated backups | Owner tested backups and isolated restore on Mac |
| License | Signed installation-bound offline activation | Owner tested Mac; complete Windows activation E2E outstanding |
| Windows | WinForms host with WebView2 and Python engine | CI build, backend launch, main-window existence only |
| Localization | Configurable country, currencies and language | Verify each language/currency combination before use |

**Not validated or provided as certified features:** payment gateway processing, fiscal receipt/facturering compliance, automatic delivery-platform API integration, printer/cash drawer/barcode-device compatibility, Internet-facing HTTPS hosting, iOS native App Store distribution, Windows 10/11 clean-install full acceptance.

The desktop host must be powered on and running for LAN-connected devices to work. SQLite is local; this is not multi-location, always-on cloud synchronization.
