"""Round-topped tombstone on projecting ground. Omit ambiguous T inscription instead of inventing letter or religious content. Shared upright walls and circular crown.
Lucide house: coherent vertical walls and ground joins; circular crown reconstructed independently.
Keyshape VRECT_L on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd26441e3-9384-56ce-a3fa-339ff35c82bb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/halloween graveyard_d26441e3-9384-56ce-a3fa-339ff35c82bb.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/halloween graveyard_d26441e3-9384-56ce-a3fa-339ff35c82bb.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/halloween graveyard_d26441e3-9384-56ce-a3fa-339ff35c82bb.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'tombstone-with-t-shaped-engraving-batch-013'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('tombstone', 'with', 't', 'shaped', 'engraving')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_arc('crown',(12,16),(36,16),radius_x=12)
        self.add_line('right',(36,16),(36,44))
        self.add_line('left',(12,44),(12,16))
        self.add_contour('stone','left','crown','right')
        self.add_polyline('ground',(8,44),(12,44),(36,44),(40,44))
        self.relate('connect','stone','ground')
