"""Presentation microphone (office), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'dc33bff7-8291-5e3a-956d-f632ad5d2bee'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__presentation-microphone/20260927T153803Z-thuan-mac-1/reference/presentation microphone_dc33bff7-8291-5e3a-956d-f632ad5d2bee.svg'
AUTHOR = 'gpt-6'

class PresentationMicrophone(Solo48):
    icon_id = 'presentation-microphone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    categories = ('office', 'primitives')
    aliases = ()
    keywords = ('presentation', 'microphone', 'office')

    def build(self) -> None:
        # Narrow capsule leaves room for the pickup cradle and full stand.
        self.add_arc('top',(18,10),(30,10),radius_x=6,sweep=True)
        self.add_line('right',(30,10),(30,18))
        self.add_arc('bottom',(30,18),(18,18),radius_x=6,sweep=True)
        self.add_line('left',(18,18),(18,10))
        self.add_contour('capsule','top','right','bottom','left',closed=True)
        self.add_bezier('cradle-left',(8,20),((8,28),(15,34),(24,34)))
        self.add_bezier('cradle-right',(24,34),((33,34),(40,28),(40,20)))
        self.add_contour('cradle','cradle-left','cradle-right')
        self.add_line('stand',(24,34),(24,44))
        self.add_line('foot',(17,44),(31,44))
        self.relate('connect','cradle','stand')
        self.relate('connect','stand','foot')
