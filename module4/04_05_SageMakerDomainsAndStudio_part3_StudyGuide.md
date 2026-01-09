SageMaker Domains and Studio Study Guide

Short-Answer Quiz

Instructions: Answer the following questions in 2-3 sentences based on the provided source material.

1. What is the strong recommendation for mapping individual people to SageMaker User Profiles, and what is the primary security reason for this recommendation?
2. Describe the two different storage volume types used by SageMaker Studio Classic and SageMaker Studio New for JupyterLab spaces.
3. How can a user determine from the command line terminal whether their JupyterLab space is running on SageMaker Studio Classic or SageMaker Studio New?
4. What customization options are available for the user interface in SageMaker Studio New that are absent in SageMaker Studio Classic?
5. Explain the purpose of a JupyterLab space and the difference between its "private" and "shared" configurations.
6. According to the source, what is a "Quick Start domain," and why is it not recommended for production environments?
7. What is an "Execution Role" in the context of creating a new SageMaker user profile?
8. List three specific benefits of SageMaker Studio New from the "Improved MLOps and Automation" category.
9. Why is the "Data and storage" pane, which refers to auto-mounting EFS, considered confusing when setting up a user profile for SageMaker Studio New?
10. What are three user profile practices that should be avoided to ensure proper security and resource management?


--------------------------------------------------------------------------------


Answer Key

1. The strong recommendation is that one user profile should directly represent one individual person (a 1-to-1 mapping). The primary security reason is to ensure true audit trails for user actions, proper resource isolation, and that role-based access controls are applied correctly to the intended individual.
2. SageMaker Studio Classic uses Amazon EFS (Elastic File System) for storage, which requires auto-mounting. SageMaker Studio New uses Amazon EBS (Elastic Block Store) volumes, which provide lower latency and greater throughput for processing jobs.
3. A user can run the df -h command in the JupyterLab terminal. If the output shows a file system mounted on /home/sagemaker-user that looks like an EFS mount, it's SageMaker Classic; if it shows something like /dev/nvme1n1, it indicates the use of high-speed local EBS storage, which means it's SageMaker Studio New.
4. In SageMaker Studio New, an administrator can customize the UI for each user by toggling the visibility of specific applications (like JupyterLab, Code Editor, Canvas, RStudio) in the applications panel. Additionally, the left-hand navigation bar can be customized to hide tools like Data Wrangler, EMR clusters, or specific job types.
5. A JupyterLab space is the environment where the JupyterLab server process runs, backed by a managed compute instance (e.g., an EC2 instance). A "private" space is visible and accessible only to the user profile that created it, while a "shared" space is visible and listed to all user profiles within that SageMaker domain.
6. A "Quick Start domain" is a configuration option that helps users get started quickly for learning or proof-of-concept purposes. It is not recommended for production because it uses the default VPC in the AWS region and does not allow for the detailed user and network configuration needed in an enterprise environment.
7. An Execution Role is an IAM (Identity and Access Management) role assigned to a user profile. This role defines the security context under which the user operates, determining what AWS resources and services they are permitted to interact with from within SageMaker.
8. Three MLOps and Automation benefits are: access to SageMaker Pipelines for orchestrating ML workflows, integrated Git support for version control of code assets, and access to the SageMaker Debugger and Model Monitor for understanding and troubleshooting models.
9. The pane is confusing because it asks about auto-mounting EFS, which is a feature required only by SageMaker Studio Classic. Since a user configured for SageMaker Studio New exclusively uses EBS volumes for JupyterLab, this configuration page is irrelevant and should ideally be hidden.
10. To maintain security and proper tracking, one should avoid: sharing user profiles between multiple people, creating generic user profiles for entire teams, and using a single profile for multiple IAM or Identity Center users.


--------------------------------------------------------------------------------


Essay Questions

Instructions: The following questions are designed for longer, more detailed responses that require synthesizing multiple concepts from the source material.

1. Discuss the security and resource management implications of adhering to the best practice of "one Identity Center user per one SageMaker profile." Contrast this with the potential issues that arise from sharing profiles, creating generic team profiles, or mapping multiple IAM users to a single profile.
2. Compare and contrast SageMaker Studio New and SageMaker Studio Classic. Cover all major differences discussed in the source, including user interface customization, storage architecture, notebook sharing, and access to advanced SageMaker features.
3. Explain the hierarchical relationship between a SageMaker Domain, User Profiles, and JupyterLab Spaces. Describe the end-to-end workflow for an administrator adding a new data scientist to a domain, detailing the key configuration decisions made at each step.
4. Detail the four primary categories of benefits provided by SageMaker Studio New: Streamlined Development and Collaboration, Better Resource and Compute Management, Improved MLOps and Automation, and Security and Governance Improvements. For each category, provide two specific examples or features mentioned in the source material and explain how they contribute to enhanced ML productivity.
5. Imagine you are an administrator tasked with configuring a SageMaker domain for a diverse team of three users: a senior data scientist who needs full access to all ML tools, a junior analyst who only needs to use SageMaker Canvas, and a data engineer who primarily works with EMR and Git but does not use JupyterLab. Describe how you would use the customization features of SageMaker Studio New to create a tailored, clutter-free user experience for each of these three user profiles.


--------------------------------------------------------------------------------


Glossary of Key Terms

Term	Definition
Amazon EBS (Elastic Block Store)	The storage type used by SageMaker Studio New. It provides lower latency and greater throughput than EFS and is identified in the terminal as high-speed local storage (e.g., /dev/nvme1n1).
Amazon EFS (Elastic File System)	The storage type used by the legacy SageMaker Studio Classic. User profiles for Classic may require configuration for EFS auto-mounting.
Execution Role (IAM Role)	An AWS IAM role assigned to a user profile that defines the security context and permissions for that user. It determines what actions the user can perform and which AWS resources they can interact with.
JupyterLab Space	A defined environment for running the JupyterLab server process, which is backed by a specified compute instance. A space can be configured as private (visible only to its creator) or shared (visible to all users in the domain).
Quick Start Domain	A simplified setup option for a SageMaker Domain, intended for learning and proof-of-concept work. It is not recommended for production because it uses the default VPC and lacks advanced configuration options.
SageMaker Domain	An administrative boundary that contains user profiles, applications, and storage configurations. A domain must be created before the SageMaker Studio UI can be launched.
SageMaker Studio Classic	The deprecated version of the SageMaker Studio interface. It lacks the UI customization of the new version, uses EFS for storage, requires explicit configuration for notebook sharing, and does not support many newer SageMaker features.
SageMaker Studio New (V2)	The current, recommended version of the SageMaker Studio interface. It provides extensive UI customization, uses EBS storage, enables real-time collaboration via shared spaces, and is required to access newer SageMaker features like Pipelines, Debugger, Model Monitor, and Canvas.
Shared Spaces	A feature in SageMaker Studio New that allows multiple data scientists to collaborate in real-time on the same JupyterLab notebooks within a shared environment.
User Profile	An entity within a SageMaker domain that should represent a single individual person. It maintains personal settings and configurations, enables accurate resource tracking and billing, and is the basis for applying user-specific security controls.
