SageMaker User Management and Studio Environment Analysis

Executive Summary

This document provides a comprehensive analysis of user and environment management within Amazon SageMaker, focusing on the critical distinctions between the modern SageMaker Studio New interface and the deprecated SageMaker Classic. The central recommendation is the exclusive adoption of SageMaker Studio New for all new development to leverage its superior capabilities in collaboration, resource management, MLOps, and security.

A foundational best practice is the strict adherence to a "one person, one profile" model. Each user profile within a SageMaker Domain should correspond to a single individual, a principle that underpins the platform's security and resource management models. Sharing profiles is strongly discouraged as it undermines auditability, resource tracking, and security controls.

SageMaker Studio New offers significant advantages, including a customizable user interface, high-performance EBS storage, real-time collaboration via shared spaces, and integrated MLOps tools. It is the exclusive gateway to modern SageMaker features such as Pipelines, Model Monitor, Debugger, and Feature Store. SageMaker Classic is an outdated option, lacking these features and flexibility, and should only be maintained for continuity in legacy projects until migration is complete.

User Profile Management in SageMaker Domains

A SageMaker Domain serves as the primary administrative boundary for defining users, applications, and storage configurations. Managing user access is performed by creating user profiles within this domain.

The Principle of Individual User Profiles

It is a strong recommendation that each user profile directly represents an individual person. The SageMaker security model is designed around this one-to-one mapping. Creating generic team profiles or sharing a single profile among multiple IAM or Identity Center users is an anti-pattern that can lead to unintended security and access consequences.

Adhering to this principle provides five key benefits:

1. Representation: The profile represents an individual user within the domain.
2. Private Directory: Each user receives a private home directory (on EFS for Classic, or a private directory/volume on EBS for New).
3. Personalization: The profile maintains personal settings and configurations.
4. Accurate Tracking: It ensures precise resource tracking and billing, attributing costs to specific individuals.
5. Specific Controls: It enables the application of user-specific security controls and constraints.

Best Practices for User Profile Creation

Category	Best Practice
Identity Federation	In enterprise environments using AWS Identity Center for federated login (e.g., from Microsoft Entra), a one-to-one relationship should be maintained: 1 Identity Center user = 1 SageMaker profile.
Automation	Profiles can be auto-created within a domain when a user is assigned from Identity Center to SageMaker Studio, ensuring consistent settings and permissions.
Prohibited Practices	- Avoid sharing user profiles between multiple people.<br>- Avoid creating generic user profiles for teams.<br>- Avoid using a single profile for multiple IAM or Identity Center users.

Benefits of Individual Profiles

Maintaining individual user profiles delivers significant advantages across security and resource management.

Security Benefits

* True Audit Trails: Provides clear audit trails to understand the actions taken by every user.
* Resource Isolation: Ensures proper isolation of resources (storage, compute) used by each individual.
* Role-Based Access: Enables sensible role-based access control (RBAC) aligned with the user, ensuring they can only perform intended actions.
* Secure Workspaces: Allows for secure workspaces with individualized controls.

Resource Management & Financial Control Benefits

* Individual Quotas: Allows resource quotas (e.g., number of instances or EBS volumes) to be applied on a per-user basis.
* Storage Allocation: Tracks storage space allocation and usage for each person.
* Separation of Permissions: Enables the assignment of separate execution roles (IAM roles), granting different users different permissions (e.g., access to different S3 buckets) within the same domain.
* Accurate Compute Tracking: Delivers better tracking of compute usage, making it clear which user created specific resources and how much they are being consumed for improved financial control.

SageMaker Studio New vs. SageMaker Studio Classic

When creating a new user profile, the most critical choice is between the SageMaker Studio New (sometimes called V2) and the deprecated SageMaker Studio Classic interfaces. Studio New is the default and strongly recommended option.

Core Distinctions and Deprecation

* SageMaker Studio New: The modern, feature-rich, and fully supported environment. It is required to unlock the full functionality of newer SageMaker services.
* SageMaker Studio Classic: An outdated, legacy interface that is no longer supported by AWS. Its use should be limited to maintaining continuity for existing projects until they can be migrated.

Key Configuration and Feature Differences

