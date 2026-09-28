"""A long rounded handle angles upward-right into a broad hammer head. One side has a curved claw opening, while the opposite side ends in a short angular striking face.
Symbol plan: One coherent claw-hammer silhouette with a circular grip end and parallel diagonal handle sides. Preserve the claw opening and angular striking face; omit grip decoration.
Keyshape: CIRCLE; centerline extremes radius 20 about (24,24).
Construction reference: hammer; local original and atomic geometry inspected for Lucide.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '20af476c-a57f-4ace-b516-465f1fa2eefd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__claw-hammer-on-diagonal/20260927T032242Z-thuan-mac-1/reference/hammer_20af476c-a57f-4ace-b516-465f1fa2eefd.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'claw-hammer-on-diagonal'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'state')
    aliases = ()
    keywords = ('claw', 'hammer', 'on', 'diagonal')

    def build(self) -> None:
        # One connected silhouette: hooked claw, sloping head and long grip.
        self.add_line('grip-left',(10,30),(22,17))
        self.add_bezier('claw-inner',(22,17),((21,14),(18,11),(14,10)))
        self.add_bezier('claw-outer',(14,10),((19,7),(24,8),(29,10)))
        points=[(29,10),(39,19),(44,24),(36,29),(31,24)]
        for j,(a,b) in enumerate(zip(points,points[1:])): self.add_line(f'head-{j}',a,b)
        self.add_line('grip-right',(31,24),(16,38))
        self.add_bezier('grip-end',(16,38),((12,40),(9,36),(10,30)))
        self.add_contour('hammer','grip-left','claw-inner','claw-outer','head-0','head-1','head-2','head-3','grip-right','grip-end',closed=True)
