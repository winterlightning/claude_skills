"""science-molecule-strucutre: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95731d8c-899f-5d6a-bb52-8d0343506c53'
SOURCE_PATH = 'pictographic-primitives/science/science molecule strucutre_95731d8c-899f-5d6a-bb52-8d0343506c53.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ScienceMoleculeStrucutre(Solo48):
    icon_id = 'science-molecule-strucutre'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('science', 'molecule', 'strucutre')

    def build(self):
        # Plan: SQUARE; equal circular terminals, reflected bonds, and exact 3:4 boundary contacts.
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

        def circle_nodes(name,cx,cy,r,nodes=()):
            import math
            pts=set(nodes)|{(cx-r,cy),(cx+r,cy),(cx,cy-r),(cx,cy+r)}
            assert all((x-cx)**2+(y-cy)**2==r*r for x,y in pts)
            pts=sorted(pts,key=lambda p:math.atan2(p[1]-cy,p[0]-cx))
            path(name,pts[0],[('A',pt,r,r,True) for pt in pts[1:]+pts[:1]],True)

        oval('top',24,11,5)
        circle_nodes('left',11,37,5,[(15,34)]);circle_nodes('right',37,37,5,[(33,34)])
        self.add_line('stem',(24,16),(24,27));self.add_polyline('bonds',(15,34),(24,27),(33,34))
        self.relate('connect','stem','top');self.relate('connect','stem','bonds')
        self.relate('connect','bonds','left');self.relate('connect','bonds','right')
