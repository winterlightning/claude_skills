"""Teapot on a serving stand with rounded vessel, curved spout and broad loop handle.
Plan: Teapot on a serving stand with rounded vessel, curved spout and broad loop handle.
Construction: Lucide wallet rounded-corner and semicircular construction; original teapot/stand arrangement.
Omissions: Lid seam omitted; knob, handle, spout, tray and feet retained."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='df688f36-b5fe-4f17-ae65-8d71d00de128'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__teapot-serving-stand/20260924T163448Z-thuan-mac/reference/tea pot 1_df688f36-b5fe-4f17-ae65-8d71d00de128.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='teapot-serving-stand'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('teapot', 'serving', 'stand')

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
        path('pot',(20,12),[('A',(30,22),10,10,True),('A',(20,32),10,10,True),('L',(14,32)),('C',(6,24),(10,32),(6,28)),('L',(6,14)),('C',(14,22),(10,14),(13,18)),('C',(20,12),(14,16),(16,12))],True)
        path('handle',(20,12),[('A',(42,22),22,10,True),('A',(20,32),22,10,True)]);join('pot','handle')
        circle('knob',20,8,2);line('stem',(20,10),(20,12));join('stem','knob');join('stem','pot');join('stem','handle')
        poly('tray',(6,32),(14,32),(20,32),(42,32),(42,40),(34,40),(14,40),(6,40),closed=True);join('tray','pot');join('tray','handle')
        for x in (14,34):line('foot-'+str(x),(x,40),(x,42));join('foot-'+str(x),'tray')
