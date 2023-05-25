void main() {
  List<dynamic> lista = ['a', 2, 0, 'b', 8, 'c'];

  // Imprimir solo los números de la lista omitiendo los caracteres
  for (var item in lista) {
    if (item is int) {
      print(item);
    }
  }
}
