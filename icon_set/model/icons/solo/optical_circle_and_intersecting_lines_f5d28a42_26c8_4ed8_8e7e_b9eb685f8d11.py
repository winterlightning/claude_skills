'Scientific Optical Interferometer Symbol.\nPlan and review: Retained circle, two vertical lines and rising diagonal ray. Moved the intersecting line toward the circle center and opened the ray angle to eliminate narrow sectors. Scientific roles remain unspecified; no invented component meaning.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5d28a42-26c8-4ed8-8e7e-b9eb685f8d11'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/interferometer_f5d28a42-26c8-4ed8-8e7e-b9eb685f8d11.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'optical-circle-and-intersecting-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('optical', 'circle', 'and', 'intersecting', 'lines')

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

        circle('circle',28,24,12)
        self.add_line('line-left',(6,6),(6,42));self.add_polyline('line-middle',(28,6),(28,24),(28,42))
        self.add_line('ray',(28,24),(42,18));self.relate('connect','line-middle','ray');self.relate('connect','circle','ray');self.relate('connect','circle','line-middle')
