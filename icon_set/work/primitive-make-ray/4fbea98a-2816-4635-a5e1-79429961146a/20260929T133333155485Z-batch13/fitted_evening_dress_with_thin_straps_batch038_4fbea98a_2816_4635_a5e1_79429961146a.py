"""Restore separate vertical straps, a fitted waist and a long tapered skirt.
Symbol plan: VRECT_M on SOLO48; named shapes and source arrangement.
Before review: The wide angular garment looks like a sleeveless top and lacks thin straps.
Construction reference: Lucide shirt: economical garment contour; source thin straps and fitted silhouette.
Omissions: Fine seam and folds omitted.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='4fbea98a-2816-4635-a5e1-79429961146a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__fitted-evening-dress-with-thin-straps-batch038/20260929T132822Z-thuan-mac/reference/evening wear_4fbea98a-2816-4635-a5e1-79429961146a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='fitted-evening-dress-with-thin-straps-batch038'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('evening', 'wear')
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
        path('dress',(12,12),[('L',(24,22)),('L',(36,12)),('B',(33,25),(41,16),(33,20)),('B',(38,34),(33,28),(38,29)),('L',(35,44)),('L',(13,44)),('L',(10,34)),('B',(15,25),(10,29),(15,28)),('B',(12,12),(15,20),(7,16))],True)
        for x in (12,36):line(f'strap-{x}',(x,4),(x,12));join(f'strap-{x}','dress')
