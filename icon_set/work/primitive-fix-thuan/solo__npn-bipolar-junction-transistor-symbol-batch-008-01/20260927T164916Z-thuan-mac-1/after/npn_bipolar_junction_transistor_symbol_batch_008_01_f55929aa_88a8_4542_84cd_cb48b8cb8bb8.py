"""NPN Bipolar Junction Transistor Symbol.
Plan: NPN base, collector and outward emitter arrow retained; optional enclosing circle omitted for clear circuit topology.
Construction reference: Lucide cpu; independently solved SOLO48 geometry.
Source copy inspected: work/brief-exports/20260917-all-todo-batches-15/batches/batch-008/references/npn bipolar transistor_f55929aa-88a8-4542-84cd-cb48b8cb8bb8.svg
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f55929aa-88a8-4542-84cd-cb48b8cb8bb8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__npn-bipolar-junction-transistor-symbol-batch-008-01/20260927T164916Z-thuan-mac-1/reference/npn bipolar transistor_f55929aa-88a8-4542-84cd-cb48b8cb8bb8.svg'
AUTHOR = 'gpt-6'


class GeneratedSolo(Solo48):
    icon_id = 'npn-bipolar-junction-transistor-symbol-batch-008-01'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    categories = ("electronics", "primitives")
    aliases = ()
    keywords = ('npn', 'bipolar', 'junction', 'transistor', 'symbol')

    def build(self):
        # A circular transistor case with an input base, collector, and outward emitter.
        quadrants = ((8,24),(24,8),(40,24),(24,40))
        for j in range(4):
            self.add_arc(f'case-{j}',quadrants[j],quadrants[(j+1)%4],radius_x=16)
        self.add_contour('case',*(f'case-{j}' for j in range(4)),closed=True)
        self.add_line('base-lead',(8,24),(18,24))
        self.add_line('base-upper',(18,18),(18,24))
        self.add_line('base-lower',(18,24),(18,30))
        self.add_line('collector',(18,18),(24,8))
        self.add_line('collector-lead',(24,8),(24,4))
        self.add_line('emitter',(18,30),(24,40))
        self.add_line('emitter-lead',(24,40),(24,44))
        self.add_polyline('arrow',(18,38),(24,40),(22,34))
        self.relate('connect','case','base-lead','collector','collector-lead','emitter','emitter-lead','arrow')
        self.relate('connect','base-lead','base-upper','base-lower')
        self.relate('connect','base-upper','base-lower','collector')
        self.relate('connect','base-lower','emitter')
        self.relate('connect','collector','collector-lead')
        self.relate('connect','emitter','emitter-lead','arrow')
