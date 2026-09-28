"""Paired equal wheels, sparse sloping frame and shared seat/handlebar attachment nodes.
Keyshape ink bounds: (2, 6, 46, 42).
Construction reference: Lucide bike; source render establishes subject.
Reduction: No spokes or pedals, as in sparse source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e453f0c-f93f-44b5-be89-28ecbc5f97cb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/bike_0e453f0c-f93f-44b5-be89-28ecbc5f97cb.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/bike_0e453f0c-f93f-44b5-be89-28ecbc5f97cb.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'bicycle-solo-batch-025-04'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('bicycle', 'solo')

    def build(self):
        for x,tag in ((11,'rear'),(37,'front')):
         self.add_arc(tag+'-a',(x,26),(x,40),radius_x=7)
         self.add_arc(tag+'-b',(x,40),(x,26),radius_x=7)
         self.add_contour(tag,tag+'-a',tag+'-b',closed=True)
        self.add_polyline('frame',(11,26),(20,23),(33,18),(37,26))
        self.add_line('seatpost',(20,23),(15,8))
        self.add_polyline('seat',(11,8),(15,8),(19,8))
        self.add_polyline('handle',(33,18),(30,10),(35,8))
        for a,b in [('frame','rear'),('frame','front'),('frame','seatpost'),('seatpost','seat'),('frame','handle')]: self.relate('connect',a,b)
