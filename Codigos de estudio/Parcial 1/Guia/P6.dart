import 'dart:math';

void main() {
  List<int> a = [4, 3, 2, 2, 1];
  List<int> b = [-3, 2, 8, 0, 1];
  List<int> c = [];

  // Multiplicar las listas a y b
  for (int i = 0; i < a.length; i++) {
    c.add(a[i] * b[i]);
  }

  // Generar una nueva lista de 5 elementos aleatorios negativos
  Random random = Random();
  for (int i = 0; i < 5; i++) {
    c.add(-1 * (random.nextInt(5) + 1));
  }

  // Ordenar la lista en forma descendente
  c.sort((a, b) => b.compareTo(a));

  print(c); // Imprimir la lista resultante
}
