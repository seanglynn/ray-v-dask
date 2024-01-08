# 1. Ray base image
FROM rayproject/ray:latest as ray-base

# Install ray[data,train,tune,serve]
RUN pip install -U "ray[data,train,tune,serve]"

CMD ["bash", "-c", "ray start --head --num-cpus 1 --dashboard-host 0.0.0.0 --include-dashboard true --block"]

# 2. Ray notebook image
## Extend base image; add notebook
FROM ray-base as ray-notebook

# Install jupyterhub
RUN pip install jupyterlab notebook

# Set notebook home
ENV HOME=/home/jovyan
WORKDIR $HOME

# Expose webUI
EXPOSE 8888

RUN jupyter notebook --generate-config

ENV CONFIG_PATH="/root/.jupyter/jupyter_notebook_config.py"

COPY "jupyter_notebook_config.py" ${CONFIG_PATH}

ENTRYPOINT ["sh", "-c", "jupyter notebook --allow-root -y --no-browser --ip=0.0.0.0 --config=${CONFIG_PATH}"]