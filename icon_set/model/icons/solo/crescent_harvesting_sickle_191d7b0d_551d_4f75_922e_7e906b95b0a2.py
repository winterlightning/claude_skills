"""Curved Harvesting Sickle Tool.
Plan: Diagonal handle attached to a broad crescent blade. Extrema (6,6)-(42,42).
Reference: Supplied source; no useful exact Lucide match. Coherent curves and shared attachment points.
Reduction: Narrow collar and handle seam omitted; crescent and long grip retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '191d7b0d-551d-4f75-922e-7e906b95b0a2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/sickle_191d7b0d-551d-4f75-922e-7e906b95b0a2.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'crescent-harvesting-sickle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('curved', 'harvesting', 'sickle', 'tool')

    def build(self):

        self.add_bezier('outer',(26,6),((36,6),(42,15),(42,24)),((42,36),(30,39),(20,34)))
        self.add_bezier('inner',(18,22),((34,28),(38,15),(26,6)))
        self.add_line('handle-a',(20,34),(12,42))
        self.add_arc('handle-end',(12,42),(6,36),radius_x=6)
        self.add_line('handle-b',(6,36),(18,22))
        self.add_contour('sickle','outer','handle-a','handle-end','handle-b','inner',closed=True)
