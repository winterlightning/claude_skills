"""Person crouching under a table during an earthquake.
HRECT_L (4,8)-(44,40). Table owns the two legs. Mirrored vibration marks.
Human reference full_body_ref.png supplies the kneeling pose. Head r2 at
(32,28), neck (22,28): exact 8 centerline gap on horizontal torso axis.
Draft omits arms for room; do not release if native pose is ambiguous.

Review: valid with zero warnings; visual identity unresolved. Do not export.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8d2595e2-135f-48bd-8886-08c5da475869'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/earthquake hiding proof table_8d2595e2-135f-48bd-8886-08c5da475869.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'person-sheltering-beneath-shaking-table'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ('Earthquake Shelter Under Table',)
    keywords = ('earthquake','shelter','person','table','crouching','safety','shaking')
    def build(self):
        self.add_polyline('table',(4,40),(4,18),(44,18),(44,40))
        for side in (-1,1):
            self.add_polyline(f'vibration-{side}',*[(24+side*x,y) for x,y in [(8,8),(12,10),(16,8)]])
        self.add_arc('head-top',(30,28),(34,28),radius_x=2)
        self.add_arc('head-bottom',(34,28),(30,28),radius_x=2)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('torso',(22,28),(14,28))
        self.add_polyline('legs',(14,28),(14,32),(24,40),(14,40))
        self.relate('connect','torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
