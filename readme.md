# Face Detection using OpenCV

Face detection app using OpenCV

### Directory Structure

```
.
├── Backend
│   ├── Dockerfile
│   ├── __pycache__
│   │   ├── app.cpython-310.pyc
│   │   ├── app.cpython-38.pyc
│   │   └── app.cpython-39.pyc
│   ├── app.py
│   ├── haarcascade_frontalface_default.xml
│   ├── readme.md
│   ├── requirements.txt
│   ├── shots
│   │   └── pixiemj00
│   │       ├── pixiemj00-face.jpg
│   │       └── pixiemj00-feed.jpg
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── index.js
│   └── templates
│       └── index.html
└── readme.md

15 directories, 33 files

```

### Docker setup

```
cd Backend
docker build -t emmanuelallan/opencv-flask:1.0 .
docker run -p 5000:5000 emmanuelallan/opencv-flask:1.0
```

or

```
docker push emmanuelallan/opencv-flask:1.4
```
