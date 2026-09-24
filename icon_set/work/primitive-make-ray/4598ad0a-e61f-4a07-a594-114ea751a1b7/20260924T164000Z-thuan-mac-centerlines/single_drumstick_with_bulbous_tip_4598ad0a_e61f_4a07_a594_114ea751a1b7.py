"""Single diagonal drumstick with a rounded tip and flowing bulb-to-shaft transition.
Plan: Single diagonal drumstick with a rounded tip and flowing bulb-to-shaft transition.
Construction: No useful exact local Lucide match; source silhouette rebuilt from coherent curves.
Omissions: No concept-bearing part omitted."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='4598ad0a-e61f-4a07-a594-114ea751a1b7'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__single-drumstick-with-bulbous-tip/20260924T163448Z-thuan-mac/reference/drumstick_4598ad0a-e61f-4a07-a594-114ea751a1b7.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='single-drumstick-with-bulbous-tip'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('single', 'drumstick', 'with', 'bulbous', 'tip')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        path('drumstick',(16,26),[('L',(34,8)),('C',(38,6),(36,6),(36,6)),('A',(42,10),4,4,True),('C',(40,14),(42,12),(42,12)),('L',(22,32)),('C',(14,42),(20,34),(22,42)),('A',(6,34),8,8,True),('C',(16,26),(6,29),(12,30))],True)
