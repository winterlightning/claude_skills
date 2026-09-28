'loading-bar: Restore the low horizontal capsule and show a partial progress fill with visible empty space. Repaired original in place.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a1357f44-093c-4bb6-93d6-7521033c44d2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__loading-bar/20260927T101636Z-thuan-mac-1/reference/loading bar_a1357f44-093c-4bb6-93d6-7521033c44d2.svg'
AUTHOR = "gpt-6"

class LoadingBar(Solo48):
    icon_id = 'loading-bar'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'loading-bar')

    def build(self):
        # A low rounded track with two slanted progress divisions, as in the source.
        self.add_line('top',(10,10),(38,10))
        self.add_arc('tr',(38,10),(44,16),radius_x=6,sweep=True)
        self.add_line('right',(44,16),(44,32))
        self.add_arc('br',(44,32),(38,38),radius_x=6,sweep=True)
        self.add_line('bottom',(38,38),(10,38))
        self.add_arc('bl',(10,38),(4,32),radius_x=6,sweep=True)
        self.add_line('left',(4,32),(4,16))
        self.add_arc('tl',(4,16),(10,10),radius_x=6,sweep=True)
        self.add_contour('track','top','tr','right','br','bottom','bl','left','tl',closed=True)
        for index,(top_x,bottom_x) in enumerate(((20,14),(32,26))):
            part=f'divider-{index}'
            self.add_line(part,(top_x,10),(bottom_x,38))
            self.relate('connect',part,'track')
