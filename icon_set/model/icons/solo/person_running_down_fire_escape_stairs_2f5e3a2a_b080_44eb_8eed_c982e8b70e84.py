'Person Running Down Emergency Fire Stairs. Plan and review: Runner, descending stairs and flame retained. Head radius3 at(16,9), torso starts(16,20): exact8 centerline /4 visible gap. Three stair levels and simple bent limbs keep the action readable. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: Human references: icon_set/references/human_ref/user.svg and full_body_ref.png. Runner, descending stairs and flame retained. Head radius3 at(16,9), torso starts(16,20): exact8 centerline /4 visible gap. Three stair levels and simple bent limbs keep the action readable.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f5e3a2a-b080-44eb-8eed-c982e8b70e84'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/wayfinding/safety fire exit stairs_2f5e3a2a-b080-44eb-8eed-c982e8b70e84.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-running-down-fire-escape-stairs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'running', 'down', 'fire', 'escape', 'stairs')

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

        circle('head',16,9,3)
        self.add_line('torso',(16,20),(16,28))
        path('arms',(6,24),[(10,20),(16,20),(21,20)]);self.relate('connect','torso','arms')
        path('legs',(8,34),[(16,28),(20,30),(22,30)]);self.relate('connect','torso','legs')
        path('stairs',(6,42),[(18,42),(18,38),(30,38),(30,32),(42,32)])
        curve('flame',(35,6),((37,12),(30,13),(30,18)),((30,25),(42,25),(42,18)),((42,14),(39,13),(40,10)))
        self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
