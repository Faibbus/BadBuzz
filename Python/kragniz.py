'''
124 0 0 100 1     0      22 12 114 30 0     124 0 0 100
2                 0                22              12
114 30 0         100              3               0
71                72            110             41
0                124           0               0
100               1           0              22
115              48         0               100
4                 0       71 72 110 23     0 124 0 0 100


2 0 22 115        66           0     100 5 0 71 72     110 5 0 124 0
0         71      72          100              0                 0
83 4 7 24         24           0             19                24
24        0       23           34          23                65
27        12      75           74        87               34
62 4 54 85           23 76 45 0       23 83 65 23 1    4 65 34 84 23
'''

_ = lambda _, ___: str(bytearray([int(i)+98 for i in __[-_:-___]]))
f = lambda: _
__ = [int(i) for i in __doc__.split()]
f.__code__ = type(f.__code__)(
    1, 1, 2, 67, str(bytearray(__)), (None, 3, 5, _(37, 29), _(37, 33),
    _(33, 29)), (), ('n',), '', '', 0, '', (), ())
for _ in range(*reversed(__[3:5])): f(_)