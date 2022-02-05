Aplikacja działa bardzo prosto, prosi użytkownika o podanie ciągu znaków(domyślnie chodzi o jakieś imię), a następnie wyświetla je na ekranie. Aby nie przeciążać bazy danych, poniżej został umieszczony usuwający. Została napisana w django oraz korzysta z zewnętrznej bazy danych PostgreSQL. Aplikacja została skonteneryzowana oraz wrzucona na Docker Huba i to właśnie z niego pobierzemy obraz, który aplikacja będzie odpalać.

Aby utworzyć taka aplikację, najlepiej będzie podążać za komendami korzystając a azure CLI.

  1. Logujemy się na nasze konto Azure.

```bash
  az login
```

  2. Tworzymy grupę zasobów
```bash
az group create -l eastus --name cloud-zaliczenie
```

  3. Tworzymy bazę danych, nazwaną dokładnie tak jak w poleceniu. Literówka została wychwycona za późno, by warto było to naprawiać.
```bash
export PSQL_PASSWORD=blank
az postgres flexible-server create --admin-password $PSQL_PASSWORD --admin-user rootadmin --database-name cloud_name --location eastus --name zaliczenoe-cloud --resource-group cloud-zaliczenie --storage-size 32 --public-access all --sku-name Standard_B1ms --tier Burstable --public-access 0.0.0.0
```

  4. Następnie tworzymy naszą aplikację. Aby mogła ona zaistnieć potrzebny będzie "szkielet" w postaci Planu.
```bash
az appservice plan create --name cloud-zaliczenie-plan --resource-group cloud-zaliczenie --location eastus --is-linux
```
  
  5. Ostatni krok, czyli stworzenie aplikacji właściwej.
```bash
az webapp create --name zaliczenie-cloud --plan cloud-zaliczenie-plan --resource-group cloud-zaliczenie --deployment-container-image-name jakubjedrzejak2000/cloud-zaliczenie:latest
```
Teraz wchodzimy konkretnie pod ten link 
https://zaliczenie-cloud.azurewebsites.net/index/

Po wejściu w link trzeba będzie poczekać znaczną ilość czasu oraz możliwe, że trzeba będzie odświeżyć raz lub dwa, ale w końcu powinna się pojawić działająca aplikacja.


### Dodatkowe zasoby

- ([Docker hub](https://hub.docker.com/repository/docker/jakubjedrzejak2000/cloud-zaliczenie))
- ([Dokumentacja django](https://docs.djangoproject.com/en/4.0/))
- ([Azure CLI](https://docs.microsoft.com/pl-pl/cli/azure/reference-index?view=azure-cli-latest))


