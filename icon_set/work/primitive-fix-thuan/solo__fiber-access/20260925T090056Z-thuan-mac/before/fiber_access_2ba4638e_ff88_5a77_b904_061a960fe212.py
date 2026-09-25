"""fiber-access: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ba4638e-ff88-5a77-b904-061a960fe212'
SOURCE_PATH = 'pictographic-primitives/networks/fiber access_2ba4638e-ff88-5a77-b904-061a960fe212.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class FiberAccess(Solo48):
    icon_id = 'fiber-access'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    categories = ('primitives', 'networks')
    aliases = ()
    keywords = ('fiber', 'access', 'networks')

    def build(self):
        # Plan: HRECT_L; identical circle nodes, reflected smooth inputs, and equal arrowheads; tangled fitted loops removed.
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

        def rounded(name,x1,y1,x2,y2,r):
            path(name,(x1+r,y1),[('L',(x2-r,y1)),('A',(x2,y1+r),r,r,True),('L',(x2,y2-r)),('A',(x2-r,y2),r,r,True),('L',(x1+r,y2)),('A',(x1,y2-r),r,r,True),('L',(x1,y1+r)),('A',(x1+r,y1),r,r,True)],True)

        for name,cy,top in [('upper',14,8),('lower',34,40)]:
         circle_nodes(name,22,cy,5,[(19,cy-4 if top<cy else cy+4)])
         # Each source line bends smoothly to an exact circle boundary.
         if top<cy:path(name+'-input',(4,8),[('L',(15,8)),('C',(17,8),(18,9),(19,10))])
         else:path(name+'-input',(4,40),[('L',(15,40)),('C',(17,40),(18,39),(19,38))])
         self.add_line(name+'-out',(27,cy),(44,cy));self.add_polyline(name+'-arrow',(40,cy-4),(44,cy),(40,cy+4))
         self.relate('connect',name+'-input',name);self.relate('connect',name+'-out',name);self.relate('connect',name+'-out',name+'-arrow')
