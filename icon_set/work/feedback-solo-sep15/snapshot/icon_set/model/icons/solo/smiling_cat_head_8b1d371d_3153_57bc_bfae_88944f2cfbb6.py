"""Smiling Cat Head.

Plan: Mirrored ear silhouette and circular jaw; paired eyes and equal smile lobes.
Keyshape centerline extremes: (6,6)-(42,42)
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b1d371d-3153-57bc-bfae-88944f2cfbb6'
SOURCE_PATH = 'pictographic-primitives/pets/cat head_8b1d371d-3153-57bc-bfae-88944f2cfbb6.svg'
AUTHOR = 'gpt-6'

class SmilingCatHead(Solo48):
    icon_id = 'smiling-cat-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('cat', 'head', 'face', 'smile', 'happy', 'feline', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(point): return (2 * axis - point[0], point[1])
        line('ear-left',(6,24),(6,6))
        line('ear-left-slope',(6,6),(16,14))
        line('crown',(16,14),mirror((16,14)))
        line('ear-right-slope',mirror((16,14)),mirror((6,6)))
        line('ear-right',mirror((6,6)),mirror((6,24)))
        arc('jaw-right',mirror((6,24)),(24,42),18)
        arc('jaw-left',(24,42),(6,24),18)
        contour('head','ear-left','ear-left-slope','crown','ear-right-slope','ear-right','jaw-right','jaw-left',closed=True)

        for i,x in enumerate((axis-8,axis+8)): self.add_dot(f'eye-{i}',(x,23))
        arc('smile-left',(19,31),(24,31),4,3,False)
        arc('smile-right',(24,31),mirror((19,31)),4,3,False)
        contour('smile','smile-left','smile-right')
