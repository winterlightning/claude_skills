'Eye Dropper and Liquid Drop.\nPlan and review: Retained diagonal pipette, rounded bulb, collar and detached droplet. Interpreted the droplet as emitted liquid within the natural scene; no independent state modifier. Preserved diagonal asymmetry.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cb9bb5f-6477-4aca-840d-2955c8f966eb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/eye dropper_0cb9bb5f-6477-4aca-840d-2955c8f966eb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-dropper-with-droplet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('diagonal', 'dropper', 'with', 'droplet')

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

        path('pipette',(6,34),[(28,12),(36,20),(14,42),(6,42),(6,34)],True)
        curve('bulb',(28,12),((30,8),(32,6),(36,6)),((42,6),(44,14),(36,20)))
        self.relate('connect','bulb','pipette')
        self.add_line('collar-left',(24,8),(28,12));self.add_line('collar-right',(36,20),(40,24))
        for s in ('collar-left','collar-right'):self.relate('connect',s,'pipette');self.relate('connect',s,'bulb')
        path('drop',(38,32),[((42,38),4,6,True),((34,38),4,4,True),((38,32),4,6,True)],True)
