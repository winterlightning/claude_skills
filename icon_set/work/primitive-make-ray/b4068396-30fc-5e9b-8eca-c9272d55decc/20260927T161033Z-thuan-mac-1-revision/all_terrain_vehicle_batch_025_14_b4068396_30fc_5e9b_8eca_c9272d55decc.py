"""Paired large off-road tires beneath high angular fenders and raised handlebar.
Keyshape ink bounds: (2, 6, 46, 42).
Construction reference: Lucide car; source render establishes subject.
Reduction: No tire tread or extra fender layer; open footwell retained in body step.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b4068396-30fc-5e9b-8eca-c9272d55decc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__all-terrain-vehicle-batch-025-14/20260927T160834Z-thuan-mac-1/reference/car atv_b4068396-30fc-5e9b-8eca-c9272d55decc.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/car atv_b4068396-30fc-5e9b-8eca-c9272d55decc.svg'
AUTHOR = "gpt-6"

class Batch025Icon(Solo48):
    icon_id = 'all-terrain-vehicle-batch-025-14'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('all', 'terrain', 'vehicle')

    def build(self):
        for x,tag in ((13,'rear'),(35,'front')):
         self.add_arc(tag+'-a',(x-6,36),(x+6,36),radius_x=6)
         self.add_arc(tag+'-b',(x+6,36),(x-6,36),radius_x=6)
         self.add_contour(tag,tag+'-a',tag+'-b',closed=True)
        self.add_polyline('body',(6,22),(14,20),(18,20),(22,23),(28,23),(34,20),(42,22))
        self.add_polyline('handle',(20,6),(25,6),(30,20))
        self.relate('connect','handle','body')
