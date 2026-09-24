"""Hair dryer with three evenly spaced smooth warm-air waves.
Plan: Hair dryer with three evenly spaced smooth warm-air waves.
Construction: No useful exact Lucide dryer match; broad circular rear and repeated smooth waves.
Omissions: Rear vent omitted to reserve room for three real waves."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='42bba311-8e3c-4b43-b08d-1ec72d87ad57'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hair-dryer-blowing-three-warm-air-waves/20260924T162241Z-thuan-mac/reference/dryer_42bba311-8e3c-4b43-b08d-1ec72d87ad57.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hair-dryer-blowing-three-warm-air-waves'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('hair', 'dryer', 'blowing', 'three', 'warm', 'air', 'waves')

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
        path('dryer',(14,8),[('L',(26,8)),('L',(26,24)),('L',(18,24)),('L',(21,40)),('L',(11,40)),('L',(9,24)),('C',(4,18),(5,24),(4,21)),('A',(14,8),10,10,True)],True)
        for j,y in enumerate((11,21,31)):
         path('air-'+str(j),(35,y),[('C',(44,y),(38,y-3),(41,y+3))])
