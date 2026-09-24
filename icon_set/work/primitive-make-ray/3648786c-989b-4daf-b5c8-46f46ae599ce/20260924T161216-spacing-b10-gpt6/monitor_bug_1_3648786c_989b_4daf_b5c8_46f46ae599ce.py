"""monitor bug 1. Four mirrored diagonal legs with shared body endpoints.
Symbol plan: enclosure and content use shared parameters and genuine attachment nodes.
Construction: Lucide smartphone/monitor/megaphone geometric enclosures and joins;
human_ref/user.svg supplies circular heads and open shoulder proportions where applicable.
Omissions: Transverse body divider omitted to preserve the body opening.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3648786c-989b-4daf-b5c8-46f46ae599ce'
SOURCE_PATH = 'pictographic-primitives/other/monitor bug 1_3648786c-989b-4daf-b5c8-46f46ae599ce.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'monitor-bug-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('monitor bug 1',)
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
        self.monitor(8,4,40,36,44)
        # Bug has a broad oval body, four diagonal legs with genuine corner nodes.
        pts=[(20,16),(28,16),(28,24),(20,24),(20,16)]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            self.add_arc('body-'+str(j),a,b,radius_x=6)
        self.add_contour('bug',*(f'body-{j}' for j in range(4)),closed=True)
        for j,(a,b) in enumerate([((20,16),(17,13)),((28,16),(31,13)),((28,24),(31,27)),((20,24),(17,27))]):
            self.add_line('leg-'+str(j),a,b)
            self.relate('connect','bug','leg-'+str(j))
