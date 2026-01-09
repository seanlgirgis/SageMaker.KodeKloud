# .\04 04 SageMakerDomainsAndStudio Part2

# 04 04 Sagemakerdomainsandstudio Part2 Blogpost

Beyond the Notebook: 5 Surprising Truths About AWS SageMaker Studio

When data scientists think of AWS SageMaker, they often picture a hosted environment for running Jupyter notebooks. While that's a core function, this perception misses the bigger picture. AWS SageMaker Studio is a far more comprehensive and nuanced platform with several surprising features that can radically improve and accelerate your machine learning workflow.

1. Your Shared Storage Isn't What You Think It Is

There's a common misconception that SageMaker Studio uses a shared EFS (Elastic File System) volume for collaboration, a behavior inherited from the older SageMaker Classic. However, the modern SageMaker Studio has shifted to using individual EBS (Elastic Block Store) volumes for both private and shared spaces. EBS volumes are the virtual hard disks attached directly to each managed instance, providing high-performance, block-level storage.

This change was made primarily for performance reasons.

We were getting far superior performance from EBS than from EFS.

Understanding this is crucial, as it avoids confusion for users familiar with the older version or those referencing outdated documentation. While you can still manually mount an EFS volume if needed, it is no longer the default storage mechanism for Studio spaces precisely because of the performance benefits of using direct-attached EBS volumes.

2. It's a Full-Fledged Workbench, Not Just a Notebook Server

SageMaker Studio is a comprehensive workbench that goes far beyond just serving Jupyter notebooks. The platform integrates a suite of applications designed to support various stages and roles within a machine learning project.

* JupyterLab: For classic, interactive, notebook-based experimentation.
* RStudio: A managed RStudio environment for statisticians and R programmers (requires an RStudio license).
* Code Editor: A hosted version of Microsoft Visual Studio Code, ideal for refactoring experimental notebooks into production-ready, automated Python scripts.
* Canvas: A low-code tool that allows users to visually build models without needing Python skills.
* MLflow: An end-to-end machine learning management framework for experiment tracking and model registration, available as a hosted application.

Beyond these primary applications, the Studio interface also directly integrates essential data management tools like Data Wrangler for low-code feature engineering, a Feature Store for reusing curated features, and direct access to EMR clusters for large-scale data processing. This suite of tools is designed to support the entire ML lifecycle, enabling a seamless transition from interactive, exploratory work in JupyterLab to productionizing models by refactoring them into automated Python scripts within the developer-focused Code Editor.

3. It Has a "Google Docs Mode" for Notebooks

One of the most powerful and often overlooked features of SageMaker Studio is real-time collaboration within shared JupyterLab spaces. This feature provides a "Google Docs shared document experience," allowing multiple users to work on the same Jupyter notebook simultaneously.

When you're in a shared space, visual indicators make it clear. You'll see an "RTC" (Real-Time Collaboration) icon on the launcher page and colored circles with user initials in the top-right corner, similar to other collaborative web applications.

...in a shared space with JupyterLab, we can have a kind of Google Docs shared document experience. So it can both be working on the same Jupyter notebook at the same time, and that can make a huge difference for productivity.

4. Your Entire Workspace is Powered by Containers

Under the hood, every application space in SageMaker Studio runs on a containerized architecture. When you start a JupyterLab space, for example, SageMaker provisions a managed EC2 instance and runs the JupyterLab server software inside a container.

These container images are pulled from the Amazon Elastic Container Registry (ECR) and come pre-packaged with the most common ML libraries and frameworks, including TensorFlow, PyTorch, Keras, Numpy, Pandas, and Scikit-learn. The SageMaker Python SDK is also included by default. This containerized approach provides a consistent, reproducible environment and means you can get started immediately without needing to manually pip install core libraries. More importantly, this guarantees a consistent, reproducible environment for every team member, eliminating the common 'it works on my machine' problem and accelerating project onboarding.

So in your Python scripts within your Jupyter lab space, you could simply say import Sagemaker or import boto3 and it will just work. You don't need to do any pip installs in this place, it's already there.

5. Private Spaces Offer True, Admin-Proof Isolation

Security and isolation are paramount, and SageMaker Studio's "private spaces" offer a surprisingly strict security model. A private space is completely hidden and invisible to any other user profile within the same SageMaker domain, unlike "shared spaces" which are visible to all users.

The most surprising aspect of this feature is its level of enforcement: even the administrators of the SageMaker domain do not have direct access to a user's private space. This provides a secure-by-default environment for working with highly sensitive data or for individual projects where intellectual property must be strictly contained, even from internal administrators.

