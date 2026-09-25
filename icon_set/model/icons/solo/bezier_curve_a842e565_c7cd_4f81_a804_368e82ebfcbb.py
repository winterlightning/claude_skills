"""An arch rises from a large square anchor through a small top square to a circular end; horizontal handle reaches a left circle."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a842e565-c7cd-4f81-a804-368e82ebfcbb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bezier-curve-with-control-handles/20260925T060624Z-thuan-mac/reference/bezier curve_a842e565-c7cd-4f81-a804-368e82ebfcbb.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'bezier-curve-with-control-handles-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('bezier curve',)

    def build(self):
        # Plan: An arch rises from a large square anchor through a small top square to a circular end; horizontal handle reaches a left circle.
        # Construction reference: spline: continuous curve with endpoint nodes

        def path(name, start, commands, closed=False):
            members=[]; here=start
            for index, command in enumerate(commands):
                ident=f'{name}-{index}'; kind,end,*args=command
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,cx,cy,r):
            path(name,(cx-r,cy),[('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        rounded('anchor',6,28,22,42,3)
        poly('node',(22,6),(30,6),(30,14),(22,14),(22,6))
        circle('handle',9,10,3)
        line('handle-bar',(12,10),(22,10));join('handle-bar','handle');join('handle-bar','node')
        path('left-curve',(12,28),[('C',(22,14),(12,21),(18,17))]);join('left-curve','anchor');join('left-curve','node')
        path('right-curve',(30,10),[('C',(39,36),(39,10),(39,23))]);join('right-curve','node')
        circle('end',39,39,3);join('right-curve','end')
