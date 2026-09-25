'A tall textile swatch with evenly spaced diagonal stripes. VRECT_L preserves the tall panel; one rounded border owns two stripes with constant x+y increments of 18. Source supplies all-over pattern; no reusable centered modifier. Lucide rectangle-vertical informs continuous quarter-circle corners; reduce source stripe count to two for clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '46622ecc-42b6-4d7f-b812-d85bb3ec076e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/pinstripe_46622ecc-42b6-4d7f-b812-d85bb3ec076e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'diagonal-striped-swatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ['Diagonal Striped Pattern']
    keywords = []
    def build(self):
        # Border is split at all stripe attachment nodes.
        points=[(12,4),(18,4),(36,4),(40,8),(40,18),(40,36),(40,40),(36,44),(32,44),(14,44),(12,44),(8,40),(8,32),(8,14),(8,8),(12,4)]
        corners={2,6,10,14}
        ids=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            name=f'border-{i}';ids.append(name)
            if i in corners: self.add_arc(name,a,b,radius_x=4,sweep=True)
            else: self.add_line(name,a,b)
        self.add_contour('border',*ids,closed=True)
        for i,(a,b) in enumerate([((8,32),(36,4)),((14,44),(40,18))]):
            name=f'stripe-{i}'
            self.add_line(name,a,b)
            self.relate('connect','border',name)
