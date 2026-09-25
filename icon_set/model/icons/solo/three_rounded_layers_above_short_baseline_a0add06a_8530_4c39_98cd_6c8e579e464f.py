"""Three rounded layers above a separate baseline. VRECT_L (8,4)-(40,44).
The stack owns three equal ten-unit layers, radius-five ends and shared seams.
One outer contour avoids overlapping closed capsules. Lucide database informs
shared layer boundaries; reference supplies capsule ends and detached baseline.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'a0add06a-8530-4c39-98cd-6c8e579e464f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/sprag_a0add06a-8530-4c39-98cd-6c8e579e464f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'three-rounded-layers-above-short-baseline'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ['Database Storage Stack']
    keywords = ['layers','stack','capsules','baseline','shape','diagram']
    def build(self):
        self.add_line('top',(13,4),(35,4))
        for i in range(3):
            y=4+10*i
            self.add_arc(f'right-{i}',(35,y),(35,y+10),radius_x=5)
            self.add_arc(f'left-{i}',(13,y+10),(13,y),radius_x=5)
        self.add_line('bottom',(35,34),(13,34))
        self.add_contour('stack','top','right-0','right-1','right-2','bottom','left-2','left-1','left-0',closed=True)
        for i in range(2):
            self.add_line(f'seam-{i}',(13,14+10*i),(35,14+10*i))
            for side in ['left','right']:
                for j in [i,i+1]:self.relate('connect',f'seam-{i}',f'{side}-{j}')
        self.add_line('baseline',(8,44),(40,44))
