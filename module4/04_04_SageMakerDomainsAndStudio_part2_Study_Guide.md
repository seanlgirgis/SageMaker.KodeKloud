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
