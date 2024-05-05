# Ohjelmistotekniikka

## BudgetBuddy

App to plan your spendings with budgets. You can create as many budgets you need and update them later on. 

### dokumentation

- [user manual](https://github.com/eveliinaalikoski/ohte-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [description](https://github.com/eveliinaalikoski/ohte-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [architecture](https://github.com/eveliinaalikoski/ohte-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [testing document](https://github.com/eveliinaalikoski/ohte-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)
- [working hours](https://github.com/eveliinaalikoski/ohte-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [changelog](https://github.com/eveliinaalikoski/ohte-harjoitustyo/blob/master/dokumentaatio/changelog.md)

### installation

1. Install dependencies:

```bash
poetry install
```

2. Perform required base command:

```bash
poetry run invoke build
```

3. Start the app:

```bash
poetry run invoke start
```

### Optional commands

run program:

```bash
poetry run invoke start
```

perform tests:

```bash
poetry run invoke test
```

test coverage report:

```bash
poetry run invoke coverage-report
```

Pylint check

```bash
poetry run invoke lint
```
