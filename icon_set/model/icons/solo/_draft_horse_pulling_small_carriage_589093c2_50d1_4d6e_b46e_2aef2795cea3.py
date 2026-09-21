'Natural horse-and-carriage scene, not a modifier combination. Reduce spokes but retain horse neck, legs, seat and wheel; no useful exact Lucide match.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_M uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '589093c2-50d1-4d6e-b46e-2aef2795cea3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/carriage_589093c2-50d1-4d6e-b46e-2aef2795cea3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horse-pulling-small-carriage'
    keyshape = Keyshape.HRECT_M
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        poly('horse',(4,20),(8,10),(16,18),(20,18),(20,28),(16,38))
        poly('foreleg',(12,22),(12,30),(8,38))
        line('back',(12,30),(19,30));join('back','foreleg')
        path('seat',(28,22),[(28,14),((32,10),4,4,True),(40,10),(40,22)])
        path('wheel',(36,22),[((36,38),8,8,True),((36,22),8,8,True)],True)
        line('shaft',(20,22),(36,22));join('shaft','horse');join('shaft','seat');join('shaft','wheel')
