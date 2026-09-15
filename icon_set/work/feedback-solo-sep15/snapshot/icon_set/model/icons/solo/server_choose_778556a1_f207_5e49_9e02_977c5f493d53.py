"""server-choose: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '778556a1-f207-5e49-9e02-977c5f493d53'
SOURCE_PATH = 'pictographic-primitives/servers/server choose_778556a1-f207-5e49-9e02-977c5f493d53.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ServerChoose(Solo48):
    icon_id = 'server-choose'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'servers'
    aliases = ()
    keywords = ('server', 'choose', 'servers')

    def build(self):
        # Plan: HRECT_L; shared level rails and mirrored tangent rounded ends.
        # Reference: Geometric repeated capsule construction.
        # Three connected courses share their dividers, avoiding doubled strokes.
        levels=(8,19,29,40)
        for i,y in enumerate(levels):self.add_line(f'rail-{i}',(10,y),(38,y))
        for side,mirror in [('left',False),('right',True)]:
            def p(x,y):return (48-x,y) if mirror else (x,y)
            for i,(t,b) in enumerate(zip(levels,levels[1:])):
                mid=(t+b)//2
                self.add_bezier(f'{side}-{i}',p(10,t),(p(6,t),p(4,t+2),p(4,mid)),(p(4,b-2),p(6,b),p(10,b)))
                self.relate('connect',f'{side}-{i}',f'rail-{i}')
                self.relate('connect',f'{side}-{i}',f'rail-{i+1}')
                if i:self.relate('connect',f'{side}-{i}',f'{side}-{i-1}')
