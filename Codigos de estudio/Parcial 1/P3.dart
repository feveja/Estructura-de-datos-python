import 'dart:io';
import 'dart:math';

void main() {
  List<int> lista1 = generarListaAleatoria(5);
  List<int> lista2 = ingresarListaPorTeclado(5);

  List<int> listaConcatenada = [...lista1, ...lista2];

  listaConcatenada.insertAll(6, [14, 20, 7]);

  double promedio = obtenerPromedio(listaConcatenada);

  listaConcatenada.sort((a, b) => b.compareTo(a));

  print('Lista generada aleatoriamente: $lista1');
  print('Lista ingresada por teclado: $lista2');
  print('Lista concatenada: $listaConcatenada');
  print('Promedio de la lista: $promedio');
  print('Lista ordenada de forma descendente: $listaConcatenada');
}

List<int> generarListaAleatoria(int longitud) {
  Random random = Random();
  List<int> lista = [];

  for (int i = 0; i < longitud; i++) {
    lista.add(random.nextInt(100));
  }

  return lista;
}

List<int> ingresarListaPorTeclado(int longitud) {
  List<int> lista = [];

  for (int i = 0; i < longitud; i++) {
    stdout.write('Ingrese el elemento ${i + 1}: ');
    int elemento = int.parse(stdin.readLineSync()!);
    lista.add(elemento);
  }

  return lista;
}

double obtenerPromedio(List<int> lista) {
  int suma = 0;

  for (int elemento in lista) {
    suma += elemento;
  }

  return suma / lista.length;
}
