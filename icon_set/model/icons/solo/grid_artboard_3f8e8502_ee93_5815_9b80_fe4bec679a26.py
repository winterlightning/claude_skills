"""A square artboard is surrounded by eight detached crop marks.
Lucide frame: shared horizontal and vertical levels; source requires detached crop marks instead of crossing rails.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3f8e8502-ee93-5815-9b80-fe4bec679a26'
SOURCE_PATH = 'icon_set/work/todo-references/grid artboard_3f8e8502-ee93-5815-9b80-fe4bec679a26.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'grid-artboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('grid', 'artboard')
    def build(self):

        # Plan: square plus a mirrored four-corner series of two crop strokes.
        # SQUARE visible extrema (4,4)-(44,44), centerlines (6,6)-(42,42).
        lo,hi=16,32
        self.add_polyline('artboard',(lo,lo),(hi,lo),(hi,hi),(lo,hi),closed=True)
        for x in (lo,hi):
            for y in (lo,hi):
                a,b=(6,8) if y==lo else (40,42)
                self.add_line(f'vertical-{x}-{y}',(x,a),(x,b))
                a,b=(6,8) if x==lo else (40,42)
                self.add_line(f'horizontal-{x}-{y}',(a,y),(b,y))
