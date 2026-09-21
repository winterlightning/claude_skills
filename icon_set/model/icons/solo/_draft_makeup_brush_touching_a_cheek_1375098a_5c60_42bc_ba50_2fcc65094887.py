'Partial facial profile beside a diagonal makeup brush. human_ref vocabulary informs minimal facial contour; Lucide paintbrush informs brush ferrule and coherent bristles.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1375098a-5c60-42bc-ba50-2fcc65094887'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/beauty massage spread_1375098a-5c60-42bc-ba50-2fcc65094887.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'makeup-brush-touching-a-cheek'
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

        bez('face',(14,6),((18,12),(13,14),(8,14)),((6,14),(6,16),(6,18)))
        bez('mouth',(6,28),((8,26),(10,26),(12,28)),((10,30),(8,32),(6,32)))
        bez('jaw',(6,42),((14,42),(22,42),(26,38)),((30,34),(30,32),(30,30)))
        poly('brush',(26,16),(36,6),(42,12),(36,22),(26,16));poly('bristles',(26,16),(22,24),(30,30),(36,22));join('brush','bristles');join('jaw','bristles')
