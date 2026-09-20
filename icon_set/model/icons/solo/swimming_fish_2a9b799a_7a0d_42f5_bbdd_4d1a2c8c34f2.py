'Simple Swimming Fish.\nPlan and review: Retained right-facing fish, forked tail and both projecting fins. Integrated fins into silhouette; omitted tiny eye and gill seam for clear interior space.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide fish: forked tail, broad body, fins and gill; source right-facing orientation.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a9b799a-7a0d-42f5-bbdd-4d1a2c8c34f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/sturgeon_2a9b799a-7a0d-42f5-bbdd-4d1a2c8c34f2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'swimming-fish'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('swimming', 'fish')

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

        curve('fish',(44,24),((40,18),(36,16),(32,16)),((30,14),(26,10),(24,8)),((23,10),(22,14),(22,17)),((18,18),(16,19),(14,20)),((10,16),(6,14),(4,14)),((4,18),(8,22),(8,24)),((8,26),(4,30),(4,34)),((6,34),(10,32),(14,28)),((16,29),(18,30),(22,31)),((21,34),(20,38),(20,40)),((24,38),(28,34),(30,32)),((36,32),(40,30),(44,24)))
