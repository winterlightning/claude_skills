'Two window slots over centered doorway; mirrored about x=24. Window holes reduced to slots to preserve doorway clearance. Lucide house informs gabled enclosure.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '947154d2-ba94-40d8-86da-58585ad61c10'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/proprietor_947154d2-ba94-40d8-86da-58585ad61c10.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'gabled-house-paired-windows'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ("House with Windows and Door",)
    keywords = ("house", "home", "roof", "windows", "door", "building")
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

        poly('shell',(4,18),(24,8),(44,18),(44,40),(28,40),(20,40),(4,40),(4,18))
        line('left-window',(14,24),(18,24));line('right-window',(30,24),(34,24))
        poly('door',(20,40),(20,32),(28,32),(28,40))
        join('door-1','shell-5','shell-6');join('door-3','shell-4','shell-5')
