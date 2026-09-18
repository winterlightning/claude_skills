"""Upper-right kite with a curling tail, asymmetric flame at lower left. Omit internal spars and tiny fuel strokes.
Lucide flame: coherent asymmetric flame silhouette.
Keyshape SQUARE on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0de72e2d-97f0-4d32-ba42-4be760f786bb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/lohri kite_0de72e2d-97f0-4d32-ba42-4be760f786bb.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/lohri kite_0de72e2d-97f0-4d32-ba42-4be760f786bb.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/lohri kite_0de72e2d-97f0-4d32-ba42-4be760f786bb.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'kite-above-bonfire-batch-013'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'culture/festivals'
    aliases = ()
    keywords = ('kite', 'above', 'bonfire')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_polyline('kite',(32,6),(42,16),(32,26),(22,16),closed=True)
        self.add_bezier('tail',(32,26),((32,34),(42,34),(42,42)))
        self.relate('connect','kite','tail')
        self.add_bezier('flame',(14,20),((16,27),(24,29),(24,34)),((24,39),(20,42),(15,42)),((9,42),(6,38),(6,33)),((6,30),(8,27),(9,26)),((8,33),(16,32),(14,20)))
        self.add_contour('fire','flame',closed=True)
