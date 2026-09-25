"""Bell has a broad flared skirt, attached top loop and modest clapper, with paired ringing marks."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4a12d6a5-374a-5c49-8bd7-4bf52793db57'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bell-with-ringing-strokes/20260925T060624Z-thuan-mac/reference/alarm bell ring_4a12d6a5-374a-5c49-8bd7-4bf52793db57.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'bell-with-ringing-strokes-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('alarm bell ring',)

    def build(self):
        # Plan: Bell has a broad flared skirt, attached top loop and modest clapper, with paired ringing marks.
        # Construction reference: bell-ring: smooth shoulder-to-skirt transitions

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

        path('bell',(10,32),[('C',(15,23),(13,28),(15,27)),('A',(33,23),9,8,True),('C',(38,32),(33,27),(35,28)),('L',(10,32))],True)
        path('loop',(20,16),[('A',(28,16),4,10,True)]);join('loop','bell')
        path('clapper',(18,32),[('A',(30,32),6,10,False)]);join('clapper','bell')
        for side,x in [('left',6),('right',42)]:
         line('ring-'+side,(x,16),(x,20))
