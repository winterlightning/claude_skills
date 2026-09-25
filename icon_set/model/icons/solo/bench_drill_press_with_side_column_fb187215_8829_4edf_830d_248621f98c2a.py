'Bench drill with upper housing, chuck, bit, side column, table and base. Lucide drill informs simple equipment contours; preserve upright drill-press arrangement.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb187215-8829-4edf-830d-248621f98c2a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/drill press_fb187215-8829-4edf-830d-248621f98c2a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bench-drill-press-with-side-column'
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

        box('housing',8,4,40,12,4)
        poly('column',(36,12),(36,44));poly('base',(8,44),(36,44),(40,44));join('housing','column');join('column','base')
        poly('chuck',(12,12),(12,20),(20,20),(20,12));join('chuck','housing')
        line('bit',(16,20),(16,24));join('bit','chuck')
        poly('table',(8,32),(16,32),(24,32));line('table-post',(16,32),(16,44));join('table','table-post');join('table-post','base')
