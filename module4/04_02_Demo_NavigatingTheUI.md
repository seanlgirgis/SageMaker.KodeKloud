# .\04 02 Demo NavigatingTheUI

# 04 02 Demo Navigatingtheui Blogpost

Don't Click That Button: 3 Truths About AWS SageMaker Newcomers Need to Know

Let's be honest: opening the AWS SageMaker console for the first time is like staring at an airplane's flight deck. The sheer number of dials, menus, and options is enough to make anyone wonder, "Where do I even start?"

What's surprising is that the most important lessons for getting started aren't found in any of the console's menus or buttons. In fact, approaching the console with the wrong assumptions can lead to confusion and frustration. This article will share three key takeaways that will fundamentally change how you approach the platform, making your learning journey smoother and more productive from day one.

1. The Console is a Dashboard, Not a Cockpit

The most counter-intuitive reality of SageMaker is that despite the complex web interface, your primary work is not done by clicking buttons in the console. It may look like a control panel where you actively drive every step, but its real purpose is much more passive.

SageMaker is fundamentally a "code-first" product. The creation of data processing jobs, model training jobs, and other core machine learning tasks is driven from Python code, where you'll use tools like the SageMaker SDK and objects like the Estimator to define, launch, and manage your ML workflows. You write code to define and launch a job, and SageMaker provisions and manages the underlying infrastructure to execute it. The main purpose of the web UI is to monitor the progress and status of these jobs after you've initiated them from your code. Think of it as a place to check on your running processes, not the place to build them.

Your day-to-day actions are not going to be driven by the UI.

This code-first principle is also the reason for another common point of confusion for newcomers: a seemingly empty console.

2. An Empty Interface is a Good Sign

A common point of confusion for new users is logging in and seeing nothing. You click on "Processing jobs," "Training jobs," or "Models," and the lists are completely empty. This can feel like something is wrong or that you've missed a setup step.

Your first instinct might be that something is broken. It's not. This blank slate is not just normal; it's a sign that you're in the right place, ready to command the platform from your code. The SageMaker console is not pre-populated with examples or templates in these sections. The interface only populates with entities like training jobs or models after you have successfully initiated them from your code. An empty dashboard simply means you haven't run any jobs yet. It’s a blank slate waiting for your first command.

The interface felt kind of empty and it will feel that way until you populate it with jobs that you have initiated from your code.

So if the console is just a status screen, where does the real work happen? That brings us to your true starting point: the notebook.

3. Understanding 'Legacy' is the Key to 'Studio'

When you navigate to the "Notebooks" section to start writing code, you will see prominent suggestions to use the newer "SageMaker Studio." This can be a bit confusing, as it presents you with two paths: the older "Notebook Instance" method and the modern "Studio" environment.

Understanding the history here is crucial. When SageMaker first launched, the only way to get a Jupyter notebook was by launching a standalone "Notebook Instance." The newer, more integrated, and strongly recommended environment is SageMaker Studio, which came later. Understanding the limitations and workflow of the older method helps you appreciate why Studio is the preferred path for modern development. This isn't just a cosmetic upgrade. A legacy Notebook Instance is a full managed virtual machine that can take up to five minutes to provision and for which you are billed every second it's running. Studio, by contrast, is a more integrated and efficient development environment, allowing you to get to your code faster and avoid paying for idle compute.

When Sagemaker started, we didn't have Sagemaker Studio. Sagemaker Studio came later and thankfully is way, way better.

Conclusion: Your True Starting Point

Ultimately, mastering SageMaker is about a mental shift. Once you see the console as your mission control dashboard and the notebook as your cockpit, the entire platform unlocks its true power. Remember that the web console is primarily for monitoring, not for hands-on creation. Don't be concerned by an empty interface—it’s a sign you’re ready to start building. And finally, embrace the modern SageMaker Studio environment, understanding that it represents a significant evolution from the platform's earlier days. Your true starting point isn't in a web form, but in a notebook, ready for your first line of code.

Now that you know the UI is for watching and the notebook is for doing, what's the first problem you're ready to solve with SageMaker?

# 04 02 Demo Navigatingtheui Breifing

Navigating the SageMaker AI User Interface: A Synthesis

Executive Summary

This document synthesizes a demonstration on navigating the Amazon SageMaker AI user interface. The primary focus is on understanding the core components of the SageMaker console and the process for creating and accessing "legacy" Jupyter Notebook instances. A central theme is the distinction between these legacy instances and the newer, highly recommended SageMaker Studio.

