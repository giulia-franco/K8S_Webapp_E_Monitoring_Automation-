
192.168.168.7

# K8S_Webapp_E_Monitoring_Automation
## Descrizione
Questo progetto ha l’obiettivo di creare un ambiente isolato per sperimentare e automatizzare il deploy di una web application su Kubernetes, integrando sistemi di monitoring avanzati.
L’ambiente viene creato con Vagrant per gestire VM locali, configurate tramite Ansible che si occupa del provisioning completo del cluster Kubernetes.
L’applicazione web è containerizzata con Docker, personalizzata per mostrare una spiegazione del progetto.
Il deploy automatico e continuo è gestito da Jenkins tramite pipeline che eseguono il build dell’immagine Docker e il deploy su Kubernetes con Helm.
Il sistema di monitoraggio include Prometheus e Grafana per raccogliere metriche e visualizzare dashboard interattive.

## Tecnologie utilizzate
- Vagrant – gestione VM per ambiente isolato
- Ansible – provisioning e configurazione cluster Kubernetes
- Kubernetes – orchestrazione container
- Docker – containerizzazione applicazione web
- Helm – gestione dei package Kubernetes (chart)
- Jenkins – automazione CI/CD (build e deploy)
- Prometheus – raccolta metriche monitoraggio
- Grafana – visualizzazione dashboard monitoraggio

## Funzionalità principali
- Creazione e configurazione automatica di VM con Vagrant
- Provisioning cluster Kubernetes con Ansible
- Build e deploy automatico dell’app Docker con Jenkins + Helm
- Monitoraggio in tempo reale con Prometheus e Grafana
- Personalizzazione dell’immagine Docker per visualizzare info progetto

## Prerequisiti
- Vagrant + VirtualBox (o altro provider)
- Ansible installato localmente
- Docker e Kubernetes (minikube/kind) configurati sulle VM (gestito da Ansible)
- Jenkins installato (può essere locale o su VM dedicata)

