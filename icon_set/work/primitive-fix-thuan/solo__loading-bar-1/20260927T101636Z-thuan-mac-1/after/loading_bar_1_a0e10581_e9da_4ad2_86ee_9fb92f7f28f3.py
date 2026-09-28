"""loading-bar-1: Regular curved loading bar; earlier revisions preserved."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a0e10581-e9da-4ad2-86ee-9fb92f7f28f3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__loading-bar-1/20260927T101636Z-thuan-mac-1/reference/loading bar 1_a0e10581-e9da-4ad2-86ee-9fb92f7f28f3.svg'
AUTHOR = 'gpt-6'

class LoadingBar1(Solo48):
    icon_id = 'loading-bar-1'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('solo-ai-full-set', 'loading-bar-1')

    def build(self):
        # Two equal slanted divisions in a broad horizontal loading track.
        self.add_line('top',(10,10),(38,10))
        self.add_arc('tr',(38,10),(44,16),radius_x=6,sweep=True)
        self.add_line('right',(44,16),(44,32))
        self.add_arc('br',(44,32),(38,38),radius_x=6,sweep=True)
        self.add_line('bottom',(38,38),(10,38))
        self.add_arc('bl',(10,38),(4,32),radius_x=6,sweep=True)
        self.add_line('left',(4,32),(4,16))
        self.add_arc('tl',(4,16),(10,10),radius_x=6,sweep=True)
        self.add_contour('track','top','tr','right','br','bottom','bl','left','tl',closed=True)
        for index,(top_x,bottom_x) in enumerate(((23,15),(36,28))):
            part=f'divider-{index}'
            self.add_line(part,(top_x,10),(bottom_x,38))
            self.relate('connect',part,'track')
