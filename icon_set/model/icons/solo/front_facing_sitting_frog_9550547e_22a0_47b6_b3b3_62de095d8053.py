'Simple Sitting Frog.\nPlan and review: Retained broad frog head with two eye bumps, torso, splayed haunches and two front legs. Omitted repeated toes; replaced near-miss haunch joins with shared points.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: No useful exact Lucide match; source silhouette and geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9550547e-22a0-47b6-b3b3-62de095d8053'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/frog_9550547e-22a0-47b6-b3b3-62de095d8053.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-facing-sitting-frog'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('front', 'facing', 'sitting', 'frog')

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

        path('head',(12,22),[((12,12),7,7,True),((22,12),5,6,True),(26,12),((36,12),5,6,True),((36,22),7,7,True),((12,22),12,4,True)],True)
        curve('left-body',(14,24),((12,28),(12,32),(14,34)),((16,38),(16,40),(18,42)))
        curve('right-body',(34,24),((36,28),(36,32),(34,34)),((32,38),(32,40),(30,42)))
        for s in ('left-body','right-body'):self.relate('connect','head',s)
        curve('left-haunch',(14,34),((6,30),(6,36),(6,38)),((6,42),(12,42),(18,42)))
        curve('right-haunch',(34,34),((42,30),(42,36),(42,38)),((42,42),(36,42),(30,42)))
        self.relate('connect','left-body','left-haunch');self.relate('connect','right-body','right-haunch')
        path('front-legs',(18,32),[(18,42),(30,42),(30,32)])
        for s in ('left-body','right-body','left-haunch','right-haunch'):self.relate('connect','front-legs',s)
