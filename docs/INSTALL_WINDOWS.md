# Windows installation (future signed production build)

> **No production Windows installer is available yet.** These are intended steps for a future tested and signed delivery, not instructions to deploy the V1.2.6 unsigned QA build in a restaurant.

1. Obtain the official Windows x64 installer or ZIP from the authorized distributor and verify its published SHA256 and Authenticode signature.
2. If it is a ZIP distribution, extract the **entire folder**. Do not copy `RestaurantPOSGlobal.Desktop.exe` without the accompanying `Engine` folder.
3. Ensure Microsoft Edge **WebView2 Evergreen Runtime** is available; the final installer should detect or document it. A customer does **not** need the Python SDK or .NET development SDK.
4. Open the desktop app on the host computer, follow the local offline-activation guidance, and then create the restaurant administrator on **that host**. Never publish or forward passwords or first-run setup codes.
5. If needed, enable access only on a trusted private Wi-Fi/LAN through the app. Never enable public network access or port forwarding. Complete firewall rules only for private networks.
6. Store backups separately. Exit the running POS cleanly before upgrades, and verify old orders and license identity after restarting.

The program stores its database outside the application folder (commonly `%LOCALAPPDATA%\RestaurantPOSGlobal`; legacy locations can differ). It does not automatically migrate databases across computers or synchronize data through GitHub.
