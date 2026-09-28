"""Hands Holding Fork and Knife.

Symbol plan: Two open-wrist grasp silhouettes; fork left and broad curved knife right, shared heights. Extrema (6,6)-(42,42).
Construction reference: Shared human reference; Lucide utensils: fork tines and broad curved knife.
Reduction: Finger wrinkles omitted; hands and three tines retained.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9e1cf36-b36d-4aa8-811a-6a0183bae548'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/fork and khife_f9e1cf36-b36d-4aa8-811a-6a0183bae548.svg'
AUTHOR = 'gpt-6'


class HandsHoldingForkKnife(Solo48):
    icon_id = 'hands-holding-fork-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('hands', 'holding', 'fork', 'knife')

    def build(self):
        for side,x in enumerate((12,36)):
            shaft=14 if side==0 else (38 if self.icon_id=='hands-holding-fork-knife' else 34)
            self.path(f'hand-{side}',(x-6,42),[(x-6,33),((x-6,29),(x-4,28),(x-2,28)),(shaft,28),(x+2,28),((x+6,28),(x+6,31),(x+6,33)),(x+6,35),(x+2,42)])
        fx,fs=14,0

        self.path('fork',(fx-8,6),[(fx-8,14),((fx-8,19),(fx-5,20),(fx,20)),((fx+5,20),(fx+8,19),(fx+8,14)),(fx+8,6)])
        self.add_polyline('fork-shaft',(fx,6),(fx,20),(fx,28))
        self.relate('connect','fork','fork-shaft')
        self.relate('connect','fork-shaft',f'hand-{fs}')

        self.path('knife',(38,6),[((30,9),(30,14),(30,20)),(38,20),(38,6)],True)
        self.add_line('knife-shaft',(38,20),(38,28))
        self.relate('connect','knife','knife-shaft')
        self.relate('connect','knife-shaft','hand-1')

    def loop(self, name, x, y, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (x-rx,y), (x+rx,y), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (x+rx,y), (x-rx,y), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def path(self, name, start, commands, closed=False):
        ids=[]
        point=start
        for i,command in enumerate(commands):
            key=f'{name}-{i}'
            if len(command)==2:
                self.add_line(key, point, command)
                point=command
            else:
                c1,c2,end=command
                self.add_bezier(key, point, (c1,c2,end))
                point=end
            ids.append(key)
        self.add_contour(name, *ids, closed=closed)
