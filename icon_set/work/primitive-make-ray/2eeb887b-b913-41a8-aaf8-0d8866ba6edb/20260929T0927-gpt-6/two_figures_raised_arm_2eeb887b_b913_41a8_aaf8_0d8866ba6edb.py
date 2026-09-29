from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '2eeb887b-b913-41a8-aaf8-0d8866ba6edb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-figures-raised-arm/20260929T090755Z-thuan-mac/reference/pass through_2eeb887b-b913-41a8-aaf8-0d8866ba6edb.svg'
AUTHOR = "gpt-6"
# Plan: Use matched heads and coherent standing bodies, with one arm visibly raised toward the other person.
# Keyshape: HRECT_L; preserve reference arrangement.
# Construction reference: human_ref/full_body_ref.png.

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
    icon_id = 'two-figures-raised-arm'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'head-a', 'M 10 12 A 4 4 1 18 12 A 4 4 1 10 12 Z')
        _draw(self, 'head-b', 'M 32 12 A 4 4 1 40 12 A 4 4 1 32 12 Z')
        _draw(self, 'torso-a', 'M 14 24 L 14 31')
        _draw(self, 'torso-b', 'M 36 24 L 36 31')
        _draw(self, 'left-arm', 'M 14 24 L 8 24 L 4 29')
        _draw(self, 'raised-arm', 'M 14 24 L 21 24 L 24 12')
        _draw(self, 'right-arms', 'M 29 29 L 31 24 L 36 24 L 41 24 L 44 29')
        _draw(self, 'legs-a', 'M 8 40 L 14 31 L 20 40')
        _draw(self, 'legs-b', 'M 30 40 L 36 31 L 42 40')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
        self.mark_human_figure('person-a', head='head-a', torso='torso-a-1', torso_junction='start')
        self.mark_human_figure('person-b', head='head-b', torso='torso-b-1', torso_junction='start')
