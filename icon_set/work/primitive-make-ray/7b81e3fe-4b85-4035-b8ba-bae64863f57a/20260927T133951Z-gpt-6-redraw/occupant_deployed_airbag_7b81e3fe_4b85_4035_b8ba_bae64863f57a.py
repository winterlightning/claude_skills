"""Occupant with Deployed Airbag, re-authored from its reference on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7b81e3fe-4b85-4035-b8ba-bae64863f57a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__occupant-deployed-airbag/20260927T133723Z-thuan-mac-1/reference/front airbag_7b81e3fe-4b85-4035-b8ba-bae64863f57a.svg'
AUTHOR = "gpt-6"

class OccupantDeployedAirbag(Solo48):
    icon_id = 'occupant-deployed-airbag'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('airbag', 'front airbag', 'safety', 'occupant', 'car', 'dashboard', 'passenger', 'srs')

    def build(self) -> None:
        # The source's large left circle is the occupant head; the smaller
        # forward circle is the deployed bag. A bent seated figure reaches it.
        self.add_arc('head-upper',(6,16),(22,16),radius_x=8)
        self.add_arc('head-lower',(22,16),(6,16),radius_x=8)
        self.add_contour('head','head-upper','head-lower',closed=True)
        self.add_arc('airbag-upper',(33,11),(39,11),radius_x=3)
        self.add_arc('airbag-lower',(39,11),(33,11),radius_x=3)
        self.add_contour('airbag','airbag-upper','airbag-lower',closed=True)
        self.add_polyline('seat',(4,40),(8,32),(14,32))
        self.add_bezier('torso',(14,32),((14,34),(22,34),(28,33)))
        self.add_line('reach',(28,33),(44,24))
        self.add_line('leg',(14,32),(22,40))
        self.relate('connect','seat','torso')
        self.relate('connect','torso','reach')
        self.relate('connect','torso','leg')
        self.mark_human_figure('occupant',head='head',torso='torso',torso_junction='start')
