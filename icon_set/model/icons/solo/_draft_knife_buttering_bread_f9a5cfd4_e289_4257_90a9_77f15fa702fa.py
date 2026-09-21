'Knife spreading butter over bread is one physical scene. Preserve bread silhouette, spread patch and diagonal blade.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9a5cfd4-e289-4257-90a9-77f15fa702fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bread slice spread_f9a5cfd4-e289-4257-90a9-77f15fa702fa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'knife-buttering-bread'
    keyshape = Keyshape.SQUARE
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

        bez('bread',(12,25),((6,24),(6,22),(6,18)),((6,10),(9,6),(16,6)),((21,6),(27,6),(32,6)),((42,6),(44,23),(36,25)))
        poly('base',(12,25),(10,42),(38,42),(36,25));join('bread','base')
        bez('knife',(18,14),((15,22),(23,31),(30,30)),((29,25),(23,17),(18,14)))
        line('handle',(30,30),(42,42));join('knife','handle')
        bez('spread',(18,32),((16,34),(16,34),(18,34)))
