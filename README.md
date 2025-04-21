# 🐍 4-Week Python Automation Roadmap with Mini Projects

## 📅 Week 1: Python Refresh + API Basics

| Day | Focus |
|-----|-------|
| 1   | Python setup, virtual environments, pip |
| 2   | Python syntax refresh (loops, functions, exceptions) |
| 3   | JSON, file handling, dictionaries |
| 4   | Intro to REST APIs + tools like Postman |
| 5   | Using `requests` to send GET/POST/DELETE |
| 6   | Validate API responses (status code, headers, JSON) |
| 7   | Create your first API test case using `pytest` |

---

## 📅 Week 2: Deep API Automation + Reporting

| Day | Focus |
|-----|-------|
| 8   | API test structure using `pytest` (setup/teardown) |
| 9   | Parameterized tests, assertions |
| 10  | Validate JSON with `jsonschema` |
| 11  | Test real APIs (e.g. ReqRes, FakeStore) |
| 12  | Generate reports with `pytest-html` |
| 13  | (Optional) Mock API responses using `responses` |
| 14  | **Mini Project #1**: API Test Suite for Fake Store API |

---

## 📅 Week 3: Selenium UI Automation

| Day | Focus |
|-----|-------|
| 15  | Install `selenium`, setup browser driver (ChromeDriver) |
| 16  | Open browser, navigate, find elements |
| 17  | Interactions: click, type, scroll, screenshots |
| 18  | Waits (implicit/explicit), alerts, popups |
| 19  | Automate form filling or login |
| 20  | Run tests in headless mode |
| 21  | **Mini Project #2**: UI Login Automation on a demo site |

---

## 📅 Week 4: Playwright + Final Project

| Day | Focus |
|-----|-------|
| 22  | Install and setup Playwright for Python |
| 23  | Launch browser, interact with elements |
| 24  | Screenshots, videos, tracing |
| 25  | Structure automation using Page Object Model (POM) |
| 26  | Compare Selenium vs Playwright |
| 27  | Intro to CI/CD (GitHub Actions or Jenkins basics) |
| 28  | **Final Project**: Combine API + UI in one flow |

---

## 🛠️ Mini Projects Overview

### ✅ Project 1: API Test Suite – Fake Store API

- **Tools**: `requests`, `pytest`, `jsonschema`
- **Goal**:
  - Test GET/POST/DELETE product endpoints
  - Validate JSON response schema
  - Generate HTML report

---

### ✅ Project 2: UI Login Automation

- **Tools**: `selenium` or `playwright`
- **Goal**:
  - Automate login to a demo site
  - Validate successful login using assertions
  - Optional: run in headless mode, capture screenshots
- **Demo Site**: [Practice Test Automation](https://practicetestautomation.com/practice-test-login/)

---

### ✅ Final Project: Full Automation Flow

- **Tools**: `requests`, `playwright` or `selenium`
- **Goal**:
  - Use API to create a user or resource
  - Use UI to log in or interact with that data
  - Validate results via API
  - Generate test report
