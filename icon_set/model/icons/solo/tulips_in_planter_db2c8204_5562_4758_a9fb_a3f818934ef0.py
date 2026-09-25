"""Two repeated notched tulip heads grow in a wide planter. HRECT extremes (4,8)-(44,40); shared flower dimensions and stems.
Reduction: Reduced three flowers to two and omitted inner marks and rim band.
Lucide: flower-2
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db2c8204-5562-4758-a9fb-a3f818934ef0'
SOURCE_PATH = 'pictographic-primitives/nature/roses_db2c8204-5562-4758-a9fb-a3f818934ef0.svg'
AUTHOR = 'gpt-6'

class TulipsInPlanter(Solo48):
    icon_id = 'tulips-in-planter'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('tulips', 'flowers', 'planter', 'window box', 'garden', 'spring', 'roses', 'potted')

    def build(self) -> None:
        for n,x in enumerate((12,36)):
         self.add_line(f'tips-{n}-1',(x-6,8),(x,12));self.add_line(f'tips-{n}-2',(x,12),(x+6,8))
         self.add_arc(f'right-{n}',(x+6,8),(x,22),radius_x=6,radius_y=14)
         self.add_arc(f'left-{n}',(x,22),(x-6,8),radius_x=6,radius_y=14)
         self.add_contour(f'flower-{n}',f'tips-{n}-1',f'tips-{n}-2',f'right-{n}',f'left-{n}',closed=True)
         self.add_line(f'stem-{n}',(x,22),(x,30))
         for p in ('right','left'): self.relate('connect',f'stem-{n}',f'{p}-{n}')
        self.add_polyline('pot',(4,30),(12,30),(36,30),(44,30),(40,40),(8,40),closed=True)
        for n in range(2):
         for j in (n+1,n+2):self.relate('connect',f'stem-{n}',f'pot-{j}')
