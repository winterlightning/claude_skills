'Windy Weather Cloud Icon. Plan and review: Rounded cloud and all three right-side wind marks retained. Upper/lower strokes extend farther than the short-streak variant; the shortest middle mark reads as a dot at48. Keyshape HRECT_L centerline envelope (4,8)-(44,40). Chosen to fit the complete subject silhouette. Reference: Lucide cloud original and atomic-debug: continuous lobe outline and flat base; streak layout from source.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '938ed972-16e5-443d-b264-00b0193289f3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/weather/visibility cloud high_938ed972-16e5-443d-b264-00b0193289f3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloud-with-long-wind-streaks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('cloud', 'with', 'long', 'wind', 'streaks')

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

        curve('cloud',(12,30),((8,30),(4,28),(4,24)),((4,20),(7,17),(11,17)),((11,12),(14,8),(19,8)),((24,8),(28,12),(28,18)),((32,18),(34,21),(34,24)),((34,28),(30,30),(26,30)),((22,30),(16,30),(12,30)))
        self.add_line('wind-top',(36,8),(44,8))
        self.add_line('wind-mid',(43,24),(44,24))
        self.add_line('wind-bottom',(32,40),(44,40))
