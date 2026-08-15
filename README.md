![GDPR DevSecOps Pipeline](https://github.com/prekshya9/gdpr-devsecops-pipeline/actions/workflows/gdpr-pipeline.yml/badge.svg)

# GDPR Automated Compliance & DevSecOps Pipeline

An automated DevSecOps pipeline implementing **Policy-as-Code** to enforce **GDPR Article 25 (Data Protection by Design and by Default)** and **GDPR Article 32 (Security of Processing)** within a continuous integration (CI/CD) workflow.

---

## 📋 Regulatory Mapping

| GDPR Article | Requirement | Technical Control in Pipeline |
| :--- | :--- | :--- |
| **Article 25** | Privacy by Design & Default | Automated SAST inspection for unmasked PII (email, card data) on every commit. |
| **Article 32** | Security of Processing | Rejection of unencrypted sensitive data in stdout/logs to prevent unauthorized access. |

---

## 🛠️ Repository Components

* **`app.js`**: Node.js Express API handling user registration and sensitive data workflows.
* **`enforce_gdpr_policy.py`**: Custom Python compliance engine evaluating scan outputs against organizational privacy thresholds.
* **`.github/workflows/gdpr-pipeline.yml`**: GitHub Actions workflow orchestrating the scanning environment, artifact storage, and compliance gates.

---

## 🚀 How to Run Locally

### 1. Run the Python Policy Gate
```bash
python enforce_gdpr_policy.py bearer-report.json
```