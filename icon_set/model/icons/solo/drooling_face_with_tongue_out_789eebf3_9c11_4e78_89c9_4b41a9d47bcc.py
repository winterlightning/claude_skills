'Drooling Face with Tongue Out.\nPlan and review: Retained round face, closed eyes, smile and hanging tongue. Opened the mouth at the tongue to avoid a trapped tiny pocket; tongue is an open U continuous with the smile.\nKeyshape: CIRCLE, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide smile: circular outline and curved mouth; source closed eyes and tongue retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '789eebf3-9c11-4e78-89c9-4b41a9d47bcc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face drooling_789eebf3-9c11-4e78-89c9-4b41a9d47bcc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'drooling-face-with-tongue-out'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('drooling', 'face', 'with', 'tongue', 'out')

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

        circle('head',24,24,20)
        for j,x in enumerate((17,31)):self.add_arc(f'eye-{j}',(x-2,17),(x+2,17),radius_x=2,radius_y=2,sweep=False)
        curve('smile-left',(15,28),((16,29),(18,30),(21,30)))
        path('tongue',(21,30),[(21,31),((29,31),4,4,False),(29,30)])
        curve('smile-right',(29,30),((31,30),(32,29),(33,28)))
        self.add_contour('mouth','smile-left','tongue-0','tongue-1','tongue-2','smile-right')
        self.contours=[c for c in self.contours if c.contour_id!='tongue']
