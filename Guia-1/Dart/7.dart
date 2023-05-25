void main() {
  List<dynamic> lista = ['a', 2, 0, 'b', 8, 'c'];
  
  for (var elemento in lista) {
    if (elemento is int) {
      print(elemento);
    }
  }
}
