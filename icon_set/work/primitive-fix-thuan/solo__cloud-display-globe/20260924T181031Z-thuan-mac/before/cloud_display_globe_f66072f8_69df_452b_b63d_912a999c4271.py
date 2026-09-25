'Cloud globe: a true circular globe around one smooth, balanced cloud; the cramped base is omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f66072f8-69df-452b-b63d-912a999c4271'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/sphere_f66072f8-69df-452b-b63d-912a999c4271.svg'
AUTHOR = 'gpt-6'


class CloudDisplayGlobe(Solo48):
    icon_id = 'cloud-display-globe'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('globe', 'cloud', 'sphere', 'pedestal', 'display', 'ornament', 'decor')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('globe-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('globe-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('cloud-left', (18, 29), (18, 19), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('cloud-crown', (18, 19), (30, 19), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('cloud-right', (30, 19), (30, 29), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('cloud-bottom', (30, 29), (18, 29))
        self.add_contour('globe', *('globe-top', 'globe-bottom'), closed=True)
        self.add_contour('cloud', *('cloud-left', 'cloud-crown', 'cloud-right', 'cloud-bottom'), closed=True)
