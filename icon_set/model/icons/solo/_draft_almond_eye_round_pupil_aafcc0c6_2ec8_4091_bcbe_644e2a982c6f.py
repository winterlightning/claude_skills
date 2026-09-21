'Almond eye and circular iris/pupil. Lucide eye informs paired eyelids; source concentric iris distinction retained for inspection.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_M uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aafcc0c6-2ec8-4091-bcbe-644e2a982c6f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/pupil_aafcc0c6-2ec8-4091-bcbe-644e2a982c6f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'almond-eye-round-pupil'
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        bez('lid',(4,24),((10,13),(16,8),(24,8)),((32,8),(38,13),(44,24)),((38,35),(32,40),(24,40)),((16,40),(10,35),(4,24)))
        circle('iris',24,24,8)
        self.add_dot('pupil',(24,24))
