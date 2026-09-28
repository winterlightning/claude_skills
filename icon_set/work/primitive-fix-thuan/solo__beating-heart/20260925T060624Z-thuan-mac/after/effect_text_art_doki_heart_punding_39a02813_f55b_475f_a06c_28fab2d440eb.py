"""A softly curved heart with three radiating beat strokes at upper left."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '39a02813-f55b-475f-a06c-28fab2d440eb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__beating-heart/20260925T060624Z-thuan-mac/reference/effect text art doki heart punding_39a02813-f55b-475f-a06c-28fab2d440eb.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'beating-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('effect text art doki heart punding',)

    def build(self):
        # Plan: A softly curved heart with three radiating beat strokes at upper left.
        # Construction reference: heart: rounded lobes and smoothly converging sides

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

        path('heart',(28,26),[('C',(42,26),(34,14),(42,17)),('C',(28,42),(42,32),(35,38)),('C',(14,26),(21,38),(14,32)),('C',(28,26),(14,17),(22,14))],True)
        line('beat-left',(6,18),(6,20))
        line('beat-diagonal',(10,9),(12,11))
        line('beat-top',(22,6),(23,9))
