"""Hand Holding Chopsticks.

Symbol plan: Upright grasp owns thumb fold and wrist; two sticks extend diagonally right, with exposed upper ends. Extrema (6,6)-(42,42).
Construction reference: Shared human full_body_ref.png for minimal anatomy; Lucide hand-grab for thumb/palm contour.
Reduction: Finger creases reduced to one thumb fold; directional asymmetry retained.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f45199b-b4b8-41dc-bf1e-5e7f32883756'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chopstick_3f45199b-b4b8-41dc-bf1e-5e7f32883756.svg'
AUTHOR = 'gpt-6'


class UprightHandHoldingChopsticks(Solo48):
    icon_id = 'upright-hand-holding-chopsticks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('upright', 'hand', 'holding', 'chopsticks')

    def build(self):
        self.path('hand',(6,42),[(6,23),((6,18),(10,16),(14,16)),(18,16),((22,16),(24,18),(24,20)),((24,23),(22,24),(18,24))])
        self.path('palm',(24,20),[((26,20),(26,23),(26,24)),(26,32),((26,36),(21,36),(21,42))])
        self.relate('connect','hand','palm')
        self.add_line('upper-stick',(6,6),(18,16))
        self.add_line('lower-stick',(24,20),(42,30))
        self.add_line('second-stick',(26,32),(42,42))
        self.relate('connect','hand','upper-stick')
        self.relate('connect','hand','lower-stick')
        self.relate('connect','palm','lower-stick')
        self.relate('connect','palm','second-stick')

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
