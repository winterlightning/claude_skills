"""Paw Print with Oval Toes.

Plan: Four oval solid toe pads and a wide notched central pad; paired toes share a series.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '889af726-96d1-594a-876a-fc99c9f32c77'
SOURCE_PATH = 'pictographic-primitives/pets/pets paw_889af726-96d1-594a-876a-fc99c9f32c77.svg'
AUTHOR = 'gpt-6'

class PawPrintNotchedPad(Solo48):
    icon_id = 'paw-print-notched-pad'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('paw', 'paw-print', 'pet', 'footprint', 'animal', 'track', 'dog')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        for i,x in enumerate((16,32)):line(f'inner-toe-{i}',(x,8),(x,12))
        for i,x in enumerate((4,44)):line(f'outer-toe-{i}',(x,21),(x,24))
        arc('pad-left',(18,28),(12,36),6,8,False)
        arc('base-left',(12,36),(18,40),6,4,False)
        line('base',(18,40),mirror((18,40)))
        arc('base-right',mirror((18,40)),mirror((12,36)),6,4,False)
        arc('pad-right',mirror((12,36)),mirror((18,28)),6,8,False)
        line('notch-1',mirror((18,28)),(24,31))
        line('notch-2',(24,31),(18,28))
        contour('pad','pad-left','base-left','base','base-right','pad-right','notch-1','notch-2',closed=True)
