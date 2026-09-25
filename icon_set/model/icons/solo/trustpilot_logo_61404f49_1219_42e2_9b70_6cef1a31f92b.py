"""trustpilot-logo: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61404f49-1219-42e2-9b70-6cef1a31f92b'
SOURCE_PATH = 'pictographic-primitives/logos/trustpilot logo_61404f49-1219-42e2-9b70-6cef1a31f92b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class TrustpilotLogo(Solo48):
    icon_id = 'trustpilot-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('trustpilot', 'logo', 'logos')

    def build(self):
        # Plan: SQUARE; mirrored star arms and valleys, straight uninterrupted edges.
        # Reference: Lucide star: common axis and deliberate corners.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        # One axis owns matching arms, not independently nudged vertices.
        axis=24
        right=[(axis,6),(axis+5,18),(42,20),(32,29),(35,42),(axis,35)]
        points=right+[(48-x,y) for x,y in reversed(right[1:-1])]
        self.add_polyline('star',*points,closed=True)
