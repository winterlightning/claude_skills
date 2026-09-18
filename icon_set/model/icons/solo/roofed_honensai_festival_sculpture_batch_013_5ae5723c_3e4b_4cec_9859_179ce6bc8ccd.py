"""Roofed festival sculpture on a plinth, with unequal side projections. Shared central axis and roof/body attachments; omit tiny smile and base thickness.
Lucide house: roof-to-upright attachment nodes; source supplies unequal projections.
Keyshape VRECT_L on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ae5723c-3e4b-4cec-9859-179ce6bc8ccd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/honensai_5ae5723c-3e4b-4cec-9859-179ce6bc8ccd.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/honensai_5ae5723c-3e4b-4cec-9859-179ce6bc8ccd.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/honensai_5ae5723c-3e4b-4cec-9859-179ce6bc8ccd.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'roofed-honensai-festival-sculpture-batch-013'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'culture/festivals'
    aliases = ()
    keywords = ('roofed', 'honensai', 'festival', 'sculpture')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_polyline('roof',(10,16),(24,4),(38,16),(32,16),(16,16),closed=True)
        self.add_polyline('body-left',(16,16),(16,28),(16,44))
        self.add_polyline('body-right',(32,16),(32,28),(32,44))
        for s in ('left','right'): self.relate('connect','roof','body-'+s)
        self.add_line('band',(16,28),(32,28))
        for s in ('left','right'): self.relate('connect','band','body-'+s)
        self.add_line('projection-left',(8,28),(16,28))
        self.add_polyline('projection-right',(32,28),(40,24))
        self.relate('connect','projection-left','body-left')
        self.relate('connect','projection-left','band')
        self.relate('connect','projection-right','body-right')
        self.relate('connect','projection-right','band')
        self.add_polyline('base',(8,44),(16,44),(32,44),(40,44))
        for s in ('left','right'): self.relate('connect','base','body-'+s)