SageMaker Studio is a deep and powerful platform with many thoughtful features hiding just beneath the surface. By understanding these capabilities, teams can move beyond notebook-centric workflows to build more robust, collaborative, and secure machine learning systems.

Now that you've seen what's under the hood, which of these features will most change how you approach your next machine learning project?

# 04 04 Sagemakerdomainsandstudio Part2 Briefing

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

# 04 04 Sagemakerdomainsandstudio Part2 Study Guide

SageMaker Studio and JupyterLab Spaces Study Guide

Short-Answer Quiz

1. What is the primary difference in the default storage mechanism between the modern SageMaker Studio and the legacy SageMaker Classic?
2. Describe the purpose of the "Code Editor" application within SageMaker Studio and identify the stage of an ML project where it is most beneficial.
3. Explain what a "space" represents in the context of SageMaker Studio and how it is provisioned.
4. How does real-time collaboration work in a shared JupyterLab space, and what visual indicators signify that you are in one?
5. What role do container images from the Elastic Container Registry (ECR) play when you launch a JupyterLab space?
6. When you stop a JupyterLab space to save on compute costs, what important warning is provided regarding other potentially running AWS resources?
7. Identify at least three applications, other than JupyterLab, that are available within the SageMaker Studio interface and briefly state their function.
8. Contrast the process of space creation in SageMaker Classic with that in the current SageMaker Studio.
9. What are the key differences in resource allocation and access control between a private space and a shared space?
10. If a user needs to access the domain's EFS volume from a modern SageMaker Studio space, how can this be achieved and what is the main caveat?


--------------------------------------------------------------------------------


Answer Key

1. In SageMaker Classic, the primary storage mechanism was a shared Amazon EFS (Elastic File System) volume defined at the domain level. In the modern SageMaker Studio, storage has transitioned to using individual EBS (Elastic Block Store) volumes, which are the virtual hard disks attached directly to the managed virtual machine instance for each space, offering superior performance.
2. The Code Editor application is essentially a hosted version of Microsoft Visual Studio Code. It provides a more developer-focused IDE, making it most beneficial when an ML project moves from the interactive experimentation phase into productionization, where Jupyter notebooks are often refactored into automated Python scripts.
3. A "space" in SageMaker Studio is essentially a managed virtual machine instance (an EC2 instance) that runs the software for a specific application, such as JupyterLab. When creating a space, you must specify its name, sharing mode (private or shared), the compute instance size (e.g., ml.t3.medium), and the container image to use.
4. Real-time collaboration in a shared space provides a "Google Docs"-like experience, allowing multiple users to co-edit the same Jupyter notebook simultaneously. Visual indicators include an "RTC" (Real-Time Collaboration) icon on the launcher page and a unique colored circle with a letter representing each active user in the top-right corner of the UI.
5. When a JupyterLab space is launched, SageMaker provisions a managed EC2 instance and pulls a specified container image from the Elastic Container Registry (ECR). This container image contains all the necessary software, such as the JupyterLab server process, Python, and key ML libraries (like TensorFlow, PyTorch, Pandas), abstracting the underlying operating system.
6. The warning provided is that stopping the JupyterLab space only shuts down its associated virtual machine instance, thereby stopping billing for that specific resource. However, any other AWS resources provisioned from within that space—such as SageMaker endpoints, EMR clusters, or S3 buckets—will continue to exist and incur charges until they are manually deprovisioned.
7. Other applications include RStudio (an IDE for the R programming language, requiring a license), SageMaker Canvas (a low-code tool for visually building models without Python skills), and MLflow (an end-to-end ML management framework for experiment tracking and model registry).
8. In SageMaker Classic, a private space was automatically created for each user profile by default. In the modern SageMaker Studio, no spaces are created automatically; users must explicitly create the JupyterLab, Code Editor, or RStudio spaces they need, giving them more control over resource provisioning.
9. A private space has dedicated virtual machine resources and an EBS volume for a single user, ensuring strict access control where only the creator can see and use it. A shared space uses a shared instance and EBS volume accessible by multiple users within the domain, requiring careful permissions management to control actions.
10. To access the domain's EFS volume from a modern Studio space, a user would have to create a manual mount point from within the space to perform an NFS mount to the EFS system. The main caveat is performance, as the transition to EBS was made primarily because EBS offered far superior performance compared to EFS for these workloads.


--------------------------------------------------------------------------------


Essay Questions

