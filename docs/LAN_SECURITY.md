# Local network / 局域网安全

The desktop host serves the order system to authorized users on a trusted private network. The tested LAN configuration uses **unencrypted HTTP**, so access is restricted to the local network. It is **not suitable for public Wi-Fi or direct Internet exposure**.

- Never configure router port forwarding, public DNS routing or direct WAN exposure for the HTTP port.
- Restrict host firewall rules to the trusted private network; use different accounts/roles for front desk and kitchen.
- Keep the host awake and online during service. Shutting down or completely exiting the host app interrupts phone/tablet access.
- When changing Wi-Fi, closing or restarting the app, make sure no order is being submitted, and verify synchronization after reconnecting.
- Do not upload backup ZIPs or signed-license material to public repositories or support tickets.

A production environment that needs remote access or untrusted networks requires additional security engineering, including HTTPS/TLS and access-control review.
