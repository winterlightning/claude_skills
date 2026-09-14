# Variant of hanging-chinese-lanterns; parent file remains unchanged.
'Hanging chinese lanterns: independent spacing revision.\n\nRoomier suspensions and separated paired lanterns on current square bounds.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6d427347-19df-52f8-8b2b-203c7d2684b1'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/chinese lantern_6d427347-19df-52f8-8b2b-203c7d2684b1.svg'
AUTHOR = 'gpt-6'

class HangingChineseLanternsVariant2(Solo48):
    icon_id = 'hanging-chinese-lanterns-v2'
    variant_of = 'hanging-chinese-lanterns'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture/objects'
    aliases = ()
    keywords = ('lantern', 'chinese', 'festival', 'lunar new year', 'hanging', 'bunting', 'celebration', 'asian')

    def build(self):
        self.add_polyline('cord',(6, 6),(12, 6),(36, 6),(42, 6),closed=False)
        self.add_line('left-suspension',(12, 6),(12, 18))
        self.add_arc('left-ne',(12, 18),(18, 27),radius_x=6,radius_y=9,sweep=True)
        self.add_arc('left-se',(18, 27),(12, 36),radius_x=6,radius_y=9,sweep=True)
        self.add_arc('left-sw',(12, 36),(6, 27),radius_x=6,radius_y=9,sweep=True)
        self.add_arc('left-nw',(6, 27),(12, 18),radius_x=6,radius_y=9,sweep=True)
        self.add_contour('left','left-ne','left-se','left-sw','left-nw',closed=True)
        self.add_polyline('left-cap',(8, 18),(12, 18),(16, 18),closed=False)
        self.add_polyline('left-base',(8, 36),(12, 36),(16, 36),closed=False)
        self.add_line('left-tassel',(12, 36),(12, 42))
        self.relate('connect','left','left-suspension','left-cap')
        self.relate('connect','left','left-tassel','left-base')
        self.relate('connect','cord','left-suspension')
        self.add_line('right-suspension',(36, 6),(36, 14))
        self.add_arc('right-ne',(36, 14),(42, 23),radius_x=6,radius_y=9,sweep=True)
        self.add_arc('right-se',(42, 23),(36, 32),radius_x=6,radius_y=9,sweep=True)
        self.add_arc('right-sw',(36, 32),(30, 23),radius_x=6,radius_y=9,sweep=True)
        self.add_arc('right-nw',(30, 23),(36, 14),radius_x=6,radius_y=9,sweep=True)
        self.add_contour('right','right-ne','right-se','right-sw','right-nw',closed=True)
        self.add_polyline('right-cap',(32, 14),(36, 14),(40, 14),closed=False)
        self.add_polyline('right-base',(32, 32),(36, 32),(40, 32),closed=False)
        self.add_line('right-tassel',(36, 32),(36, 38))
        self.relate('connect','right','right-suspension','right-cap')
        self.relate('connect','right','right-tassel','right-base')
        self.relate('connect','cord','right-suspension')
