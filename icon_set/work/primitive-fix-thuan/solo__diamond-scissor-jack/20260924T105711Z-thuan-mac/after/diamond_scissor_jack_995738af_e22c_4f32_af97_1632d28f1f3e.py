"""diamond-scissor-jack.
Plan: Diamond scissor mechanism with a broad saddle, rounded base and horizontal screw crank. Centered mechanism x20 leaves space for the right crank.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: No useful Lucide subject match.
Omissions: Circular crank knob represented by a short turning handle.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '995738af-e22c-4f32-af97-1632d28f1f3e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diamond-scissor-jack/20260924T105711Z-thuan-mac/reference/car jack_995738af-e22c-4f32-af97-1632d28f1f3e.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'diamond-scissor-jack'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('car', 'jack')

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

        box('saddle',14,6,26,14,2)
        self.add_polyline('arms',(20,14),(34,24),(20,34),(6,24),closed=True)
        box('base',10,34,30,42,3)
        self.relate('connect','saddle','arms');self.relate('connect','base','arms')
        self.add_line('screw',(6,24),(42,24));self.relate('connect','screw','arms')
        self.add_line('crank',(42,20),(42,28));self.relate('connect','crank','screw')
