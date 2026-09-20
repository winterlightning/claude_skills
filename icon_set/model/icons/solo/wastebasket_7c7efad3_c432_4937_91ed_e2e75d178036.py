'Simple Trash Can.\nPlan and review: Retained plain tapered wastebasket and rounded upper rim. No lid or markings added.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: No useful exact Lucide match; source silhouette and geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c7efad3-c432-4937-91ed-e2e75d178036'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/wastebasket_7c7efad3-c432-4937-91ed-e2e75d178036.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wastebasket'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('wastebasket',)

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

        box('rim',8,4,40,12,3)
        path('basket',(10,12),[(14,40),((18,44),4,4,False),(30,44),((34,40),4,4,False),(38,12)]);self.relate('connect','rim','basket')
