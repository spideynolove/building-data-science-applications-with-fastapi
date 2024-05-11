prompt = """
Write a github README for "building-data-science-applications-with-fastapi":
Write a github README for "building-data-science-applications-with-fastapi", tiếp theo với 5 chương từ 6 đến 10:

1. Python Programming Specificities
The goal of this chapter is thus to get you acquainted with its specificities, but we expect you already have some experience with programming.
In this chapter, we’re going to cover the following main topics:
• Basics of Python programming
• List comprehensions and generators
• Classes and objects
• Type hinting and type checking with mypy
• Asynchronous I/O

2. Developing a RESTful API with FastAPI
By the end of this chapter, you’ll know how to start a FastAPI application and how to write an API endpoint.
In this chapter, we’ll cover the following main topics:
• Creating the first endpoint and running it locally
• Handling request parameters
• Customizing the response
• Structuring a bigger project with multiple routers

3. Managing Pydantic Data Models in FastAPI
This chapter will cover in detail the definition of a data model with Pydantic, the underlying data validation library used by FastAPI.
In this chapter, we’re going to cover the following main topics:
• Defining models and their field types with Pydantic
• Creating model variations with class inheritance
• Adding custom data validation with Pydantic
• Working with Pydantic objects

4. Dependency Injection in FastAPI
In this chapter, we’ll focus on one of the most interesting parts of FastAPI: dependency injection.
In this chapter, we’re going to cover the following main topics:
• What is dependency injection?
• Creating and using a function dependency
• Creating and using a parameterized dependency with a class
• Using dependencies at the path, router, and global level

5. Databases and Asynchronous ORMs
The goal of this chapter is to show you how you can interact with different types of databases and related libraries inside FastAPI.
n this chapter, we’re going to cover the following main topics:
• An overview of relational and NoSQL databases
• Communicating with a SQL database with SQLAlchemy ORM
• Communicating with a MongoDB database using Motor

6. Managing Authentication and Security in FastAPI
In this chapter, we’ll see how FastAPI provides security dependencies to help us retrieve credentials by following different standards that are directly integrated into the automatic documentation.
In this chapter, we’re going to cover the following main topics:
• Security dependencies in FastAPI
• Retrieving a user and generating an access token
• Securing API endpoints for authenticated users
• Securing endpoints with access tokens
• Configuring CORS and protecting against CSRF attacks

7. Defining WebSockets for Two-Way Interactive Communication in FastAPI
The goal of this protocol is to open a communication channel between a client and a server so that they can exchange data in real time, in both directions.
In this chapter, we’re going to cover the following main topics:
• Understanding the principles of two-way communication with WebSockets
• Creating a WebSocket with FastAPI
• Handling multiple WebSocket connections and broadcasting messages

8. Testing an API Asynchronously with pytest and HTTPX
In this chapter, you’ll learn how to write tests for your FastAPI application, both for HTTP endpoints and WebSockets.
In this chapter, we’re going to cover the following main topics:
• An introduction to unit testing with pytest
• Setting up the testing tools for FastAPI with HTTPX
• Writing tests for REST API endpoints
• Writing tests for WebSocket endpoints

9. Deploying a FastAPI Project
Once that’s done, we’ll show you three ways to deploy your application: with a serverless cloud platform, with a Docker container, and with a traditional Linux server.
n this chapter, we’re going to cover the following main topics:
• Setting and using environment variables
• Managing Python dependencies
• Deploying a FastAPI application on a serverless platform
• Deploying a FastAPI application with Docker
• Deploying a FastAPI application on a traditional server

10. Introduction to Data Science in Python
In this chapter, we’ll introduce the fundamental concepts of machine learning before diving into the Python libraries used daily by data scientists.
In this chapter, we’re going to cover the following main topics:
• Understanding the basic concepts of machine learning
• Creating and manipulating NumPy arrays and pandas datasets
• Training and evaluating machine learning models with scikit-learn

11. Creating an Efficient Prediction API Endpoint with FastAPI
Of course, we now have to think about a convenient interface so that we can take advantage of their intelligence. This way, microservices or frontend applications can ask our model to make predictions to improve the user experience or business operations. In this chapter, we’ll learn how to do that with FastAPI.
In this chapter, we’re going to cover the following main topics:
• Persisting a trained model with Joblib
• Implementing an efficient prediction endpoint
• Caching results with Joblib

12. Implementing a Real-Time Object Detection System Using WebSockets with FastAPI
we’ll rely on Hugging Face, which is both a set of tools and a library of pretrained AI models.
In this chapter, we’re going to cover the following main topics:
• Using a computer vision model with Hugging Face libraries
• Implementing an HTTP endpoint to perform object detection on a single image
• Sending a stream of images from the browser in a WebSocket
• Showing the object detection results in a browser

13. Creating a Distributed Text-to-Image AI System Using the Stable Diffusion Model.
we’ll build our very own AI system to generate images from text prompts using the Stable Diffusion model.
In this chapter, we’re going to cover the following main topics:
• Using the Stable Diffusion model with Hugging Face Diffusers to generate images from
text prompts
• Implementing a worker process using Dramatiq and an image-generation task
• Storing and serving files in object storage

14. Monitoring the Health and Performance of a Data Science System
In this chapter, we will cover the extra mile so you are able to build robust, production-ready systems.
We’re going to cover the following main topics:
• Configuring and using a logging facility with Loguru
• Configuring Prometheus metrics and monitoring them in Grafana
• Configuring Sentry for reporting errors

"""