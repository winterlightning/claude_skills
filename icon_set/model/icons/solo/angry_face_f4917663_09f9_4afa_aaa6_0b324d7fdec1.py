"""angry-face-symbol: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4917663-09f9-4afa-aaa6-0b324d7fdec1'
SOURCE_PATH = 'pictographic-primitives/symbol/angry face_f4917663-09f9-4afa-aaa6-0b324d7fdec1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class AngryFaceSymbol(Solo48):
    icon_id = 'angry-face-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('angry', 'face', 'symbol')

    def build(self):
        # Plan: SQUARE; each eye is drawn once; mirrored brows and a smooth continuous frown replace retraced eyes and kinked mouth joins.
        # Reference: Shared human_ref/user.svg: simple clean facial vocabulary; this icon has no head/body pair.
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

        # Detached expression only: no head/body proportions to alter.
        self.add_line('brow-left',(6,6),(18,13));self.add_line('brow-right',(42,6),(30,13))
        self.add_line('eye-left',(9,18),(12,20));self.add_line('eye-right',(39,18),(36,20))
        path('frown',(8,42),[('C',(11,33),(12,26),(24,26)),('C',(36,26),(37,33),(40,42))])