1. Discuss the architectural evolution from SageMaker Classic to the modern SageMaker Studio. Detail the significant changes in storage (EFS vs. EBS), application availability, and the user experience regarding space management, and explain the rationale behind these changes.
2. Analyze the suite of tools and applications available within the SageMaker Studio interface (e.g., JupyterLab, Code Editor, Canvas, Data Wrangler, Feature Store). Describe how these tools collectively support an end-to-end machine learning workflow, from initial data preparation and experimentation to model deployment and management.
3. Elaborate on the concepts of "Private Spaces" and "Shared Spaces" in SageMaker Studio. Compare and contrast their use cases, resource models, security implications, and collaboration capabilities for a data science team working on both individual research and joint projects.
4. Describe the underlying technology stack that powers a JupyterLab space in SageMaker Studio. Your explanation should cover the roles of managed EC2 instances, containerization using images from the Elastic Container Registry (ECR), and the function of EBS volumes for persistent storage.
5. Imagine you are an administrator of a SageMaker domain with multiple user profiles. Explain the different interfaces (AWS Management Console vs. SageMaker Studio UI) available for managing spaces. Detail how you would view all existing spaces, differentiate between private and shared ones, and how visibility and access are enforced for different users.


--------------------------------------------------------------------------------


Glossary of Key Terms

Term	Definition
Code Editor	An application within SageMaker Studio, essentially a hosted Microsoft Visual Studio Code, providing a developer-focused IDE suitable for productionizing code and refactoring notebooks into Python scripts.
Container Image	A package containing software and its dependencies (e.g., JupyterLab, Python, ML libraries). SageMaker uses these images, stored in ECR, to launch applications like JupyterLab in a managed, containerized environment on an EC2 instance.
Data Wrangler	A tool, now integrated into SageMaker Canvas, that allows for data preparation and feature engineering in a graphical, low-code manner.
EBS (Elastic Block Store)	The primary storage mechanism for modern SageMaker Studio spaces. It functions as a virtual hard disk attached directly to the managed EC2 instance running the space, providing high-performance storage.
ECR (Elastic Container Registry)	An AWS service that stores, manages, and deploys container images. SageMaker Studio pulls application images (like the JupyterLab image) from ECR to run on managed instances.
EFS (Elastic File System)	The primary storage mechanism for the legacy SageMaker Classic. It is a shared NFS volume defined at the SageMaker Domain level. In modern Studio, it is no longer used by default due to performance limitations but can be manually mounted.
EMR (Elastic MapReduce)	Managed Hadoop clusters that can be accessed from SageMaker Studio. EMR is ideal for distributed data processing on large datasets, particularly for running PySpark scripts.
Endpoint	A managed deployment of a model artifact and inference-handling code inside a virtual machine. Endpoints are used to host a trained model for real-time predictions.
Feature Store	A centralized repository within SageMaker to store, retrieve, and share engineered features, which can be reused across different projects or to accelerate model inference.
HyperPod	A feature for creating extremely large, resilient clusters of instances, specifically designed for training large language models (LLMs).
JupyterLab Space	A managed virtual machine instance running the JupyterLab application. Users can create, start, stop, and manage these spaces, choosing their compute size and sharing settings.
MLflow	An end-to-end machine learning management framework available as a hosted application within SageMaker Studio. It provides capabilities for experiment management and model registry.
Private Space	A space (e.g., for JupyterLab) that is accessible only to the user profile that created it. It runs on dedicated resources and uses a private EBS volume for storage. Even domain administrators do not have direct access.
RStudio	An integrated development environment (IDE) for the R programming language, popular with statisticians and data scientists. It is available as a hosted application in SageMaker Studio but requires a separate RStudio license.
RTC (Real-Time Collaboration)	A feature of shared JupyterLab spaces that allows multiple users to co-edit the same notebook simultaneously. It is visually indicated by an "RTC" icon on the launcher page.
SageMaker Canvas	A low-code application within SageMaker Studio that enables users to build ML models visually without writing any Python code, making it suitable for rapid prototyping.
SageMaker Classic	The legacy version of the SageMaker Studio interface. It is being deprecated (end of support in 2025) and differs from the modern Studio in its use of EFS for storage and automatic creation of spaces.
SageMaker Domain	A foundational entity in SageMaker that consists of a shared EFS volume, a list of authorized users (User Profiles), and various security and network settings. It serves as the entry point for accessing SageMaker Studio.
SageMaker Studio	The current, comprehensive integrated development environment (IDE) for machine learning that provides a single web-based interface for all ML development steps. It hosts various applications like JupyterLab, Code Editor, and Canvas.
Shared Space	A space that is visible and accessible to all users within the same SageMaker Domain, subject to permissions. It facilitates real-time collaboration by allowing multiple users to work within the same shared instance and EBS volume.
User Profile	A profile within a SageMaker Domain that corresponds to a specific user. Each user profile has an associated IAM execution role that defines its permissions.

