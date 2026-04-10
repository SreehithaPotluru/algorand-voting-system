print("Welcome to CertiChain - Algorand Certificate Verification System")

def issue_certificate(name, course):
    print(f"Certificate issued to {name} for {course}")

def verify_certificate(cert_id):
    print(f"Verifying certificate ID: {cert_id}")

# Example
issue_certificate("Sreehitha", "Blockchain Basics")
verify_certificate("CERT123")
