int: N;                    % Tamaño del cuadrado
int: M;                     % Número de ciudades

array[1..M] of tuple(string, int, int): ciudades;

% Dominio posible para el lugar del concierto
var 0..N: concert_x;
var 0..N: concert_y;

% Las distancias Manhattan desde el concierto a cada ciudad
array[1..M] of var 0..2*(N-1): distances;

% Llenar el array con las distancias
constraint
  forall(i in 1..M)(
    distances[i] = abs(concert_x - ciudades[i].2) + abs(concert_y - ciudades[i].3)
  );

/* Que no esté exactamente donde está una ciudad */
constraint
  forall(i in 1..M)(
    concert_x != ciudades[i].2 \/ concert_y != ciudades[i].3
  );

/* Queremos que sea lo más equitativo, minimizando la distancia máxima */
% la distancia maxima es el maximo de manhattan
var 0..2*(N-1): max_distance;

constraint max_distance = max(distances);

solve minimize max_distance;

output [
  "Concierto en: (", show(concert_x), ", ", show(concert_y), ")\n",
  "Distancia máxima a una ciudad: ", show(max_distance), "\n"
];