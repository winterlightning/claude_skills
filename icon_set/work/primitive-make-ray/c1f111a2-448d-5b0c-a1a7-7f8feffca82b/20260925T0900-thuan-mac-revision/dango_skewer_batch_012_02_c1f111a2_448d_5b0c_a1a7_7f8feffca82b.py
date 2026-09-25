"""Fresh reference reconstruction for manual fix request. Preserve complete subject and arrangement."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c1f111a2-448d-5b0c-a1a7-7f8feffca82b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dango-skewer-batch-012-02/20260925T085648Z-thuan-mac/reference/japanese sweets dango on stick_c1f111a2-448d-5b0c-a1a7-7f8feffca82b.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'dango-skewer-batch-012-02'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    aliases = ()
    keywords = ()

    def build(self):
        # Three equal round dumplings form a diagonal series; preserve their touching arrangement.
        for i in range(3):
            x,y=11+11*i,37-11*i
            self.add_arc(f'ball-{i}-a',(x-7,y),(x+7,y),radius_x=7)
            self.add_arc(f'ball-{i}-b',(x+7,y),(x-7,y),radius_x=7)
            self.add_contour(f'ball-{i}',f'ball-{i}-a',f'ball-{i}-b',closed=True)
        self.add_line('skewer-tip',(38,10),(44,4))
