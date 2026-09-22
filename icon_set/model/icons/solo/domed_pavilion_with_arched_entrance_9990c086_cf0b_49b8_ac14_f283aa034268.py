"""A domed pavilion with a central arched entrance.

SQUARE (6,6)-(42,42) balances a semicircular dome above the facade.
Shared axis x24 owns the dome, door and mirrored walls. Cornice and plinth
are single strokes, omitting reference double edges to preserve openings.
Lucide landmark informs the sparse cornice/column/base hierarchy.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9990c086-cf0b-49b8-ac14-f283aa034268'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/atrium_9990c086-cf0b-49b8-ac14-f283aa034268.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'domed-pavilion-with-arched-entrance'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'buildings'
    aliases = ('Domed Building with Arched Entrance', 'atrium')
    keywords = ('pavilion','dome','arch','entrance','building','architecture','plinth')

    def build(self):
        self.add_arc('dome',(12,18),(36,18),radius_x=12)
        for name,y,xs in [('cornice',18,[6,8,12,36,40,42]),('plinth',42,[6,8,18,30,40,42])]:
            parts=[]
            for i,(a,b) in enumerate(zip(xs,xs[1:])):
                part=f'{name}-{i}'; parts.append(part)
                self.add_line(part,(a,y),(b,y))
            self.add_contour(name,*parts)
        for side,x in [('left',8),('right',40)]:
            self.add_line(f'wall-{side}',(x,18),(x,42))
            self.relate('connect',f'wall-{side}','cornice')
            self.relate('connect',f'wall-{side}','plinth')
        self.add_line('door-left',(18,42),(18,36))
        self.add_arc('door-arch',(18,36),(30,36),radius_x=6)
        self.add_line('door-right',(30,36),(30,42))
        self.add_contour('door','door-left','door-arch','door-right')
        self.relate('connect','door','plinth')
        self.relate('connect','dome','cornice')
