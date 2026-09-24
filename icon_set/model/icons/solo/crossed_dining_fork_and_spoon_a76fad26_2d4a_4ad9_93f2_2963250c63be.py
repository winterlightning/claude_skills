"""crossed-dining-fork-and-spoon.
Plan: Crossed fork and spoon; diagonal parallel tines spaced from one common step, smoothly rounded fork bowl and slender oval spoon; handles cross below the bowls.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: Lucide utensils-crossed: diagonal tine construction and crossing shaft strokes.
Omissions: Outlined grip thickness.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a76fad26-2d4a-4ad9-93f2-2963250c63be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/cuisine_a76fad26-2d4a-4ad9-93f2-2963250c63be.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'crossed-dining-fork-and-spoon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cuisine',)

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        self.add_line('fork-left-0',(6,18),(12,24))
        curve('fork-bowl',(12,24),((16,28),(20,24),(22,22)),((26,18),(26,14),(24,12)))
        self.add_line('fork-right',(24,12),(18,6));self.add_contour('fork','fork-left-0','fork-bowl','fork-right')
        self.add_line('middle-tine',(6,6),(16,16))
        path('spoon',(37,6),[((42,14),5,8,True),((37,22),5,8,True),((32,14),5,8,True),((37,6),5,8,True)],True)
        self.add_line('fork-handle',(22,22),(42,42));self.relate('connect','fork-handle','fork')
        self.add_line('spoon-handle',(37,22),(17,42));self.relate('connect','spoon-handle','spoon');self.relate('connect','fork-handle','spoon-handle')
