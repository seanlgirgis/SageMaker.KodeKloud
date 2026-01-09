Briefing: Amazon SageMaker Studio and JupyterLab Spaces

Executive Summary

This document provides a comprehensive analysis of the Amazon SageMaker Studio environment, focusing on its core applications, the architecture of JupyterLab Spaces, and the significant evolution from the legacy SageMaker Classic interface. The new SageMaker Studio introduces a more complete, integrated development environment (IDE) that centralizes various machine learning tools beyond JupyterLab, including RStudio, a VS Code-based Code Editor, the low-code SageMaker Canvas, and MLflow for experiment management.

A central concept in the modern Studio is the "Space," a managed virtual machine instance running a specific application. A critical distinction is made between Private Spaces, designed for individual, sensitive work with dedicated resources, and Shared Spaces, which enable real-time, Google Docs-style collaboration among multiple users on a shared instance.

Architecturally, SageMaker Studio marks a fundamental shift in storage strategy. It moves away from the shared Amazon EFS (Elastic File System) volume that was central to SageMaker Classic. Instead, Studio now defaults to using individual Amazon EBS (Elastic Block Store) volumes attached to each Space's virtual machine. This change was primarily driven by the need for superior performance. While the domain's EFS volume still exists, it is no longer used by default and requires manual mounting. As SageMaker Classic is formally deprecated as of 2025, users must understand this new EBS-centric model for all storage and collaboration.


--------------------------------------------------------------------------------


1. Overview of the SageMaker Studio Environment

SageMaker Studio provides a comprehensive, web-based IDE for the entire machine learning workflow. It moves beyond a simple notebook interface to offer a suite of integrated, managed applications running on dedicated instances within an AWS region.

1.1. Available Applications

The Applications panel in the Studio UI provides access to multiple development environments:

* JupyterLab: A hosted interface for interactive data science and notebook-based experimentation.
* RStudio: An IDE for the R programming language, popular with statisticians. A separate RStudio license is required for use.
* Code Editor: A hosted version of Microsoft Visual Studio Code, providing a developer-focused IDE. This is ideal for refactoring Jupyter notebooks into production-ready Python scripts and building automated pipelines.
* SageMaker Canvas: A low-code, visual tool for building machine learning models without requiring Python skills, suitable for rapid prototyping.
* MLflow: An end-to-end machine learning management framework. Though it has some functional overlap with SageMaker, it is provided as a hosted application to leverage its capabilities in experiment management and model registry.

1.2. Legacy Access

For users with existing workflows, Studio provides a link to Access your Studio Classic applications. SageMaker Classic is the older interface and is being deprecated. AWS strongly encourages migration to the modern SageMaker Studio environment.

2. Core Components and Tools in SageMaker Studio

The left navigation bar exposes a range of integrated tools for managing the ML lifecycle:

* Running instances: A dashboard to view, stop, and start all active application instances (Spaces).
* HyperPod: Provides access to large, resilient compute clusters designed for training large language models (LLMs).
* Data Tools:
  * Data Wrangler: A low-code, graphical tool for data preparation and feature engineering, now integrated with SageMaker Canvas.
  * Feature Store: A centralized repository to store, share, and reuse engineered features across different models and projects.
  * EMR Clusters: Provides direct access to Elastic MapReduce clusters, enabling distributed data processing on large datasets using tools like PySpark.
* Deployments: This section is used to view and manage Endpoints, which are managed virtual machines hosting a deployed model for real-time inference.
* Projects: Enables the creation of turnkey projects that deploy complete CI/CD pipelines for automated model training and deployment.

3. Understanding JupyterLab Spaces

A "Space" is the fundamental unit of work in SageMaker Studio. It is a managed, self-contained environment consisting of a virtual machine instance (e.g., an ml.t3.medium EC2 instance) and an attached storage volume. This instance runs the software for a chosen application, such as JupyterLab.

When a user wishes to use an application like JupyterLab, they must first create a Space. The creation process involves:

1. Providing a name for the Space.
2. Choosing a Sharing Mode: either Private or Share with my domain.
3. Specifying the underlying compute instance type.
4. Selecting a container image that provides the necessary software.

4. Deep Dive: Private vs. Shared Spaces

The choice between a Private and Shared Space is critical as it defines the environment's access, resource allocation, and collaborative capabilities.

