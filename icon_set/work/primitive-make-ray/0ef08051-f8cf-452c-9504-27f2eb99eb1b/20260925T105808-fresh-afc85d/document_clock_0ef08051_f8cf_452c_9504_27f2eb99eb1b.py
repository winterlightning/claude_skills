"""Clipped document containing a circular clock with short detached right-angle hands."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0ef08051-f8cf-452c-9504-27f2eb99eb1b'
SOURCE_PATH='pictographic-primitives/other/file clock_0ef08051-f8cf-452c-9504-27f2eb99eb1b.svg'
AUTHOR='gpt-6'
PLAN='Detached L-shaped hands restore the clock instead of the previous pie-slice appearance. Readable 4-unit hands leave only 2 ink units to the radius-10 ring. Smaller one-unit hands passed but read as a dot and were rejected visually.'
CONSTRUCTION_REFERENCE='file-code original and atomic-debug: clipped file contour. file-clock original inspected; its external overlay arrangement was not substituted for the supplied internal clock.'
OMISSIONS='Rounded paper corner arcs simplified to round stroke joins; clock, hands, and clipped corner retained.'

class Drawing(Solo48):
    icon_id='document-clock'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('file', 'clock')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,start,commands,closed=False):
        ids=[];here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid);here=end
        self.add_contour(n,*ids,closed=closed)

    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def file(self,l=8,t=4,r=40,b=44):
        self.path('page',(l+4,t),[('L',(r-10,t)),('L',(r,t+10)),('L',(r,b-4)),('A',(r-4,b),4,4,True),('L',(l+4,b)),('A',(l,b-4),4,4,True),('L',(l,t+4)),('A',(l+4,t),4,4,True)],True)

    def build(self):
        self.add_polyline('page',(6,6),(32,6),(42,16),(42,42),(6,42),closed=True)
        self.circle('clock',24,24,10)
        self.add_polyline('hands',(24,20),(24,24),(28,24))
