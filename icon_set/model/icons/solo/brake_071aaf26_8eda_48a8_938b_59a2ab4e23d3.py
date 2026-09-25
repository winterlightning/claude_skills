"""Circular brake rotor with a curved upper-left caliper and an open central hub, rather than a filled dot."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '071aaf26-8eda-48a8-938b-59a2ab4e23d3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__brake-disc-with-caliper/20260925T060624Z-thuan-mac/reference/brake_071aaf26-8eda-48a8-938b-59a2ab4e23d3.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'brake-disc-with-caliper-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('brake',)

    def build(self):
        # Plan: Circular brake rotor with a curved upper-left caliper and an open central hub, rather than a filled dot.
        # Construction reference: no useful Lucide match; concentric rotor and caliper construction

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

        path('rotor',(24,4),[('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True)])
        path('caliper',(4,24),[('A',(24,4),20,20,True),('L',(24,12)),('A',(12,24),12,12,False),('L',(4,24))],True);join('caliper','rotor')
        circle('hub',24,26,4)
