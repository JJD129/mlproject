# End-to-End Machine Learning Project

This repository contains an end-to-end machine learning project, including data preprocessing, model training, and deployment on AWS.

## Project Structure
- `.github/workflows/`: Contains GitHub Actions workflows for CI/CD.
- `notebook/`: Jupyter notebooks for data exploration and model development.
- `src/`: Source code for data processing and model training.
- `templates/`: HTML templates for the web application.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `Dockerfile`: Instructions to build the Docker image for the project.
- `README.md`: This file.
- `app.py`: Flask application for model inference.
- `requirements.txt`: Lists Python dependencies.
- `setup.py`: Script for packaging the project.

## Getting Started
### Prerequisites
Python 3.8 or higher
Docker
AWS account (for deployment)

### Installation
1. Clone the repository:
```
git clone https://github.com/JJD129/mlproject.git
cd mlproject
```
2. Install the required Python packages:
```
pip install -r requirements.txt
```
### Usage
1. Run the Flask application locally:
```
python app.py
```
2. Access the application at http://localhost:8000.

### Deployment
To deploy the application on AWS:

1. Build the Docker image:
```
docker build -t mlproject .
```
2. Tag and push the image to Amazon Elastic Container Registry (ECR).
3. Deploy the image using Amazon Elastic Container Service (ECS) or another AWS service.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.