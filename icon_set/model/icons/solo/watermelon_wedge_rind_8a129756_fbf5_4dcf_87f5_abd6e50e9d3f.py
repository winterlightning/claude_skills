"""Watermelon semicircle with broad rind and seed. HRECT_M 4,10..44,38.
Reorient the cut horizontally to budget rind and seed clearance. Mirror arcs about x24.
Reference supplies the rind band; reduce three seeds to one. No exact Lucide match.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='8a129756-fbf5-4dcf-87f5-abd6e50e9d3f'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/melon_8a129756-fbf5-4dcf-87f5-abd6e50e9d3f.svg'
AUTHOR='gpt-6-astra'
class Drawing(Solo48):
    icon_id='watermelon-wedge-rind'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=('watermelon slice',)
    keywords=('watermelon','fruit','slice','rind','seeds','food')
    def build(self):
        for i,(a,b) in enumerate(((4,13),(13,35),(35,44))):self.add_line(f'cut-{i}',(a,10),(b,10))
        self.add_arc('rind-outer',(44,10),(4,10),radius_x=20,radius_y=28)
        self.add_arc('rind-inner',(35,10),(13,10),radius_x=11,radius_y=19)
        self.add_contour('outline','cut-0','cut-1','cut-2','rind-outer',closed=True)
        self.relate('connect','outline','rind-inner')
        self.add_dot('seed',(24,19))
