'Cylindrical Hockey Puck.\nPlan and review: Retained elliptical top and cylindrical sidewall. Increased sidewall depth to preserve clearance.\nKeyshape: HRECT_M, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide cylinder: elliptical top and curved base joined at side extrema.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3ed6f9c-ff99-46e2-8edb-cef7cdc6eae5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hockey puck_a3ed6f9c-ff99-46e2-8edb-cef7cdc6eae5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cylindrical-hockey-puck'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cylindrical', 'hockey', 'puck')

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

        path('top',(4,18),[((44,18),20,8,True),((4,18),20,8,True)],True)
        path('side',(4,18),[(4,30),((44,30),20,8,False),(44,18)]);self.relate('connect','top','side')
