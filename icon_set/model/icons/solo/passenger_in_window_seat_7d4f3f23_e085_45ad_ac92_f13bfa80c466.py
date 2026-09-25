'Passenger in Airplane Window Seat. Plan and review: Seated passenger, bent knees, seat and cabin window retained. Head radius4 at(15,10), torso starts(15,22): exact8 centerline /4 visible gap, with vertical torso alignment. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: Human references: icon_set/references/human_ref/user.svg and full_body_ref.png. Seated passenger, bent knees, seat and cabin window retained. Head radius4 at(15,10), torso starts(15,22): exact8 centerline /4 visible gap, with vertical torso alignment.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d4f3f23-e085-45ad-ac92-f13bfa80c466'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/wayfinding/seat regular_7d4f3f23-e085-45ad-ac92-f13bfa80c466.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'passenger-in-window-seat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('passenger', 'in', 'window', 'seat')

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

        circle('head',15,10,4)
        path('seat',(6,22),[(6,32),((14,40),8,8,False),(24,40)])
        self.add_line('torso',(15,22),(15,30));path('legs',(15,30),[(30,30),(34,42)])
        self.relate('connect','torso','legs')
        box('window',30,6,42,20,4)
        self.mark_human_figure('passenger',head='head',torso='torso',torso_junction='start')
