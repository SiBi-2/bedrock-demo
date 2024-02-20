# AWS Bedrock AI Models Access and Invocation

This project demonstrates how to configure AWS IAM (Identity and Access Management) to access AWS Bedrock, a service that provides access to AI models. We will also showcase how to invoke these models using Visual Studio Code and integrate them into a simple application.

## Overview

AWS Bedrock allows developers to access various AI models for different purposes. This proof of concept guides you through setting up AWS, configuring necessary permissions, accessing Bedrock AI models, and invoking these models through code. The final part of the project involves creating a simple application that utilizes these models.

**Note**: This setup is intended as a demo and proof of concept. Production environments may require additional configurations.

## Getting Started

### Prerequisites

- An AWS account
- Visual Studio Code installed on your system

### Configuring AWS IAM

1. **Create an IAM Group**:
   - Navigate to IAM in AWS and create a new group named `demo`.
   - Add `BedrockReadOnlyAccess` permission to the group.

2. **Create Custom IAM Policies**:
   - Create an inline policy for the `demo` group that includes `read` and `invoke` permissions for Bedrock models.

3. **Create a Service Account**:
   - Create a user named `svc-bedrock` and add it to the `demo` group.

4. **Generate API Keys**:
   - Navigate to the security credentials of `serviceBedrock` and create new access keys.

### Configuring Access to Bedrock Models

1. **Access Bedrock in AWS Console**:
   - Go to Bedrock service and navigate to `Model Access`.

2. **Manage Model Access**:
   - Select and add models you want to access, such as AI21, Amazon, Anthropic, etc.

### Setting Up Local Environment

1. **Configure AWS Credentials**:
   - Edit the `.aws/credentials` file with the access key and secret key obtained earlier.

2. **Set Region Configuration**:
   - Modify the `.aws/config` file to specify the desired AWS region.

## Developing the Application

1. **Setup in Visual Studio Code**:
   - Open Visual Studio Code and prepare the application that will invoke the AI models.

2. **Use Bedrock Helper**:
   - Implement a helper module to manage the invocation of different AI models with varying parameters.

3. **Invoke AI Models**:
   - Run the application to invoke AI models and process their responses.

## Application Features

- The application allows invoking several AI models for text, image, and embedding purposes.
- Supports dynamic parameter handling to accommodate differences in model API requirements.
- Includes a streaming feature for responses, with support for markdown formatting.

## Running the Application

To run the application, use the following command:

```bash
python app.py
```

```bash
python autorun.py
```