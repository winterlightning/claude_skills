from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'c8eb6f70-a59a-410a-ab73-429758565aa2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-kidney-beans/20260929T090755Z-thuan-mac/reference/kidney bean_c8eb6f70-a59a-410a-ab73-429758565aa2.svg'
AUTHOR = "gpt-6"
# Plan: Restore two plump asymmetric kidney forms with inward notches and a diagonal upper bean.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: bean.

def _draw(icon, name, description):
    tokens=description.split(); pos=0; part=0; count=0; members=[]; start=None; point=None
    def finish(closed=False):
        nonlocal members,part
        if members: icon.add_contour(name if part==0 else f"{name}-part{part}",*members,closed=closed)
        members=[];part+=1
    while pos<len(tokens):
        op=tokens[pos];pos+=1
        if op=='M':
            if members: finish()
            point=tuple(map(int,tokens[pos:pos+2]));pos+=2;start=point
        elif op=='Z':
            if point!=start:
                count+=1;eid=f"{name}-{count}";icon.add_line(eid,point,start);members.append(eid);point=start
            finish(True)
        else:
            count+=1;eid=f"{name}-{count}";members.append(eid)
            if op=='L':
                end=tuple(map(int,tokens[pos:pos+2]));pos+=2;icon.add_line(eid,point,end)
            elif op=='C':
                values=list(map(int,tokens[pos:pos+6]));pos+=6;c1=tuple(values[:2]);c2=tuple(values[2:4]);end=tuple(values[4:]);icon.add_bezier(eid,point,(c1,c2,end))
            elif op=='A':
                rx,ry,sweep,x,y=map(int,tokens[pos:pos+5]);pos+=5;end=(x,y);icon.add_arc(eid,point,end,radius_x=rx,radius_y=ry,sweep=bool(sweep))
            point=end
    if members: finish()

class Revision(Solo48):
    icon_id = 'two-kidney-beans'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve two plump asymmetric beans in diagonal arrangement; curved silhouettes and compact separation are visibly distinct.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'e161477973501dc86d3025c024920baff6a6faa59dc9fad7427b81c50a249d94'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'upper', 'M 15 14 C 15 9 22 13 26 11 C 32 8 33 4 38 7 C 46 14 39 22 29 25 C 19 28 11 23 15 14 Z')
        _draw(self, 'lower', 'M 6 31 C 10 25 15 32 21 31 C 27 30 33 27 34 34 C 35 41 23 44 13 41 C 7 40 3 36 6 31 Z')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