The key takeaway is that SageMaker is fundamentally a "code-first product." The primary workflow for a data scientist or ML engineer is driven by Python code within a Jupyter notebook, using the SageMaker SDK. The web-based UI serves mainly as a monitoring tool to check the status of entities like data processing jobs, model training jobs, and deployed endpoints, rather than as a primary interface for executing tasks. The demonstration methodically walks through the UI to locate these key components and provides a detailed, step-by-step guide to provisioning a legacy notebook instance, highlighting crucial configuration choices regarding compute resources and security permissions.

I. Introduction to the SageMaker Environment

The AWS environment for machine learning offers two primary Sagemaker services:

* Amazon SageMaker AI: The original product, available since approximately 2016. It is used for developing, training, and hosting machine learning models. The demonstration focuses entirely on this service.
* Amazon SageMaker Platform: A newer offering introduced in mid-2024. It builds upon SageMaker AI by adding enhanced data governance and deeper integration with data warehousing and data lakes. All functionalities of SageMaker AI are available within the SageMaker Platform.

II. Core Components of the SageMaker AI Console

The SageMaker AI console's left-hand navigation bar provides access to the key entities involved in the machine learning lifecycle. For a new account, many of these sections will appear empty until jobs are initiated via code.

Section	Component	Purpose & Description
Applications and IDEs	Notebooks	Provides access to Jupyter environments. The demonstration focuses on "Notebook instances," the legacy method for launching a managed virtual machine with a Jupyter server.
Processing	Processing jobs	Lists data processing tasks, such as data preparation and cleanup jobs. These are typically initiated from code to prepare data for model training.
Training	Training jobs	Lists all initiated machine learning model training processes. The interface displays their duration and completion status (e.g., Completed, Failed). These are typically launched from code using the SageMaker SDK's Estimator object.
Inference	Models	A registry of model artifacts created from successful training jobs. Until a model is trained and registered, this section will be empty.
Inference	Endpoints	Shows currently deployed models that are being hosted on managed instances for real-time predictions. An endpoint makes a model available to provide inference.

Key Insight: "The interface felt kind of empty and it will feel that way until you populate it with jobs that you have initiated from your code. Remember, we are really a code first product."

III. Legacy Notebook Instances vs. SageMaker Studio

A critical distinction is made between two methods of working with Jupyter notebooks in SageMaker:

* Legacy Notebook Instances: When SageMaker first launched, this was the only method available. It involves creating a dedicated, managed virtual machine (an EC2 instance) that runs a Jupyter server. The demonstration focuses on this method to provide historical context and demystify the platform's evolution.
* SageMaker Studio: The modern, integrated development environment (IDE) for machine learning in SageMaker. It is presented as a vastly superior and strongly recommended alternative to legacy instances. The UI itself displays a prominent banner encouraging users to adopt Studio.

Direct Recommendation: "Try the new Jupyter Lab in Sagemaker Studio. This is excellent advice and I would strongly encourage you if you're going to use Sagemaker, to use Sagemaker Studio... When Sagemaker started, we didn't have Sagemaker Studio. Sagemaker Studio came later and thankfully is way, way better."

IV. Demonstration: Creating a Legacy Notebook Instance

The demonstration provides a detailed walkthrough of provisioning a legacy notebook instance.

1. Configuration and Naming The process begins by navigating to Notebooks > Notebook instances and clicking "Create notebook instance." A unique name is provided, such as KodeKloud-legacy-Jupyter.

2. Instance Sizing Users must select a compute instance type, which determines the vCPUs and RAM of the underlying virtual machine. The demonstration shows two examples:

* t3.medium: A burstable CPU type suitable for non-intensive workloads, providing 2 vCPUs and 4 GB of RAM.
* c5.xlarge: A more powerful option with 4 vCPUs and 8 GB of RAM, running on an Intel Xeon Platinum processor. The presenter recommends using external tools like the Vantage.sh website to quickly look up the specifications and pricing for different AWS instance types.

3. Platform and Software Selection The desired JupyterLab version can be selected. The recommendation is to use the latest available version, which was Jupyter Lab 4 at the time of the demonstration.

4. IAM Role and Permissions Configuration An IAM (Identity and Access Management) role must be attached to the notebook instance. This role grants the instance permissions to interact with other AWS services, such as S3.

* Purpose: The IAM role acts like a security context for the instance. Any code running inside the notebook will inherit the permissions granted by the role.
* Creation: The demo uses the "Create a new role" option. For simplicity, it grants access to "Any S3 bucket."
* Security Warning: It is explicitly stated that granting access to any bucket is not good security practice. In a production environment, permissions should be narrowed to only the specific S3 buckets required for the project.

