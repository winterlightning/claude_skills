'Triangular martini glass with stem, foot, olive and diagonal pick. Lucide martini informs the glass silhouette; retain the separate olive cue.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96c9812c-13cb-4856-884d-c1360a6bd316'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/appetizer_96c9812c-13cb-4856-884d-c1360a6bd316.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'martini-glass-with-skewered-olive'
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

        poly('bowl',(6,12),(24,32),(42,12),(6,12));line('stem',(24,32),(24,42));line('foot',(14,42),(34,42));join('bowl','stem');join('stem','foot')
        circle('olive',24,21,3);line('pick',(18,27),(36,6));join('pick','olive');join('pick','bowl')
