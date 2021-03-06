# piece values 
pv = {'P': 100, 'N': 300, 'B': 325, 'R': 525, 'Q': 950, 'K': 10000}
# piece square values
pst = {
    'P': (
        ( 0,  0,  0,  0,  0,  0,  0,  0),
        (80, 80, 80, 80, 80, 80, 80, 80),
        (15, 25, 25, 35, 35, 25, 25, 15),
        ( 0,  5, 10, 20, 20, 10,  5,  0),
        (-5,  0, 10, 15, 15, 10,  0, -5),
        ( 5,  0,  5,  5,  5,  5,  0,  5),
        ( 0,  5, -5,-15,-15, -5,  5,  0),
        ( 0,  0,  0,  0,  0,  0,  0,  0)
    ),
    'N': (
        (-40, -25, -25, -20, -20, -25, -25, -40),
        (-10,  10,  60,  30,  30,  60,  10, -10),
        (  5,  50,  45,  50,  50,  45,  50,   5),
        ( 10,  25,  40,  35,  35,  40,  25,  10),
        ( -5,  15,  25,  25,  25,  25,  15,  -5),
        ( -5,   5,  10,  10,  10,  10,   5,  -5),
        (-15, -10,   0,   5,   5,   0, -10, -15),
        (-50, -30, -25, -25, -25, -25, -30, -50),
    ),
    'B': (
        (-50, -60, -60, -60, -60, -60, -60, -50),
        (-10,  -5,  -5,  -5,  -5,  -5,  -5, -10),
        (  5,  20,  15,  30,  30,  15,  20,   5),
        ( 10,  10,  20,  20,  20,  20,  10,  10),
        ( 15,  10,  20,  25,  25,  20,  10,  15),
        ( 10,  10,  10,  15,  15,  10,  10,  10),
        ( 15,  20,  10,   5,   5,  10,  20, -15),
        (-10,  -5, -15, -10, -10, -15, -5,  -10),
    ),
    'R': (
        ( 20,  20,  30,  30,  30,  30,  20,  20),
        ( 40,  40,  55,  55,  55,  55,  40,  40),
        ( 15,  25,  25,  30,  30,  25,  25,  15),
        (  0,   5,  10,  10,  10,  10,   5,   0),
        (-15, -15, -10, -10, -10, -10, -15, -15),
        (-30, -10, -20, -20, -20, -20, -10, -30),
        (-50, -30, -30, -30, -30, -30, -30, -50),
        (-30, -15,  -5,  10,  10,  5,  -15, -30),
    ),
    'Q': (
        (  0,   5,   5,   5,   5,   5,   5,   0),
        ( 20,  40,  40,  25,  25,  40,  40,  20),
        ( 10,  25,  35,  50,  50,  35,  25,  10),
        ( -5,  -5,  25,  30,  30,  25,  -5,  -5),
        (-15, -15, -10,   5,   5, -10, -15, -15),
        (-25,  -5,  -5,  -5,  -5,  -5,  -5, -25),
        (-20, -10,   0, -10, -10,   0, -10, -20),
        (-15, -15, -15,  -5, -15, -15, -15, -15),
    ),
    'K': (
        (-70, -30, -30, -60, -60, -30, -30, -70),
        (-10,  15,  10, -15, -15,  10,  15, -10),
        (-25, -15, -10, -20, -20, -10, -15, -25),
        (-50, -25, -20, -40, -40, -20, -25, -50),
        (-50, -40, -30, -40, -40, -30, -40, -50),
        (-30, -30, -35, -50, -50, -35, -30, -30),
        (  5,   5, -10, -40, -40, -10,   5,   5),
        ( 20,  35,  15, -10,   0, -10,  40,  20),
    ),
    
}
