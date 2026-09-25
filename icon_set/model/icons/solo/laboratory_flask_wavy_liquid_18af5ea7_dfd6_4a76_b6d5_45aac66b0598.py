'Erlenmeyer Flask with Liquid.\nPlan and review: Retained projecting lip, narrow neck, conical flask and wavy liquid level. Liquid line joins both vessel sides.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide flask-conical: neck, sloping sides and shared liquid line.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18af5ea7-dfd6-4a76-b6d5-45aac66b0598'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/laboratory_18af5ea7-dfd6-4a76-b6d5-45aac66b0598.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'laboratory-flask-wavy-liquid'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('laboratory', 'flask', 'wavy', 'liquid')

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

        self.add_polyline('lip',(16,4),(20,4),(28,4),(32,4))
        path('flask',(20,4),[(20,16),(14,28),(8,40),((12,44),4,4,False),(36,44),((40,40),4,4,False),(34,28),(28,16),(28,4)])
        self.relate('connect','lip','flask')
        curve('liquid',(14,28),((20,24),(28,32),(34,28)));self.relate('connect','liquid','flask')
