# pylint disable: missing-docstring

from word_search import WordSearch


EXAMPLE1 = """BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA,CHEWY
U,M,K,H,U,L,K,I,N,V,J,O,C,W,E
L,L,S,H,K,Z,Z,W,Z,C,G,J,U,Y,G
H,S,U,P,J,P,R,J,D,H,S,B,X,T,G
B,R,J,S,O,E,Q,E,T,I,K,K,G,L,E
A,Y,O,A,G,C,I,R,D,Q,H,R,T,C,D
S,C,O,T,T,Y,K,Z,R,E,P,P,X,P,F
B,L,Q,S,L,N,E,E,E,V,U,L,F,M,Z
O,K,R,I,K,A,M,M,R,M,F,B,A,P,P
N,U,I,I,Y,H,Q,M,E,M,Q,R,Y,F,S
E,Y,Z,Y,G,K,Q,J,P,C,Q,W,Y,A,K
S,J,F,Z,M,Q,I,B,D,B,E,M,K,W,D
T,G,L,B,H,C,B,E,C,H,T,O,Y,I,K
O,J,Y,E,U,L,N,C,C,L,Y,B,Z,U,H
W,Z,M,I,S,U,K,U,R,B,I,D,U,X,S
K,Y,L,B,Q,Q,P,M,D,F,C,K,E,A,B"""


