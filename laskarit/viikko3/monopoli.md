## Monopoli

```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Aloitusruutu "1" --> "40" Ruutu
    Aloitusruutu "1" -- "1" Monopolipeli
    Vankila "1" --> "40" Ruutu
    Vankila "1" -- "1" Monopolipeli
    Ruutu -.-> Toiminto
    Sattuma -- Kortit
    Yhteismaa -- Kortit
    Kortit -.-> Toiminto
    Sattuma "3" --> "40" Ruutu
    Yhteismaa "3" --> "40" Ruutu
    Asemat "4" --> "40" Ruutu
    Laitokset "2" --> "40" Ruutu
    Kadut "22" -- "40" Ruutu: nimet
    Kadut "1" -- "4" Talo
    Kadut "1" -- "1" Hotelli
    Hotelli -.-> Talo
    Kadut "1..22" -- "1" Pelaaja
    Pelaaja -.-> Raha
```