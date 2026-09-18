'Round bomb body; upper fuse attachment and detached spark. Lucide bomb circular body construction. Fuse intentionally points right. Omit neck ring and reduce sparks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16dc929d-f417-42ec-9982-47da477969ca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gunpowder_16dc929d-f417-42ec-9982-47da477969ca.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'round-bomb-with-burning-fuse-batch-057'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/tools'
    aliases = ()
    keywords = ('bomb', 'fuse', 'spark', 'explosive', 'round', 'danger')

    def build(self):
        cx,cy,r=24,28,16
        self.add_arc('body-left',(cx,cy-r),(cx,cy+r),radius_x=r,sweep=False)
        self.add_arc('body-right',(cx,cy+r),(cx,cy-r),radius_x=r,sweep=False)
        self.add_contour('body','body-left','body-right',closed=True)
        self.add_arc('fuse',(24,12),(31,4),radius_x=7, radius_y=8)
        self.relate('connect','body','fuse')
        self.add_line('spark',(40,4),(40,6))
