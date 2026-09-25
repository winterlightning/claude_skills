'Scalloped scoop above shallow stemmed bowl. Lucide ice-cream-bowl informs bowl, stem and foot; scalloping remains source-specific.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f17d875-a878-4b45-af5f-0e7c0f02a26b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/sherbet_2f17d875-a878-4b45-af5f-0e7c0f02a26b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'scalloped-ice-cream-in-stemmed-bowl'
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

        bez('scoop',(6,24),((6,19),(9,18),(12,16)),((12,10),(17,6),(24,6)),((31,6),(36,10),(36,16)),((39,18),(42,19),(42,24)))
        bez('scallop',(6,24),((9,26),(15,19),(19,23)),((24,27),(28,20),(33,23)),((37,26),(40,26),(42,24)))
        bez('bowl',(6,24),((6,33),(15,34),(24,34)),((33,34),(42,33),(42,24)))
        line('stem',(24,34),(24,42));line('foot',(14,42),(34,42));join('scoop','bowl');join('scoop','scallop');join('scallop','bowl');join('stem','bowl');join('foot','stem')
