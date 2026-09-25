'Asymmetric nose with extended left bridge, rounded tip and shorter right nostril. Preserve original asymmetry.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7613627-bdaa-4c01-b2cf-4e57115e6ce0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nose_e7613627-bdaa-4c01-b2cf-4e57115e6ce0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'asymmetric-nose-outline'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
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

        bez('left',(22,6),((22,22),(6,24),(6,32)),((6,38),(9,39),(12,39)))
        bez('right',(36,28),((40,29),(42,32),(42,35)),((42,38),(39,39),(36,39)))
        bez('tip',(12,39),((17,35),(17,42),(24,42)),((31,42),(31,35),(36,39)))
        join('left','tip');join('right','tip')