EXAMPLE2 = """ACCELERATION,ALACRITY,ANTICIPATION,AUTHENTICITY,BELLIGERENT,BLISSFUL,CHARISMATIC,COMPLICATION,DELIBERATE,DELIGHTFUL,ECSTATIC,EXTRATERRESTRIAL,FACILITATION,FLUCTUATE,FORMIDABLE,GORGEOUS,HARMONIOUS,HESITATION,IMAGINATION,INDISPENSABLE,INEVITABLE,IRIDESCENT,JUBILANT,JUBILATION,JUXTAPOSITION,KALEIDOSCOPE,LABYRINTH,LUMINESCENT,MAGNIFICENT,MYSTERIOUS,NOSTALGIC,OPPORTUNITY,PERPENDICULAR,QUIZZICAL,RESILIENCE,REVERBERATE,SERENDIPITY,STUPENDOUS,SUBSTANTIAL,TRANQUILITY,TRIUMPH,UNFORGETTABLE,UNPRECEDENTED,VIBRANT,WANDERLUST,WHIMSICAL,WONDERFUL,XENOPHOBIA,YEARNING,ZEALOUS,
M,V,W,I,B,H,Q,W,S,A,C,N,Y,K,P,Q,E,A,M,Z,N,Z,L,O,T,W,Q,X,W,Q,B,E,N,M,E,O,D,U,V,G
H,Y,F,S,R,H,C,U,Q,H,G,T,O,E,T,X,J,A,J,A,T,L,F,K,B,S,L,T,J,H,L,T,D,H,N,O,O,N,D,Y
U,E,Q,L,N,I,O,J,A,F,I,M,R,I,T,M,G,Z,A,A,J,L,N,C,M,M,C,X,E,C,I,A,G,M,H,F,L,P,C,U
T,S,L,B,C,E,D,R,J,C,E,P,J,R,T,N,L,O,W,C,B,V,C,Z,I,S,I,J,G,K,S,U,G,A,T,L,Y,R,Q,H
K,E,U,B,G,E,I,E,I,D,E,W,A,P,I,A,Q,U,I,Z,Z,I,C,A,L,T,U,B,F,K,S,T,L,U,W,S,Y,E,Z,T
M,A,W,R,A,S,L,T,S,N,V,T,G,F,D,O,P,X,G,P,T,X,I,W,E,K,A,O,P,X,F,C,S,O,M,T,X,C,E,O
L,F,O,C,M,T,N,S,D,C,E,J,I,M,G,P,J,I,V,J,E,X,S,O,W,P,Z,T,I,N,U,U,E,K,J,U,I,E,D,X
E,G,M,A,A,E,T,I,W,R,E,C,D,N,U,H,U,E,C,Q,U,S,Z,R,V,G,T,L,S,R,L,L,G,L,Y,P,D,D,B,A
D,J,T,N,H,L,C,E,R,N,E,N,I,Q,O,W,X,R,O,I,T,S,V,V,D,G,H,T,T,C,E,F,O,C,A,E,Y,E,T,U
I,I,C,T,I,U,U,E,G,N,X,N,T,T,X,D,T,A,B,F,T,O,F,E,Y,Z,B,S,S,F,E,T,Z,Z,D,N,E,N,V,M
C,E,U,N,L,I,S,F,T,R,R,Y,I,K,D,K,A,G,Q,P,D,N,L,Z,D,E,U,H,B,V,C,D,S,E,G,D,J,T,X,A
Z,A,W,A,U,T,D,S,R,A,O,U,I,H,N,A,P,J,S,F,E,F,A,C,I,L,I,T,A,T,I,O,N,Y,X,O,R,E,C,Z
G,F,R,G,R,A,N,R,E,E,R,F,G,S,X,L,O,Y,J,H,Y,G,G,E,R,C,S,H,X,F,C,N,N,N,M,U,E,D,Q,U
D,P,J,I,X,N,C,Y,B,O,D,I,N,B,R,E,S,D,R,D,R,Z,D,E,E,W,L,D,W,D,V,X,L,I,B,S,L,X,G,U
Z,Y,A,J,E,S,W,A,A,P,S,N,F,U,S,I,I,J,J,M,B,W,D,Q,Y,S,K,W,T,P,M,V,T,Z,M,U,T,L,E,D
K,L,D,E,L,I,B,E,R,A,T,E,O,L,X,D,T,B,S,P,Q,N,R,S,A,X,H,B,G,F,H,N,Z,S,M,Q,U,G,E,Q
E,F,F,X,R,D,S,D,K,A,Y,K,O,W,D,O,I,Z,J,S,A,J,Y,E,M,V,D,K,O,F,E,R,H,I,J,C,V,O,C,U
O,J,C,C,P,P,K,W,C,C,C,Q,X,B,B,S,O,W,C,W,R,T,U,L,V,Q,L,B,Q,R,O,W,N,U,S,O,N,S,I,X
Z,C,E,E,C,N,E,I,L,I,S,E,R,G,N,C,N,E,W,I,I,G,R,V,D,E,A,Z,E,A,Q,E,B,B,P,J,X,A,G,V
E,T,I,J,F,T,M,L,A,E,N,T,L,H,Q,O,F,E,T,N,M,H,V,A,W,H,R,G,K,I,S,I,O,M,C,J,V,R,L,D
O,P,J,F,H,O,B,J,Q,E,I,R,V,L,Y,P,I,G,U,B,A,W,U,F,H,W,I,B,T,C,L,V,L,F,U,F,W,U,A,J
Q,W,S,Y,L,G,R,L,R,D,Q,H,J,K,W,E,S,T,E,B,G,Q,F,V,Y,L,S,T,E,A,W,E,W,P,W,L,F,Q,T,Q
U,T,V,T,Z,W,R,M,K,C,X,K,A,L,D,D,R,G,J,L,I,N,L,V,L,E,T,N,N,R,D,L,U,X,I,A,S,D,S,E
S,Z,G,I,V,Z,T,H,I,J,N,F,H,C,A,O,P,X,I,G,N,R,H,E,K,D,T,T,J,E,A,C,A,H,E,D,W,B,O,O
X,Q,X,L,C,V,N,Z,R,D,V,E,E,W,P,I,B,R,T,U,A,H,B,B,O,C,O,K,O,N,S,T,Z,J,X,P,M,O,N,B
A,O,P,I,X,R,O,H,T,V,A,M,Y,P,R,U,T,L,U,F,T,H,G,I,L,E,D,E,Z,J,W,H,E,I,D,Y,G,Q,B,I
H,T,F,U,K,G,H,B,E,Z,M,B,O,H,L,O,H,N,E,L,I,G,N,U,K,N,O,L,H,A,R,M,O,N,I,O,U,S,B,P
I,N,Y,Q,T,Z,F,Q,D,S,Z,L,L,S,K,T,V,V,A,F,O,J,Z,R,Z,J,U,A,J,J,N,M,H,S,H,A,Z,B,V,C
A,O,Y,N,I,T,F,K,Z,C,I,R,A,E,A,K,T,W,Z,T,N,Q,K,T,D,B,I,C,M,U,O,D,U,X,W,V,B,T,C,C
I,I,A,A,N,F,D,E,T,M,N,T,D,R,F,L,D,H,F,B,S,M,T,N,A,R,B,I,V,Q,B,B,F,F,I,F,E,L,Y,G
B,T,Z,R,E,R,Y,O,L,J,M,B,A,B,N,Y,A,B,D,R,D,B,G,A,X,N,J,S,H,V,I,I,B,C,I,H,B,E,N,C
O,A,E,T,V,C,U,J,Y,J,G,O,V,T,Q,D,V,C,H,D,L,W,U,A,O,P,F,M,K,P,V,U,L,Q,U,K,H,A,O,P
H,R,O,T,I,G,P,P,V,U,B,A,N,Q,I,R,P,K,R,O,S,O,P,S,J,E,M,I,X,G,W,T,E,A,M,W,E,I,A,I
P,E,A,C,T,E,L,O,H,Q,Q,E,B,T,H,O,J,X,V,I,E,W,Q,K,V,Y,Q,H,G,P,B,Y,U,Q,T,G,F,K,O,T
O,L,D,E,A,E,L,B,A,S,N,E,P,S,I,D,N,I,T,S,T,E,V,B,K,U,Y,W,Y,G,F,M,C,X,B,I,O,S,R,F
N,E,A,T,B,H,T,N,I,R,Y,B,A,L,U,E,N,U,T,H,E,Y,Z,Y,Y,B,V,E,D,M,X,R,H,Z,E,J,O,I,S,O
E,C,H,J,L,I,U,G,D,P,B,B,U,J,T,K,O,P,F,W,N,I,Y,Y,L,K,L,F,M,L,Y,I,H,D,J,Z,U,N,B,Y
X,C,H,W,E,W,S,F,D,J,Q,P,J,B,V,S,Z,P,Q,M,B,O,I,M,M,E,I,B,W,X,U,J,L,T,P,M,C,Z,N,I
Z,A,Z,E,A,L,O,U,S,W,Y,Q,Z,D,C,W,B,C,T,T,N,K,B,N,S,M,L,N,O,I,Q,Q,G,B,P,X,Z,R,T,J
Y,T,I,P,I,D,N,E,R,E,S,W,V,X,O,G,R,E,V,X,V,C,O,M,P,L,I,C,A,T,I,O,N,H,Y,N,Z,Z,O,N"""


