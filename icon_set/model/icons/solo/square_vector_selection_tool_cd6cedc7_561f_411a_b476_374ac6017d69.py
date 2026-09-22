"""Square Vector Selection Tool. Four equal corner handles attached at edge midpoints to an empty square selection frame. Square bounds 6 to 42. Lucide scan informs the open center and four-corner symmetry; handles retained from source, square corners simplify the small loops."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'cd6cedc7-561f-411a-b476-374ac6017d69'
SOURCE_PATH = 'pictographic-primitives/design/vectors anchor square_cd6cedc7-561f-411a-b476-374ac6017d69.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'square-vector-selection-tool'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    aliases = ('Square Vector Selection Tool',)
    keywords = ('square', 'vector', 'selection', 'tool')
    def build(self):
        # Four corner handles share the same square definition.
        for i,(x,y) in enumerate(((6,6),(34,6),(34,34),(6,34))):
            name=f'handle-{i}'
            self.add_polyline(name,(x+4,y),(x+8,y),(x+8,y+4),(x+8,y+8),(x+4,y+8),(x,y+8),(x,y+4),(x,y),(x+4,y),closed=True)
        for name,a,b,owners in (
            ('top',(14,10),(34,10),(0,1)),
            ('right',(38,14),(38,34),(1,2)),
            ('bottom',(34,38),(14,38),(2,3)),
            ('left',(10,34),(10,14),(3,0))):
            self.add_line(name,a,b)
            for owner in owners:self.relate('connect',name,f'handle-{owner}')
