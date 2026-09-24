'Room with Door and Window.\nPlan and review: Retained door, four-pane window, ceiling and floor. Omitted vertical room sidewalls and door knob; enlarged panes to keep all four openings clear.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '15d7928a-0a97-4ec4-b4c0-f21360f062be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/interior_15d7928a-0a97-4ec4-b4c0-f21360f062be.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'interior-wall-with-door-and-window'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('interior', 'wall', 'with', 'door', 'and', 'window')

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

        self.add_line('ceiling',(6,6),(42,6));self.add_line('floor',(6,42),(42,42))
        path('door',(6,42),[(6,20),(16,20),(16,42)]);self.relate('connect','door','floor')
        path('window',(26,16),[(42,16),(42,32),(26,32),(26,16)],True)
        self.add_line('mullion',(34,16),(34,32));self.add_line('window-bar',(26,24),(42,24))
        self.relate('connect','window','mullion');self.relate('connect','window','window-bar');self.relate('connect','mullion','window-bar')
