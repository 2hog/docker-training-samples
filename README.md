# Sample Docker Microservices

This is a set of example microservices written in Django, Flask and Sinatra intended to be used as part of 2hog's Docker trainings.

## Spec
The [front-facing Django service](./docker-training-samples-micro-django) provides a sign in mechanism along with a single endpoint (`GET /`), which:

1. Requires session authentication
2. Requests a greeting via a `POST` request to the [**greeting** service](./docker-training-samples-micro-sinatra)
3. Passes the provided greeting via a `GET` URL parameter to the [**content** service](./docker-training-samples-micro-flask)
4. Returns the received HTML fragment as part of a complete HTML document to the user

## Deployment

Before deploying these apps with Docker Swarm or Kubernetes, make sure to build their images by running the following command

```sh
docker-compose build
```

### Docker Swarm

```sh
docker stack deploy -c docker-compose.yml docker-training-samples
```

### Kubernetes

```sh
kubectl apply -f docker-training-sample-micro-sinatra/kube -f docker-training-sample-micro-flask/kube -f docker-training-sample-micro-django/kube
```

## License

This software is [MIT licensed](LICENSE).