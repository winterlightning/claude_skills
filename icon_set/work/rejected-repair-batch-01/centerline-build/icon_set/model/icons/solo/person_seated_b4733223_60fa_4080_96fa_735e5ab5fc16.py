"""Seated person with round head, curved torso and bent legs. Lucide accessibility informs separation of head and body. Interior forearm detail omitted to keep the compact seated silhouette open.

SOLO48 VRECT_L; live visible envelope (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4733223-60fa-4080-96fa-735e5ab5fc16'
SOURCE_PATH = 'pictographic-primitives/symbol/sit_b4733223-60fa-4080-96fa-735e5ab5fc16.svg'
AUTHOR = 'gpt-6'


class PersonSeated(Solo48):
    icon_id = 'person-seated'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('sitting', 'person', 'seat', 'waiting', 'rest', 'chair', 'passenger', 'lounge')

    def build(self) -> None:
        cx,cy,r=30,9,5

        self.add_arc('head-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc('head-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour('head','head-top','head-bottom',closed=True)

        self.add_arc('shoulders',(24,31),(40,31),radius_x=8)
        self.add_line('back',(40,31),(40,34))
        self.add_arc('hip',(40,34),(34,42),radius_x=6,radius_y=8)
        pts=[(34,42),(18,42),(16,44),(8,44),(8,38)]
        for j,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line('legs-'+str(j),a,b)
        self.add_arc('knee',(8,38),(12,34),radius_x=4)
        self.add_line('lap-1',(12,34),(22,34))
        self.add_line('lap-2',(22,34),(24,31))
        self.add_contour('body','shoulders','back','hip',*['legs-'+str(j) for j in range(1,5)],'knee','lap-1','lap-2',closed=True)
