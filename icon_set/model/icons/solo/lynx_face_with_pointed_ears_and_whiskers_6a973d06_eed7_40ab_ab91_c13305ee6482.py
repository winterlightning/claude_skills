'Frontal lynx with pointed ears, angular nose and whiskers. Omit small eyes and extra whisker repetitions to keep the feline face readable.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a973d06-eed7-40ab-ab91-c13305ee6482'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/lynx_6a973d06-eed7-40ab-ab91-c13305ee6482.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lynx-face-with-pointed-ears-and-whiskers'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        bez('face',(6,25),((6,16),(13,12),(20,12)),((22,12),(26,12),(28,12)),((35,12),(42,16),(42,25)),((42,36),(34,42),(24,42)),((14,42),(6,36),(6,25)))
        poly('ear-left',(6,25),(6,6),(20,12));poly('ear-right',(42,25),(42,6),(28,12));join('ear-left','face');join('ear-right','face')
        poly('nose',(18,22),(24,29),(30,22));line('mouth',(24,29),(24,33));join('mouth','nose')
        for side in (-1,1):line(f'whisker{side}',(24+side*10,31),(24+side*18,33));join(f'whisker{side}','face')
