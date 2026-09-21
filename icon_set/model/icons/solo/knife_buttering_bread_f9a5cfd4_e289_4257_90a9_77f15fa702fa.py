'A broad round-tipped butter knife lies diagonally across a slice of bread. SQUARE preserves the toast silhouette and diagonal handle. One bread contour owns the scene; the blade has a rounded curved back, straight cutting edge and attached handle. Source supplies bread and the spreading gesture. No useful direct Lucide toast-and-knife match was found. Widen the blade for readable negative space and omit the separate butter dab after left and central placements crowded the base or blade. The lower-right bread edge is physically behind the knife. No source metadata or original reference artwork changed.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9a5cfd4-e289-4257-90a9-77f15fa702fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bread slice spread_f9a5cfd4-e289-4257-90a9-77f15fa702fa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'knife-buttering-bread'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Knife Spreading Butter on Toast',)
    keywords = ('knife', 'spreading', 'butter', 'on', 'toast')
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

        bez('bread-top',(8,25),((6,24),(6,22),(6,18)),((6,10),(9,6),(16,6)),((21,6),(27,6),(32,6)),((42,6),(44,23),(36,25)))
        line('bread-right',(36,25),(38,42))
        line('bread-bottom',(38,42),(6,42))
        line('bread-left',(6,42),(8,25))
        self.add_contour('bread','bread-top','bread-right','bread-bottom','bread-left',closed=True)
        bez('knife-back',(22,14),((16,10),(12,20),(16,26)),((20,32),(25,33),(32,30)))
        line('knife-edge',(32,30),(22,14))
        self.add_contour('knife','knife-back','knife-edge',closed=True)
        line('handle',(32,30),(42,42));join('knife','handle')

