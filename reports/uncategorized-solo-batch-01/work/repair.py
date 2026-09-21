"""Apply bounded model repairs only to this batch's new originals."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
BATCH=ROOT/'reports/uncategorized-solo-batch-01'
entries=json.loads((BATCH/'manifest.json').read_text())['entries']
SOURCE_ICON_ID=tuple(e['source_uuid'] for e in entries)
SOURCE_PATH=tuple(e['source_path'] for e in entries)
AUTHOR='gpt-6-astra'
def path(n):
 e=entries[n-1]
 return ROOT/'icon_set/model/icons/solo'/((e['icon_id']+'_'+e['source_uuid']).replace('-','_')+'.py')
def replace(n,a,b):
 p=path(n);s=p.read_text();assert a in s,(n,a);p.write_text(s.replace(a,b))

# Joined polylines nested in a larger continuous contour must have one owner.
for n in [17,22,25,27,32,34,35,36,41]:
 p=path(n);s=p.read_text()
 lines=s.splitlines();result=[]
 for line in lines:
  if "self.add_contour(" in line and not ('name,' in line or 'name+' in line):
   import ast
   call=ast.parse(line.strip()).body[0].value
   members=[arg.value for arg in call.args[1:]]
   result.append('        # Merge the temporary runs into one continuous contour.')
   result.append(f'        self.contours = [c for c in self.contours if not set(c.members).issubset({set(members)!r})]')
  result.append(line)
 p.write_text('\n'.join(result)+'\n')

# Whole-subject rebalancing, preserving each part's identity.
replace(7,"self.circle('head',26,16,4)","self.circle('head',26,18,4)")
replace(7,"(26,28)","(26,30)")
replace(7,"(6,18),(42,6)","(6,6),(42,6)")
replace(7,"(14,28),(12,16)","(10,30),(10,6)")
replace(12,"self.circle('head',24,24,12,20)","self.circle('head',24,24,16,20)")
replace(12,"self.circle('muzzle',24,30,4,8)","self.circle('muzzle',24,28,5,7)")
replace(12,"        for side,x in [('left',8),('right',40)]: self.add_dot('ear-'+side,(x,16))", "        # Ears are omitted: the long muzzle is the primary identity cue.")
replace(15,"(6,38),(42,38),30,10,sweep=False","(6,36),(42,36),18,6,sweep=False")
replace(18,"[(6,6),(6,18),(14,14)]","[(6,6),(6,14),(10,10)]")
for n in [19,20]:
 replace(n,"self.arc('cork',(6,30),(18,42),9,sweep=False)","self.arc('cork',(6,30),(18,42),12,sweep=False)")
replace(21,"6,22,20,16,3","6,22,20,12,3")
replace(28,"(16,6),(16,42)","(12,8),(12,40)")
replace(28,"(26,4),(26,44)","(24,4),(24,44)")
replace(28,"self.circle('spot',36,24,2)","self.circle('spot',33,24,2)")
replace(33,"Keyshape.HRECT_L","Keyshape.HRECT_M")
replace(33,"(4,24),(44,24),20,16","(4,22),(44,22),20,12")
replace(33,"(44,24),(4,24)","(44,22),(4,22)")
replace(33,"x,36,6,4","x,34,6,4")
replace(33,"(20,36),(28,36)","(20,34),(28,34)")
replace(40,"self.circle('sun',12,16,8)","self.circle('sun',10,14,6)")
replace(48,"[(16,26),(32,26),(30,42),(18,42)]","[(18,30),(30,30),(28,42),(20,42)]")
replace(48,"[(6,18),(14,18),(12,34),(6,34)]","[(6,18),(14,18),(12,26),(6,26)]")
replace(48,"[(34,18),(42,18),(42,34),(36,34)]","[(34,18),(42,18),(42,26),(36,26)]")
for n in [49,50]:
 replace(n,"(24+sgn*5,12)","(24+sgn*5,10)")
 replace(n,"(20,30,40)","(26,34,42)")
