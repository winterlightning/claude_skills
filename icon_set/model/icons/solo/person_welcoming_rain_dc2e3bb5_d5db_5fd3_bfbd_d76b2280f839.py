"""Person Welcoming Rain.

Plan: Mirrored raised arms below round head; rain series across upper band. Extremes (6,6)-(42,42).
Construction: human_ref/full_body_ref.png round head and bent limbs.
Reduction: Rain reduced to three strokes; torso and arms use single strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'dc2e3bb5-d5db-5fd3-bfbd-d76b2280f839'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/blessed rainy day_dc2e3bb5-d5db-5fd3-bfbd-d76b2280f839.svg'
AUTHOR = 'gpt-6'


class IconPersonWelcomingRain(Solo48):
    icon_id = 'person-welcoming-rain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('person', 'welcoming', 'rain')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        circle('head',24,22,5)
        self.add_line('torso',(24,35),(24,42))
        for side in [-1,1]:
         self.add_polyline('arm'+str(side),(24,35),(14 if side<0 else 34,35),(6 if side<0 else 42,27));self.relate('connect','arm'+str(side),'torso')
        for i,x in enumerate((10,24,38)):self.add_line('rain'+str(i),(x,6),(x-2,8))
        self.relate('connect','arm-1','arm1');self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
