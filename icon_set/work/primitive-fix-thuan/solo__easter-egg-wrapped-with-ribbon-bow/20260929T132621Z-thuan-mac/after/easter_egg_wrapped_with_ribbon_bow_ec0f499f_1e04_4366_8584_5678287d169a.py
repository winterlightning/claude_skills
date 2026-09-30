"""Restore the full egg silhouette with a central ribbon and bow knot.
Symbol plan: VRECT_L on SOLO48; named shapes and source arrangement.
Before review: The bow replaces the top of the egg and the ribbon band and tails are absent.
Construction reference: Lucide square: coherent contours and tangent quarter-circle corners.
Omissions: Ribbon knot and tails merged into the broad central bow; shell occluded behind ribbon.
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
        # The ribbon occludes the middle shell; top and bottom retain one egg silhouette.
        path('egg-top',(14,17),[('B',(24,4),(16,8),(20,4)),('B',(34,17),(28,4),(32,8))])
        path('egg-bottom',(34,33),[('B',(24,44),(34,41),(30,44)),('B',(14,33),(18,44),(14,41))])
        path('bow-left',(24,25),[('B',(14,17),(21,20),(18,17)),('B',(8,25),(9,17),(8,19)),('B',(14,33),(8,31),(9,33)),('B',(24,25),(18,33),(21,30))],True)
        path('bow-right',(24,25),[('B',(34,17),(27,20),(30,17)),('B',(40,25),(39,17),(40,19)),('B',(34,33),(40,31),(39,33)),('B',(24,25),(30,33),(27,30))],True)
        for x in ('egg-top','egg-bottom'):
            for y in ('bow-left','bow-right'):join(x,y)
        join('bow-left','bow-right')