5. Launch and Activation After creation, the instance enters a "Pending" state, which can last for up to five minutes. Once ready, its status changes to "In Service."

* Billing: It is critical to note that billing for the instance begins as soon as it is "In Service." Unused instances should always be shut down or deleted to avoid unnecessary costs.

V. Accessing and Utilizing Jupyter Environments

Once the instance is "In Service," two options are available to access the development environment: "Open Jupyter" and "Open JupyterLab."

Jupyter Interface (Classic)

* This is the original Jupyter interface.
* It is functional but limited, primarily allowing work on a single file at a time.
* The demo shows a basic notebook (untitled.ipynb) being created and simple Python code (a=7; b=3; print(a+b)) being executed to confirm functionality.

JupyterLab Interface (Modern)

* JupyterLab provides a more modern and feature-rich IDE experience.
* Multi-Tab Environment: Its primary advantage is the ability to have multiple tabs open simultaneously, including different notebooks, data files (like CSVs), and system terminals.
* Terminal Access: Users can open a terminal directly into the underlying instance to perform shell commands, such as pip list to view installed Python packages.
* Extensibility: JupyterLab can be enhanced with extensions. The demo highlights a built-in Git extension for cloning repositories and managing source control directly within the environment.
* Sample Notebooks: The environment often comes with pre-built sample notebooks, demonstrating various algorithms and features, which can be explored and executed.

On the value of Jupyter: "Notice how neat it is because they're making really good use of markdown to render it neatly. And This is why I love Jupiter so much. Because of that kind richness of mixing your code and mixing your documentation, your annotations with it."

VI. The Code-First Workflow Philosophy

The demonstration concludes by reinforcing the core operational paradigm of SageMaker.

* Primary Driver: The day-to-day workflow is not driven by clicks in the UI but by executing Python code within a Jupyter notebook.
* UI's Role: The web console's main purpose is for monitoring. It is the place to check the progress of a long-running training job or to see if a data processing job has completed successfully.
* Code-Based Initiation: Actions like starting a training job are initiated programmatically, for example, by using the Estimator object from the SageMaker Python SDK.

Concluding Advice: "Don't get too concerned about the web interface. Your workflow will be driven from your Jupyter notebook and your code. And generally you'll only be coming back to the web interface to check on progress... Your day-to-day actions are not going to be driven by the UI."

# 04 02 Demo Navigatingtheui Studyguide

Study Guide: Navigating the SageMaker AI User Interface

This guide is designed to review and reinforce understanding of the Amazon SageMaker AI user interface, its core components, and the workflow for setting up development environments as demonstrated in the source material.

Quiz

Answer the following questions in 2-3 sentences each based on the provided source context.

1. What is the key difference between Amazon SageMaker AI and the Amazon SageMaker Platform?
2. Explain the primary distinction between a legacy Jupyter Notebook Instance and the newer SageMaker Studio.
3. Where in the SageMaker AI navigation bar would you look to monitor the status of data preparation tasks, and what information can be found there?
4. In the context of SageMaker, what is the relationship between a "model" and an "endpoint"?
5. What is an IAM Role, and why is it a necessary component when creating a notebook instance?
6. Describe the advantage of using the JupyterLab interface over the classic Jupyter interface within a notebook instance.
7. What does it mean when a notebook instance's status is "In Service," and what important consideration comes with this status?
8. The source material describes SageMaker as a "code first product." What does this imply about the primary role of the web UI versus a Jupyter notebook in a typical workflow?
9. When creating a notebook instance, what is an "instance type" and how can a user determine the specific resources (like vCPUs and RAM) associated with it?
10. If a user is navigating the SageMaker console for the very first time, what would they typically find in the "Training jobs" section and why?


--------------------------------------------------------------------------------


Answer Key

