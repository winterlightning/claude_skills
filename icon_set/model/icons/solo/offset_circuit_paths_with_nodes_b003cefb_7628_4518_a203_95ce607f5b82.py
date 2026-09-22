'Two offset circuit paths, three circular terminals. SQUARE accommodates path ends and terminal extrema. Shared radius four for every terminal; semicircles expose vertical attachment nodes. Source supplies asymmetrical path arrangement; Lucide circuit-board teaches terminal-and-track joins. Outer board omitted because absent from source.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b003cefb-7628-4518-a203-95ce607f5b82'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/circuit_b003cefb-7628-4518-a203-95ce607f5b82.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'offset-circuit-paths-with-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Offset Circuit Paths with Nodes',)
    keywords = ('circuit', 'nodes', 'paths', 'electronics', 'connections', 'diagram', 'technology')
    def build(self):
        for name,x,y in (('left',14,10),('right',38,10),('lower',28,38)):
            self.add_arc(name+'-a',(x,y-4),(x,y+4),radius_x=4,sweep=True)
            self.add_arc(name+'-b',(x,y+4),(x,y-4),radius_x=4,sweep=True)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        self.add_polyline('left-track',(14,14),(14,24),(6,32),(6,42))
        self.add_polyline('right-track',(38,14),(28,24),(28,34))
        self.relate('connect','left-track','left')
        self.relate('connect','right-track','right')
        self.relate('connect','right-track','lower')
