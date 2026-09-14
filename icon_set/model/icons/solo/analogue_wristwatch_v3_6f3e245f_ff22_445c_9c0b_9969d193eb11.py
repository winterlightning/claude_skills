# Variant of analogue-wristwatch; parent file remains unchanged.
"""An analogue wristwatch with an open strap, circular face and two hands; double bezel and crown omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f3e245f-ff22-445c-9c0b-9969d193eb11'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/watch_6f3e245f-ff22-445c-9c0b-9969d193eb11.svg'
AUTHOR = 'gpt-6'

class AnalogueWristwatchVariant3(Solo48):
    icon_id = 'analogue-wristwatch-v3'
    variant_of = 'analogue-wristwatch'
    variant_label = 'Roomier straps and balanced face'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('watch', 'wristwatch', 'time', 'clock', 'analogue', 'dial', 'strap', 'accessory')

    def build(self):
        # Circular envelope: centerline radius 20. Face radius 13; paired straps.
        self.add_arc('face-a',(19,12),(29,36),radius_x=13)
        self.add_arc('face-b',(29,36),(19,12),radius_x=13)
        self.add_contour('face','face-a','face-b',closed=True)
        for label, y, tip, sweep in [('upper',12,9,True),('lower',36,39,False)]:
            self.add_line(label+'-left',(19,y),(19,tip))
            self.add_arc(label+'-cap',(19,tip),(29,tip),radius_x=5,sweep=sweep)
            self.add_line(label+'-right',(29,tip),(29,y))
            self.add_contour(label,label+'-left',label+'-cap',label+'-right')
            self.relate('connect',label,'face')
        self.add_polyline('hands',(20,22),(24,24),(27,21))
