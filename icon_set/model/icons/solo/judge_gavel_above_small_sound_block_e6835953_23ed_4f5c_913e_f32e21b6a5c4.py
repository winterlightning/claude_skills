'Diagonal gavel with separate sounding block; one natural tool-and-support subject. Head caps retained as contour boundaries.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6835953-23ed-4f5c-913e-f32e21b6a5c4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mallet_e6835953-23ed-4f5c-913e-f32e21b6a5c4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'judge-gavel-above-small-sound-block'
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

        poly('head',(18,18),(30,6),(42,18),(30,30),(18,18))
        bez('handle',(22,22),((16,27),(6,33),(6,37)),((6,40),(8,42),(11,42)),((14,42),(23,31),(28,28)))
        join('handle','head')
        line('block',(30,42),(42,42))
