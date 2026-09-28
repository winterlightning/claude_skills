'Craftsman Holding a Hammer.\nPlan and review: Retained worker and held upright hammer. Simplified torso/arm outlines to round-ended limbs and handle to one stroke. Head center(15,13), radius7; neck(15,28): 8 centerline / 4 ink gap, with head aligned to vertical torso.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this subject.\nConstruction reference: human_ref/full_body_ref.png: outlined head, round-ended limbs, exact detached gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04ebbce5-fdd2-4c6c-bc45-d497a7339082'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/greek god hephaestus_04ebbce5-fdd2-4c6c-bc45-d497a7339082.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'craftsman-holding-a-hammer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('craftsman', 'holding', 'a', 'hammer')

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

        circle('head',15,13,7)
        self.add_line('torso',(15,28),(15,42))
        path('left-arm',(15,28),[(6,32),(6,42)]);self.relate('connect','torso','left-arm')
        path('right-arm',(15,28),[(25,36),(36,36)]);self.relate('connect','torso','right-arm')
        box('hammer',31,14,42,24,2)
        self.add_line('handle',(36,24),(36,42));self.relate('connect','hammer','handle');self.relate('connect','handle','right-arm')
        self.mark_human_figure('worker',head='head',torso='torso',torso_junction='start')
