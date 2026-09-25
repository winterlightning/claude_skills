"""Electric Rice Cooker."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab69d9ac-7f2d-5166-8a4b-9327523f750b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/appliances rice cooker_ab69d9ac-7f2d-5166-8a4b-9327523f750b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'footed-electric-rice-cooker'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('rice cooker', 'appliance', 'rice', 'kitchen', 'lid', 'handle', 'cooking')

    def build(self):
        # Plan: Rounded rice cooker with raised handle, front control and two feet. Lucide cooking-pot coherent curves. Blank display reduced to dot. Mirrored envelope (6,6)-(42,42).
        self.add_polyline('handle',(18,14),(18,6),(30,6),(30,14))
        self.add_bezier('lid-l',(6,22),((6,16),(12,14),(18,14)))
        self.add_line('lid-top',(18,14),(30,14))
        self.add_bezier('lid-r',(30,14),((36,14),(42,16),(42,22)))
        self.add_contour('lid','lid-l','lid-top','lid-r');self.relate('connect','handle','lid')
        self.add_line('rim',(6,22),(42,22));self.relate('connect','rim','lid')
        self.add_bezier('body',(42,22),((42,26),(42,28),(42,32)),((42,36),(38,38),(34,38)))
        self.add_line('base',(34,38),(14,38))
        self.add_bezier('body-l',(14,38),((10,38),(6,36),(6,32)),((6,28),(6,26),(6,22)))
        for a,b in (('body','rim'),('body','lid'),('body','base'),('base','body-l'),('body-l','rim'),('body-l','lid')):self.relate('connect',a,b)
        for x,n in ((14,'body-l'),(34,'body')):
         self.add_line(f'foot-{x}',(x,38),(x,42));self.relate('connect',f'foot-{x}','base');self.relate('connect',f'foot-{x}',n)
        self.add_dot('control',(24,30))
