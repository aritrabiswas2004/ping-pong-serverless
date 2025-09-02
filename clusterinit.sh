#!/bin/bash

echo "================ INSTALL required custom resources ================"

kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.18.1/serving-crds.yaml

echo "================ INSTALL core components of Knative Serving ================"

kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.18.1/serving-core.yaml

echo "================ NETWORK: KOURIER ================"

kubectl apply -f https://github.com/knative/net-kourier/releases/download/knative-v1.18.0/kourier.yaml

kubectl patch configmap/config-network \
  --namespace knative-serving \
  --type merge \
  --patch '{"data":{"ingress-class":"kourier.ingress.networking.knative.dev"}}'

kubectl --namespace kourier-system get service kourier

echo "================ VERIFICATION OF INSTALLTION ================"

kubectl get pods -n knative-serving

echo "================ CONFIGURE DNS ================"

kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.18.1/serving-default-domain.yaml

echo "================ CREATE EXERCISES NAMESPACE ================"

kubectl create namespace exercises

echo "================ KUBECONFIG LAYOUT ================"

kubectl config view --minify --raw
