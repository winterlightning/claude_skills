"""soccer: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fe0e6dd-1153-4514-a8b0-e771b8b8525c'
SOURCE_PATH = 'pictographic-primitives/symbol/soccer_1fe0e6dd-1153-4514-a8b0-e771b8b8525c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Soccer(Solo48):
    icon_id = 'soccer'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('soccer', 'symbol')

    def build(self):
        # Plan: CIRCLE; reflected pentagonal panel and five seams ending on real circle nodes, without uneven edge intrusions.
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

        flip=False
        def pt(p):return (p[0],48-p[1]) if flip else p
        vertices=[(19,18),(29,18),(32,28),(24,34),(16,28)]
        outer=[(12,8),(36,8),(40,36),(24,44),(8,36)]
        circle_nodes('ball',24,24,20,[pt(p) for p in outer])
        self.add_polyline('panel',*[pt(p) for p in vertices],closed=True)
        for i,(a,b) in enumerate(zip(vertices,outer)):
         self.add_line(f'seam-{i}',pt(a),pt(b));self.relate('connect',f'seam-{i}','panel');self.relate('connect',f'seam-{i}','ball')
