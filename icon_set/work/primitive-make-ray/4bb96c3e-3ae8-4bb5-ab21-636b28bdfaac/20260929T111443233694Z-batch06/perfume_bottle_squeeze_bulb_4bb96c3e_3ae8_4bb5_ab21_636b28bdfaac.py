"""The current atomizer has stacked cramped rectangular necks and a tiny circular bulb. No written feedback. Simplified the neck to one open spray stem and enlarged the squeeze bulb; restored a taller rounded bottle.
Construction: Lucide cooking-pot: rounded body with clear attachment; source supplies atomizer hose and bulb.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4bb96c3e-3ae8-4bb5-ab21-636b28bdfaac'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__perfume-bottle-squeeze-bulb/20260929T110914Z-thuan-mac/reference/perfume_4bb96c3e-3ae8-4bb5-ab21-636b28bdfaac.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'perfume-bottle-squeeze-bulb'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('perfume', 'bottle', 'squeeze', 'bulb')
    
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*ps,closed=False): self.add_polyline(n,*ps,closed=closed)
        def bez(n,a,*ss): self.add_bezier(n,a,*ss)
        def arc(n,a,b,rx,ry=None,s=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=s)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'a',n+'b',closed=True)
        def path(n,a,commands,closed=False):
            members=[]
            for j,c in enumerate(commands):
                k,b,*args=c; name=n+str(j)
                if k=='L': line(name,a,b)
                elif k=='A': arc(name,a,b,*args)
                elif k=='C': bez(name,a,(args[0],args[1],b))
                members.append(name);a=b
            self.add_contour(n,*members,closed=closed)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r),('L',(x+r,y+h)),('A',(x,y+h-r),r),('L',(x,y+r)),('A',(x+r,y),r)],True)
        def join(*ns): self.relate('connect',*ns)

        rect('bottle',6,21,24,21,5)
        poly('neck',(14,21),(14,6),(22,6),(22,21));join('neck','bottle')
        line('hose',(22,10),(32,10));join('hose','neck')
        path('bulb',(32,10),[('C',(37,6),(32,7),(34,6)),('C',(42,12),(41,6),(42,9)),('C',(37,18),(42,15),(41,18)),('C',(32,10),(32,18),(31,14))],True);join('bulb','hose')
