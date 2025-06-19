# 🚀 Microservices Project on AWS EKS with Terraform, Docker, Kubernetes & CI/CD

A complete microservices application consisting of Django, Flask, and Spring Boot services deployed on AWS EKS using Terraform. This project includes infrastructure as code, containerization, orchestration, service discovery, Ingress routing, persistent storage, and CI/CD automation.

---

## 📂 Project Structure

```bash
├── terraform/                  # Infrastructure as Code (VPC, EKS)
├── auth-service/              # Django-based authentication microservice
├── data-service/              # Fast data API microservice
├── report-service/            # Java Spring Boot-based reporting microservice
├── ingress/                   # Ingress configuration for service routing
├── helm/                      # Helm charts for PostgreSQL and Redis
├── k8s-configs/               # ConfigMaps, Secrets, PVCs, Storage Classes
├── .github/workflows/         # GitHub Actions CI/CD workflows
└── README.md                  # Project documentation

📌 Features
 Infrastructure provisioning with Terraform (VPC, subnets, EKS)

 Containerization of Django, FastAPI, and Spring Boot apps

 Kubernetes deployments for each service

Helm charts for PostgreSQL and Redis

ConfigMaps and Secrets for secure configuration

NGINX Ingress for routing (/auth/*, /data/*, /report/*)

 GitHub Actions-based CI/CD pipeline


✅ Prerequisites
AWS account with programmatic access

AWS CLI configured (aws configure)

Tools installed: terraform, kubectl, eksctl, docker, helm, git

Docker Hub or Amazon ECR account

GitHub repository (if using CI/CD)

🛠️ Setup Instructions
1️⃣ Infrastructure Provisioning
'''bash
cd terraform
terraform init
terraform apply
'''
Creates VPC, public/private subnets, Internet Gateway, EKS cluster, IAM roles.

2️⃣ Configure AWS CLI & EKS Access
'''bash
aws eks --region <region> update-kubeconfig --name <eks-cluster-name>
kubectl get nodes
'''
3️⃣ Deploy PostgreSQL & Redis via Helm
'''bash
helm repo add bitnami https://charts.bitnami.com/bitnami

helm install my-postgresql bitnami/postgresql \
  --set auth.postgresPassword=mydbpass

helm install my-redis bitnami/redis \
  --set auth.password=myredispass
'''
4️⃣ Dockerize & Push Microservices
'''bash
# Auth Service (Django)
cd auth-service
docker build -t mayur702/loginapi .
docker push mayur702/loginapi:v1
'''
5️⃣ Deploy Services to Kubernetes
'''bash
kubectl apply -f ConfigMap.yaml
kubectl apply -f secret.yaml

kubectl apply -f LoginAP-deployment.yaml
kubectl apply -f LoginAp-svc.yaml

kubectl apply -f SimpleAPI-deployment.yaml
kubectl apply -f SimpleAPI-svc.yaml

kubectl apply -f Springboot-deployment.yaml
kubectl apply -f Springboot-svc.yaml

kubectl apply -f app-ingress.yaml
'''
7️⃣ Setup Ingress Controller
'''bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.0/deploy/static/provider/cloud/deploy.yaml
kubectl apply -f ingress/ingress.yaml
'''

Test access using:
'''bash
curl http://<external-ip>/auth/login
curl http://<external-ip>/data/info
curl http://<external-ip>/report/summary
'''






