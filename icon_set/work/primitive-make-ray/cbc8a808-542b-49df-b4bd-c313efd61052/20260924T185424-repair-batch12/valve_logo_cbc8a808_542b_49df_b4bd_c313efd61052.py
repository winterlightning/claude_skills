"""The five-letter VALVE wordmark.
Symbol plan and construction: No useful local Lucide wordmark match; the supplied wordmark owns the lettering.
Keyshape: HRECT_L is the widest available envelope; several distributions were attempted.
Omissions: No letters removed. Rounded A and condensed V strokes were attempted.
Review: BLOCKED: the final V is 5.66175 centreline units from L and 3 from E, below 8. Condensed V strokes also lose their letter identity. Six candidates saved; no visual approval."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cbc8a808-542b-49df-b4bd-c313efd61052'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/valve logo_cbc8a808-542b-49df-b4bd-c313efd61052.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='valve-logo'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('valve', 'logo')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        # Five letters remain in source order; A bar uses exact shared nodes.
        top,bottom=8,40
        self.add_polyline('v-first',(4,top),(5,bottom),(6,top))
        self.add_polyline('a-left',(14,bottom),(14,24),(14,14))
        self.add_arc('a-cap',(14,14),(22,14),radius_x=4)
        self.add_polyline('a-right',(22,14),(22,24),(22,bottom))
        self.relate('connect','a-left','a-cap');self.relate('connect','a-right','a-cap')
        self.add_line('a-bar',(14,24),(22,24));self.relate('connect','a-left','a-bar');self.relate('connect','a-right','a-bar')
        self.add_polyline('l',(30,top),(30,bottom-8),(32,bottom-8))
        self.add_polyline('v-second',(37,top+8),(38,bottom),(39,top+8))
        self.add_polyline('e',(44,top),(42,top),(42,24),(42,bottom),(44,bottom))
        self.add_line('e-middle',(42,24),(44,24));self.relate('connect','e','e-middle')
