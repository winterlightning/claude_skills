"""A speech balloon has two separated jagged fracture edges and a bottom-left tail; enclosing halves remain recognizably one bubble."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9390f65a-a76b-451f-b66d-2d0bd6fbda66'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__broken-speech-bubble-solo-b003-03/20260925T060624Z-thuan-mac/reference/language barrier broken bubble_9390f65a-a76b-451f-b66d-2d0bd6fbda66.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'broken-speech-bubble-solo-b003-03-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('language barrier broken bubble',)

    def build(self):
        # Plan: A speech balloon has two separated jagged fracture edges and a bottom-left tail; enclosing halves remain recognizably one bubble.
        # Construction reference: no useful Lucide match; rounded enclosure corners with deliberate fractured edges

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

        path('left',(19,6),[('L',(10,6)),('A',(6,10),4,4,False),('L',(6,34)),('A',(10,38),4,4,False),('L',(14,38)),('L',(14,42)),('L',(22,36))])
        poly('crack-left',(19,6),(24,14),(19,18),(24,27))
        join('left','crack-left')
        path('right',(31,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,34)),('A',(38,38),4,4,True),('L',(30,38))])
        poly('crack-right',(31,6),(34,16),(31,21),(34,28));join('right','crack-right')
