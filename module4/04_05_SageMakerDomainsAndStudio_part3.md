# .\04 05 SageMakerDomainsAndStudio part3

# 04 05 Sagemakerdomainsandstudio Part3 Blogpost

5 SageMaker Studio Secrets That Will Save You From Headaches and High Bills

Introduction: Beyond the Quick Start

Setting up an AWS SageMaker Studio domain using the "Quick Start" option can feel deceptively simple. However, when you move beyond a solo proof-of-concept and start managing an environment for a team, hidden complexities emerge. Getting the foundation of user management and environment setup right from the start is critical.

This post reveals five crucial, often overlooked, insights about SageMaker user management that go beyond the basic setup. These are the key takeaways that will help your team improve security, manage costs, and work more efficiently on the AWS machine learning platform.


--------------------------------------------------------------------------------


1. One Person, One Profile. Period.

The single most critical best practice for managing a SageMaker Domain is this: every user profile must correspond to a single, individual person. The entire security model is designed around this one-to-one mapping.

To ensure a secure and manageable environment, you must avoid these common anti-patterns:

* Avoid sharing user profiles between multiple people.
* Avoid creating generic user profiles for teams.
* Avoid using a single profile for multiple IAM or Identity Center users.

The "why" behind this principle is clear and delivers benefits across two key areas:

* For Security & Governance: This approach provides true audit trails for tracking user actions, proper resource isolation, logical role-based access control, and secure workspaces with individualized controls.
* For Resource & Cost Management: It enables individual resource quotas, personal storage allocation tracking, and precise tracking of compute usage. You'll know exactly which person created a resource, preventing situations like discovering a huge, expensive EMR cluster of 22 nodes running C524X larges was created by an anonymous "team" account.

"It's a strong recommendation that a user profile directly represents a person, a user, and the security model has been designed in that way. So please don't share multiple AWS account users. Sharing the same user profile in a Sagemaker domain could lead to unintended consequences for security access."


--------------------------------------------------------------------------------


2. The UI Customization Is for Visibility, Not Security

A powerful feature in the new SageMaker Studio experience allows administrators to customize the user interface for each user profile. Using simple toggle switches, you can hide applications like RStudio, Canvas, or MLFlow, and also hide specific ML tools in the navigation bar, such as Data Wrangler or the option to interface with EMR clusters.

However, there is a crucial and counter-intuitive truth here: hiding a tool in the UI does not prevent a user from accessing it.

These UI settings are purely for visibility—they help declutter the interface and present only the tools a specific user needs. To actually restrict a user from using a feature, you must define security controls in the permissions of their assigned IAM role.

"Now, do remember that this is purely just a visibility setting. They could still access those features via code. If you wanted to limit them from actually using them altogether. That would still need to be something defined in the permissions of the IAM role."


--------------------------------------------------------------------------------


3. That Confusing EFS Setting? You Can Ignore It for Studio New

When you're setting up a new user profile for the modern SageMaker Studio New interface, the wizard presents a "Data and Storage" page that asks about auto-mounting an EFS (Elastic File System). This step is a confusing legacy element that often trips up new administrators.

EFS is the storage mechanism for the deprecated SageMaker Classic interface. The new SageMaker Studio uses faster, isolated EBS (Elastic Block Store) volumes. Specifically, a user gets their own directory in a shared EBS volume for a shared space, or the entire dedicated EBS volume if the space is private.

This page "should be hidden" in the new user workflow. EFS is not required for JupyterLab when using the new Studio interface, so you can safely ignore this configuration step and avoid unnecessary confusion.


--------------------------------------------------------------------------------


4. The Simple Terminal Trick to Know Your Environment

Once a user is working inside a JupyterLab space, it might not be immediately obvious whether they are in a "Classic" environment (using shared EFS storage) or a "Studio New" environment (using dedicated EBS storage).

There's a simple terminal command you can run to reveal the underlying storage type: df -h.

Here is how to interpret the output to know which environment you are in:

* If the output shows a filesystem like EFS... mounted specifically on /home/sagemaker-user, you are in SageMaker Classic.
* If the output shows a filesystem like /dev/nvme1n1, you are in SageMaker Studio New, which uses faster, local EBS storage.

This is a useful trick to clarify which storage system is in use, which directly impacts performance characteristics like latency and throughput.


--------------------------------------------------------------------------------


5. Studio "New" Is a Power-Up, Not Just a Facelift

Unless you have a specific legacy requirement, SageMaker Studio New should always be your default choice over the deprecated Studio Classic. The benefits go far beyond a cosmetic UI update; it's a fundamental power-up for your entire MLOps workflow.

Here are the key advantages of using the new Studio experience:

* Better Performance & Cost Control: The switch from EFS to faster EBS storage provides lower latency and greater throughput. You also gain the ability to configure auto-shutdown for resources to better control costs.
* Enhanced MLOps and Automation: Studio New is required to unlock crucial MLOps tools like SageMaker Pipelines for orchestration, SageMaker Experiments for tracking, SageMaker Debugger for analysis, and SageMaker Model Monitor for post-deployment oversight. It also features integrated Git support and makes deployment easier with SageMaker Endpoints.
* Superior Collaboration: It enables the use of shared spaces, allowing multiple data scientists to collaborate in real-time on the same JupyterLab notebooks.
* Finer-Grained Security: The new experience offers improved IAM role-based access control and better network customization options. Crucially, it enhances governance with improved auditability and logging through deep integration with CloudTrail and CloudWatch.

Ultimately, all of the newer, more powerful SageMaker features—including SageMaker Model Monitor, the SageMaker Feature Store, the SageMaker Model Registry, the SageMaker Debugger, and SageMaker Canvas—are accessible only through SageMaker Studio.


--------------------------------------------------------------------------------


Conclusion: Build on a Strong Foundation

The thoughtful setup of SageMaker domains and user profiles is not just an administrative task—it is the foundation for a secure, efficient, and cost-effective machine learning platform. By understanding these nuances, you can avoid common pitfalls and empower your team to work more effectively.

Now that you know these details, what's one small change you can make to your team's SageMaker setup to better align with these best practices?

# 04 05 Sagemakerdomainsandstudio Part3 Breifing

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

# 04 05 Sagemakerdomainsandstudio Part3 Studyguide

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

