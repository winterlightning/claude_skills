'Two jagged car halves and impact burst; wheels integrated as broad semicircular lower contours. Source supplies the broken-car scene; Lucide bus supplies sparse wheel construction. Burst is a physical impact in the scene, not an independent corner modifier. Deliberate mirrored halves use shared x24 axis.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '757187c1-fd16-4577-8bb6-b25ad4df2330'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car explode_757187c1-fd16-4577-8bb6-b25ad4df2330.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-broken-beneath-impact-burst'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Head-on Vehicle Collision Impact',)
    keywords = ('head', 'on', 'vehicle', 'collision', 'impact')
    def build(self):


        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        poly('burst',(12,18),(8,10),(18,14),(24,8),(29,14),(39,10),(36,18))
        for side in (-1,1):
            x=lambda a:24+side*a
            path(f'car{side}',(x(20),30),[(x(17),26),(x(10),26),(x(6),30),(x(10),33),(x(6),36),(x(10),36),((x(18),36),4,4,side<0),(x(20),36),(x(20),30)],True)
