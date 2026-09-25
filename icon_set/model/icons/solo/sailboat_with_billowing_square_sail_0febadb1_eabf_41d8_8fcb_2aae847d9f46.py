'Sailing Boat with Single Sail.\nPlan and review: Retained broad curved hull, central mast and billowing sail. Omitted doubled hull rim and increased sail-to-hull clearance.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0febadb1-eabf-41d8-8fcb-2aae847d9f46'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/galley_0febadb1-eabf-41d8-8fcb-2aae847d9f46.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sailboat-with-billowing-square-sail'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('sailboat', 'with', 'billowing', 'square', 'sail')

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

        path('hull',(4,32),[((44,32),20,8,False),(4,32)],True)
        self.add_line('mast',(24,24),(24,32));self.relate('connect','mast','hull')
        curve('sail',(14,8),((18,14),(18,18),(14,24)),((20,24),(26,24),(32,24)),((40,24),(40,8),(32,8)),((26,8),(20,8),(14,8)))
        self.relate('connect','sail','mast')
