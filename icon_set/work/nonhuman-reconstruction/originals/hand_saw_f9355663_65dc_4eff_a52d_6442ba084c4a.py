"""Diagonal hand saw with a toothed blade and notched handle. No useful local Lucide saw match; a coherent outline retains two large teeth, blade divider and grip notch.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9355663-65dc-4eff-a52d-6442ba084c4a'
SOURCE_PATH = 'pictographic-primitives/symbol/saw_f9355663-65dc-4eff-a52d-6442ba084c4a.svg'
AUTHOR = 'gpt-6'


class HandSaw(Solo48):
    icon_id = 'hand-saw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('saw', 'handsaw', 'tool', 'carpentry', 'woodwork', 'cut', 'diy', 'construction')

    def build(self) -> None:

        upper=[(6,12),(14,6),(30,22),(40,32)]
        for i,(a,b) in enumerate(zip(upper,upper[1:]),1):self.add_line('upper-'+str(i),a,b)
        self.add_arc('handle-end',(40,32),(40,38),radius_x=2,radius_y=3)
        lower=[(40,38),(36,42),(27,37),(31,33),(24,28),(20,32),(18,30),(18,24),(12,24),(12,18),(6,18),(6,12)]
        for i,(a,b) in enumerate(zip(lower,lower[1:]),1):self.add_line('lower-'+str(i),a,b)
        self.add_contour('outline',*['upper-'+str(i) for i in range(1, 4)],'handle-end',*['lower-'+str(i) for i in range(1, 12)],closed=True)
        self.add_polyline('blade-divider',(30,22),(24,28),(20,32))
        self.relate('connect','outline','blade-divider')
