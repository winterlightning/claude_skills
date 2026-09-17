"""Gingerbread Man Cookie Shape.

Symbol plan: Continuous cookie outline; round head, mirrored rounded arms and splayed feet. Extrema (8,4)-(40,44).
Construction reference: Shared human full_body_ref.png: frontal symmetry and leg spread; continuous cookie anatomy as requested.
Reduction: No decoration; cookie is not a detached-head stick figure.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b43c0dd-c7e9-506f-9e01-999bcf0602db'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/gingerbread man_4b43c0dd-c7e9-506f-9e01-999bcf0602db.svg'
AUTHOR = 'gpt-6'


class PlainGingerbreadPerson(Solo48):
    icon_id = 'plain-gingerbread-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/food"
    aliases = ()
    keywords = ('plain', 'gingerbread', 'person')

    def build(self):
        axis = 24  # Paired x positions derive from the same symmetry axis.
        self.path('cookie',(axis+0,4),[
         ((axis+7,4),(axis+10,13),(axis+5,18)),(axis+11,18),((axis+16,18),(axis+16,18),(axis+16,22)),((axis+16,26),(axis+14,26),(axis+11,26)),(axis+6,26),(axis+11,38),((axis+13,44),(axis+5,44),(axis+4,44)),((axis+3,44),(axis+2,42),(axis+2,40)),(axis+0,35),(axis-2,40),((axis-2,42),(axis-3,44),(axis-4,44)),((axis-12,44),(axis-13,44),(axis-11,38)),(axis-6,26),(axis-11,26),((axis-16,26),(axis-16,26),(axis-16,22)),((axis-16,18),(axis-14,18),(axis-11,18)),(axis-5,18),((axis-10,13),(axis-7,4),(axis+0,4))],True)

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
