'A person stands in side view with a round head and a prominent rounded belly projecting left. One arm bends back toward the hip above a short flared garment and visible leg.\n\nConstruction: Side profile with a curved pregnant abdomen, circular head and an arm resting on the lower back. Bounds (8,4)-(40,44).\nLucide: person-standing: separate circular head and connected limbs.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2230e8dc-ec40-46aa-97fe-c7a3278e68e9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-pregnant-person/20260927T093533Z-thuan-mac-1/reference/disability pregant_2230e8dc-ec40-46aa-97fe-c7a3278e68e9.svg'
AUTHOR = "gpt-6"

class StandingPregnantPerson(Solo48):
    icon_id = 'standing-pregnant-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('pregnant', 'pregnancy', 'person', 'standing', 'maternity', 'belly')

    def build(self):
        """Round abdomen, dress hem, single leg and bent arm follow the source."""
        self.add_arc('head-upper',(20,8),(28,8),radius_x=4)
        self.add_arc('head-lower',(28,8),(20,8),radius_x=4)
        self.add_contour('head','head-upper','head-lower',closed=True)

        self.add_bezier('abdomen',(22,20),((13,21),(8,27),(8,34)))
        self.add_line('hem-left',(8,34),(18,34))
        self.add_line('hem-right',(18,34),(24,34))
        self.add_line('back',(24,34),(22,20))
        self.add_contour('dress','abdomen','hem-left','hem-right','back',closed=True)

        self.add_line('leg',(18,34),(18,44))
        self.relate('connect','dress','leg')
        self.add_polyline('arm',(22,20),(40,24),(34,32))
        self.relate('connect','dress','arm')
