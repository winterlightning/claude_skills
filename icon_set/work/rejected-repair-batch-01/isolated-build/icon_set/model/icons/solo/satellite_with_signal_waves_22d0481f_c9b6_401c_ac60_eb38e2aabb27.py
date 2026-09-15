"""Satellite with Signal Waves — authored for the current SOLO48 contract."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22d0481f-c9b6-401c-ac60-eb38e2aabb27'
SOURCE_PATH = 'pictographic-primitives/tv/satellite signal_22d0481f-c9b6-401c-ac60-eb38e2aabb27.svg'
AUTHOR = 'gpt-6'

class SatelliteWithSignalWaves(Solo48):
    icon_id = 'satellite-with-signal-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('satellite', 'signal', 'broadcast', 'orbit', 'space', 'transmission', 'wireless', 'communication')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def box(self, name, x, y, right, bottom, r=3, attachments=()):
        points=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; k=f'{name}-{i}'; members.append(k)
            if i%2: self.add_arc(k,a,b,radius_x=r)
            else:
                nodes=[p for p in attachments if (a[0]==b[0]==p[0] and min(a[1],b[1])<p[1]<max(a[1],b[1])) or (a[1]==b[1]==p[1] and min(a[0],b[0])<p[0]<max(a[0],b[0]))]
                if nodes:
                    members.pop()
                    nodes.sort(key=lambda p:(p[0]-a[0])**2+(p[1]-a[1])**2)
                    chain=[a]+nodes+[b]
                    for j,(u,v) in enumerate(zip(chain,chain[1:])):
                        part=f'{k}-{j}'; members.append(part); self.add_line(part,u,v)
                else: self.add_line(k,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Plan: Mirrored solar panels connect at their nearest corners to a small circular bus; longer rods replace cramped face attachments. Preserve the broadcast arc.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        poly('panel-a',(6,12),(12,6),(18,12),(12,18),closed=True)
        poly('panel-b',(30,36),(36,30),(42,36),(36,42),closed=True)
        path('bus',(24,21), [('A',(24,27),3,3,True),('A',(24,21),3,3,True)],True)
        line('strut-a',(18,12),(24,21));line('strut-b',(24,27),(30,36))
        join('strut-a','panel-a');join('strut-a','bus');join('strut-b','bus');join('strut-b','panel-b')
        path('wave',(6,28), [('A',(20,42),14,14,False)])