def test_search_example1():
    assert WordSearch(EXAMPLE1).search_for_words() == {
        "BONES": [(0, 6), (0, 7), (0, 8), (0, 9), (0, 10)],
        "KHAN": [(5, 9), (5, 8), (5, 7), (5, 6)],
        "KIRK": [(4, 7), (3, 7), (2, 7), (1, 7)],
        "SCOTTY": [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
        "SPOCK": [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)],
        "SULU": [(3, 3), (2, 2), (1, 1), (0, 0)],
        "UHURA": [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)],
        "CHEWY": [(8, 12), (9, 11), (10, 10), (11, 9), (12, 8)],
    }


def test_search_example2():
    assert WordSearch(EXAMPLE2).search_for_words() == {
        "XENOPHOBIA": [(0, 37), (0, 36), (0, 35), (0, 34), (0, 33), (0, 32), (0, 31), (0, 30), (0, 29), (0, 28)],
        "GORGEOUS": [(1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)],
        "AUTHENTICITY": [(1, 11), (2, 10), (3, 9), (4, 8), (5, 7), (6, 6), (7, 5), (8, 4), (9, 3), (10, 2), (11, 1), (12, 0)],
        "ACCELERATION": [(1, 38), (1, 37), (1, 36), (1, 35), (1, 34), (1, 33), (1, 32), (1, 31), (1, 30), (1, 29), (1, 28), (1, 27)],
        "DELIBERATE": [(2, 15), (3, 15), (4, 15), (5, 15), (6, 15), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15)],
        "ZEALOUS": [(2, 38), (3, 38), (4, 38), (5, 38), (6, 38), (7, 38), (8, 38)],
        "IRIDESCENT": [(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5), (9, 6), (10, 7), (11, 8), (12, 9)],
        "TRANQUILITY": [(3, 31), (3, 30), (3, 29), (3, 28), (3, 27), (3, 26), (3, 25), (3, 24), (3, 23), (3, 22), (3, 21)],
        "FORMIDABLE": [(4, 19), (5, 20), (6, 21), (7, 22), (8, 23), (9, 24), (10, 25), (11, 26), (12, 27), (13, 28)],
        "INEVITABLE": [(4, 28), (4, 29), (4, 30), (4, 31), (4, 32), (4, 33), (4, 34), (4, 35), (4, 36), (4, 37)],
        "YEARNING": [(7, 13), (8, 12), (9, 11), (10, 10), (11, 9), (12, 8), (13, 7), (14, 6)],
        "HESITATION": [(7, 25), (8, 26), (9, 27), (10, 28), (11, 29), (12, 30), (13, 31), (14, 32), (15, 33), (16, 34)],
        "CHARISMATIC": [(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)],
        "SERENDIPITY": [(10, 39), (9, 39), (8, 39), (7, 39), (6, 39), (5, 39), (4, 39), (3, 39), (2, 39), (1, 39), (0, 39)],
        "RESILIENCE": [(12, 18), (11, 18), (10, 18), (9, 18), (8, 18), (7, 18), (6, 18), (5, 18), (4, 18), (3, 18)],
        "OPPORTUNITY": [(12, 26), (13, 25), (14, 24), (15, 23), (16, 22), (17, 21), (18, 20), (19, 19), (20, 18), (21, 17), (22, 16)],
        "UNFORGETTABLE": [(13, 14), (12, 13), (11, 12), (10, 11), (9, 10), (8, 9), (7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2)],
        "WONDERFUL": [(13, 16), (12, 15), (11, 14), (10, 13), (9, 12), (8, 11), (7, 10), (6, 9), (5, 8)],
        "LABYRINTH": [(13, 35), (12, 35), (11, 35), (10, 35), (9, 35), (8, 35), (7, 35), (6, 35), (5, 35)],
        "PERPENDICULAR": [(14, 0), (13, 1), (12, 2), (11, 3), (10, 4), (9, 5), (8, 6), (7, 7), (6, 8), (5, 9), (4, 10), (3, 11), (2, 12)],
        "ALACRITY": [(14, 28), (15, 29), (16, 30), (17, 31), (18, 32), (19, 33), (20, 34), (21, 35)],
        "KALEIDOSCOPE": [(15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15), (15, 16), (15, 17), (15, 18), (15, 19), (15, 20), (15, 21)],
        "EXTRATERRESTRIAL": [(16, 0), (15, 1), (14, 2), (13, 3), (12, 4), (11, 5), (10, 6), (9, 7), (8, 8), (7, 9), (6, 10), (5, 11), (4, 12), (3, 13), (2, 14), (1, 15)],
        "QUIZZICAL": [(16, 4), (17, 4), (18, 4), (19, 4), (20, 4), (21, 4), (22, 4), (23, 4), (24, 4)],
        "JUXTAPOSITION": [(16, 6), (16, 7), (16, 8), (16, 9), (16, 10), (16, 11), (16, 12), (16, 13), (16, 14), (16, 15), (16, 16), (16, 17), (16, 18)],
        "INDISPENSABLE": [(17, 34), (16, 34), (15, 34), (14, 34), (13, 34), (12, 34), (11, 34), (10, 34), (9, 34), (8, 34), (7, 34), (6, 34), (5, 34)],
        "MAGNIFICENT": [(18, 0), (17, 1), (16, 2), (15, 3), (14, 4), (13, 5), (12, 6), (11, 7), (10, 8), (9, 9), (8, 10)],
        "WANDERLUST": [(19, 17), (20, 16), (21, 15), (22, 14), (23, 13), (24, 12), (25, 11), (26, 10), (27, 9), (28, 8)],
        "IMAGINATION": [(20, 18), (20, 19), (20, 20), (20, 21), (20, 22), (20, 23), (20, 24), (20, 25), (20, 26), (20, 27), (20, 28)],
        "FACILITATION": [(21, 11), (22, 11), (23, 11), (24, 11), (25, 11), (26, 11), (27, 11), (28, 11), (29, 11), (30, 11), (31, 11), (32, 11)],
        "COMPLICATION": [(21, 39), (22, 39), (23, 39), (24, 39), (25, 39), (26, 39), (27, 39), (28, 39), (29, 39), (30, 39), (31, 39), (32, 39)],
        "ANTICIPATION": [(22, 11), (21, 10), (20, 9), (19, 8), (18, 7), (17, 6), (16, 5), (15, 4), (14, 3), (13, 2), (12, 1), (11, 0)],
        "REVERBERATE": [(22, 15), (23, 16), (24, 17), (25, 18), (26, 19), (27, 20), (28, 21), (29, 22), (30, 23), (31, 24), (32, 25)],
        "BELLIGERENT": [(22, 24), (23, 23), (24, 22), (25, 21), (26, 20), (27, 19), (28, 18), (29, 17), (30, 16), (31, 15), (32, 14)],
        "SUBSTANTIAL": [(23, 32), (22, 31), (21, 30), (20, 29), (19, 28), (18, 27), (17, 26), (16, 25), (15, 24), (14, 23), (13, 22)],
        "DELIGHTFUL": [(26, 25), (25, 25), (24, 25), (23, 25), (22, 25), (21, 25), (20, 25), (19, 25), (18, 25), (17, 25)],
        "WHIMSICAL": [(27, 34), (27, 33), (27, 32), (27, 31), (27, 30), (27, 29), (27, 28), (27, 27), (27, 26)],
        "HARMONIOUS": [(28, 26), (29, 26), (30, 26), (31, 26), (32, 26), (33, 26), (34, 26), (35, 26), (36, 26), (37, 26)],
        "JUBILATION": [(28, 27), (29, 28), (30, 29), (31, 30), (32, 31), (33, 32), (34, 33), (35, 34), (36, 35), (37, 36)],
        "VIBRANT": [(28, 29), (27, 29), (26, 29), (25, 29), (24, 29), (23, 29), (22, 29)],
        "BLISSFUL": [(30, 0), (30, 1), (30, 2), (30, 3), (30, 4), (30, 5), (30, 6), (30, 7)],
        "ECSTATIC": [(30, 9), (29, 8), (28, 7), (27, 6), (26, 5), (25, 4), (24, 3), (23, 2)],
        "FLUCTUATE": [(31, 8), (31, 7), (31, 6), (31, 5), (31, 4), (31, 3), (31, 2), (31, 1), (31, 0)],
        "MYSTERIOUS": [(34, 12), (33, 11), (32, 10), (31, 9), (30, 8), (29, 7), (28, 6), (27, 5), (26, 4), (25, 3)],
        "JUBILANT": [(34, 16), (33, 17), (32, 18), (31, 19), (30, 20), (29, 21), (28, 22), (27, 23)],
        "STUPENDOUS": [(35, 4), (35, 5), (35, 6), (35, 7), (35, 8), (35, 9), (35, 10), (35, 11), (35, 12), (35, 13)],
        "LUMINESCENT": [(36, 13), (35, 14), (34, 15), (33, 16), (32, 17), (31, 18), (30, 19), (29, 20), (28, 21), (27, 22), (26, 23)],
        "UNPRECEDENTED": [(37, 0), (37, 1), (37, 2), (37, 3), (37, 4), (37, 5), (37, 6), (37, 7), (37, 8), (37, 9), (37, 10), (37, 11), (37, 12)],
        "NOSTALGIC": [(38, 24), (38, 23), (38, 22), (38, 21), (38, 20), (38, 19), (38, 18), (38, 17), (38, 16)],
        "TRIUMPH": [(39, 33), (38, 34), (37, 35), (36, 36), (35, 37), (34, 38), (33, 39)],
    }
