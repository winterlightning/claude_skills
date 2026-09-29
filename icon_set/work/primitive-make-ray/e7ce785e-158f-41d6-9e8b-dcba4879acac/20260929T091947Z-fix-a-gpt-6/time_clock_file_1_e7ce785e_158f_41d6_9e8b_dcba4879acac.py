from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'e7ce785e-158f-41d6-9e8b-dcba4879acac'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__time-clock-file-1/20260929T091947Z-thuan-mac/reference/time clock file 1_e7ce785e-158f-41d6-9e8b-dcba4879acac.svg'
AUTHOR = "gpt-6"
# Plan: Restore a larger round clock with clearly separate hands inside the clipped-corner page.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: none.

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
    icon_id = 'time-clock-file-1'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve the larger clock face and detached hands inside the page; compact clock clearance and larger page envelope remain readable at 48px.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'a2e7087b2977c4572d7bea78372c4afea25b5dd6b65d5e8a92583557a2f864b0'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'page', 'M 8 4 L 31 4 L 44 17 L 44 40 A 4 4 1 40 44 L 8 44 A 4 4 1 4 40 L 4 8 A 4 4 1 8 4 Z')
        _draw(self, 'clock', 'M 12 27 A 12 12 1 36 27 A 12 12 1 12 27 Z')
        _draw(self, 'hands', 'M 24 20 L 24 27 L 29 31')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
