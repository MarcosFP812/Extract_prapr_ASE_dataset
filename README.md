# Extract_prapr_ASE_dataset
 
La finalidad de este repositorio es extraer los datos del dataset (...) para un futuro entrenamiento de un modelo de APR. En este repositorio encontramos, como se dice en el paper (...), 3 datasets diferentes:

- ASE_patches
- prapr_patches_1.2
- prapr_patches_2.0

## Formas de extraer los datos

Para la extracción de los datos lo hemos realizado de 2 formas diferentes.

### Obtener solo el parche

El código para su obtención está en la carpeta src1. En este caso nos queremos quedar unicamente con los archivos src.patch que se encuentran en el último directorio del dataset en cuestión. Para los dataset de ASE y prapr es identica la extracción.

Se almacenará con el json:
```python=
{
'path':,
'content':,
'correct':,
'Not_overlap':
}
```

### Obtener los codigos enteros orginal-fixed

El código se encuentra en la carpeta src2. En este caso distinguimos si es el archivo original cuando empieza por 'ori-' y el corregido cuando empiezz por 'fixed-' o 'man-', en caso de que no existan esos dos anteriores será el que empiece por 'patched-' 

```python=
{
'path':,
'original':,
'fixed':,
'correct':
}
```
