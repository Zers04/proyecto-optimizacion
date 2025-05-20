int: N = 12;
int: M = 5;

array[1..M] of tuple(string, int, int): ciudades = [
  ("Palmira", 2, 3),
  ("Cali", 10, 2),
  ("Buga", 11, 0),
  ("Tulua", 0, 3),
  ("RioFrio", 1, 2)
];

var 0..N: concert_x;
var 0..N: concert_y;

array[1..M] of var 0..22: distances;

constraint
  forall(i in 1..M)(
    distances[i] = abs(concert_x - ciudades[i].2) + abs(concert_y - ciudades[i].3)
  );

constraint
  forall(i in 1..M)(
    concert_x != ciudades[i].2 \/ concert_y != ciudades[i].3
  );

var 0..22: max_distance;
constraint max_distance = max(distances);

solve minimize max_distance;

output [
  "Concierto en: (", show(concert_x), ", ", show(concert_y), ")\n",
  "Distancia máxima a una ciudad: ", show(max_distance), "\n"
];

