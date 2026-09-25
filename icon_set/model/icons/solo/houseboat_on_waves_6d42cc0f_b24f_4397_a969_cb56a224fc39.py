'Floating Houseboat on Water.\nPlan and review: Retained pitched-roof house on broad boat hull. Omitted small doorway and waterlines to keep the houseboat structure readable.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d42cc0f-b24f-4397-a969-cb56a224fc39'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/houseboat_6d42cc0f-b24f-4397-a969-cb56a224fc39.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'houseboat-on-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('houseboat', 'on', 'waves')

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

        path('roof',(8,22),[(24,8),(40,22)])
        self.add_line('wall-left',(12,19),(12,30));self.add_line('wall-right',(36,19),(36,30))
        path('hull',(4,30),[(12,30),(36,30),(44,30),(36,40),(12,40),(4,30)],True)
        for s in ('wall-left','wall-right'):self.relate('connect','roof',s);self.relate('connect','hull',s)
