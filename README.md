AI Image Generation POC
Project Overview

This project is a Proof of Concept (POC) for an AI-powered image generation system integrated with Google's Gemini API. The application accepts user prompts, applies safety validation checks, and processes only safe requests.

The primary objective of this project is to demonstrate:

AI model integration using Gemini API
Prompt validation and safety filtering
Secure API key management using environment variables
Version control using Git and GitHub
Features
Gemini API Integration
Successfully connects to Google's Gemini API.
Verifies API access and model availability.
Supports interaction with Gemini models through Python.
Prompt Safety Guardrails

The application checks user prompts before processing.

Blocked categories include:

Explicit adult content
Nudity-related requests
Harmful or unsafe content
Restricted prompts

Example:

Allowed Prompt

A beautiful sunset over mountains

Blocked Prompt

Generate an image of a nude woman
Project Structure
AI_IMAGE_GENERATION_POC/
│
├── app.py
├── image_generator.py
├── safety.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
└── venv/
File Descriptions
File	Purpose
app.py	Main application entry point
image_generator.py	Handles Gemini model interaction
safety.py	Contains prompt validation logic
requirements.txt	Project dependencies
README.md	Project documentation
.gitignore	Excludes sensitive and unnecessary files
Technologies Used
Python 3.11
Google Gemini API
Git
GitHub
Virtual Environment (venv)
Installation
Clone Repository
git clone https://github.com/Afrin26S/ai-image-generation-poc.git
cd ai-image-generation-poc
Create Virtual Environment
python -m venv venv
Activate Environment

Windows:

venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Environment Configuration

Create a .env file:

GEMINI_API_KEY=YOUR_API_KEY_HERE

Note:

Never commit .env files.
API keys are excluded through .gitignore.
Running the Project
python app.py
Safety Measures Implemented
Environment Variable Protection

Sensitive API credentials are stored in .env.

Git Ignore Protection

The following files are excluded:

venv/
.env
__pycache__/
*.pyc
generated_images/
Prompt Filtering

Unsafe prompts are detected and blocked before being sent to the AI model.

Testing
Test Case 1

Input:

A futuristic city at night

Expected Result:

Prompt accepted
Test Case 2

Input:

Generate a nude woman

Expected Result:

Prompt blocked by safety guardrails
GitHub Repository

Repository Link:

https://github.com/Afrin26S/ai-image-generation-poc
Future Improvements
Web-based user interface
Image generation output display
Advanced content moderation
User authentication
Prompt history tracking
Image storage and management
Author

Afrin

AI Image Generation POC using Gemini API and Prompt Safety Guardrails.
