"""monitor globe. Expanded screen with short pedestal, maximizing circular globe diameter.
Symbol plan: enclosure and content use shared parameters and genuine attachment nodes.
Construction: Lucide smartphone/monitor/megaphone geometric enclosures and joins;
human_ref/user.svg supplies circular heads and open shoulder proportions where applicable.
Omissions: Second latitude and horizontal monitor foot omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '47d2e77c-7d13-4e49-a9d3-b0ee7dd5fe74'
SOURCE_PATH = 'pictographic-primitives/other/monitor globe_47d2e77c-7d13-4e49-a9d3-b0ee7dd5fe74.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'monitor-globe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('monitor globe',)
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def circle(self,n,x,y,r):
        pts=[(x-r,y),(x,y-r),(x+r,y),(x,y+r),(x-r,y)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            self.add_arc(n+str(i),a,b,radius_x=r)
        self.add_contour(n,*(n+str(i) for i in range(4)),closed=True)

    def box(self,n,l,t,r,b,rad=3,breaks=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]
            if i%2:
                p=f'{n}-{i}';self.add_arc(p,a,z,radius_x=rad);members.append(p)
            else:
                nodes=[a]+(breaks or {}).get(i,[])+[z]
                for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                    if u==v:continue
                    p=f'{n}-{i}-{j}';self.add_line(p,u,v);members.append(p)
        self.add_contour(n,*members,closed=True)

    def monitor(self,l=6,t=6,r=42,b=34,foot=42):
        self.box('screen',l,t,r,b,3,{4:[(24,b)]})
        self.add_line('stand',(24,b),(24,foot))
        self.add_polyline('foot',(16,foot),(24,foot),(32,foot))
        self.relate('connect','screen','stand')
        self.relate('connect','stand','foot')

    def bust(self,n,x,y,r,w,h):
        # human_ref/user.svg: circular head, smooth open shoulders, exact 4 ink gap.
        self.circle(n+'-head',x,y,r)
        top=y+r+8
        self.add_arc(n+'-shoulder-l',(x-w,top+h),(x,top),radius_x=w,radius_y=h)
        self.add_arc(n+'-shoulder-r',(x,top),(x+w,top+h),radius_x=w,radius_y=h)
        self.add_contour(n+'-shoulders',n+'-shoulder-l',n+'-shoulder-r')

    def build(self):
        self.box('screen',6,6,42,40,3,{4:[(24,40)]})
        self.add_line('stand',(24,40),(24,42))
        self.relate('connect','screen','stand')
        self.circle('globe',24,23,8)
        self.add_polyline('meridian',(24,15),(24,23),(24,31))
        self.add_polyline('equator',(16,23),(24,23),(32,23))
        self.relate('connect','globe','meridian');self.relate('connect','globe','equator');self.relate('connect','meridian','equator')
