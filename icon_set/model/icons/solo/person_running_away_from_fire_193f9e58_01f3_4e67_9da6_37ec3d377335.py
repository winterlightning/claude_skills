'Person Running Away from Fire. Plan and review: Left-running figure and separate flame remain a natural emergency scene. Head radius4 at(16,10), torso starts(16,22): exact8 centerline /4 visible gap. Limbs simplified to coherent centerlines. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: Human references: icon_set/references/human_ref/user.svg and full_body_ref.png. Left-running figure and separate flame remain a natural emergency scene. Head radius4 at(16,10), torso starts(16,22): exact8 centerline /4 visible gap. Limbs simplified to coherent centerlines.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '193f9e58-01f3-4e67-9da6-37ec3d377335'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/wayfinding/safety fire exit_193f9e58-01f3-4e67-9da6-37ec3d377335.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-running-away-from-fire'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'running', 'away', 'from', 'fire')

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

        circle('head',16,10,4)
        self.add_line('torso',(16,22),(16,30))
        path('arms',(6,26),[(10,22),(16,22),(21,26)])
        self.relate('connect','torso','arms')
        path('legs',(6,42),[(10,34),(16,30),(22,38),(26,38)]);self.relate('connect','torso','legs')
        curve('flame',(36,6),((38,13),(30,15),(30,22)),((30,29),(42,29),(42,22)),((42,17),(39,16),(40,13)))
        self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
