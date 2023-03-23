# Face Detection using OpenCV

Face detection app using OpenCV

### Directory Structure

```
.
├── Backend
│   ├── Dockerfile
│   ├── **pycache**
│   │   ├── app.cpython-310.pyc
│   │   ├── app.cpython-38.pyc
│   │   └── app.cpython-39.pyc
│   ├── app.py
│   └── requirements.txt
├── Frontend
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   │   └── vite.svg
│   ├── src
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── assets
│   │   │   └── react.svg
│   │   ├── index.css
│   │   └── main.jsx
│   └── vite.config.js
└── readme.md

6 directories, 17 files
```

### Docker setup

```
docker build -t emmanuelallan/opencv-flask:1.0 .
docker run -p 5000:5000 emmanuelallan/opencv-flask:1.0
```

or

```
docker push emmanuelallan/opencv-flask:1.3
```
