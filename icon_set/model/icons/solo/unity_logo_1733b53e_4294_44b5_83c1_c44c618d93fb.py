"""unity-logo: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1733b53e-4294-44b5-83c1-c44c618d93fb'
SOURCE_PATH = 'pictographic-primitives/logos/unity logo_1733b53e-4294-44b5-83c1-c44c618d93fb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class UnityLogo(Solo48):
    icon_id = 'unity-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('unity', 'logo', 'logos')

    def build(self):
        # Plan: HRECT_L; symmetric upper/lower facets, straight sides and shared central spoke node; kinked two-piece side removed.
        # Reference: No close Lucide match; reconstruct the supplied subject from its owning geometry.
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

        # Both right corners derive from reflection about y=24.
        self.add_polyline('left-tip',(16,16),(4,24),(16,32))
        self.add_polyline('top-tip',(26,12),(40,8),(44,20))
        self.add_polyline('bottom-tip',(26,36),(40,40),(44,28))
        self.add_polyline('spokes',(40,8),(29,24),(40,40))
        self.add_line('left-spoke',(4,24),(29,24))
        for tip in ['top-tip','bottom-tip']:self.relate('connect',tip,'spokes')
        self.relate('connect','left-spoke','spokes');self.relate('connect','left-spoke','left-tip')
