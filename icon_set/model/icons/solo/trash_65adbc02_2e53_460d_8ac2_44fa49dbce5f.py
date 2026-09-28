"""trash-symbol: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65adbc02-2e53-460d-8ac2-44fa49dbce5f'
SOURCE_PATH = 'pictographic-primitives/symbol/trash_65adbc02-2e53-460d-8ac2-44fa49dbce5f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class TrashSymbol(Solo48):
    icon_id = 'trash-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('trash', 'symbol')

    def build(self):
        # Plan: VRECT_L; equal bucket slopes and a tangent rounded handle attached exactly to a straight lid.
        # Reference: Lucide trash-2: shared lid/handle nodes and matched corner radii.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L':self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C':self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A':self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry=None):
            ry=rx if ry is None else ry
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)

        # One mirrored bucket, one lid, one radius-four handle.
        self.add_polyline('bucket',(12,14),(16,44),(32,44),(36,14))
        self.add_polyline('lid',(8,14),(12,14),(18,14),(30,14),(36,14),(40,14))
        path('handle',(18,14),[('L',(18,8)),('A',(22,4),4,4,True),('L',(26,4)),('A',(30,8),4,4,True),('L',(30,14))])
        self.relate('connect','bucket','lid');self.relate('connect','handle','lid')
