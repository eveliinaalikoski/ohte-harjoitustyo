# Ohjelmistotekniikka

## BudgetBuddy

### dokumentation

- [working hours](https://github.com/eveliinaalikoski/ohte-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [description](https://github.com/eveliinaalikoski/ohte-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [changelog](https://github.com/eveliinaalikoski/ohte-harjoitustyo/blob/master/dokumentaatio/changelog.md)

### installation

1. Install dependencies:

```poetry install```

2. Perform required base command:

```poetry run invoke build```

3. Start the app:

```poetry run invoke start```

### Optional commands

run program:

```poetry run invoke start```

perform tests:

```poetry run invoke test```

test coverage report:

```poetry run invoke coverage-report```

Pylint check

```poetry run invoke pylint```
