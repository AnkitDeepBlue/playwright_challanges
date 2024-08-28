
# Playwright Challenges 🚀

![GitHub Workflow Status](https://github.com/AnkitDeepBlue/playwright_challanges)

## Overview

**Playwright Challenges** is a project designed to automate web UI testing using Playwright and pytest, with CI/CD integration via GitHub Actions. The project also includes dynamic reporting using Allure, and the final test reports are deployed automatically to Netlify.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To get started with the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AnkitDeepBlue/playwright_challenges.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd playwright_challenges
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**

   ```bash
   playwright install
   ```

## Usage

To run the tests locally and generate the Allure report:

1. **Run the tests:**

   ```bash
   pytest --alluredir=allure-results
   ```

2. **Generate the Allure HTML report:**

   ```bash
   allure generate allure-results --clean -o allure-report
   ```

3. **Serve the Allure report:**

   ```bash
   allure open allure-report
   ```

## Running Tests

Tests can be run dynamically via GitHub Actions. You can manually trigger test runs with specific pytest markers from the GitHub Actions tab.

To run the tests with a specific marker:

```bash
pytest -m <marker_name> --alluredir=allure-results
```

For example, to run the smoke tests:

```bash
pytest -m smoke --alluredir=allure-results
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the repository.**
2. **Create a new branch:**

   ```bash
   git checkout -b feature-branch
   ```

3. **Make your changes.**
4. **Commit your changes:**

   ```bash
   git commit -m 'Add some feature'
   ```

5. **Push to the branch:**

   ```bash
   git push origin feature-branch
   ```

6. **Open a pull request.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Created by [Ankit Tripathi]
