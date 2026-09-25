"""Horizontal striped bar with two repeated rising diagonal divisions.
HRECT_M envelope x4..44/y10..38. Source supplies rounded border and diagonal
seams; reduce three seams to two to retain clearance. Lucide rectangle-horizontal
supplies tangent rounded corners. Shared endpoints split receiving border runs.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '537ef89a-3255-4de5-963f-3e20a738be5d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_36/strip_537ef89a-3255-4de5-963f-3e20a738be5d.svg'
AUTHOR = 'gpt-6-astra'
class RoundedHorizontalStrip(Solo48):
    icon_id = 'rounded-horizontal-strip-with-diagonal-bands'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ('Diagonal Patterned Horizontal Bar',)
    keywords = ('strip','band','stripes','diagonal','rectangle','pattern')
    def build(self):
        nodes={};border=[]
        def line(n,a,b):
            self.add_line(n,a,b)
            for pt in (a,b):nodes.setdefault(pt,[]).append(n)
        def arc(n,a,b):
            self.add_arc(n,a,b,radius_x=4)
            for pt in (a,b):nodes.setdefault(pt,[]).append(n)
        for i,(a,b) in enumerate(zip([8,24,36],[24,36,40])):
            n=f'top-{i}';line(n,(a,10),(b,10));border.append(n)
        arc('tr',(40,10),(44,14));line('right',(44,14),(44,34));arc('br',(44,34),(40,38));border+=['tr','right','br']
        for i,(a,b) in enumerate(zip([40,24,12],[24,12,8])):
            n=f'bottom-{i}';line(n,(a,38),(b,38));border.append(n)
        arc('bl',(8,38),(4,34));line('left',(4,34),(4,14));arc('tl',(4,14),(8,10));border+=['bl','left','tl']
        self.add_contour('border',*border,closed=True)
        for i,x in enumerate((12,24)):line(f'seam-{i}',(x,38),(x+12,10))
        from itertools import combinations
        for members in nodes.values():
            for a,b in combinations(members,2):self.relate('connect',a,b)
