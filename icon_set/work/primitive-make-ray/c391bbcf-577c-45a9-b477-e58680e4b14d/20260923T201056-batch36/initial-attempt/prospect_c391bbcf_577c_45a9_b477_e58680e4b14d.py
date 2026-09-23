"""A prospective person with a right-pointing arrow.
Symbol plan: Circular head above a rounded bust; a separate arrow points right. Ink extremes (4,4)-(44,44).
Construction: user-round: circular head and broad smooth shoulders; shared human guide governs spacing.
Human construction: human-reference.md and human_ref/user.svg: head center(18,14), radius8; head bottom22 and body top30 give exactly 8 centerline /4 ink units. Bust outline has broad equal-radius shoulders, not stick-figure anatomy.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c391bbcf-577c-45a9-b477-e58680e4b14d'
SOURCE_PATH = 'icon_set/work/todo-references/prospect_c391bbcf-577c-45a9-b477-e58680e4b14d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'prospect'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('prospect',)

    def build(self):
        self.circle('head',18,14,8)
        self.add_arc('shoulder-left',(6,38),(14,30),radius_x=8)
        self.add_line('shoulder-top',(14,30),(22,30))
        self.add_arc('shoulder-right',(22,30),(30,38),radius_x=8)
        self.add_line('body-base-1',(30, 38),(30, 42))
        self.add_line('body-base-2',(30, 42),(6, 42))
        self.add_line('body-base-3',(6, 42),(6, 38))
        self.add_contour('body','shoulder-left','shoulder-top','shoulder-right','body-base-1','body-base-2','body-base-3')
        self.add_polyline('arrow-head',(36,20),(42,26),(36,32))
        self.add_line('arrow-shaft',(34,26),(42,26))
        self.relate('connect','arrow-head','arrow-shaft')

    def circle(self,name,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-upper',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-lower',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-upper',name+'-lower',closed=True)

    def box(self,name,x,y,right,bottom,r=4):
        pts=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if a==b:continue
            n=f'{name}-{i}'
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def opening_quote(self,name,x,closing=False):
        # A shared 15-unit body and 25-unit pitch own both repeated quotation marks.
        def p(v):
            a,b=v
            return (x+15-a,48-b) if closing else (x+a,b)
        def line(n,a,b):self.add_line(name+n,p(a),p(b))
        def arc(n,a,b):self.add_arc(name+n,p(a),p(b),radius_x=4)
        def bez(n,a,*segs):self.add_bezier(name+n,p(a),*[(p(a),p(b),p(c)) for a,b,c in segs])
        bez('-outer',(0,24),((0,16),(5,8),(11,8)))
        arc('-crown',(11,8),(15,12))
        arc('-return',(15,12),(11,16))
        bez('-inner',(11,16),((7,16),(7,20),(7,24)))
        line('-shelf',(7,24),(11,24))
        arc('-tr',(11,24),(15,28))
        line('-right',(15,28),(15,36))
        arc('-br',(15,36),(11,40))
        line('-bottom',(11,40),(4,40))
        arc('-bl',(4,40),(0,36))
        line('-left',(0,36),(0,24))
        self.add_contour(name,*[name+n for n in ('-outer','-crown','-return','-inner','-shelf','-tr','-right','-br','-bottom','-bl','-left')],closed=True)

