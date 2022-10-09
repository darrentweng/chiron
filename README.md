# Chiron
### "Wisest and justest of all the centaurs" ... A personal tutor in your pocket.

## How to Run

### On Streamlit Cloud

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://darrentweng-chiron-main-1sr32u.streamlitapp.com/)
### Run with Docker
Run the following commands to build the dev docker image and run the container that use local files throughout development process:
```
docker build -t trivia .
docker run -p 8501:8501 -v %cd%:/home/streamlit trivia
```
### Run with local Python
Create a new virtual environment and install the dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Run the app:
```bash
streamlit run Main.py
```

Then visit [localhost:8501](http://localhost:8501/)

## Inspiration

We were inspired by a lifelong love of trivia and game-based learning platforms such as Kahoot and Quizlet. At home, we have always loved learning new information and developing new thinking skills and at school, we enjoyed participating in class games such as Kahoot and utilized services such as Quizlets to study for quizzes and tests. We wanted to create a platform that would allow us to continue to learn and have fun while doing so. We also wanted to create a platform that would allow us to learn in a way that was more engaging and interactive than traditional learning methods.

## What it does

This project has two main functions: a trivia app, and a chatbot. Students and/or their teachers/tutors can upload questions and answers to the website and then practice those questions and answers on the website in a trivia format. The website counts how many right or wrong answers the user inputs so that they can know how they are doing. The chatbot interacts with the user to gauge their mood and helps to tailor a learning experience to each student. Currently. it can:
- let users play trivaial with 80,000+ questions
- allow uers to upload new questions
- chat with users
- detect the modes of users


## How we built it

To build this project, we used a mix of Streamlit and co:here. Streamlit allowed us to easily make the backend and frontend of the website through Python code. It also allows us to host the website on Streamlit Cloud for free. 

Co:here is a natural language processing tool that can be used to generate, categorize, and organize text. We employed prompt engineering techniques to create a conversational chatbot that could eventually encourage young users to learn while having fun. We also used cohere.classify to analyze the mood of students.

## Challenges we ran into

We had to learn how to use co:here and it took a while to learn prompt engineering because it is so new. It was also a bit of a challenge to find open-source trivia data and make it into a format that we can use. 

## Accomplishments that we're proud of

Successfully making a chatbot through `prompt engineering` with co:here, and integrate it into the website. We are also proud of the trivia app with 80,000+ open sourced trivia questions with the ability to add any number of new questions through upload. 

## What we learned

Co:here is a very versatile tool that can be manipulated to perform several services through prompt engineering
We learned more about Streamlit and how to host Streamlit applications on the cloud.

## What's next for Chiron

- Add multi-player support. It will be fun to play trivia with friends and family.
- Add user authentication support. We want to make sure that only the user can access their own data, and allow users to track their progress through time.
- Support more modes detection. Currently we only support happy, sad and confused, but we want to add more modes such as angry, excited, etc.
- Add a working leaderboard. We want to make it fun to compete with friends and family.
- Add OCR/AI to automatically add new questions/categories through uploaded images and/or websites
- Add AI-generated answers and questions.
