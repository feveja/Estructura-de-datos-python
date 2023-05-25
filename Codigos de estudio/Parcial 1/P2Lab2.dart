import 'dart:io';
import 'dart:math';

void main() {
  // Primera lista
  List<int> lista1 = [14, 2, 5, 3, 9];

  // Segunda lista ingresada por teclado
  List<int> lista2 = [];
  print('Ingrese 5 números enteros para la segunda lista:');
  for (int i = 0; i < 5; i++) {
    int numero = int.parse(stdin.readLineSync()!);
    lista2.add(numero);
  }

  // Tercera lista con números aleatorios negativos
  List<int> lista3 = [];
  Random random = Random();
  for (int i = 0; i < 5; i++) {
    int numero = random.nextInt(11) - 25;
    lista3.add(numero);
  }

  // Restar la primera y segunda lista, y sumarla con la tercera lista
  List<int> resultado = [];
  for (int i = 0; i < 5; i++) {
    int resta = lista1[i] - lista2[i];
    int suma = resta + lista3[i];
    resultado.add(suma);
  }

  // Insertar elementos en la primera y segunda posición del resultado
  resultado.insert(0, 17);
  resultado.insert(1, 24);

  // Ordenar las listas de forma descendente
  lista1.sort((a, b) => b.compareTo(a));
  lista2.sort((a, b) => b.compareTo(a));
  resultado.sort((a, b) => b.compareTo(a));

  // Imprimir el resultado obtenido
  print('Resultado obtenido: $resultado');
}
