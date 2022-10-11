# 0x13. Firewall

---
### [0. Block all incoming traffic but](./0-block_all_incoming_traffic_but)
* Let’s install the ufw firewall and setup a few rules on web-01.
* Configure ufw so that it blocks all incoming traffic, except the following TCP ports: 22 (SSH) 443 (HTTPS SSL) 80 (HTTP)

### [1. Port forwarding](./100-port_forwarding)
* Firewalls can not only filter requests, they can also forward them.
* Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.

---

## Author
* **Faruna Benjamin Adejo** - [BenFaruna](https://github.com/BenFaruna)
