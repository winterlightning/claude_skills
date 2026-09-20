'Dizzy Grimacing Face.\nPlan and review: Retained both crossed eyes and wide mouth with two tooth dividers; no enclosing head added.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1a8b3ec-bca2-435d-8314-8cbee6ce9bd8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face grimace_b1a8b3ec-bca2-435d-8314-8cbee6ce9bd8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dizzy-grimacing-face'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('dizzy', 'grimacing', 'face')

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

        for j,x in enumerate((12,36)):
         self.add_polyline(f'cross-a-{j}',(x-4,8),(x,12),(x+4,16))
         self.add_polyline(f'cross-b-{j}',(x-4,16),(x,12),(x+4,8))
         self.relate('connect',f'cross-a-{j}',f'cross-b-{j}')
        path('mouth',(12,28),[(20,28),(28,28),(36,28),((44,34),8,6,True),((36,40),8,6,True),(28,40),(20,40),(12,40),((4,34),8,6,True),((12,28),8,6,True)],True)
        for j,x in enumerate((20,28)):
         self.add_line(f'tooth-{j}',(x,28),(x,40));self.relate('connect',f'tooth-{j}','mouth')
