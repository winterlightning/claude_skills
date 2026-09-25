'An outlined equal-armed plus with rounded terminal caps. SQUARE fits its four equal extents; rotate one arm definition around (24,24). Arms retain 8-unit internal centerline width. Source supplies outline and balanced silhouette; Lucide rectangle-vertical supplies rounded-terminal construction. No details omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f1449e0a-c5a1-4ede-806c-ca36de940e2c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/plus large_f1449e0a-c5a1-4ede-806c-ca36de940e2c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'rounded-equal-armed-plus'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ['Rounded Plus Addition Symbol']
    keywords = []
    def build(self):
        # Rotate a single cap-and-arm definition four times about the center.
        def rotate(p,n):
            x,y=p[0]-24,p[1]-24
            for _ in range(n): x,y=-y,x
            return (x+24,y+24)
        members=[]
        for n in range(4):
            a,b,c,d=[rotate(p,n) for p in [(20,10),(28,10),(28,20),(38,20)]]
            names=[f'cap-{n}',f'inner-{n}',f'arm-{n}'];members.extend(names)
            self.add_arc(names[0],a,b,radius_x=4,sweep=True)
            self.add_line(names[1],b,c);self.add_line(names[2],c,d)
        self.add_contour('plus',*members,closed=True)
