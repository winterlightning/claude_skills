'Pear-shaped bladder with two upper ureters and lower outlet. Preserve physical tubing, not a symbol combination.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa2f0590-bd03-4d41-8846-978c972a01fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bladder_aa2f0590-bd03-4d41-8846-978c972a01fe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bladder-with-connecting-tubes'
    keyshape = Keyshape.VRECT_L
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

        bez('bladder',(19,44),((19,37),(20,34),(16,31)),((4,23),(12,12),(24,12)),((36,12),(44,23),(32,31)),((28,34),(29,37),(29,44)))
        bez('tube-left',(14,17),((8,15),(8,9),(8,4)))
        bez('tube-right',(34,17),((40,15),(40,9),(40,4)))
        join('bladder','tube-left');join('bladder','tube-right')
