"""Dense three-cell wings and low links obscure the airy horizontal panel arrangement. Restore two-cell wings and central alignment.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: satellite: balanced linked modules
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='920fba2e-1282-4f3c-a45c-8bd917d8f0f4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__space-station-with-paired-solar-wings/20260929T131521Z-thuan-mac/reference/space station_920fba2e-1282-4f3c-a45c-8bd917d8f0f4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='space-station-with-paired-solar-wings'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('space', 'station', 'with', 'paired', 'solar', 'wings')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        for x in (6,34):
         box(f'wing{x}',x,16,x+8,42)
         line(f'row{x}',(x,29),(x+8,29));join(f'row{x}',f'wing{x}')
        box('upper',20,6,28,14)
        box('core',20,24,28,36)
        line('spine',(24,14),(24,24));join('spine','upper');join('spine','core')
        line('link-left',(14,29),(20,29));line('link-right',(28,29),(34,29))
        for n,a,b in [('link-left','wing6','core'),('link-right','wing34','core')]:join(n,a);join(n,b)
