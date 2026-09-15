"""chrome-logo: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0636dc6-50c0-4ddc-a838-20c77bcb4a61'
SOURCE_PATH = 'pictographic-primitives/logos/chrome logo_f0636dc6-50c0-4ddc-a838-20c77bcb4a61.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ChromeLogo(Solo48):
    icon_id = 'chrome-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('chrome', 'logo', 'logos')

    def build(self):
        # Plan: CIRCLE; three clean spinning blades meet explicit nodes on smooth concentric outlines, with continuous curve tangents.
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

        # The integer contact nodes are explicit; every arc has a continuous radial tangent.
        import math
        def ring(name,cx,cy,nodes):
         commands=[]
         for a,b in zip(nodes,nodes[1:]+nodes[:1]):
          aa=math.atan2(a[1]-cy,a[0]-cx);bb=math.atan2(b[1]-cy,b[0]-cx)
          angle=(bb-aa)%(2*math.pi);ra=math.dist(a,(cx,cy));rb=math.dist(b,(cx,cy))
          f=4/3*math.tan(angle/4)*(.99 if name=='outer' else 1)
          commands.append(('C',(a[0]-math.sin(aa)*ra*f,a[1]+math.cos(aa)*ra*f),(b[0]+math.sin(bb)*rb*f,b[1]-math.cos(bb)*rb*f),b))
         path(name,nodes[0],commands,True)
        ring('outer',24,24,[(24,4),(42,16),(44,24),(24,44),(4,24),(8,12)])
        ring('inner',24,24,[(24,16),(32,24),(31,28),(24,32),(17,28),(16,24)])
        for name,a,b in [('right',(24,16),(42,16)),('lower',(31,28),(24,44)),('left',(17,28),(8,12))]:
         self.add_line(name,a,b);self.relate('connect',name,'outer');self.relate('connect',name,'inner')
