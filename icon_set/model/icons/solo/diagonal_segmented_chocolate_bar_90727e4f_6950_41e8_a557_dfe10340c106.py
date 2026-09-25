'Chocolate bar rotated toward upper right, two columns and three exposed rows above a plain wrapper band. SQUARE accommodates the diagonal. A shared integer basis defines all grid intersections with 8.49 centerline separation; all grid contacts are real split nodes. Source supplies diagonal and wrapper. No exact Lucide chocolate-bar match; rectangular grid construction. Reduced exposed block count.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90727e4f-6950-41e8-a557-dfe10340c106'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/chocolate_90727e4f-6950-41e8-a557-dfe10340c106.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'diagonal-segmented-chocolate-bar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Diagonal Segmented Chocolate Bar',)
    keywords = ('chocolate', 'bar', 'blocks', 'food', 'sweet', 'candy', 'segments')
    def build(self):
        def node(row,col): return (30-6*row+6*col,6+6*row+6*col)
        boundary=[node(0,0),node(0,1),node(0,2)]+[node(r,2) for r in range(1,5)]+[node(4,0)]+[node(r,0) for r in range(3,0,-1)]
        self.add_polyline('bar',*boundary,closed=True)
        self.add_polyline('column',*(node(r,1) for r in range(4)))
        self.relate('connect','column','bar')
        for row in range(1,4):
            name=f'row-{row}'
            self.add_polyline(name,*(node(row,c) for c in range(3)))
            self.relate('connect',name,'bar')
            self.relate('connect',name,'column')
