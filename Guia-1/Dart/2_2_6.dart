// ignore_for_file: unused_local_variable

import 'dart:math';

void main() {
  List<int> a = [4, 3, 2, 2, 1];
  print("la primera lista es: $a");
  List<int> b = [-3, 2, 8, 0, 1];
  print("la segunda lista es: $b");
  List<int> c = [];
  for (int i = 0; i < 5; i++) {
    int numerito = a[i] * b[i];
    c.add(numerito);
  }
  print("la multiplicacion de las primeras listas es: $c");
  List<int> d = [];
  for (int i = 0; i < 5; i++) {
    int numerito = Random().nextInt(5) - 5;
    d.add(numerito);
  }
  print("la tercera lista es: $d");
  c.addAll(d);
  print("la concatenacion de las listas es: $c");
}