Feature	SageMaker Studio New	SageMaker Studio Classic
Default Choice	Yes, this is the default selection for new user profiles.	No
UI Customization	Yes, extensive control to show/hide applications and navigation tools per user.	No, customization of the Studio UI is not available.
Primary Storage	EBS (Elastic Block Store) volumes, offering lower latency and greater throughput.	EFS (Elastic File System).
Notebook Sharing	Integrated and seamless. Can be done via shared links or Git version control.	Requires explicit configuration, including enabling the feature and specifying an S3 location for shared artifacts.
Feature Access	Provides access to all modern SageMaker features (Pipelines, Debugger, Canvas, etc.).	Limited access to older features only.

Identifying the Active Environment

Because both environments use a JupyterLab interface, it may not be immediately obvious which version is active. A simple trick to verify the environment is to use the df -h command in a JupyterLab terminal.

* SageMaker Classic: The output will show a file system path like EFF... mounted on /home/sagemaker-user, indicating it is using EFS.
* SageMaker Studio New: The output will show a file system path like /dev/nvme1n1 mounted on /home/sagemaker-user, indicating it is using high-speed local EBS storage.

Advanced Configuration in SageMaker Studio New

SageMaker Studio New offers granular control over the user experience, allowing administrators to tailor the environment to each user's specific needs.

UI Customization for User Profiles

During user profile creation, an administrator can customize two key aspects of the UI:

1. Application Visibility: A series of toggle switches allows an admin to control which applications appear in the user's application panel. This is useful for decluttering the UI by hiding unused tools. The list includes:
  * Core Tools: JupyterLab, Code Editor (VS Code-based), Canvas
  * Licensed Tools: RStudio
  * Third-Party Integrations: MLflow, Comet ML, Fiddler, DeepChecks, etc.
2. Navigation Panel Customization: The left-hand navigation bar can also be customized to hide tools that are not relevant to a particular user's role. This includes hiding major sections or individual items like:
  * Data: Data Wrangler, Feature Store, EMR Clusters
  * Jobs: Training Jobs, AutoML, Experiments
  * Models & Deployments

Important Caveat: These UI settings only control visibility. They do not restrict a user's permissions. To prevent a user from accessing these features altogether (e.g., via the SDK or CLI), permissions must be explicitly denied in the user profile's associated IAM role.

Data and Storage Configuration

The user profile setup wizard includes a "Data and Storage" page that references auto-mounting EFS. This can be confusing, as EFS is a SageMaker Classic feature. EFS is not required for JupyterLab when using the SageMaker Studio New interface, which relies on EBS. This page is a legacy artifact in the wizard and should ideally be hidden for Studio New configurations.

Comprehensive Advantages of SageMaker Studio New

Adopting SageMaker Studio New enhances ML productivity across four key domains.

1. Streamlined Development and Collaboration

* JupyterLab-Based IDE: Provides a unified, industry-standard environment for coding, data exploration, and debugging.
* Shared Spaces: Enables real-time collaboration where multiple team members can work within the same shared JupyterLab environments.
* Notebook Sharing: Facilitates easy sharing of notebooks via direct links or, more robustly, through integrated version control with Git.
* Experiment Tracking: Integrates with SageMaker Experiments to log, compare, and organize model results in a structured manner.

2. Better Resource and Compute Management

* On-Demand Kernel Selection: Allows users to switch between different compute instances for different notebook tabs without restarting the entire environment.
* Auto-Shutdown & Resource Scaling: Reduces costs with auto-stop functionality for idle resources and scalable compute options. This addresses a major source of unnecessary cost in legacy notebook instances.
* EBS Storage: Utilizes EBS instead of EFS, providing faster, more isolated storage with lower latency and greater throughput for both private and shared spaces.

3. Improved MLOps and Automation

* SageMaker Pipelines: Unlocks access to SageMaker Pipelines, an orchestration tool for automating the entire ML lifecycle (e.g., training, evaluation, deployment).
* Integrated Git Support: Offers seamless integration to clone, push, and manage code repositories directly within the Studio interface.
* Debugging and Monitoring: Includes built-in integration with SageMaker Debugger and SageMaker Model Monitor to analyze and maintain model health.
* Easier Deployment: Simplifies model deployment to SageMaker Endpoints.

4. Security and Governance Improvements

* IAM Role-Based Access Control: Allows for finer-grained permission management for different team members and Studio components.
* Network Isolation: Provides better integration with VPCs and security groups for controlled network access, allowing instances to be attached to private networks.
* Auditability and Logging: Integrates with AWS CloudTrail and Amazon CloudWatch for comprehensive logging and compliance, making logs searchable and actionable through alerts and remediation actions.
