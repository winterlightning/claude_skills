"""diagonal-open-end-spanner.
Plan: Open-end wrench with a wide square jaw, rounded head and a smooth broad grip; diagonal construction preserves the reference.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: Lucide wrench: broad head, open jaw and rounded grip.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '41bd81cf-2446-4283-b6f3-90c7dde89ad1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-open-end-spanner/20260924T105711Z-thuan-mac/reference/socket wrench_41bd81cf-2446-4283-b6f3-90c7dde89ad1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'diagonal-open-end-spanner'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('socket', 'wrench')

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        self.add_line('jaw-1',(32,6),(24,14))
        self.add_line('jaw-2',(24,14),(32,22))
        self.add_line('jaw-3',(32,22),(42,12))
        curve('head-right',(42,12),((42,24),(40,30),(30,28)))
        self.add_line('grip-right',(30,28),(14,42))
        curve('grip-end',(14,42),((10,42),(6,42),(6,36)),((6,34),(7,33),(9,31)))
        self.add_line('grip-left',(9,31),(18,22))
        curve('head-left',(18,22),((14,12),(22,6),(32,6)))
        self.add_contour('outline','jaw-1','jaw-2','jaw-3','head-right','grip-right','grip-end','grip-left','head-left',closed=True)
