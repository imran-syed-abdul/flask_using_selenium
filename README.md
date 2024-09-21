### Step1

Replace syedimran1 with your docker username

```bash
docker build -t syedimran1/flask-1:latest .
```

### Step2

```bash
docker push -t syedimran1/flask-1:latest .
```

### Deploy

```bash
cf push flask-1 --docker-image syedimran1/flask-1:latest --docker-username syedimran1
```

### if the fails, make sure to increase disk size and instance memory in manifest.json
