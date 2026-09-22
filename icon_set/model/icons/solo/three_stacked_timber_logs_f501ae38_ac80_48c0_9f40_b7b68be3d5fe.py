"""Three horizontal timber logs; shared seams avoid doubled contacting outlines.
SQUARE bounds 6..42. Three equal 12-high logs derive from one series.
Reference supplies cut-end circles and stacked bodies; omit grain texture.
Lucide has no useful exact stacked timber construction match.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'f501ae38-ac80-48c0-9f40-b7b68be3d5fe'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/lumber_f501ae38-ac80-48c0-9f40-b7b68be3d5fe.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'three-stacked-timber-logs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('lumber', 'timber stack')
    keywords = ('logs','timber','wood','stack','lumber','trunks','material')
    def build(self):
        for i in range(3):
            top=6+12*i; bottom=top+12
            self.add_arc(f'left-{i}',(12,top),(12,bottom),radius_x=6,sweep=False)
            self.add_arc(f'grain-{i}',(12,top),(12,bottom),radius_x=6,sweep=True)
            self.add_arc(f'right-{i}',(36,top),(36,bottom),radius_x=6,sweep=True)
        for i in range(4):
            y=6+12*i
            self.add_line(f'seam-{i}',(12,y),(36,y))
            left=[f'seam-{i}'];right=[f'seam-{i}']
            for j in (i-1,i):
                if 0<=j<3:
                    left.extend([f'left-{j}',f'grain-{j}'])
                    right.append(f'right-{j}')
            for group in (left,right):
                for a in group:
                    for b in group:
                        if a<b:self.relate('connect',a,b)
