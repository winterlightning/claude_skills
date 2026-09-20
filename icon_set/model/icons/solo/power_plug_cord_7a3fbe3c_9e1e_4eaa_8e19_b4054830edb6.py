'Electrical Power Plug and Cord.\nPlan and review: Retained two-prong plug and deep winding cable. Asymmetric cable follows the source; plug corners are rounded.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide plug: U-shaped plug with two prongs; source winding cable.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a3fbe3c-9e1e-4eaa-8e19-b4054830edb6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/wire_7a3fbe3c-9e1e-4eaa-8e19-b4054830edb6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'power-plug-cord'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('power', 'plug', 'cord')

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

        path('cable',(6,42),[(6,14),((22,14),8,8,True),(22,34),((38,34),8,8,False),(38,28)])
        path('plug',(30,18),[(42,18),(42,24),((30,24),6,4,True),(30,18)],True)
        self.add_line('prong-left',(32,10),(32,18));self.add_line('prong-right',(40,10),(40,18))
        for s in ('prong-left','prong-right','cable'):self.relate('connect','plug',s)
