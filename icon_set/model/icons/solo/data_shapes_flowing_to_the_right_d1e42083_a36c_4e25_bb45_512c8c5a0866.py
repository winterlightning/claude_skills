'Data circles transform into a block beside a sweeping right arrow. Source supplies the transformation scene; Lucide arrow-right supplies shared tip and head. HRECT_L leaves space for the curved divider. Three circles reduced to two, two blocks to one and upper arrow omitted to keep the transformation legible.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd1e42083-a36c-4e25-bb45-512c8c5a0866'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon web service glue data brew visual data preparation_d1e42083-a36c-4e25-bb45-512c8c5a0866.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'data-shapes-flowing-to-the-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ['Visual Data Preparation']
    keywords = ['data', 'flow', 'shapes', 'arrows', 'conversion', 'circles', 'blocks']
    def build(self):
        for j,y in enumerate((20,34)):
            self.add_arc(f'data-{j}-a',(4,y),(8,y),radius_x=2)
            self.add_arc(f'data-{j}-b',(8,y),(4,y),radius_x=2)
            self.add_contour(f'data-{j}',f'data-{j}-a',f'data-{j}-b',closed=True)
        self.add_polyline('block',(32,8),(44,8),(44,20),(32,20),closed=True)
        self.add_bezier('flow',(4,8),((24,8),(18,34),(44,34)))
        self.add_polyline('arrowhead',(38,28),(44,34),(38,40))
        self.relate('connect','flow','arrowhead')
