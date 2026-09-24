"""Hand gripping a plain cup with a smoothly raised thumb and rounded cup corners.
Plan: Hand gripping a plain cup with a smoothly raised thumb and rounded cup corners.
Construction: Lucide hand: coherent curves and rounded fingertips.
Omissions: Separate finger divisions omitted; thumb, curled finger and cup retained."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='9264b9dc-a5f7-44e5-8956-5e45e3269681'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hand-gripping-plain-cup/20260924T162241Z-thuan-mac/reference/ceramic making_9264b9dc-a5f7-44e5-8956-5e45e3269681.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-gripping-plain-cup'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('hand', 'gripping', 'plain', 'cup')

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
        path('cup',(26,14),[('L',(38,14)),('A',(42,18),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(26,42)),('L',(26,32))])
        path('hand',(6,24),[('L',(10,24)),('C',(18,6),(16,24),(14,6)),('L',(22,6)),('A',(26,10),4,4,True),('L',(26,14)),('L',(24,24)),('L',(28,24)),('A',(28,32),4,4,True),('L',(20,32))])
        path('palm',(6,38),[('C',(16,42),(10,38),(11,42)),('L',(26,42))]);join('palm','cup');join('hand','cup')
