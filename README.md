# fastapi_practice

## make environment

```
uv venv
source .venv/bin/activate
```

## sync

```
uv pip sync requirements.txt
```

## start app

```
uv run fastapi run main.py
```

need it the below

```
uv pip install "fastapi[standard]"
```

## start app with uvicorn

```
uvicorn main:app
```