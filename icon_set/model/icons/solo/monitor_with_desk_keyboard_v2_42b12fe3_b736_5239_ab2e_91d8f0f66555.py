# Variant of monitor-with-desk-keyboard; parent file remains unchanged.
'Monitor with desk keyboard: independent spacing revision.\n\nNine-unit stand separation and a deeper keyboard opening.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '42b12fe3-b736-5239-ab2e-91d8f0f66555'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/desktop monitor keyboard_42b12fe3-b736-5239-ab2e-91d8f0f66555.svg'
AUTHOR = 'gpt-6'

class MonitorWithDeskKeyboardVariant2(Solo48):
    icon_id = 'monitor-with-desk-keyboard-v2'
    variant_of = 'monitor-with-desk-keyboard'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('monitor', 'keyboard', 'desktop', 'computer', 'workstation', 'screen', 'typing', 'pc')

    def build(self):
        self.add_line('top',(9, 6),(39, 6))
        self.add_arc('ne',(39, 6),(42, 9),radius_x=3,radius_y=3,sweep=True)
        self.add_line('right',(42, 9),(42, 21))
        self.add_arc('se',(42, 21),(39, 24),radius_x=3,radius_y=3,sweep=True)
        self.add_polyline('bottom',(39, 24),(24, 24),(9, 24),closed=False)
        self.add_arc('sw',(9, 24),(6, 21),radius_x=3,radius_y=3,sweep=True)
        self.add_line('left',(6, 21),(6, 9))
        self.add_arc('nw',(6, 9),(9, 6),radius_x=3,radius_y=3,sweep=True)
        self.contours = [c for c in self.contours if c.contour_id != 'bottom']
        self.add_contour('screen','top','ne','right','se','bottom-1','bottom-2','sw','left','nw',closed=True)
        self.add_line('stand',(24, 24),(24, 33))
        self.add_polyline('keyboard',(10, 33),(24, 33),(38, 33),(42, 42),(6, 42),closed=True)
        self.relate('connect','screen','stand')
        self.relate('connect','keyboard','stand')
