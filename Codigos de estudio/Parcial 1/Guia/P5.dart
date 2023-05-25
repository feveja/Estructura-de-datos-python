import 'dart:math';

void main() {
  List<List<int>> listas = [];

  for (int i = 0; i < 3; i++) {
    List<int> lista = [];
    Random random = Random();
    
    for (int j = 0; j < 7; j++) {
      int numeroAleatorio = random.nextInt(71) + 30; // Generar número aleatorio entre 30 y 100
      lista.add(numeroAleatorio);
    }

    listas.add(lista);
  }

  List<double> promedios = [];

  for (var lista in listas) {
    double promedio = lista.reduce((a, b) => a + b) / lista.length;
    promedios.add(promedio);
  }

  print(promedios);
}
