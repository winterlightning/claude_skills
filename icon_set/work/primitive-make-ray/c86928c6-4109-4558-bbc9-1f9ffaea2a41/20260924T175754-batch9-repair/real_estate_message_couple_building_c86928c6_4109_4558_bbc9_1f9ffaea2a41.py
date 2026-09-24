"""Two people discussing a house in a speech bubble.
Plan: VRECT_L gives the upper bubble and two lower busts enough vertical room. Visible ink bounds: (6, 2, 42, 46).
Reduction: House reduced to an open roof and short walls; door and house floor omitted. Bubble tail centered; heads and shoulders use the shared touching-bust construction.
Construction: Lucide house: roof and wall silhouette. Shared human user.svg: equal circular heads and centered shoulders."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c86928c6-4109-4558-bbc9-1f9ffaea2a41'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/real estate message couple building_c86928c6-4109-4558-bbc9-1f9ffaea2a41.svg'
AUTHOR = 'gpt-6'
PLAN = 'Two people discussing a house in a speech bubble.'
OMISSIONS = 'House reduced to an open roof and short walls; door and house floor omitted. Bubble tail centered; heads and shoulders use the shared touching-bust construction.'
CONSTRUCTION_REFERENCES = 'Lucide house: roof and wall silhouette. Shared human user.svg: equal circular heads and centered shoulders.'
KEYSHAPE_INK_BOUNDS = (6, 2, 42, 46)

class Drawing(Solo48):
    icon_id = 'real-estate-message-couple-building'
    keyshape = Keyshape.VRECT_L
    human_construction = 'bust'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('real', 'estate', 'message', 'couple', 'building')

    def circle(self, n, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(n + '-a', (x - r, y), (x + r, y), radius_x=r, radius_y=ry)
        self.add_arc(n + '-b', (x + r, y), (x - r, y), radius_x=r, radius_y=ry)
        self.add_contour(n, n + '-a', n + '-b', closed=True)

    def build(self):
        self.add_polyline('bubble', (8, 4), (40, 4), (40, 24), (28, 24), (24, 28), (20, 24), (8, 24), closed=True)
        self.add_polyline('house', (20, 16), (20, 14), (24, 12), (28, 14), (28, 16))
        for (name, x) in [('left', 13), ('right', 35)]:
            self.circle(name + '-head', x, 35, 3)
            self.add_arc(name + '-shoulders', (x - 4, 44), (x + 4, 44), radius_x=5)
            self.relate('connect', name + '-head', name + '-shoulders')
