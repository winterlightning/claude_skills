'Frontal nose with rounded bridge and paired nostrils around low central tip. Shared bilateral parameters guide contour balance.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e13c726-4e08-47a0-912a-4b28505eb789'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nasal_6e13c726-4e08-47a0-912a-4b28505eb789.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'frontal-rounded-nose'
    keyshape = Keyshape.VRECT_L
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

        bez('nose',(16,42),((8,42),(8,40),(8,36)),((8,32),(9,30),(12,29)),((17,26),(17,18),(18,10)),((18,2),(30,2),(30,10)),((31,18),(31,26),(36,29)),((39,30),(40,32),(40,36)),((40,40),(40,42),(32,42)))
        bez('nostrils',(16,42),((16,34),(20,44),(24,44)),((28,44),(32,34),(32,42)))
        join('nose','nostrils')
