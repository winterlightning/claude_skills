'Binder clip: balanced body and symmetric wire handle, preserving curved wire corners and exact attachment points.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61ccd621-bbc0-4581-842b-098e1372d4ff'
SOURCE_PATH = 'icons-json/office/clip_61ccd621-bbc0-4581-842b-098e1372d4ff.json'
AUTHOR = 'gpt-6'

class Clip(Solo48):
    icon_id = 'clip'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('clip', 'office')

    def build(self) -> None:
        # Binder clip: rounded body and a continuous wire handle; all contacts share nodes.
        self.add_line('top-a',(8,20),(20,20))
        self.add_line('top-b',(20,20),(28,20))
        self.add_line('top-c',(28,20),(40,20))
        self.add_arc('tr',(40,20),(44,24),radius_x=4)
        self.add_line('right',(44,24),(44,36))
        self.add_arc('br',(44,36),(40,40),radius_x=4)
        self.add_line('bottom-a',(40,40),(32,40))
        self.add_line('bottom-b',(32,40),(16,40))
        self.add_line('bottom-c',(16,40),(8,40))
        self.add_arc('bl',(8,40),(4,36),radius_x=4)
        self.add_line('left',(4,36),(4,24))
        self.add_arc('tl',(4,24),(8,20),radius_x=4)
        self.add_contour('body','top-a','top-b','top-c','tr','right','br','bottom-a','bottom-b','bottom-c','bl','left','tl',closed=True)
        self.add_line('handle-left',(16,40),(20,20))
        self.add_bezier('handle-top-left',(20,20),((20,17),(16,16),(16,12)))
        self.add_arc('handle-corner-left',(16,12),(20,8),radius_x=4)
        self.add_line('handle-top',(20,8),(28,8))
        self.add_arc('handle-corner-right',(28,8),(32,12),radius_x=4)
        self.add_bezier('handle-top-right',(32,12),((32,16),(28,17),(28,20)))
        self.add_line('handle-right',(28,20),(32,40))
        self.add_contour('handle','handle-left','handle-top-left','handle-corner-left','handle-top','handle-corner-right','handle-top-right','handle-right')
        self.relate('connect','handle','body')
