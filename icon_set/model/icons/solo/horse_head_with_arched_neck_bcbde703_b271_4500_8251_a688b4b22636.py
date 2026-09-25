'Left-facing horse silhouette with pointed ear, muzzle and arched neck. Deliberate directional asymmetry, no useful exact Lucide match.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bcbde703-b271-4500-8251-a688b4b22636'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mare_bcbde703-b271-4500-8251-a688b4b22636.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horse-head-with-arched-neck'
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

        bez('silhouette',(24,44),((28,34),(26,31),(26,28)),((23,28),(19,32),(16,32)),((12,32),(8,30),(8,26)),((8,24),(15,17),(20,10)),((20,8),(19,6),(18,4)),((22,4),(25,7),(26,10)),((35,11),(40,24),(40,36)))
        bez('jaw',(26,28),((28,28),(29,26),(29,24)))
        join('silhouette','jaw')
