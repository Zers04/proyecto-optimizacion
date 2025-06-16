int: N = 12;          % Tamaño del Valle del Cauca 
int: M = 5;         % Número de ciudades

% Ciudades: (nombre, x, y)
array[1..M] of tuple(string, int, int): ciudades = [
  ("Palmira", 2, 3),
  ("Cali", 10, 2),
  ("Buga", 11, 0),
  ("Tulua", 0, 3),
  ("RioFrio", 1, 2)
];

% Variables del concierto
var 0..N: concert_x;       % Coordenada x del concierto
var 0..N: concert_y;       % Coordenada y del concierto

array[1..M] of var 0..22: distances;   % Distancias a cada ciudad

% Restricciones:
  % Calcular las distancias Manhattan desde el concierto a cada ciudad, no puede superar 2*(N-1)
constraint
  forall(i in 1..M)(
    distances[i] = abs(concert_x - ciudades[i].2) + abs(concert_y - ciudades[i].3)
  );

  % El concierto no puede estar en la misma posición que ninguna ciudad
constraint
  forall(i in 1..M)(
    concert_x != ciudades[i].2 \/ concert_y != ciudades[i].3
  );

  % La diferencia máxima entre distancias es 2 (nadie es favorecido)
constraint
  max(distances) - min(distances) <= 2;

% Objetivo: Minimizar la distancia máxima 
var int: max_distance = max(distances);
solve minimize max_distance;

output [
  "Concierto en: (", show(concert_x), ", ", show(concert_y), ")\n",
  "Distancia máxima a una ciudad: ", show(max_distance), "\n",
  "Ciudades y sus distancias:\n",
] ++ [
   if i > 1 then "\n" else "" endif ++
  "- " ++ show(ciudades[i].1) ++ ": " ++ show(distances[i])
  | i in 1..M
];

