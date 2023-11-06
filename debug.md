# Debug on local machine

## environment preparation, and dependencies install

``` bash
virtualenv  ../python/agent-env --python python3.10
source ../python/agent-env/bin/activate

pip install pydantic fastapi typer uvicorn pyautogen
```

## start server

```bash
export OPENAI_API_KEY=sk-xxxx
export OPENAI_API_BASE=
python -m autogenui.cli
```

## common used libraries

```bash
pip install matplotlib panda tushare yfinance
```

## Enable Docker, 

```bash
pip install docker
```

```bash
vim autogenui/manager.py
```

Update code_execution_config to enable docker for running autogen.