"""Rotary Pizza Cutter Tool."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '146303ff-87be-59be-ab7a-decec547ca14'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pizza cutter_146303ff-87be-59be-ab7a-decec547ca14.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rotary-pizza-cutter'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('rotary', 'pizza', 'cutter')

    def build(self):
        # Plan: Supplied cutter: capsule handle above circular blade. Axle simplified to an attached radial arm; no useful exact Lucide match.
        # Envelope: VRECT_M; visible ink (8, 2, 40, 46) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('handle',(20,16),[('L',(20,8)),('A',(28,8),4,4,True),('L',(28,16)),('A',(20,16),4,4,True)],True)
        path('wheel',(24,20),[('A',(24,44),14,12,True),('A',(24,20),14,12,True)],True)
        line('arm',(24,20),(24,32));join('arm','wheel');join('handle','wheel');join('arm','handle')
