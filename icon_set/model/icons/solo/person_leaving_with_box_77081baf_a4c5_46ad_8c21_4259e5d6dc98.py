'Fired Employee Leaving Office.\nPlan and review: Retained person carrying a box with doorway behind. Simplified body to round-ended stick limbs; omitted door knob. Head center(32,14), radius4, outline bottom18; torso neck(32,26) gives exactly8 centerline /4 ink clearance and vertical alignment.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: human_ref/full_body_ref.png: round detached head and rounded limbs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77081baf-a4c5-46ad-8c21-4259e5d6dc98'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/worker lay off fired user sad door box_77081baf-a4c5-46ad-8c21-4259e5d6dc98.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-leaving-with-box'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'leaving', 'with', 'box')

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

        path('door',(18,42),[(6,42),(6,6),(22,6)])
        circle('head',32,14,4)
        path('torso',(32,26),[(32,32),(30,42)])
        self.add_line('leg-right',(32,32),(42,42));self.relate('connect','torso','leg-right')
        box('box',16,24,24,32,1)
        self.add_line('arm',(32,26),(24,28));self.relate('connect','arm','torso');self.relate('connect','arm','box')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
