from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='bd44c072-c5cf-4191-b2b0-3681a58f3a3a'
SOURCE_PATH='pictographic-primitives/_uncategorized_40/workflow data table increasing arrow_bd44c072-c5cf-4191-b2b0-3681a58f3a3a.svg'
AUTHOR="gpt-6"
PLAN='Table reduced to two rows and two columns, with evenly spaced row lines; rising zigzag retained.'
class Drawing(Solo48):
    icon_id='workflow-data-table-increasing-arrow'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,p,ops,closed=False):
        members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';end=op[1]
            if op[0]=='L': self.add_line(eid,p,end)
            elif op[0]=='A': self.add_arc(eid,p,end,radius_x=op[2],radius_y=op[3],sweep=op[4])
            else: self.add_bezier(eid,p,(op[2],op[3],end))
            p=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def rect(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        self.add_polyline('growth',(6,22),(14,14),(22,18),(30,10),(34,14),(42,6))
        self.add_polyline('arrow-head',(34,6),(42,6),(42,14))
        self.relate('connect','growth','arrow-head')
        self.add_polyline('table',(14,26),(28,26),(42,26),(42,34),(42,42),(28,42),(14,42),(14,34),closed=True)
        self.add_polyline('column',(28,26),(28,34),(28,42))
        self.add_polyline('row',(14,34),(28,34),(42,34))
        self.relate('connect','table','row')
        self.relate('connect','table','column')
        self.relate('connect','row','column')
