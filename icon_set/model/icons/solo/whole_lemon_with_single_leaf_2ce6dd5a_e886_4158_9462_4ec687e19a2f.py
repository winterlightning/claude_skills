'Whole diagonal lemon with pointed tip and single plain leaf. No invented vein or extra fruit.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. Lucide leaf supplies pointed-loop construction; source supplies whole diagonal fruit and leaf. A short stem separates the loops with real endpoint joins. No vein added.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ce6dd5a-e886-4158-9462-4ec687e19a2f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/citron_2ce6dd5a-e886-4158-9462-4ec687e19a2f.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'whole-lemon-with-single-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ("Lemon with Small Leaf",)
    keywords = ("lemon", "citrus", "fruit", "leaf", "food", "produce", "oval")
    category = "Uncategorized"
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

        bez('lemon',(6,42),((6,38),(6,36),(6,34)),((6,26),(14,20),(22,20)),((32,20),(34,30),(28,36)),((24,40),(18,42),(12,40)),((10,40),(8,42),(6,42)))
        bez('leaf',(32,14),((32,6),(36,6),(42,6)),((42,14),(38,14),(32,14)))
        line('stem',(32,14),(22,20));join('stem','leaf');join('stem','lemon')
