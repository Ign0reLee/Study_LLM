from langserve import RemoteRunnable

chain = RemoteRunnable("https://0.0.0.0:8000/prompt/")