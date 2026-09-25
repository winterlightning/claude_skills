'Close left face with nose, lips, chin, ear and short neck. No full skull is invented; flowing anatomical contours.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6f5a36d-d963-47a3-bbf8-3d73f4db6df2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cheek_a6f5a36d-d963-47a3-bbf8-3d73f4db6df2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'close-side-view-face'
    keyshape = Keyshape.VRECT_L
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

        bez('face',(18,4),((18,11),(8,17),(8,20)),((8,23),(13,22),(14,24)),((11,29),(15,29),(14,33)),((13,39),(19,40),(25,40)),((30,40),(35,36),(36,32)))
        bez('ear',(30,14),((30,4),(40,4),(40,14)),((40,21),(36,23),(32,23)))
        line('neck',(25,40),(28,44));join('neck','face')
