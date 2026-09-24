"""Plain task list with two repeated open square checkboxes and paired short text strokes. Shared box size and row pitch retain a regular series."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cbffa972-bda1-56ed-9c77-cf75b93eefd1'
SOURCE_PATH = 'pictographic-primitives/work/task list plain_cbffa972-bda1-56ed-9c77-cf75b93eefd1.svg'
AUTHOR = 'gpt-6'
PLAN = 'Plain task list with two repeated open square checkboxes and paired short text strokes. Shared box size and row pitch retain a regular series.'
OMISSIONS = ['Third checkbox row omitted to fit 8-unit checkbox openings; text strokes reduced to dots within the remaining width.']
class Drawing(Solo48):
    icon_id = 'task-list-plain'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('task', 'list', 'plain')
    def build(self):
        self.add_polyline('page',(8,4),(40,4),(40,44),(8,44),closed=True)
        for i,y in enumerate((12,28)):
            self.add_polyline(f'check-{i}',(16,y),(24,y),(24,y+8),(16,y+8),closed=True)
            self.add_line(f'text-{i}',(32,y+4),(32,y+4))


    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]; p=n+str(i)
            if i%2:self.add_arc(p,a,z,radius_x=rad)
            else:self.add_line(p,a,z)
            members.append(p)
        self.add_contour(n,*members,closed=True)
