"""Phone shell under a two-scallop awning; centered bottom bezel.
Keyshape ink bounds: (6, 2, 42, 46).
Construction reference: Lucide store; source render establishes subject.
Reduction: Four narrow awning scallops reduced to two broad lobes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52c708f4-a507-499a-ba67-b97481d798ed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mobile shop 1_52c708f4-a507-499a-ba67-b97481d798ed.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/mobile shop 1_52c708f4-a507-499a-ba67-b97481d798ed.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'mobile-storefront-batch-025-05'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('mobile', 'storefront')

    def build(self):
        self.add_line('awning-top-1', (8, 16), (12, 4))
        self.add_line('awning-top-2', (12, 4), (36, 4))
        self.add_line('awning-top-3', (36, 4), (40, 16))
        self.add_arc('scallop-right',(40,16),(24,16),radius_x=8,radius_y=5)
        self.add_arc('scallop-left',(24,16),(8,16),radius_x=8,radius_y=5)
        self.add_contour('awning','awning-top-1','awning-top-2','awning-top-3','scallop-right','scallop-left',closed=True)
        self.add_line('phone-1', (8, 16), (8, 40))
        self.add_arc('bl',(8,40),(12,44),radius_x=4,sweep=False)
        self.add_line('base',(12,44),(36,44))
        self.add_arc('br',(36,44),(40,40),radius_x=4,sweep=False)
        self.add_line('right',(40,40),(40,16))
        self.add_contour('shell','phone-1','bl','base','br','right')
        self.relate('connect','shell','awning')
        self.add_line('bezel',(8,35),(40,35))
        self.relate('connect','bezel','shell')
