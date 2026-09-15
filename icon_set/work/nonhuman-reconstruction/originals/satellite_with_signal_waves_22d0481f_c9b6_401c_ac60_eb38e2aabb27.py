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

        # Diagonal paired solar panels, circular bus, two broadcast ripples.
        # Centerline extremes (6,6)-(42,42).
        self.add_polyline('panel-a',(6,14),(14,6),(22,14),(18,18),(14,22),closed=True)
        self.add_polyline('panel-b',(26,34),(30,30),(34,26),(42,34),(34,42),closed=True)
        self.add_arc('bus-a',(22,19),(28,27),radius_x=5)
        self.add_arc('bus-b',(28,27),(22,19),radius_x=5)
        self.add_contour('bus','bus-a','bus-b',closed=True)
        self.add_line('strut-a',(18,18),(22,19))
        self.add_line('strut-b',(28,27),(30,30))
        self.relate('connect','panel-a','strut-a')
        self.relate('connect','bus','strut-a')
        self.relate('connect','bus','strut-b')
        self.relate('connect','panel-b','strut-b')
        
        self.add_arc('wave-outer',(6,28),(20,42),radius_x=14,sweep=False)
