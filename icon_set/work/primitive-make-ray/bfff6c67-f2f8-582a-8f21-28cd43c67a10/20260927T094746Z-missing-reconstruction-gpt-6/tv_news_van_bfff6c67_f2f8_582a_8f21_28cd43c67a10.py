"""TV Broadcast Van with Satellite Dish — authored for the current SOLO48 contract."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bfff6c67-f2f8-582a-8f21-28cd43c67a10'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tv-news-van/20260927T094425Z-thuan-mac-1/reference/modern tv channel van_bfff6c67-f2f8-582a-8f21-28cd43c67a10.svg'
AUTHOR = "gpt-6"
REVISION_COMPARISON = 'The rejected dish looked like a curved antenna, and wheel rings crowded the body.'
REVISION_CHANGE = 'Shaped a dish with a clear angled rim and integrated rounded wheel lobes into the van outline.'


class TvNewsVan(Solo48):
    icon_id = 'tv-news-van'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tv"
    categories = ("tv", "primitives")
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
        points=((6,38),(6,22),(26,22),(32,22),(42,32),(42,38),(38,38))
        for j,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'body-upper-{j}',a,b)
        self.add_arc('wheel-right',(38,38),(30,38),radius_x=4,radius_y=4,sweep=True)
        self.add_line('chassis',(30,38),(18,38))
        self.add_arc('wheel-left',(18,38),(10,38),radius_x=4,radius_y=4,sweep=True)
        self.add_line('body-close',(10,38),(6,38))
        self.add_contour('body','body-upper-1','body-upper-2','body-upper-3','body-upper-4','body-upper-5','body-upper-6','wheel-right','chassis','wheel-left','body-close',closed=True)
        self.add_polyline('dish',(14,6),(12,10),(18,14),(26,14))
        self.add_line('feed',(26,14),(32,6))
        self.relate('connect','feed','dish')
        self.add_line('dish-mast',(26,14),(26,22))
        self.relate('connect','dish-mast','body')
        self.relate('connect','dish-mast','dish')
