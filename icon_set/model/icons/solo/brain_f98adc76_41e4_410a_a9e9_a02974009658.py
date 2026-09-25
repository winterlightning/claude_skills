"""Side-view brain with asymmetric smooth lobes and two curved sulci, preserving the wider anatomical shape."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f98adc76-41e4-410a-a9e9-a02974009658'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__brain-f98adc76/20260925T060624Z-thuan-mac/reference/brain_f98adc76-41e4-410a-a9e9-a02974009658.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'brain-f98adc76-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "artificial-intelligence"
    aliases = ()
    keywords = ('brain',)

    def build(self):
        # Plan: Side-view brain with asymmetric smooth lobes and two curved sulci, preserving the wider anatomical shape.
        # Construction reference: brain: coherent lobes with attached fold strokes

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

        path('brain',(10,20),[('C',(16,8),(10,12),(12,8)),('C',(24,10),(19,8),(22,8)),('C',(29,8),(26,8),(27,8)),('C',(36,15),(33,8),(36,10)),('C',(44,24),(41,15),(44,19)),('C',(41,31),(44,28),(42,29)),('C',(33,40),(41,37),(37,40)),('C',(26,36),(30,40),(28,39)),('C',(17,36),(22,40),(19,39)),('C',(4,29),(8,41),(4,36)),('C',(10,20),(4,24),(6,21))],True)
        path('upper-fold',(24,10),[('C',(20,22),(21,14),(20,17))]);join('upper-fold','brain')
        path('lower-fold',(26,36),[('C',(30,24),(24,31),(26,26))]);join('lower-fold','brain')
