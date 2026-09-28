"""Baseball Batter Holding Bat.

Plan: Batter with an upright torso, round head and raised diagonal bat; exact 4-unit detached head gap.
Construction reference: human_ref/full_body_ref.png: outlined head, coherent limbs, angled held bat.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c59f6204-2e2e-4ea5-9bb5-8c01e97f2ea3'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baseball player_c59f6204-2e2e-4ea5-9bb5-8c01e97f2ea3.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'baseball-batter-with-raised-bat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('baseball', 'batter', 'holding', 'bat')

    def build(self):

        self.circle('head',30,14,4)
        self.add_line('torso',(30,26),(30,34))
        self.path('arms',[(30,26),(18,28),(10,22)])
        self.add_line('bat',(10,22),(18,6));self.relate('connect','arms','bat')
        self.path('legs',[(18,42),(30,34),(42,42)])
        self.relate('connect','torso','arms');self.relate('connect','torso','legs')
        self.add_line('grip',(6,24),(10,22));self.relate('connect','arms','grip');self.relate('connect','bat','grip')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

    def circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def path(self, name, points, closed=False):
        self.add_polyline(name, *points, closed=closed)

    def arc(self, name, a, b, r, ry=None, sweep=True):
        self.add_arc(name, a, b, radius_x=r, radius_y=r if ry is None else ry, sweep=sweep)

    def rect(self, name, x, y, w, h, r=4):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; ids.append(part)
            if i%2: self.arc(part,a,b,r)
            elif a != b: self.add_line(part,a,b)
            else: ids.pop()
        self.add_contour(name,*ids,closed=True)
