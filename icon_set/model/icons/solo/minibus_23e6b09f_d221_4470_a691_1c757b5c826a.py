"""minibus-symbol: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23e6b09f-d221-4470-a691-1c757b5c826a'
SOURCE_PATH = 'pictographic-primitives/symbol/minibus_23e6b09f-d221-4470-a691-1c757b5c826a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class MinibusSymbol(Solo48):
    icon_id = 'minibus-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('minibus', 'symbol')

    def build(self):
        # Plan: HRECT_L; equal circular wheels, exact chassis contacts, clean body corners and a shared straight window rail.
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

        for name,cx in [('front',13),('back',35)]:oval(name,cx,35,5)
        path('body',(8,35),[('L',(7,35)),('A',(4,32),3,3,True),('L',(4,20)),('L',(10,8)),
         ('L',(40,8)),('A',(44,12),4,4,True),('L',(44,20)),('L',(44,32)),('A',(41,35),3,3,True),('L',(40,35))])
        self.add_line('window',(4,20),(44,20));self.relate('connect','window','body')
        self.add_line('chassis',(18,35),(30,35))
        for name in ['front','back']:self.relate('connect','chassis',name);self.relate('connect','body',name)
