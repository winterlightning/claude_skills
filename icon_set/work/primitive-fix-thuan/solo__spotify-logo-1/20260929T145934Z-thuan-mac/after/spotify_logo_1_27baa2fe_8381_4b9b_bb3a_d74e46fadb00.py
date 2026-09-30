"""The rejected sound lines are short symmetric arches. Restore three progressively shorter curved strokes slanting down toward the right inside the circular logo.
Plan: CIRCLE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct Lucide match; original owns the three asymmetric broadcast curves.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='27baa2fe-8381-4b9b-bb3a-d74e46fadb00'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__spotify-logo-1/20260929T145934Z-thuan-mac/reference/spotify logo 1_27baa2fe-8381-4b9b-bb3a-d74e46fadb00.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='spotify-logo-1'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('spotify', 'logo', '1')
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

        oval('disc',24,24,20,20)
        path('wave-top',(16,16),[('C',(32,18),(21,14),(28,16))])
        path('wave-middle',(15,25),[('C',(31,27),(20,23),(26,24))])
        path('wave-bottom',(20,34),[('C',(27,34),(22,33),(25,34))])
