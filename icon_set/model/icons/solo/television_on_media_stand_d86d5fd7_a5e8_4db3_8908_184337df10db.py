"""Television on a Media Stand — authored for the current SOLO48 contract."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd86d5fd7-a5e8-4db3-8908-184337df10db'
SOURCE_PATH = 'pictographic-primitives/tv/movies home_d86d5fd7-a5e8-4db3-8908-184337df10db.svg'
AUTHOR = 'gpt-6'

class TelevisionOnMediaStand(Solo48):
    icon_id = 'television-on-media-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tv"
    categories = ("tv", "primitives")
    aliases = ()
    keywords = ('television', 'tv', 'stand', 'cabinet', 'home', 'movies', 'entertainment', 'living-room', 'furniture')

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

        # Centerline extremes (6,6)-(42,42); axis x=24.
        self.box('screen',6,6,42,22,attachments=((24,22),))
        self.add_line('stand',(24,22),(24,30))
        self.box('cabinet',6,30,42,38,r=2,attachments=((24,30),(10,38),(38,38)))
        for x in (10,38):
            self.add_line(f'leg-{x}',(x,38),(x,42))
            self.relate('connect','cabinet',f'leg-{x}')
        self.relate('connect','screen','stand')
        self.relate('connect','stand','cabinet')
