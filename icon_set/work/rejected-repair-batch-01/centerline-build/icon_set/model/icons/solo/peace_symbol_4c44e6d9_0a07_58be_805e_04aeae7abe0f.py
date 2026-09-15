"""A circular peace emblem with a central stem and paired downward branches.

Construction: No useful exact local match; simple circular arcs and a shared central junction.
Reduction: No features omitted; diagonal endpoints use the integer 12/16/20 radius triangle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c44e6d9-0a07-58be-805e-04aeae7abe0f'
SOURCE_PATH = 'pictographic-primitives/travel/peace_4c44e6d9-0a07-58be-805e-04aeae7abe0f.svg'
AUTHOR = 'gpt-6'


class PeaceSymbol(Solo48):
    icon_id = 'peace-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('peace', 'symbol', 'sign', 'pacifism', 'harmony', 'circle', 'antiwar')

    def build(self) -> None:
        # CIRCLE: center (24,24), centerline radius20, visible radius22.
        points=[(24,6),(36,40),(24,42),(12,40),(24,6)]
        for i,(a,b) in enumerate(zip(points,points[1:])):
         self.add_arc(f'rim-{i}',a,b,radius_x=20)
        self.add_contour('rim',*(f'rim-{i}' for i in range(4)),closed=True)
        for name,end in [('top',(24,6)),('bottom',(24,42)),('left',(12,40)),('right',(36,40))]:
         self.add_line(name,(24,24),end)
         self.relate('connect','rim',name)
        for a,b in [('top','bottom'),('top','left'),('top','right'),('bottom','left'),('bottom','right'),('left','right')]:
         self.relate('connect',a,b)
