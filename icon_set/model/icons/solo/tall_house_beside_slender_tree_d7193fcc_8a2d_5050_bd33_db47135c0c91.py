"""Tall House beside Slender Tree.

Plan: HRECT centerlines (4,8)-(44,40); tall narrow house and slender pointed tree share a baseline. Broad trapezoid roof contrasts with the smooth tree crown.
Construction references: Lucide trees: coherent pointed crown and attached trunk; Lucide building: minimal façade.
Reduction: Simplified the small outlined doorway to one vertical stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'd7193fcc-8a2d-5050-bd33-db47135c0c91'
SOURCE_PATH = 'pictographic-primitives/building/building nature_d7193fcc-8a2d-5050-bd33-db47135c0c91.svg'
SOURCE_ICON_IDS = ('d7193fcc-8a2d-5050-bd33-db47135c0c91',)
SOURCE_PATHS = ('pictographic-primitives/building/building nature_d7193fcc-8a2d-5050-bd33-db47135c0c91.svg',)
AUTHOR = 'gpt-6'


class TallHouseBesideSlenderTree(Solo48):
    icon_id = 'tall-house-beside-slender-tree'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('tall', 'house', 'beside', 'slender', 'tree')

    def build(self) -> None:
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[("A",(x,y+r),r,r,True),("A",(x,y-r),r,r,True)],True)

        self.add_polyline("roof",(4,16),(8,8),(24,8),(28,16),(24,16),(8,16),closed=True)
        self.add_polyline("house",(8,16),(8,40),(16,40),(24,40),(24,16))
        self.relate("connect","house","roof")
        self.add_polyline("ground",(4,40),(8,40),(24,40),(40,40),(44,40))
        self.relate("connect","ground","house")
        self.add_line("door",(16,32),(16,40))
        self.relate("connect","door","house")
        path("tree",(40,16),[("C",(44,28),(42,21),(44,25)),("A",(40,32),4,4,True),("A",(36,28),4,4,True),("C",(40,16),(36,25),(38,21))],True)
        self.add_line("trunk",(40,32),(40,40))
        self.relate("connect","trunk","tree")
        self.relate("connect","trunk","ground")
