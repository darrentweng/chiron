# Streamlit Trivia



## Development with Docker
Run the following commands to build the dev docker image and run the container that use local files throughout development process:
```
docker build -t trivia .
docker run -p 8501:8501 -v %cd%:/home/streamlit trivia
```

## Package with Docker
Run the following command to build the production docker image and test run it:
```
docker build -t trivia .
docker run -p 8501:8501 trivia  # can be launched anywhere, no need to mount local files
```
Then visit [localhost:8501](http://localhost:8501/)

## Inspiration

We were inspired by a lifelong love of trivia and game-based learning platforms such as Kahoot and Quizlet. At home, we have always loved learning new information and developing new thinking skills and at school, we enjoyed participating in class games such as Kahoot and utilized services such as Quizlets to study for quizzes and tests.

## What it does

This project has two main functions: a trivia app, and a chatbot. Students and/or their teachers/tutors can upload questions and answers to the website and then practice those questions and answers on the website in a trivia format. The website counts how many right or wrong answers the user inputs so that they can know how they are doing. The chatbot interacts with the user to gauge their mood and helps to tailor a learning experience to each student.

## How we built it

To build this project, we used a mix of Streamlit and co:here. Using Streamlit, we could easily make the backend and frontend of the website and host the website on Streamlit’s free cloud. We used co:here to create our chatbot. Co:here is a natural language processing tool that can be used to generate, categorize, and organize text. We used prompt engineering to generate text off of conversation and analyze the mood of students.

## Challenges we ran into
We had to learn how to use co:here and it took a while to learn prompt engineering because it is so new. It was also a bit of a challenge to find open-source trivia data and make it into a format that we can use. 

## Accomplishments that we're proud of

Successfully making a chatbot through prompt engineering using co:here
Launching the streamlit app and connecting it to our domain.

## What we learned

Co:here is a very versatile tool that can be manipulated to perform several services through prompt engineering
We learned more about Streamlit and how to host Streamlit applications on the cloud.

## What's next for Chiron

Add multi-player support
Add user authentication support
Add a working leaderboard
Add a way to add new questions/categories through uploaded files
Add OCR/AI to automatically add new questions/categories through uploaded images and/or websites
Add text generation for explanations to answers.
Add AI-generated answers to questions


