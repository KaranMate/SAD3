# SAST Security Testing Practical

## Aim

To study Static Application Security Testing (SAST)
tools and implement GitHub CodeQL and Bandit to detect
security vulnerabilities in Python applications.

## Tools Used

1. GitHub
2. GitHub Actions
3. GitHub CodeQL
4. Bandit
5. Python

## Theory

Static Application Security Testing (SAST) is a
white-box testing technique used to identify security
vulnerabilities in source code without executing it.

SAST helps developers detect security weaknesses
during the software development life cycle.

## Types of Vulnerabilities

1. Hardcoded Password
2. Weak Cryptographic Algorithm
3. Command Injection

## Implementation

Step 1: Create a GitHub repository.

Step 2: Upload the vulnerable Python application.

Step 3: Upload the corrected Python application.

Step 4: Configure GitHub Actions workflow.

Step 5: Run Bandit and GitHub CodeQL.

Step 6: Analyze security reports.

Step 7: Compare vulnerable and corrected code.

## Observation

| Vulnerability | Before Fix | After Fix |
|---|---|---|
| Hardcoded Password | Present | Resolved |
| Weak Hashing | Present | Resolved |
| Unsafe Shell Execution | Present | Resolved |

## Expected Result

Bandit identifies security vulnerabilities in the
insecure application and verifies that the targeted
issues have been corrected in the fixed application.

## Conclusion

The SAST practical demonstrates how static analysis
tools identify insecure coding practices.

GitHub Actions automates security scanning using
Bandit and GitHub CodeQL.

Static analysis helps developers detect potential
vulnerabilities early in the development process.

SAST Security Testing
│
├── Bandit SAST Scan
│
│   ├── Checkout Repository
│   ├── Setup Python
│   ├── Install Bandit
│   ├── Scan Vulnerable Application
│   ├── Scan Fixed Application
│   └── Upload Security Reports
│
└── GitHub CodeQL Scan
    │
    ├── Checkout Repository
    ├── Initialize CodeQL
    └── Perform CodeQL Analysis