1. Amazon SageMaker AI is the original product, launched around 2016, for developing, training, and hosting machine learning models. The Amazon SageMaker Platform, introduced in mid-2024, integrates SageMaker AI with superior data governance and better integration with data warehousing and data lakes.
2. A legacy Jupyter Notebook Instance is a managed virtual machine that runs a Jupyter server; it was the original way to use notebooks in SageMaker. SageMaker Studio is the newer, strongly recommended development environment that provides a more modern, complete, and superior implementation of JupyterLab.
3. You would look under the "Processing" section in the navigation bar to find "Processing jobs." This area shows a history of data processing jobs, such as data cleanup tasks, along with their status (e.g., completed, failed) and duration.
4. A "model" is the artifact created after a training job has completed successfully; it is the trained algorithm. An "endpoint" is a deployed, managed instance that hosts a model, making it available to provide real-time predictions (or inference).
5. An IAM Role is a security context, similar to a user account, that has policies attached to it conferring permissions to interact with other AWS services like S3. It is attached to the notebook instance to ensure any code running inside it operates under that specific security context and has the necessary permissions.
6. The JupyterLab interface is more modern and allows a user to work on multiple files at once, such as several notebooks or a notebook and a CSV file. It also provides the ability to open a terminal into the underlying instance and can be extended with additional functionality through extensions.
7. An "In Service" status indicates that the notebook instance is fully up and running and ready for use. This status also means that the user is actively being billed for the instance, so it is important to shut down or delete instances when they are not in use to manage costs.
8. Being a "code first product" means the user's day-to-day workflow and actions, such as initiating processing or training jobs, are driven primarily from Python code within a Jupyter notebook. The web UI is generally used for secondary tasks like checking on the progress and status of these jobs.
9. An "instance type" (e.g., t3.medium, c5.xlarge) defines the computational resources of the managed virtual machine, such as the number of vCPUs and the amount of RAM. A user can find the exact specifications for an instance type by using external tools like the Vantage.sh website, which provides detailed pricing and spec information.
10. A first-time user would find the "Training jobs" section to be empty. This is because the interface only populates with entries after the user has initiated training jobs from their code, typically using the SageMaker SDK and an Estimator object.


--------------------------------------------------------------------------------


Essay Questions

Construct detailed, essay-format answers to the following prompts. Answers are not provided.

1. Discuss the evolution of development environments within SageMaker, comparing the legacy notebook instances with the newer SageMaker Studio. Why is Studio strongly recommended, and what historical context makes understanding the legacy instances still valuable?
2. Walk through the entire lifecycle of a machine learning asset as presented in the SageMaker UI navigation. Describe where you would find information related to data preparation, model training, the resulting model artifact, and its deployment for real-time predictions.
3. Explain the role of infrastructure and security in the process of setting up a Jupyter Notebook Instance. Cover the concepts of managed virtual machines, instance types (e.g., T3, C5), and the function and configuration of IAM roles for granting permissions.
4. Describe the user experience and functionality of JupyterLab within a SageMaker notebook instance. What features, such as terminal access, Git integration, and multi-tab editing, contribute to a more comprehensive development environment compared to the classic Jupyter interface?
5. The presenter emphasizes that the SageMaker UI is primarily for monitoring rather than daily interaction. Elaborate on this "code first" philosophy, explaining how tasks are typically initiated and what role the SageMaker SDK plays in this workflow.


--------------------------------------------------------------------------------


Glossary

Term	Definition
Amazon SageMaker AI	The original SageMaker product, available since circa 2016, used for developing, training, and hosting machine learning models.
Amazon SageMaker Platform	A newer service introduced in mid-2024 that encompasses SageMaker AI but adds enhanced data governance and integration with data warehouses and data lakes.
AWS Web Management Console	The primary web interface used to administer and manage all services within Amazon Web Services, including SageMaker.
Endpoint	A deployed, managed instance that hosts a trained model. Its purpose is to make the model available to provide real-time predictions, a process known as inference.
Estimator Object	A component of the SageMaker SDK used within Python code to represent and launch a machine learning training job.
IAM Role	An Identity and Access Management (IAM) role is a security context with attached permission policies. It is assigned to an AWS resource, such as a notebook instance, to grant it the necessary permissions to interact with other AWS services (e.g., S3 buckets).
Inference	The process of using a trained machine learning model to make predictions. In SageMaker, this is facilitated by deploying models to endpoints.
Jupyter	The classic web-based interactive interface for notebooks. It is noted as being more limited, typically allowing a user to work on only one file at a time.
JupyterLab	A more modern, feature-rich, web-based integrated development environment (IDE). It supports working with multiple tabs and files simultaneously, includes terminal access, and can be customized with extensions.
Model	An artifact created as the result of a successful machine learning training job. These are listed in the SageMaker UI under the "Inference" section.
Notebook Instance	The legacy method for creating a development environment in SageMaker. It consists of a managed virtual machine (an EC2 instance) that runs a Jupyter server, which can be accessed via a web browser.
Processing Job	A task executed in SageMaker, typically for preparing data (e.g., data cleanup) before it is used for model training. The history of these jobs is viewable in the UI.
SageMaker Studio	The modern, recommended IDE for SageMaker. It provides a more complete and superior implementation of JupyterLab and is the preferred way of working with notebooks.
Training Job	The process of training a machine learning model using a specified algorithm and dataset. The status and history of these jobs are listed under the "Training" section of the SageMaker UI.

