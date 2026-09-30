"""Make a tall rounded pin above a deeper folded map.
Symbol plan: VRECT_L on SOLO48; named shapes and source arrangement.
Before review: The broad flattened pin looks like an eye; map is a short strip.
Construction reference: Lucide map-pin: taller crown and tapered tip; source folded-map rhythm.
Omissions: Pin hole becomes a dot to retain the pointed silhouette.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='7c2df1dc-523f-47e8-98ed-1291ecbe59b3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__folded-map-with-location-pin/20260929T132621Z-thuan-mac/reference/map location_7c2df1dc-523f-47e8-98ed-1291ecbe59b3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='folded-map-with-location-pin'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('map', 'location')
    def build(self):

        def path(n,start,steps,closed=False):
            p=start; members=[]
            for i,step in enumerate(steps):
                k,end,*a=step; name=f'{n}-{i}'
                if k=='L': self.add_line(name,p,end)
                elif k=='A': self.add_arc(name,p,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif k=='B': self.add_bezier(name,p,(a[0],a[1],end))
                members.append(name);p=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=4):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('pin',(24,27),[('L',(16,17)),('A',(32,17),8,13,True),('L',(24,27))],True)
        self.add_dot('pin-hole',(24,14))
        poly('map',(8,34),(19,31),(29,34),(40,31),(40,41),(29,44),(19,41),(8,44),closed=True)
        line('fold-left',(19,31),(19,41));line('fold-right',(29,34),(29,44));join('fold-left','map');join('fold-right','map')
