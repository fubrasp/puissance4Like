## STEPS TO ACHIEVE "Puissance 4" like game

### 1 - Determine objectives

Do a "puissance 4" like game playable by 2 gamers on a computer

### 2 - Understand what we are doing

Understand rules of the game.

game system :
- put a chip in a column
- we have 42 chips 
- we have two colors of chips (yellow and red, same number of chips for each color)

Winning:
- have a column with 4 following chips horizontally
- have a column with 4 following chips vertically
- have a column with 4 following chips in diagonals

### 3 -  Model the game

#### - Model the board

See [GameBoard](GameBoard.py)


Take a matrix (or 2d list in our case)

```python
[
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0]
]
```

corresponds to [puissance4_board_example](puissance4_board_example.png)

caption:

- 0 empty box
- 1 yellow chip
- -1 red chip

#### - Model the turn system 

- modulo 2 is good to determine the player

#### - Model the wining rules (by summing following box values):

- 1+1+1+1 = **4 yellow win** 
- -1-1-1-1 = **-4 red win**

This addition work in all possibles directions (vertical, horizontal, diagonals)

### 4 - Manage UX 

See [GameBoard](GameView.py)

### 5 - Link all

See [GameBoard](GameView.py)

