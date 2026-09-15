"""Two grain ears above a broad mound. VRECT extremes (8,4)-(40,44); ear repeats share barb spacing with unequal heights.
Reduction: Reduced barbs to two pairs per ear and overlapping mounds to one broad mound.
Lucide: wheat
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f25bca26-2843-43fb-ae33-1a0de098f1b5'
SOURCE_PATH = 'pictographic-primitives/nature/reishit katzir feast of firstfruits_f25bca26-2843-43fb-ae33-1a0de098f1b5.svg'
AUTHOR = 'gpt-6'

class GrainStalksAndMounds(Solo48):
    icon_id = 'grain-stalks-and-mounds'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-03"
    aliases = ()
    keywords = ('firstfruits', 'grain', 'barley', 'harvest', 'stalks', 'feast', 'agriculture', 'offering')

    def build(self) -> None:
        for n,(x,top) in enumerate(((14,8),(34,4))):
         levels=(top,top+8,top+20)
         for j in range(2):self.add_line(f'stem-{n}-{j}',(x,levels[j]),(x,levels[j+1]))
         for j,y in enumerate(levels[1:]):
          self.add_polyline(f'barb-{n}-{j}',(x-6,y-6),(x,y),(x+6,y-6))
          for side in (1,2):
           self.relate('connect',f'barb-{n}-{j}-{side}',f'stem-{n}-{j}')
           if j==0:self.relate('connect',f'barb-{n}-{j}-{side}',f'stem-{n}-1')
        self.add_arc('mound',(8,44),(40,44),radius_x=16,radius_y=6)
        self.add_line('ground',(40,44),(8,44));self.add_contour('earth','mound','ground',closed=True)
