# Log Output Application

This application is split into `log-reader` and `log-writer`.

## Deployment (in `k3d`)

First create the PVC and PV

```shell
kubectl apply -f ping-pong/volumes # yes it is in ping-pong directory
```

then apply manifests

```shell
kubectl apply -f log-output/manifests
```
