"""Front-view beetle with antennae and three mirrored leg pairs. Lucide bug informs rounded body and paired attachments; elytra seam omitted.

SOLO48 SQUARE; geometry authored from its exact centerline extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64'
SOURCE_PATH = 'pictographic-primitives/symbol/piece_9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64.svg'
AUTHOR = 'gpt-6'


class BugBeetle(Solo48):
    icon_id = 'bug-beetle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('bug', 'beetle', 'insect', 'debug', 'error', 'software', 'pest', 'virus', 'sub icon')

    def build(self) -> None:

        self.add_line('head-top', (18,10), (30,10))
        self.add_arc('head-right', (30,10), (36,16), radius_x=6)
        self.add_line('side-r1', (36,16), (36,18))
        self.add_line('side-r2', (36,18), (36,26))
        self.add_line('side-r3', (36,26), (36,34))
        self.add_arc('abdomen', (36,34), (12,34), radius_x=12, radius_y=8)
        self.add_line('side-l3', (12,34), (12,26))
        self.add_line('side-l2', (12,26), (12,18))
        self.add_line('side-l1', (12,18), (12,16))
        self.add_arc('head-left', (12,16), (18,10), radius_x=6)
        self.add_contour('body','head-top','head-right','side-r1','side-r2','side-r3','abdomen','side-l3','side-l2','side-l1','head-left',closed=True)
        self.add_line('head-divider',(12,18),(36,18))
        self.relate('connect','head-divider','body')
        for side, sign in [('left',-1),('right',1)]:
            def p(x,y): return (24+sign*x,y)
            self.add_line('antenna-'+side,p(6,10),p(10,6))
            self.relate('connect','antenna-'+side,'body')
            self.add_polyline('leg-top-'+side,p(12,18),p(16,18),p(18,12))
            self.add_line('leg-mid-'+side,p(12,26),p(18,26))
            self.add_polyline('leg-low-'+side,p(12,34),p(16,36),p(18,40))
            for level in ('top','mid','low'):
                self.relate('connect','leg-'+level+'-'+side,'body')
            self.relate('connect','leg-top-'+side,'head-divider')


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('9a3ccf45-79d9-442e-9bbb-bf6598cc98bf', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/bug_9a3ccf45-79d9-442e-9bbb-bf6598cc98bf.svg')]
