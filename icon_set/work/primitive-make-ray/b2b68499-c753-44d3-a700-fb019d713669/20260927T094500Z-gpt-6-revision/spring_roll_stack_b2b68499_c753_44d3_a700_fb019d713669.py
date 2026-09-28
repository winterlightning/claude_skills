"""Stack of Spring Rolls."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b2b68499-c753-44d3-a700-fb019d713669'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__spring-roll-stack/20260927T093533Z-thuan-mac-1/reference/exotic food rolls_b2b68499-c753-44d3-a700-fb019d713669.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'spring-roll-stack'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('spring', 'roll', 'stack')

    def build(self):
        # Plan: The original pile has overlapping angled rolls. Keep two broad end faces
        # at native size and tilt the upper roll so the stack reads as arranged food.
        # Envelope: VRECT_L; visible ink (6, 2, 42, 46) on SOLO48.

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

        path('lower',(15,30),[('L',(33,30)),('A',(40,37),7,7,True),('A',(33,44),7,7,True),('L',(15,44)),('A',(15,30),7,7,True)],True)
        path('end-lower',(33,30),[('A',(33,44),7,7,False)]);join('end-lower','lower')
        path('upper',(19,4),[('L',(31,10)),('A',(36,15),5,5,True),('A',(31,20),5,5,True),('L',(19,14)),('A',(19,4),5,5,True)],True)
        path('end-upper',(31,10),[('A',(31,20),5,5,False)]);join('end-upper','upper')
