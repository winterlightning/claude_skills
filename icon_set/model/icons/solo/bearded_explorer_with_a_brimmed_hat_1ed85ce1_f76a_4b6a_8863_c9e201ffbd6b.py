"""Bearded explorer with a brimmed hat and backpack sides.

VRECT_L (8,4)-(40,44). The large circular jaw accommodates a beard division;
hat band and backpack outline are omitted, keeping crown, brim and the raised backpack sides.
Human user.svg supplies curved open shoulders; Lucide hat-glasses supplies
the crown-to-brim construction. Axis24 owns the mirrored features.
Jaw radius16 at (24,16), bottom32; shoulders36: zero visible ink gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '1ed85ce1-f76a-4b6a-8863-c9e201ffbd6b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/avatar adventure man_1ed85ce1-f76a-4b6a-8863-c9e201ffbd6b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bearded-explorer-with-a-brimmed-hat'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ('Bearded Explorer Avatar',)
    keywords = ('explorer','beard','hat','backpack','straps','person','adventure')

    def build(self):
        self.add_polyline('hat',(12,16),(16,4),(32,4),(36,16))
        self.add_polyline('brim',(8,16),(12,16),(36,16),(40,16))
        self.add_arc('jaw',(40,16),(8,16),radius_x=16)
        self.add_bezier('beard',(8,16),((12,24),(16,26),(24,24)),((32,26),(36,24),(40,16)))
        self.relate('connect','hat','brim')
        self.relate('connect','jaw','brim','beard')
        top=32+HEAD_BODY_CENTERLINE_GAP
        self.add_arc('body-left',(8,44),(16,top),radius_x=8)
        self.add_line('body-top',(16,top),(32,top))
        self.add_arc('body-right',(32,top),(40,44),radius_x=8)
        self.add_contour('body','body-left','body-top','body-right')
        self.relate('connect','jaw','body')
        for x in (8,40):
            self.add_line(f'body-backpack-{x}',(x,36),(x,44))
            self.relate('connect',f'body-backpack-{x}','body')
