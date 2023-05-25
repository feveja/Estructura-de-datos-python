import "dart:math";
void main() {
    List lista1 = [];
    List lista2 = [];
    List lista3 = [];
    //Llenar listas
    for (int i = 0; i<7 ; i++) {
      lista1.add(Random().nextInt(71) + 30);
      lista2.add(Random().nextInt(71) + 30);
      lista3.add(Random().nextInt(71) + 30);
    }
    print("Lista 1: $lista1 \nLista 2: $lista2 \nLista 3: $lista3");
    double promedio1 = 0;
    double promedio2 = 0;
    double promedio3 = 0;
    for (int i = 0; i<7; i++) {
      promedio1 += lista1[i];
      promedio2 += lista2[i];
      promedio3 += lista3[i];
    }
    promedio1 = promedio1/7;
    promedio2 = promedio2/7;
    promedio3 = promedio3/7;
    print("Los promedios son: \n-Lista 1: $promedio1 \n-Lista 2: $promedio2 \n-Lista 3: $promedio3");
    List promedios = [promedio1,promedio2,promedio3];
    print("Lista de promedios: $promedios");
}