# Dask Cluster Introduction
Local development environment for exploring [Dask](https://www.dask.org/).

## Dask
Dask is a Python library for parallel and distributed computing.

### Get Started
A docker compose file was created to configure the cluster for us. You can start it as follows:
```
docker-compose -f dask-docker-compose.yaml up
```
Or optionally run in detatched mode by adding -d.

The notebook dashboard should now be accessible here: http://localhost:8888

When the notebook is deployed, follow the [10 minutes to Dask tutorial](https://docs.dask.org/en/stable/10-minutes-to-dask.html).

Once you are done, tear down the cluster with
```
docker-compose -f dask-docker-compose.yaml down
```
## ML Integrations

https://ml.dask.org/

https://ml.dask.org/modules/generated/dask_ml.model_selection.GridSearchCV.html

https://ml.dask.org/hyper-parameter-search.html#neither-compute-nor-memory-constrained


