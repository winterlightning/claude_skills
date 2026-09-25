"""An astronaut floats diagonally with a round helmet at upper right and two extended legs toward lower left. Bent arms flank the torso, a backpack sits behind the shoulders, and a tether curves out to the right.

SQUARE visible extremes (4,4)-(44,44); diagonal helmet, bent arms, two legs and tether. Suit seams and separate backpack outline dropped for native clarity. No useful Lucide astronaut match; floating pose deliberately asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b9c24dd-f3e9-5017-bdd5-c22d677a5a29'
SOURCE_PATH = 'pictographic-primitives/science/astronaut_0b9c24dd-f3e9-5017-bdd5-c22d677a5a29.svg'
AUTHOR = 'gpt-6'

class TetheredAstronaut(Solo48):
    icon_id = 'tethered-astronaut'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('astronaut', 'spacesuit', 'tether', 'space', 'helmet', 'orbit')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.circle('helmet',32,14,8)
        self.add_polyline('body',(32,22),(24,26),(19,31),(10,40))
        self.add_polyline('leg-right',(19,31),(28,34),(20,42))
        self.add_polyline('arm-left',(24,26),(15,18),(6,27))
        self.add_polyline('arm-right',(28,34),(34,30),(42,22))
        self.relate('connect','body','helmet')
        self.relate('connect','body','leg-right')
        self.relate('connect','body','arm-left')
        self.relate('connect','leg-right','arm-right')
        self.add_arc('tether',(28,34),(42,42),radius_x=14,radius_y=8,sweep=False)
        self.relate('connect','tether','leg-right')
        self.relate('connect','tether','arm-right')
