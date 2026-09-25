"""A broad blank rounded board sits on outward leaning easel legs with a crossbar."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80878854-c232-44fa-a536-c8570d598e41'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__blank-presentation-easel/20260925T060624Z-thuan-mac/reference/chalkboard_80878854-c232-44fa-a536-c8570d598e41.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'blank-presentation-easel-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('chalkboard',)

    def build(self):
        # Plan: A broad blank rounded board sits on outward leaning easel legs with a crossbar.
        # Construction reference: presentation: sparse screen outline with supporting stand

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

        rounded('board',6,6,42,30,3)
        for side,a,b,c in [('left',17,14,12),('right',31,34,36)]:
         poly('leg-'+side,(a,30),(b,38),(c,42));join('board','leg-'+side)
        line('crossbar',(14,38),(34,38));join('crossbar','leg-left');join('crossbar','leg-right')
