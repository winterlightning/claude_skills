"""Long hanging thread above compact oval abdomen; eight legs arranged in mirrored pairs, bent outwards. Shared body attachment nodes.
Keyshape VRECT_L. Lucide bug: compact body and mirrored jointed limbs.
Omissions: Head merged with abdomen; all eight legs and hanging thread retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c5352ba7-8705-433f-bfb4-5f356398c838'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hanging-spider/20260924T094233Z-thuan-mac/reference/spider hang_c5352ba7-8705-433f-bfb4-5f356398c838.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hanging-spider-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "animals"
    aliases=()
    keywords=('hanging', 'spider')

    def build(self):

        def path(n, start, steps, closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(steps):
                if here==end: continue
                tag=f'{n}-{i}'
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C': self.add_bezier(tag,here,(a[0],a[1],end))
                members.append(tag); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,q=4):
            path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('body',(18,23),[('A',(24,17),6,6,True),('A',(30,23),6,6,True),('L',(30,31)),('A',(24,37),6,6,True),('A',(18,31),6,6,True),('L',(18,23))],True)
        line('thread',(24,4),(24,17));join('thread','body')
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         for name,pts in [('upper',[(6,23),(15,18),(16,12)]),('middle',[(6,23),(16,26)]),('lower',[(6,31),(16,35)]),('bottom',[(6,31),(10,44)])]:
          poly(f'{name}-{side}',*[p(x,y) for x,y in pts]);join(f'{name}-{side}','body')
         join(f'upper-{side}',f'middle-{side}');join(f'lower-{side}',f'bottom-{side}')

