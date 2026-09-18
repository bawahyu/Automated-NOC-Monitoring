# Automated NOC Infrastructure Audit Tool

This containerized Python solution performs scheduled audits on critical NOC servers to replace manual log extraction, ensuring operational high-availability.

### System Architecture & OSI Focus
The system architecture and testing methods are designed with a strict focus on standard network layers:

*   **Layer 3 (Network):** Confirms network-level connectivity via automated ICMP Ping checks to specified critical server IPs.
*   **Layer 7 (Application):** Verifies the application service availability and extracts server error logs via HTTP Requests.

### Pre-requisites
This tool is containerized using **Docker**, ensuring consistency and zero-dependency issues. You will need Docker installed to execute the audit script.

### How to Run
To perform an automated audit, execute the following command in your terminal. This command mounts a `logs` directory to save the output CSV report to your host machine.

```bash
docker run -v "$(pwd)/logs:/app/logs" Automated-NOC-Monitoring:latest
