"""Open upper thigh bends into a horizontal knee and a tapering shin and foot. Smooth anatomical contours replace the angular boot. Human full_body_ref consulted for simple limb flow; no head present."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '87d9a32d-418e-48eb-9d3b-c61d18048ab3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bent-leg/20260925T060624Z-thuan-mac/reference/limb_87d9a32d-418e-48eb-9d3b-c61d18048ab3.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'bent-leg-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('limb',)

    def build(self):
        # Plan: Open upper thigh bends into a horizontal knee and a tapering shin and foot. Smooth anatomical contours replace the angular boot. Human full_body_ref consulted for simple limb flow; no head present.
        # Construction reference: human_ref/full_body_ref.png: rounded continuous limb construction; no exact Lucide match

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

        path('leg',(24,4),[('L',(24,18)),('C',(22,21),(24,20),(24,21)),('L',(17,22)),('C',(15,28),(14,23),(14,25)),('L',(17,37)),('C',(14,40),(17,39),(15,39)),('C',(10,44),(11,41),(10,41)),('L',(22,44)),('A',(25,41),3,3,False),('L',(25,30)),('L',(31,30)),('C',(38,22),(36,30),(38,27)),('L',(38,4))])
