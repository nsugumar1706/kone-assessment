# kone-assessment
This is kone assessment repo
# CI/CD Blueprint Framework

This project demonstrates a modular CI/CD framework that dynamically generates pipelines based on a `blueprint.yml` file. It supports multiple languages (Python, Java), build tools (pip, Maven), and deployment methods (Docker, CDK, CloudFormation).

## How It Works

1. Modify `blueprint.yml` to define your project's tech stack.
2. Run `python generate_pipeline.py`.
3. A `.gitlab-ci.yml` pipeline will be generated based on the blueprint.

## Run Example

```bash
python generate_pipeline.py
