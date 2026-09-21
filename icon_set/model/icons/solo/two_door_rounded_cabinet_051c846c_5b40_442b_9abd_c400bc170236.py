'A tall cabinet has two doors with paired upright handles. SQUARE opens enough width for separated paired handles. One rounded shell owns the central seam; handles mirror about x24 with exact nine-unit straight clearances. Source supplies the entire subject; no useful direct Lucide cabinet match, with rounded-shell construction informed by bus-front. No source details omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '051c846c-5b40-442b-9abd-c400bc170236'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_09/cabinet_051c846c-5b40-442b-9abd-c400bc170236.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'two-door-rounded-cabinet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Double Door Storage Cabinet',)
    keywords = ('double', 'door', 'storage', 'cabinet')
    def build(self):
        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        path('shell',(10,6),[(24,6),(38,6),((42,10),4,4,True),(42,38),((38,42),4,4,True),(24,42),(10,42),((6,38),4,4,True),(6,10),((10,6),4,4,True)],True)
        self.add_line('seam',(24,6),(24,42));self.relate('connect','seam','shell')
        for x in (15,33):self.add_line(f'handle-{x}',(x,22),(x,28))