Feature	Private Space	Shared Space
Access	Individual use only. Visible only to the creator.	Multi-user collaboration. Visible to all users in the domain.
Collaboration	Solo work.	Real-time co-editing, similar to Google Docs.
Resources	Dedicated EC2 instance and resources for one user.	A single EC2 instance and resources are shared among users.
Storage	A dedicated EBS volume per user.	A single, shared EBS volume for all users of the space.
Use Cases	Individual projects, sensitive work.	Team projects, knowledge sharing, paired programming.
Customization	High degree of isolation allows for personal settings.	Settings changes can affect all collaborators.
Security	Strict access control; only the user profile can access.	Requires careful permissions management to control actions.

Visibility: A key security feature is that a user's Private Space is completely hidden from all other user profiles in the domain, including administrators. User Profile A cannot see User Profile B's private spaces. Both users, however, can see and potentially access any Shared Spaces within the domain.

5. The Evolution from SageMaker Classic to Studio

SageMaker Studio represents a significant architectural and functional evolution from the older SageMaker Classic. New users should exclusively use Studio and can safely ignore references to Classic. The primary differences are outlined below.

Feature	SageMaker Classic	SageMaker Studio (Modern)
Default Creation	Automatically created a private space for each user profile.	Spaces for applications must be explicitly created by the user.
Storage	Relied on a shared Amazon EFS volume for the entire domain.	Uses individual Amazon EBS volumes attached to each Space's instance.
Collaboration	Supported shared spaces, with collaboration occurring on the EFS file system.	Supports shared spaces with collaboration on a shared EBS volume.
Execution Role	Assumes the IAM role of the user profile.	Same; assumes the IAM role of the user profile.
Customization	Offered specific customization procedures.	Provides greater flexibility and more options for customization.
Application Support	Supported a limited set of applications.	Supports a broader range of integrated applications (RStudio, MLflow, etc.).

5.1. The Critical Shift from EFS to EBS Storage

The most important change is the move from EFS to EBS for default storage.

* Reason: The primary driver for this change was to achieve superior performance. EBS volumes provide dedicated, high-performance block storage directly to the instance.
* Deprecation Note: As of 2025, SageMaker Classic and its EFS-centric model will be end-of-support. Any documentation written before 2024 may contain outdated information suggesting EFS is the default for shared spaces, which is no longer correct.
* Current EFS Use: The EFS volume created with a SageMaker Domain is now considered a legacy component. While SageMaker will not prevent users from manually creating an NFS mount point from a Space to the EFS volume, this is not the default behavior and may have performance limitations.

6. Architecture and Management of Spaces

Spaces are built on a container-based architecture to ensure consistent and reproducible environments.

6.1. Containerization

When a Space is launched, SageMaker does not install software directly onto the managed EC2 instance's operating system. Instead, it uses containerization:

1. A managed EC2 instance is provisioned with a container runtime.
2. A specified container image is pulled from the Amazon Elastic Container Registry (ECR) within the AWS account.
3. The image is used to launch a container (e.g., a JupyterLab Server Container) on the instance.

The default images, such as SageMaker Distribution 2.1, come pre-installed with common ML libraries (TensorFlow, PyTorch, Keras, NumPy, Pandas, Scikit-learn) and the SageMaker Python SDK. This means users can immediately import sagemaker or import boto3 in their notebooks without needing to perform pip install.

6.2. Space Management

* Start/Stop Functionality: Spaces can be stopped to avoid incurring costs for the EC2 compute instance. When stopped, the attached EBS volume persists. The Space can be re-run (started) later.
* Cost Management Warning: Stopping a Space only stops billing for its EC2 instance. Any other AWS resources provisioned from within that Space's notebooks—such as SageMaker Endpoints, EMR clusters, or S3 buckets—will continue to exist and incur charges until they are explicitly de-provisioned.
* Viewing and Managing Spaces: Administrators can view all spaces within a domain from the AWS Management Console under the domain's Space Management tab. Individual users can manage the spaces visible to them directly within the SageMaker Studio UI.

7. Identifying Shared Spaces in the User Interface

The JupyterLab interface provides clear visual indicators when a user is in a Shared Space to facilitate collaboration.

* RTC Indicator: On the JupyterLab launcher page, a shared space will display an "RTC" (Real-Time Collaboration) icon.
* User Identity Circle: In the top-right corner of the interface, a colored circle with a letter will appear for each user currently active in the space. This allows collaborators to identify who is making changes, similar to the experience in Google Docs. If these indicators are not present, the user is in a Private Space.
