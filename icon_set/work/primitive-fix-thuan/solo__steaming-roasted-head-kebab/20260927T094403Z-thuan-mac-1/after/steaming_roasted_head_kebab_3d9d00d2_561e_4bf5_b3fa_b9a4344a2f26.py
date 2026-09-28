"""Steaming Roasted Head Kebab."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3d9d00d2-561e-4bf5-b3fa-b9a4344a2f26'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__steaming-roasted-head-kebab/20260927T094403Z-thuan-mac-1/reference/exotic food kebab_3d9d00d2-561e-4bf5-b3fa-b9a4344a2f26.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steaming-roasted-head-kebab'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('steaming', 'roasted', 'head', 'kebab')

    def build(self):
        # Plan: Stylized roasted head-like kebab on a hooked spit with two steam curls. The oval food shape follows the reference; mouth omitted and closed eyes reduced to short marks. Human reference user.svg was inspected for context; no human body or detached head/body pair is depicted.
        # Envelope: VRECT_L; visible ink (6, 2, 42, 46) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        oval('roast',24,25,14,11)
        path('hook',(24,14),[('L',(24,10)),('A',(28,10),2,6,True)])
        join('hook','roast');line('spit',(24,36),(24,44));join('spit','roast');poly('base',(12,44),(24,44),(36,44));join('base','spit')
        line('eye-left',(19,24),(20,24));line('eye-right',(28,24),(29,24))
        path('steam-left',(10,4),[('C',(10,8),(12,5),(10,7))])
        path('steam-right',(38,4),[('C',(38,8),(36,5),(38,7))])
