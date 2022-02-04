az login


az group create -l eastus --name cloud-zaliczenie


az network vnet create --name cloud-zaliczenie --resource-group cloud-zaliczenie


az network vnet subnet create --name cloud-zaliczenie --resource-group cloud-zaliczenie --vnet-namecloud-zaliczenie --address-prefixes 10.0.0.0/16

az appservice plan create --name cloud-zaliczenie-plan --resource-group cloud-zaliczenie --location eastus

az webapp create --name cloud-zaliczenie --plan cloud-zaliczenie-plan --resource-group cloud-zaliczenie

az postgres flexible-server create --admin-password Pa$$w0rd12345 --admin-user rootadmin --database-name postgres --location eastus --name zaliczenoe-cloud --resource-group cloud-zaliczenie --storage-size 32 --public-access all --sku-name Standard_B1ms --tier Burstable --public-access 0.0.0.0

az postgres flexible-server create --admin-password Pa$$w0rd12345 --admin-user rootadmin --location eastus --name zaliczenoe-cloud --resource-group cloud-zaliczenie --storage-size 32 --public-access all --sku-name Standard_B1ms --tier Burstable --public-access 0.0.0.0
