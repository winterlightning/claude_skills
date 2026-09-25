"""curved-drainage-pipe.
Plan: Open-ended S-shaped drainage elbow with tangent quarter arcs and two short flowing water strokes.
Keyshape: VRECT_L, exact SOLO48 inset envelope.
Reference construction: No useful Lucide subject match.
Omissions: Top flange and one of three water trails omitted to maintain spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a4710d47-9041-49d6-96a8-3a84a671fe4a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gutter_a4710d47-9041-49d6-96a8-3a84a671fe4a.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'curved-drainage-pipe'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('gutter',)

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

        path('pipe',(8,4),[(20,4),(20,16),((24,20),4,4,False),(28,20),((40,32),12,12,True),(40,34),(32,34),(32,32),((28,28),4,4,False),(20,28),((8,16),12,12,True),(8,4)],True)
        for x in (28,39):
            self.add_line(f'water-{x}',(x,43),(x,44))
