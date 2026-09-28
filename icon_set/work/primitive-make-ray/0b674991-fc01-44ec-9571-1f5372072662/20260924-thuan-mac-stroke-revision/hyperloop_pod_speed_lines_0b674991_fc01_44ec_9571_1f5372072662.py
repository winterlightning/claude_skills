"""Horizontal streamlined pod with semicircular rear, rising rounded nose and curved window; long separated speed strokes.
Keyshape HRECT_M. No useful subject-specific Lucide match; supplied original determines the silhouette.
Omissions: Middle speed dash omitted because rounded rear occupies its space."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0b674991-fc01-44ec-9571-1f5372072662'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hyperloop-pod-speed-lines/20260924T094233Z-thuan-mac/reference/hyperloop speed_0b674991-fc01-44ec-9571-1f5372072662.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hyperloop-pod-speed-lines'
    keyshape = Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('hyperloop', 'pod', 'speed', 'lines')

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

        path('pod',(22,10),[('L',(26,10)),('C',(44,26),(35,10),(44,18)),('A',(32,38),12,12,True),('L',(22,38)),('A',(8,24),14,14,True),('A',(22,10),14,14,True)],True)
        path('window',(22,10),[('A',(34,26),12,16,False),('L',(44,26))]);join('window','pod')
        line('speed-top',(4,10),(22,10));join('speed-top','pod')
        line('speed-bottom',(4,38),(22,38));join('speed-bottom','pod')

