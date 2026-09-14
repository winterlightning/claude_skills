"""Paw Print with Round Toes.

Plan: Four toes around a rounded triangular pad; two inner toes are round and larger than outer marks.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d3f443a-fb06-4e76-808c-702c115f4835'
SOURCE_PATH = 'pictographic-primitives/pets/pets allowed_4d3f443a-fb06-4e76-808c-702c115f4835.svg'
AUTHOR = 'gpt-6'

class PawPrintRoundToes(Solo48):
    icon_id = 'paw-print-round-toes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('paw', 'paw-print', 'pets-allowed', 'footprint', 'pet', 'animal', 'track')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        for i,cx in enumerate((16,32)):
         arc(f'toe-{i}-a',(cx,8),(cx,14),3)
         arc(f'toe-{i}-b',(cx,14),(cx,8),3)
         contour(f'toe-{i}',f'toe-{i}-a',f'toe-{i}-b',closed=True)
        for i,x in enumerate((4,44)):line(f'outer-{i}',(x,22),(x,24))
        arc('pad-top',(18,30),mirror((18,30)),6,5)
        line('pad-right',mirror((18,30)),mirror((12,36)))
        arc('base-right',mirror((12,36)),mirror((16,40)),4)
        line('base',mirror((16,40)),(16,40))
        arc('base-left',(16,40),(12,36),4)
        line('pad-left',(12,36),(18,30))
        contour('pad','pad-top','pad-right','base-right','base','base-left','pad-left',closed=True)
