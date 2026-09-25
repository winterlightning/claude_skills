"""Chow Chow Face.

Plan: Broad rounded mane owns small rounded upper ears, mirrored dot eyes and centered split muzzle. Extra chin and tongue detail removed.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20f6e6a2-1290-47ff-bba7-e87ab03f93c6'
SOURCE_PATH = 'pictographic-primitives/pets/chow chow_20f6e6a2-1290-47ff-bba7-e87ab03f93c6.svg'
AUTHOR = 'gpt-6'

class ChowChowFace(Solo48):
    icon_id = 'chow-chow-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'chow-chow', 'face', 'breed', 'fluffy', 'mane', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis = 24
        def mirror(p): return (2 * axis - p[0], p[1])
        arc('ear-left',(6,12),(18,12),6)
        line('crown',(18,12),mirror((18,12)))
        arc('ear-right',mirror((18,12)),mirror((6,12)),6)
        arc('mane-right',mirror((6,12)),mirror((16,42)),10,30)
        line('chin',mirror((16,42)),(16,42))
        arc('mane-left',(16,42),(6,12),10,30)
        contour('mane','ear-left','crown','ear-right','mane-right','chin','mane-left',closed=True)
        for i,x in enumerate((16,32)): self.add_dot(f'eye-{i}',(x,23))
        self.add_polyline('muzzle',(19,32),(24,29),mirror((19,32)))
