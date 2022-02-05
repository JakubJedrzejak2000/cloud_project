Aplikacja działa bardzo prosto. Została napisana w django oraz korzysta z zentrznej bazy danych PostgreSQL.

```
  az login
```

az group create -l eastus --name cloud-zaliczenie

az postgres flexible-server create --admin-password 'Pa$$w0rd12345' --admin-user rootadmin --database-name cloud_name --location eastus --name zaliczenoe-cloud --resource-group cloud-zaliczenie --storage-size 32 --public-access all --sku-name Standard_B1ms --tier Burstable --public-access 0.0.0.0

az appservice plan create --name cloud-zaliczenie-plan --resource-group cloud-zaliczenie --location eastus --is-linux

az webapp create --name zaliczenie-cloud --plan cloud-zaliczenie-plan --resource-group cloud-zaliczenie --deployment-container-image-name jakubjedrzejak2000/cloud-zaliczenie:latest
