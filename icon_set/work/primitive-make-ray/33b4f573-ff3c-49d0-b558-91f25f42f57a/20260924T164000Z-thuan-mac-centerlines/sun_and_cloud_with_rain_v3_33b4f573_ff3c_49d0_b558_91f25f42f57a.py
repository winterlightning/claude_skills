"""Sun behind a rounded rain cloud with three parallel rain strokes.
Plan: Sun behind a rounded rain cloud with three parallel rain strokes.
Construction: Lucide cloud-sun-rain original and atoms: overlapping sun/cloud and separate rain series.
Omissions: Rays omitted to preserve a broad sun arc and complete cloud; three rain marks retained."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='33b4f573-ff3c-49d0-b558-91f25f42f57a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__sun-and-cloud-with-rain-v3/20260924T163448Z-thuan-mac/reference/cloud sun rain_33b4f573-ff3c-49d0-b558-91f25f42f57a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='sun-and-cloud-with-rain-v3'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('sun', 'and', 'cloud', 'with', 'rain', 'v3')

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
        path('cloud',(14,32),[('A',(6,24),8,8,True),('A',(14,16),8,8,True),('C',(24,14),(14,12),(20,10)),('C',(28,20),(26,16),(24,20)),('A',(34,26),6,6,True),('A',(28,32),6,6,True),('L',(14,32))],True)
        path('sun',(24,14),[('C',(34,6),(24,8),(30,6)),('C',(42,16),(39,6),(42,10)),('C',(34,26),(42,22),(38,26))]);join('sun','cloud')
        for j,x in enumerate((14,24,34)):line('rain-'+str(j),(x,40),(x-1,42))
