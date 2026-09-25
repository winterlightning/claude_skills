"""Bowl of Noodles with Chopsticks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'efe6dc96-0160-51dd-aa03-f6ab0e96f4bd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/noodles bowl_efe6dc96-0160-51dd-aa03-f6ab0e96f4bd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lifted-noodles-over-footed-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('noodle', 'chopsticks', 'bowl', 'meal', 'food', 'asian', 'eating')

    def build(self):
        # Plan: Two lifted noodle strands meet chopsticks and bowl at explicit nodes. Lucide soup. Directional sticks and reduced strand count. Envelope (6,6)-(42,42).
        xs=(6,18,34,42);y=28
        for j,(a,b) in enumerate(zip(xs,xs[1:])):self.add_line(f'rim-{j}',(a,y),(b,y))
        self.add_bezier('right',(42,y),((42,34),(36,38),(30,38)))
        self.add_line('fr',(30,38),(30,42));self.add_line('fb',(30,42),(18,42));self.add_line('fl',(18,42),(18,38))
        self.add_bezier('left',(18,38),((12,38),(6,34),(6,y)))
        self.add_contour('bowl',*[f'rim-{j}' for j in range(len(xs)-1)],'right','fr','fb','fl','left',closed=True)

        self.add_line('upper-stick',(10,10),(42,6))
        self.add_polyline('lower-stick',(10,19),(18,18),(34,16),(42,15))
        for i,(x,y) in enumerate(((18,18),(34,16))):
         self.add_bezier(f'noodle-{i}',(x,y),((x-2,y+4),(x+2,24),(x,28)))
         self.relate('connect',f'noodle-{i}','bowl');self.relate('connect',f'noodle-{i}','lower-stick')
