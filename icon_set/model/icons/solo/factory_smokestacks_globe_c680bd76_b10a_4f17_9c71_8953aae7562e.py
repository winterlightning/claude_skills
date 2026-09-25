'Factory Smokestacks on Planet Earth.\nPlan and review: Retained two industrial stacks, smoke curls and globe horizon. Omitted globe land mark and chimney bands. Classified as one environmental scene, not a status/action combination.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c680bd76-b10a-4f17-9c71-8953aae7562e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/air pollution 1_c680bd76-b10a-4f17-9c71-8953aae7562e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'factory-smokestacks-globe'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('factory', 'smokestacks', 'globe')

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

        path('globe',(8,44),[((40,44),16,16,True)])
        path('chimney-left',(10,36),[(12,16),(20,16),(22,28)])
        path('chimney-right',(32,30),[(32,20),(40,20),(40,44)])
        self.relate('connect','globe','chimney-left');self.relate('connect','globe','chimney-right')
        curve('smoke-left',(14,8),((12,4),(18,4),(20,4)))
        curve('smoke-right',(32,12),((28,8),(34,4),(38,4)))
