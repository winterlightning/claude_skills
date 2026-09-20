'Running Man Messenger Icon.\nPlan and review: Retained running pose with round head, forward-leaning torso and bent limbs. Simplified the filled body silhouette to rounded strokes. Head center(30,10), radius4; torso starts(30,22), exact8 centerline/4 ink gap.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: human_ref/full_body_ref.png: circular head, rounded limbs, pose-specific torso alignment.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e67d265c-c409-4a6f-a8fd-58e1dec4e65f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/aim logo_e67d265c-c409-4a6f-a8fd-58e1dec4e65f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'running-person-rounded-silhouette'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('running', 'person', 'rounded', 'silhouette')

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

        circle('head',30,10,4)
        curve('torso',(30,22),((30,26),(26,30),(24,32)))
        path('arm-forward',(30,22),[(36,28),(42,22)]);path('arm-back',(30,22),[(20,22),(12,28)])
        path('leg-front',(24,32),[(36,36),(34,42)]);path('leg-back',(24,32),[(16,38),(6,38)])
        for s in ('arm-forward','arm-back','leg-front','leg-back'):self.relate('connect','torso',s)
        self.relate('connect','arm-forward','arm-back');self.relate('connect','leg-front','leg-back')
        self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
