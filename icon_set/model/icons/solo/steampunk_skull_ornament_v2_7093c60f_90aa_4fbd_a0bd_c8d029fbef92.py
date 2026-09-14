# Variant of steampunk-skull-ornament; parent file remains unchanged.
'Steampunk skull ornament: independent spacing revision.\n\nKeep forehead band and skull jaw; filled eyes/nose replace cramped rings, wedge and tooth marks.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7093c60f-90aa-4fbd-a0bd-c8d029fbef92'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/steampunk decoration dia de los muertos_7093c60f-90aa-4fbd-a0bd-c8d029fbef92.svg'
AUTHOR = 'gpt-6'

class SteampunkSkullOrnamentVariant2(Solo48):
    icon_id = 'steampunk-skull-ornament-v2'
    variant_of = 'steampunk-skull-ornament'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('skull', 'steampunk', 'ornament', 'teeth', 'eyes', 'dia de los muertos', 'decor')

    def build(self):
        self.add_line('top',(14, 6),(34, 6))
        self.add_arc('tr',(34, 6),(42, 14),radius_x=8,radius_y=8,sweep=True)
        self.add_line('right',(42, 14),(42, 28))
        self.add_arc('cheek-right',(42, 28),(34, 36),radius_x=8,radius_y=8,sweep=True)
        self.add_polyline('jaw',(34, 36),(34, 42),(14, 42),(14, 36),closed=False)
        self.add_arc('cheek-left',(14, 36),(6, 28),radius_x=8,radius_y=8,sweep=True)
        self.add_line('left',(6, 28),(6, 14))
        self.add_arc('tl',(6, 14),(14, 6),radius_x=8,radius_y=8,sweep=True)
        self.contours = [c for c in self.contours if c.contour_id != 'jaw']
        self.add_contour('skull','top','tr','right','cheek-right','jaw-1','jaw-2','jaw-3','cheek-left','left','tl',closed=True)
        self.add_line('band',(6, 14),(42, 14))
        self.relate('connect','skull','band')
        self.add_dot('eye-left',(16, 25))
        self.add_dot('eye-right',(32, 25))
        self.add_dot('nose',(24, 33))
