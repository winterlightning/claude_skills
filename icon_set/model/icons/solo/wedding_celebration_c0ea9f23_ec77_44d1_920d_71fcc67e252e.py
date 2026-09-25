"""Wedding bunting above two overlapping hearts.
Symbol plan and construction: heart: coherent paired lobes and pointed bases; source supplies hanging flags.
Keyshape: SQUARE balances a broad bunting row above the paired hearts.
Omissions: Three flags reduced to two larger flags, removing undersized triangular holes.
Review: Approved: two open triangular flag counters and two distinct overlapping hearts remain clear in both themes. Rear-heart lobes lowered to separate them from the bunting; shared heart contacts are genuine."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c0ea9f23-ec77-44d1-920d-71fcc67e252e'
SOURCE_PATH = 'pictographic-primitives/romance/wedding celebration_c0ea9f23-ec77-44d1-920d-71fcc67e252e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='wedding-celebration'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'romance'
    aliases=()
    keywords=('wedding', 'celebration')

    # Visible extrema (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Two enlarged bunting flags above two overlapping hearts.
        self.add_polyline('cord',(6,6),(24,6),(42,6))
        for i,(a,b,c) in enumerate(((6,15,24),(24,33,42))):
            self.add_polyline(f'flag-{i}',(a,6),(b,16),(c,6))
            self.relate('connect','cord',f'flag-{i}')
        self.add_bezier('rear-heart',(32,29),((32,24),(24,22),(20,28)),
            ((16,22),(6,24),(6,29)),((6,33),(12,37),(18,39)))
        self.add_line('rear-heart-end',(18,39),(24,35))
        self.add_contour('heart-back','rear-heart','rear-heart-end')
        self.add_bezier('heart-front',(24,35),((23,34),(22,32),(22,30)),
            ((22,24),(29,24),(32,29)),((35,24),(42,24),(42,30)),
            ((42,35),(35,40),(32,42)),((29,40),(26,38),(24,35)))
        self.add_contour('heart-front-outline','heart-front',closed=True)
        self.relate('connect','heart-back','heart-front-outline')
