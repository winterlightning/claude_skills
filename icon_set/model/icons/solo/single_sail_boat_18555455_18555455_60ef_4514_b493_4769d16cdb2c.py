'Simple Small Sailboat.\nPlan and review: Retained single bowed sail to right of mast and deep curved hull with raised ends.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide ship: shared mast and hull; source single right sail retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18555455-60ef-4514-b493-4769d16cdb2c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/ketch_18555455-60ef-4514-b493-4769d16cdb2c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-sail-boat-18555455'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('single', 'sail', 'boat', '18555455')

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

        path('hull',(6,30),[(14,32),(34,32),(42,30),((32,42),10,12,True),(16,42),((6,30),10,12,True)],True)
        self.add_polyline('mast',(22,6),(22,22),(22,32));self.relate('connect','mast','hull')
        curve('sail',(22,6),((28,6),(38,12),(38,22)),((32,22),(28,22),(22,22)));self.relate('connect','sail','mast')
