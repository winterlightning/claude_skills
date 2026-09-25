"""domed-observatory.
Plan: Domed observatory building with a diagonal telescope barrel connected at two dome outline nodes; retain curved roof and architectural base.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: Lucide telescope: a simple diagonal optical barrel.
Omissions: Narrow raised rim band reduced to the building roof line.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'af83b2d3-a6c8-48f0-bf59-777e2e438dbf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/observatory_af83b2d3-a6c8-48f0-bf59-777e2e438dbf.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'domed-observatory'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('observatory',)

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

        curve('dome',(6,30),((6,20),(12,14),(22,14)),((24,14),(26,15),(28,16)),((30,17),(32,20),(34,22)),((37,25),(38,27),(38,30)))
        self.add_polyline('telescope',(28,16),(36,6),(42,12),(34,22));self.relate('connect','telescope','dome')
        box('building',6,30,38,42,1);self.relate('connect','building','dome')
