'Coiled Water Hose with Nozzle.\nPlan and review: Retained coil and flared nozzle; reduced two hose walls to a coherent single spiral stroke.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc92dec5-22d0-4f56-9dd6-0810621f7885'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hose_bc92dec5-22d0-4f56-9dd6-0810621f7885.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'coiled-water-hose-with-nozzle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('coiled', 'water', 'hose', 'with', 'nozzle')

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

        path('hose',(34,12),[(18,12),((4,26),14,14,False),((18,40),14,14,False),(24,40),((36,28),12,12,False),((24,20),12,8,False),(18,20),((18,32),6,6,False),(24,32)])
        path('nozzle',(34,12),[(44,8),(44,20),(34,12)],True)
        self.relate('connect','hose','nozzle')
