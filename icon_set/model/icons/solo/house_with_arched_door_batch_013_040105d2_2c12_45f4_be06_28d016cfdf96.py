"""House front with steep roof, eaves and a central arched doorway. Mirror about x24, reuse exact eave-wall and doorway-ground nodes.
Lucide house: single facade with roof/wall joints, arched doorway from supplied source.
Keyshape SQUARE on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '040105d2-2c12-45f4-be06-28d016cfdf96'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house_040105d2-2c12-45f4-be06-28d016cfdf96.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_040105d2-2c12-45f4-be06-28d016cfdf96.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/house_040105d2-2c12-45f4-be06-28d016cfdf96.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'house-with-arched-door-batch-013'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('house', 'with', 'arched', 'door')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_polyline('roof',(6,24),(10,20),(24,6),(38,20),(42,24))
        self.add_polyline('walls',(10,20),(10,42),(18,42),(30,42),(38,42),(38,20))
        self.relate('connect','roof','walls')
        self.add_line('door-left',(18,42),(18,30))
        self.add_arc('door-arch',(18,30),(30,30),radius_x=6)
        self.add_line('door-right',(30,30),(30,42))
        self.add_contour('door','door-left','door-arch','door-right')
        self.relate('connect','door','walls')
