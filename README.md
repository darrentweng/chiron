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

## To Do
- Add multi-player support
- Add user authentication support
- Add a leaderboard
- Add a way to add new questions/categories through uploaded files
- Add OCR/AI to automatically add new questions/categories through uploaded images and/or websites

