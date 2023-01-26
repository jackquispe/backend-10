## Para correr la aplicacion 

Para correr la aplicacion de flask ejecutamos

```
flask --debug run
```

## Para ejecutar las migraciones
```
flask db init
flask db migrate -m "primera migracion"
flask db upgrade
```