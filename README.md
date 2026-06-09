# shipfast-api

Demo project for **Production Grade CI/CD with GitHub Actions** training.

Used across all 10 sessions — built incrementally each day.

## Repository Structure

```
shipfast-api/
├── apps/
│   ├── python/          ← Python app (primary demo — Days 2–7)
│   │   ├── calculator.py
│   │   ├── requirements.txt
│   │   ├── pytest.ini
│   │   ├── .flake8
│   │   └── tests/
│   │       └── test_calculator.py
│   └── node/            ← Node.js app (path-filter demo — Days 2, 10)
│       ├── src/
│       │   └── utils.js
│       ├── __tests__/
│       │   └── utils.test.js
│       ├── package.json
│       └── .eslintrc.json
└── .github/
    └── workflows/
        ├── ci-python.yml       ← Python CI: lint + test + build-check
        ├── ci-node.yml         ← Node CI: lint + test + build-check
        ├── cd.yml              ← CD: triggered by workflow_run
        ├── manual-dispatch.yml ← workflow_dispatch demo
        └── nightly.yml         ← schedule demo

```

## Running Locally

### Python

```bash
cd apps/python
pip install -r requirements.txt
flake8 . --config .flake8
pytest tests/ -v
```

### Node.js

```bash
cd apps/node
npm install
npm run lint
npm test
```

## Training Sessions

| Day | Topic | What gets added |
|-----|-------|-----------------|
| 1 | Architecture | Repo created, first workflow traced |
| 2 | Events & Triggers | ci-python.yml, ci-node.yml, path filters live |
| 3 | Workflow Architecture | Workflows split and restructured |
| 4 | CI Pipeline | Full CI stages with SonarQube |
| 5 | Artifacts & JFrog | Build artifacts stored in JFrog |
| 6 | Caching & CD | pip/npm cache + deploy to AWS EC2 |
| 7 | Security & OIDC | OIDC auth, least-privilege tokens |
| 8 | Environments & Docker | Docker image, approval gates |
| 9 | Scale & Terraform | Matrix, reusable workflows, Terraform |
| 10 | Capstone | Full end-to-end pipeline live run |
