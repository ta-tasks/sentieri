# Sentieri bollenti

Mojito, il piccolo cane Jack Russell mascotte delle OII, ha accompagnato Monica per la supervisione della sede di gara della finale nazionale delle Olimpiadi 2016, a Catania. Dal momento che non era troppo interessato alla disposizione dei computer, Mojito è andato a farsi una passeggiata. Adesso però il sole si è alzato e, come spesso capita in Sicilia, fa molto caldo e l’asfalto che è stato esposto al sole è bollente. Per fortuna non tutti i sentieri sono esposti al sole.

Ad esempio, nella figura sottostante, Mojito parte dal punto 1 e deve arrivare al punto 8. I sentieri bollenti sono quelli in rosso. Si può vedere che Mojito, per minimizzare il numero di sentieri bollenti può andare dal punto 1 al punto 5, da qui al 3, poi al 4 e infine al punto 8, percorrendo solo l’ultimo sentiero bollente. Altri percorsi equivalenti sono 1 -> 5 -> 3 -> 4 -> 6 -> 8 (un solo sentiero bollente tra 6 e 8) e 1 -> 5 -> 3 -> 4 -> 6 -> 7 -> 8 (un solo sentiero bollente tra 6 e 7).

Come si vede dall’esempio, non conta il numero complessivo di sentieri percorsi, ma solo il numero di sentieri bollenti. Il vostro compito consiste nell’aiutare Mojito a trovare una strada per tornare alla sede di gara che abbia il numero minimo di tratti esposti al sole.

### Funzioni

#### `shortest_path`

<description for="shortest_path">

Calcola il **cammino minimo** fra l'origine (nodo 1) al nodo (nodo <param>N</param>)

Parametri:
- <param>N</param>: numero di nodi
- <param>M</param>: numero di archi 
- <param>a</param>: partenza degli archi
- <param>b</param>: arrivo degli archi
- <param>c</param>: 1 se l'arco è caldo, 0 altrimenti

Return <return>the length of the shortest path</return>

</description>
