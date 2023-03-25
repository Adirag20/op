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
├── Frontend
│   ├── dist
│   │   ├── assets
│   │   │   ├── index-140bef59.css
│   │   │   ├── index-e0e1258e.js
│   │   │   └── react-35ef61ed.svg
│   │   ├── index.html
│   │   └── vite.svg
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── postcss.config.cjs
│   ├── public
│   │   └── vite.svg
│   ├── readme.md
│   ├── src
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── assets
│   │   │   └── react.svg
│   │   ├── components
│   │   │   └── Camera.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── tailwind.config.cjs
│   └── vite.config.js
└── readme.md

15 directories, 33 files

```

### Docker setup

```
docker build -t emmanuelallan/opencv-flask:1.0 .
docker run -p 5000:5000 emmanuelallan/opencv-flask:1.0
```

or

```
docker push emmanuelallan/opencv-flask:1.4
```
