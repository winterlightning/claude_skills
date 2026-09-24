"""Clipped-corner document containing a clock.
Plan: Nine-unit margin around the clock. Larger clock hands read clearly; the real dial attachment is declared.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e7ce785e-158f-41d6-9e8b-dcba4879acac'
SOURCE_PATH = 'pictographic-primitives/interface-essential/time clock file 1_e7ce785e-158f-41d6-9e8b-dcba4879acac.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'time-clock-file-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('time', 'clock', 'file', '1')
    def build(self):
        self.add_polyline('file',(6,6),(32,6),(42,16),(42,42),(6,42),closed=True)
        self.add_arc('clock-1',(15,24),(24,15),radius_x=9)
        self.add_arc('clock-2',(24,15),(33,24),radius_x=9)
        self.add_arc('clock-3',(33,24),(24,33),radius_x=9)
        self.add_arc('clock-4',(24,33),(15,24),radius_x=9)
        self.add_contour('clock','clock-1','clock-2','clock-3','clock-4',closed=True)
        # Minute hand joins the dial at its 12 o'clock endpoint.
        self.add_polyline('hands',(24,15),(24,24),(28,27))
        self.relate('connect','clock','hands')


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

PLAN = 'Clipped-corner document containing a clock. Nine-unit margin around the clock.'
OMISSIONS = 'Minute hand joins the dial at the real 12 o’clock endpoint.'
CONSTRUCTION_REFERENCES = ['icon_set/references/lucide/original/file-clock.svg', 'icon_set/references/lucide/atomic-debug/file-clock.svg']
PARENT_SOURCE = 'icon_set/model/icons/solo/time_clock_file_1_e7ce785e_158f_41d6_9e8b_dcba4879acac.py'
