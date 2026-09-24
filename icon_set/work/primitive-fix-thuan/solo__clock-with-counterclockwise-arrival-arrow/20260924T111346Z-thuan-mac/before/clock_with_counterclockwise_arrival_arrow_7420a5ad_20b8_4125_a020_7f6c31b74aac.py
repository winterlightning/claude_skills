'Clock rim is a counterclockwise arrow; intrinsic clock hands retained.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape CIRCLE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7420a5ad-20b8-4125-a020-7f6c31b74aac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shipping logistic estimate time arrival 1_7420a5ad-20b8-4125-a020-7f6c31b74aac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clock-with-counterclockwise-arrival-arrow'
    keyshape = Keyshape.HRECT_L
    category = "objects"
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

        path('arrow',(28,8),[((44,24),16,16,True),((28,40),16,16,True),((12,24),16,16,True)])
        poly('head',(4,32),(12,24),(20,32));join('arrow','head')
        poly('hands',(28,17),(28,27),(34,27))
