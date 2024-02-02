# Ray + Dask Cluster Introduction
Local development environment for exploring [Ray](https://www.ray.io/) v [Dask](https://www.dask.org/).

## Ray
[Ray Core](https://docs.ray.io/en/latest/ray-core/walkthrough.html) provides a small number of core primitives (i.e., tasks, actors, objects) for building and scaling distributed applications.

### Get Started
A docker compose file was created to configure the cluster for us. You can start it as follows:
```
docker-compose -f ray-docker-compose.yaml up
```
Or optionally run in detached mode by adding -d.

The Ray dashboard should now be accessible here: http://localhost:8265

When the Ray notebook container is deployed, open the jupyter notebook UI: http://localhost:8888 
Follow the [A Gentle Introduction to Ray Core by Example tutorial](notebooks/ray.ipynb) notebook.

Once you are done, tear down the cluster with
```
docker-compose -f ray-docker-compose.yaml down
```

## Ports
The following ports are exposed by default:
* ```8265```    Ray dashboard
* ```6379```    Reddis port to allow external workers to join (optional)
* ```10001```   Head node access port to connect external Ray client (optional)

# Connect to Cluster
The following is a minimum working example to connect to the cluster head node **
```
import ray
ray.init(address='ray://<head_node_ip_address>:10001')
```

For more information on Ray:
* https://www.ray.io/
* https://github.com/ray-project/ray



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