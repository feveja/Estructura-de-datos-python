import 'dart:math';
import 'dart:io';

void main() {
  List<int> lista1 = generarListaAleatoria(5);
  List<int> lista2 = generarListaTeclado(5);
  print('Lista generada aleatoriamente: $lista1');
  print('Lista generada por teclado: $lista2');
  List<int> listaConcatenada = [...lista1, ...lista2];
  listaConcatenada.insertAll(6, [14, 20, 7]);
  listaConcatenada.sort((a, b) => b.compareTo(a));
  print('Lista concatenada: $listaConcatenada');
}

List<int> generarListaTeclado(int longitud) {
  List<int> lista = [];
  for (int i = 0; i < longitud; i++) {
    stdout.write('ingrese el elemento ${i+1}: ');
    int elemento = int.parse(stdin.readLineSync()!);
    lista.add(elemento);
  }
  return lista;
}

List<int> generarListaAleatoria(int longitud) {
  Random random = Random();
  List<int> lista = [];
  for (int i = 0; i < longitud; i++) {
    lista.add(random.nextInt(100));
  }
  return lista;
}
