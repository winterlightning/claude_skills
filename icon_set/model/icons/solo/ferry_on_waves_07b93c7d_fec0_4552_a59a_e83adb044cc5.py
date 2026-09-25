'Ferry Ship on Waves.\nPlan and review: Retained ferry cabin, chimney, broad hull and a rolling waterline. Omitted small windows and reduced two waterlines to one; rebalanced vertical proportions to restore the water cue.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide ship: simple cabin, broad hull and chimney; source side view.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07b93c7d-fec0-4552-a59a-e83adb044cc5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/ferry_07b93c7d-fec0-4552-a59a-e83adb044cc5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ferry-on-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('ferry', 'on', 'waves')

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

        path('hull',(4,20),[(44,20),(36,29),(12,29),(4,20)],True)
        path('cabin',(12,20),[(12,12),(32,12),(36,20)]);self.relate('connect','hull','cabin')
        self.add_line('chimney',(20,8),(20,12));self.relate('connect','cabin','chimney')
        path('waves',(4,39),[((14,39),5,1,False),((24,39),5,1,True),((34,39),5,1,False),((44,39),5,1,True)])
