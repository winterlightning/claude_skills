"""Restore the full egg silhouette with a central ribbon and bow knot.
Symbol plan: VRECT_L on SOLO48; named shapes and source arrangement.
Before review: The bow replaces the top of the egg and the ribbon band and tails are absent.
Construction reference: Lucide square: coherent contours and tangent quarter-circle corners.
Omissions: Ribbon tails omitted; band and bow prioritized.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='ec0f499f-1e04-4366-8584-5678287d169a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__easter-egg-wrapped-with-ribbon-bow/20260929T132621Z-thuan-mac/reference/easter egg ribbon_ec0f499f-1e04-4366-8584-5678287d169a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='easter-egg-wrapped-with-ribbon-bow'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('easter', 'egg', 'ribbon')
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
        path('egg',(24,4),[('B',(40,29),(33,4),(40,18)),('A',(24,44),16,15,True),('A',(8,29),16,15,True),('B',(24,4),(8,18),(15,4))],True)
        poly('bow',(16,20),(24,25),(32,20),(32,30),(24,25),(16,30),closed=True)
        line('band-left',(8,29),(16,29));line('band-right',(32,29),(40,29));join('band-left','egg');join('band-right','egg');join('band-left','bow');join('band-right','bow')
