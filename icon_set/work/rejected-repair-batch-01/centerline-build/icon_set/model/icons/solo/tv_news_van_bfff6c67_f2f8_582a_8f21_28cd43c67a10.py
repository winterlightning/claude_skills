"""TV Broadcast Van with Satellite Dish — authored for the current SOLO48 contract."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfff6c67-f2f8-582a-8f21-28cd43c67a10'
SOURCE_PATH = 'pictographic-primitives/tv/modern tv channel van_bfff6c67-f2f8-582a-8f21-28cd43c67a10.svg'
AUTHOR = 'gpt-6'

class TvNewsVan(Solo48):
    icon_id = 'tv-news-van'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('van', 'tv', 'broadcast', 'news', 'satellite', 'dish', 'vehicle', 'media', 'outside-broadcast')

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

        # A right-facing body with matched wheels and an open rooftop dish.
        # Centerline extremes (6,6)-(42,42).
        self.add_polyline('body',(10,38),(6,38),(6,22),(26,22),(32,22),(42,32),(42,38),(38,38))
        self.add_line('sill',(18,38),(30,38))
        for x in (14,34):
            self.circle(f'wheel-{x}',x,38,4)
            self.relate('connect','body',f'wheel-{x}')
            self.relate('connect','sill',f'wheel-{x}')
        self.add_arc('dish',(14,6),(26,18),radius_x=12,sweep=False)
        self.add_line('feed',(26,18),(32,6))
        self.relate('connect','feed','dish')
        self.add_line('dish-mast',(26,18),(26,22))
        self.relate('connect','dish-mast','body')
        self.relate('connect','dish-mast','dish')
