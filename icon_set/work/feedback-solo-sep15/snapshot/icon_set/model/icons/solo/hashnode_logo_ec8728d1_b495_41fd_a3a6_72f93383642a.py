"""A rounded square tilted 45 degrees like a diamond holds a ring at its centre.

Plan: Rounded diamond has four identical radius-5 corners and a centred radius-5 ring.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: diamond: matched rounded corners.
Simplification: Rounded diamond and inner ring retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec8728d1-b495-41fd-a3a6-72f93383642a'
SOURCE_PATH = 'pictographic-primitives/logos/hashnode logo_ec8728d1-b495-41fd-a3a6-72f93383642a.svg'
AUTHOR = 'gpt-6'


class HashnodeLogo(Solo48):
    icon_id = 'hashnode-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('hashnode', 'blogging', 'developer', 'diamond', 'logo', 'brand', 'community')

    def build(self):
        points=[(20,8),(28,8),(40,20),(40,28),(28,40),(20,40),(8,28),(8,20)]
        for i,(a,b) in enumerate(zip(points,points[1:]+points[:1])):
            if i%2==0:self.add_arc(f'edge-{i}',a,b,radius_x=5)
            else:self.add_line(f'edge-{i}',a,b)
        self.add_contour('diamond',*(f'edge-{i}' for i in range(8)),closed=True)
        self.add_arc('ring-top',(19,24),(29,24),radius_x=5)
        self.add_arc('ring-bottom',(29,24),(19,24),radius_x=5)
        self.add_contour('ring','ring-top','ring-bottom',closed=True)
