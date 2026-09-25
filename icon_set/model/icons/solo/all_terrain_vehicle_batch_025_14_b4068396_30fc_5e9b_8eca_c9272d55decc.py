"""Paired large off-road tires beneath high angular fenders and raised handlebar.
Keyshape ink bounds: (2, 6, 46, 42).
Construction reference: Lucide car; source render establishes subject.
Reduction: No tire tread or extra fender layer; open footwell retained in body step.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4068396-30fc-5e9b-8eca-c9272d55decc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/car atv_b4068396-30fc-5e9b-8eca-c9272d55decc.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/car atv_b4068396-30fc-5e9b-8eca-c9272d55decc.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'all-terrain-vehicle-batch-025-14'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('all', 'terrain', 'vehicle')

    def build(self):
        for x,tag in ((11,'rear'),(37,'front')):
         self.add_arc(tag+'-a',(x-7,33),(x+7,33),radius_x=7)
         self.add_arc(tag+'-b',(x+7,33),(x-7,33),radius_x=7)
         self.add_contour(tag,tag+'-a',tag+'-b',closed=True)
        self.add_polyline('body',(4,18),(15,18),(21,21),(27,21),(32,18),(44,18))
        self.add_polyline('handle',(25,8),(30,8),(34,18))
        self.relate('connect','handle','body')
