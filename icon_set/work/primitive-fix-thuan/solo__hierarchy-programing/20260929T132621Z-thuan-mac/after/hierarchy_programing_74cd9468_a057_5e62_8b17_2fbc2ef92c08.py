"""Center the top node and attach each edge at exact circle extrema, with larger equal nodes.
Symbol plan: SQUARE on SOLO48; named shapes and source arrangement.
Before review: Top node is offset from the branch junction and several links stop away from the circle outlines.
Construction reference: Lucide square: coherent contours and tangent quarter-circle corners.
Omissions: 
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='74cd9468-a057-5e62-8b17-2fbc2ef92c08'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hierarchy-programing/20260929T132621Z-thuan-mac/reference/hierarchy_74cd9468-a057-5e62-8b17-2fbc2ef92c08.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hierarchy-programing'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('hierarchy',)
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
        for n,x,y in [('top',24,12),('left',12,36),('right',36,36)]: circle(n,x,y,6)
        for n,a,b,u,v in [('left-link',(18,12),(12,30),'top','left'),('right-link',(30,12),(36,30),'top','right'),('base',(18,36),(30,36),'left','right')]:
            line(n,a,b);join(n,u);join(n,v)
