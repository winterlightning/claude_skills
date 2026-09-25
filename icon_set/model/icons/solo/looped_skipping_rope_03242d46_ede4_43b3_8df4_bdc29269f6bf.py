'Fitness Jump Rope.\nPlan and review: Retained jump rope with two rounded handles and broad rope arch. Removed the central crossed loop because it created two trapped tiny pockets. The handles and connecting rope preserve the fitness subject.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03242d46-ede4-43b3-8df4-bdc29269f6bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/jumping rope 3_03242d46-ede4-43b3-8df4-bdc29269f6bf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'looped-skipping-rope'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ()
    keywords = ('looped', 'skipping', 'rope')

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

        box('handle-left',8,30,16,44,3);box('handle-right',32,30,40,44,3)
        curve('rope',(12,30),((12,12),(12,4),(24,4)),((36,4),(36,12),(36,30)))
        self.relate('connect','rope','handle-left');self.relate('connect','rope','handle-right')
