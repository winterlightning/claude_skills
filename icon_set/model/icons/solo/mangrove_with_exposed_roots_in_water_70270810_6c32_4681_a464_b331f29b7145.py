'Mangrove with lobed crown, trunk, branches, exposed roots and water. Lucide tree informs crown; reduce water to one coherent wave row.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70270810-6c32-4681-a464-b331f29b7145'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mangrove_70270810-6c32-4681-a464-b331f29b7145.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mangrove-with-exposed-roots-in-water'
    keyshape = Keyshape.SQUARE
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

        path('crown',(14,26),[(((14,10)),8,8,True),((34,10),10,4,True),((34,26),8,8,True),(24,26),(14,26)],True)
        line('trunk',(24,26),(24,40));join('crown','trunk')
        bez('root-left',(24,26),((16,26),(8,32),(12,40)));bez('root-right',(24,26),((32,26),(40,32),(36,40)));join('root-left','trunk');join('root-right','trunk');join('root-left','crown');join('root-right','crown')
        path('water',(6,40),[((12,40),3,2,False),((18,40),3,2,True),((24,40),3,2,False),((30,40),3,2,True),((36,40),3,2,False),((42,40),3,2,True)])
        join('water','trunk');join('water','root-left');join('water','root-right')
