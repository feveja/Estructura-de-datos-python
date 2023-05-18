import 'dart:math';

void main() {
  List<int> lista1 = [3, 4, 7, 9, 8, 5, 1, 2, 5, 7];
  List<int> lista2 = generarListaAleatoria(10, -1, -5);

  print(lista1);
  print(lista2);
}

List<int> generarListaAleatoria(int cantidad, int rangoMin, int rangoMax) {
  Random random = Random();
  List<int> lista = [];

  for (int i = 0; i < cantidad; i++) {
    int numeroAleatorio = random.nextInt(rangoMax - rangoMin + 1) + rangoMin;
    lista.add(numeroAleatorio);
  }

  return lista;
}
