# 1. Ray base image
FROM rayproject/ray:latest as ray-base

# Install ray[data,train,tune,serve]
RUN pip install -U "ray[data,train,tune,serve]"

CMD ["bash", "-c", "ray start --head --num-cpus 1 --dashboard-host 0.0.0.0 --include-dashboard true --block"]

# 1. Ray notebook image
## Extend base image; add notebook
FROM ray-base as ray-notebook

# Install jupyterhub
RUN pip install jupyterlab notebook

# Set notebook home
ENV HOME=/home/jovyan
WORKDIR $HOME

# Expose webUI
EXPOSE 8888

# Init
CMD ["jupyter lab --ip=0.0.0.0 --no-browser --allow-root"]
