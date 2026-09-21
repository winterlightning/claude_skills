'Whole diagonal lemon with pointed tip and single plain leaf. No invented vein or extra fruit.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ce6dd5a-e886-4158-9462-4ec687e19a2f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/citron_2ce6dd5a-e886-4158-9462-4ec687e19a2f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'whole-lemon-with-single-leaf'
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

        bez('lemon',(8,40),((6,36),(6,30),(6,26)),((6,16),(17,8),(26,8)),((36,8),(40,17),(40,25)),((40,35),(29,42),(20,42)),((16,42),(14,40),(10,42)),((6,42),(6,42),(8,40)))
        bez('leaf',(34,10),((34,6),(38,6),(42,6)),((42,12),(39,15),(34,10)));join('leaf','lemon')
