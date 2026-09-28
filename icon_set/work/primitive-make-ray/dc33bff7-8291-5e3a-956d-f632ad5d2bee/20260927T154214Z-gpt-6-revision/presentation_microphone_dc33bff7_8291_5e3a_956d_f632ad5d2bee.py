"""Presentation microphone (office), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'dc33bff7-8291-5e3a-956d-f632ad5d2bee'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__presentation-microphone/20260927T153803Z-thuan-mac-1/reference/presentation microphone_dc33bff7-8291-5e3a-956d-f632ad5d2bee.svg'
AUTHOR = "gpt-6"

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
        # Upright mic capsule, surrounding pickup cradle, and a readable stand.
        self.add_line('body-left',(14,12),(14,20))
        self.add_arc('body-bottom-left',(14,20),(24,30),radius_x=10,sweep=False)
        self.add_arc('body-bottom-right',(24,30),(34,20),radius_x=10,sweep=False)
        self.add_line('body-right',(34,20),(34,12))
        self.add_arc('body-top-right',(34,12),(24,4),radius_x=10,sweep=False)
        self.add_arc('body-top-left',(24,4),(14,12),radius_x=10,sweep=False)
        self.add_contour('capsule','body-left','body-bottom-left','body-bottom-right','body-right','body-top-right','body-top-left',closed=True)
        self.add_arc('cradle-left',(8,27),(24,38),radius_x=18,sweep=False)
        self.add_arc('cradle-right',(24,38),(40,27),radius_x=18,sweep=False)
        self.add_contour('cradle','cradle-left','cradle-right')
        self.add_line('stand',(24,38),(24,44))
        self.add_line('foot',(17,44),(31,44))
        self.relate('connect','cradle','stand')
        self.relate('connect','stand','foot')
