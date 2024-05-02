# Teddy Note Study Files


## [Chapter 1.](./Chapter1/)
Download the Korean model from the hugging face and put it on Ollama, use LangServe to host it for free and finally, even a RAG demo.
<a href="https://www.youtube.com/watch?v=VkcaigvTrug">
<img  src="https://img.shields.io/badge/Youtube-FF0000?style=flat-square&logo=youtube&logoColor=FFFFFF" />
</a>
<a href="https://www.youtube.com/watch?v=VkcaigvTrug">
<img  src="https://img.shields.io/badge/Git-Hub-181717?style=flat-square&logo=github&logoColor=FFFFFF" />
</a>

 
## OLLAMA hosting
Terminal 1
```cmd
ngrok http --domain=delicate-weevil-exact.ngrok-free.app 8000
```
<br/>

---

Terminal 2
```cmd
cd app
python server.py
```
<br/>

## OLLAMA hosting + RAG

Terminal 1
```cmd
ngrok http --domain=delicate-weevil-exact.ngrok-free.app 8501
```
<br/>

---

Terminal 2 
```cmd
cd main_example
streamlit run main.py
```
<br/>

---

Terminal 3
```cmd
cd app
python server.py
```
<br/>
