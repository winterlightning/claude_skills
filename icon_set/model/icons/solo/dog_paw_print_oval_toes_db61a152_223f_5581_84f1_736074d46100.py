"""Dog Paw Print.

Plan: Four rounded solid toe marks, two higher inner toes and lower outer toes; broad rounded triangular pad. Shared mirrored toe series.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db61a152-223f-5581-84f1-736074d46100'
SOURCE_PATH = 'pictographic-primitives/pets/dog paw_db61a152-223f-5581-84f1-736074d46100.svg'
AUTHOR = 'gpt-6'

class DogPawPrintOvalToes(Solo48):
    icon_id = 'dog-paw-print-oval-toes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('paw', 'paw-print', 'dog', 'footprint', 'pet', 'track', 'animal')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis = 24
        def mirror(p): return (2 * axis - p[0], p[1])
        for i,x in enumerate((16,32)):line(f'inner-toe-{i}',(x,8),(x,12))
        for i,x in enumerate((4,44)):line(f'outer-toe-{i}',(x,21),(x,24))
        arc('pad-top',(18,30),mirror((18,30)),6,5)
        line('pad-right',mirror((18,30)),mirror((12,36)))
        arc('pad-right-base',mirror((12,36)),mirror((16,40)),4)
        line('pad-base',mirror((16,40)),(16,40))
        arc('pad-left-base',(16,40),(12,36),4)
        line('pad-left',(12,36),(18,30))
        contour('pad','pad-top','pad-right','pad-right-base','pad-base','pad-left-base','pad-left',closed=True)
