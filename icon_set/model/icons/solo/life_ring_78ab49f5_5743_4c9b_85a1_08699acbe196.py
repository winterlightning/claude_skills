'Safety Lifebuoy Ring.\nPlan and review: Retained both circular ring edges and all four diagonal band cues. Reduced doubled strap boundaries to single radial connectors.\nKeyshape: CIRCLE, exact SOLO48 envelope.\nConstruction reference: Lucide life-buoy: circular ring and four radial band cues.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78ab49f5-5743-4c9b-85a1-08699acbe196'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/life ring_78ab49f5-5743-4c9b-85a1-08699acbe196.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'life-ring'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('life', 'ring')

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

        circle('outer',24,24,20);circle('inner',24,24,10)
        for j,(a,b) in enumerate((((12,8),(18,16)),((36,8),(30,16)),((12,40),(18,32)),((36,40),(30,32)))):
         self.add_line(f'band-{j}',a,b);self.relate('connect',f'band-{j}','outer');self.relate('connect',f'band-{j}','inner')
