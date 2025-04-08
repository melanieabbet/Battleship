# Battleship  
CAS-IDD Module PYTHON  


**Professor:** 
- Matthieu Amiguet

**By:**  
- Mélanie Abbet  
- Arthur Pfister  

---

# Introduction  

**Local network Battleship game.**  
This program allows you to play Battleship over a local network via the terminal.  

It's a two-player game.  

---

# How to  

***Important***: ```Python 3.13``` or higher is required.  

## Starting the Game  

At the project root, execute *main.py* in the terminal:  
```bash  
python main.py  
```  

The game will then ask for your name, followed by whether you want to create or join a lobby.  

```bash  
Enter your name: Edward John Smith  
Enter your role (Join or Host):  
```  

- To create a lobby and host the game, type ```Host```.  
- To join an existing lobby, type ```Join```.  

## Connecting Players  

If you are the host, you will need to share your IP address with the other player:  
```bash  
Your IP is: 127.0.0.1  
```  

If you are joining a lobby, enter the host's IP address:  
```bash  
Enter the Host IP address (ex: 192.168.1.42):  
```  

Once players are connected, the game begins...  

---

# The Game  

## Placing Ships  

The game starts with a phase where all players place their ships.  

```bash  
[\][A][B][C][D][E][F][G][H][I]  
[1] ·  ·  ·  ·  ·  ·  ·  ·  ·  
[2] ·  ·  ·  ·  ·  ·  ·  ·  ·  
[3] ·  ·  ·  ·  ·  ·  ·  ·  ·  
[4] ·  ·  ·  ·  ·  ·  ·  ·  ·  
[5] ·  ·  ·  ·  ·  ·  ·  ·  ·  
[6] ·  ·  ·  ·  ·  ·  ·  ·  ·  
[7] ·  ·  ·  ·  ·  ·  ·  ·  ·  
[8] ·  ·  ·  ·  ·  ·  ·  ·  ·  
[9] ·  ·  ·  ·  ·  ·  ·  ·  ·  

Enter 2 coordinates that follow: 2 remaining  
Enter a grid coordinate:  
```  

To place ships, enter multiple consecutive coordinates.  
Previously entered coordinates are displayed above the input:  
```bash  
Enter 2 coordinates that follow: 1 remaining  
[A2]  
Enter a grid coordinate:  
```  

Once all ships are placed, the rounds begin...
```bash  
            Arthur                            Mélanie            
[\][A][B][C][D][E][F][G][H][I]     [\][A][B][C][D][E][F][G][H][I]
[1] ·  ·  ·  ·  ·  ·  ·  ·  ·      [1] ·  ·  ·  ·  ·  ·  ·  ·  · 
[2] ·  □  ·  ·  ·  ·  ·  ·  ·      [2] ·  ·  ·  ·  ·  ·  ·  ·  · 
[3] ·  □  ·  ·  ·  ·  ·  ·  ·      [3] ·  ·  ·  ·  ·  ·  ·  ·  · 
[4] ·  □  ·  ·  ·  ·  ·  ·  ·      [4] ·  ·  ·  ·  ·  ·  ·  ·  · 
[5] ·  □  ·  □  □  □  ·  ·  ·      [5] ·  ·  ·  ·  ·  ·  ·  ·  · 
[6] ·  ·  ·  ·  ·  ·  ·  ·  ·      [6] ·  ·  ·  ·  ·  ·  ·  ·  · 
[7] ·  ·  ·  ·  ·  ·  ·  ·  ·      [7] ·  ·  ·  ·  ·  ·  ·  ·  · 
[8] ·  ·  ·  ·  ·  ·  ·  ·  ·      [8] ·  ·  ·  ·  ·  ·  ·  ·  · 
[9] ·  ·  ·  ·  ·  ·  ·  ·  ·      [9] ·  ·  ·  ·  ·  ·  ·  ·  · 
     

Enter a grid coordinate:g6 
```  

## Round  

Each turn, players enter the coordinates of their attack.  
After all players have entered their coordinates, the results are displayed on the grids, and a new round starts.  

```bash  
        Arthur                                Mélanie            
[\][A][B][C][D][E][F][G][H][I]     [\][A][B][C][D][E][F][G][H][I]
[1] ·  ·  ·  O  ·  ·  □  ·  ·      [1] ·  ·  X  X  X  O  ·  ·  · 
[2] O  O  ·  ·  ·  ·  □  O  ·      [2] ·  ·  ·  ·  ·  ·  ·  ·  X 
[3] ·  ·  ·  ·  ·  ·  X  ·  ·      [3] ·  ·  ·  ·  ·  ·  ·  ·  X 
[4] ·  ·  O  ·  ·  ·  ·  ·  ·      [4] O  ·  O  ·  ·  ·  ·  O  X 
[5] ·  ·  X  X  □  □  ·  ·  O      [5] ·  ·  ·  ·  ·  O  ·  ·  O 
[6] ·  O  ·  ·  ·  ·  ·  ·  ·      [6] ·  ·  ·  ·  ·  ·  ·  O  · 
[7] ·  ·  ·  ·  ·  ·  ·  ·  ·      [7] ·  ·  ·  ·  ·  ·  ·  ·  · 
[8] ·  ·  O  ·  ·  ·  O  ·  ·      [8] ·  ·  ·  ·  ·  ·  ·  ·  · 
[9] ·  O  ·  ·  ·  O  ·  ·  ·      [9] ·  ·  ·  ·  O  ·  ·  ·  · 
     

Enter a grid coordinate:i1
``` 

After each turn, the gris is updated:

### Grid Symbols

|Square symbols |Content   |
|---------------|----------|
|```□```        | Boat     |
|```X```        |Hit Boat  |
|```O```        |Miss      |
|```.```        |Watter    |

## Win Condition  

The game continues until all of a player's ships are sunk.  

---

# Doxygen

The code has been commented with the ```doxygen```format

To generate the Doxygen documentation, you need to have [Doxygen](https://www.doxygen.nl/download.html) installed.  

Then, in the source directory (where the Doxyfile is located), run:  
```bash  
doxygen Doxyfile  
```  

Open the following file in your browser:  
```bash  
/_doxygen/html/index.html  
```  

---