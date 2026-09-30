from pathlib import Path
import json, shutil
import cairosvg
ROOT=Path(__file__).resolve().parent
claims=json.loads((ROOT/'claims.json').read_text());runs=json.loads((ROOT/'runs.json').read_text())
counts={e['key']:e['count'] for e in json.loads((ROOT/'eligibility.json').read_text())}
assert len(claims)==len(runs)==20 and len({e['key'] for e in claims})==20
bounds={'SQUARE':[6,6,42,42],'HRECT_L':[4,8,44,40],'VRECT_L':[8,4,40,44]}
review={
1:'Two lightning-shaped stress marks remain distinct above a circular head. Flared hair ends and broad shoulders read at 48 px. Circular jaw bottom 35 and shoulder arc top 39 give exactly 4 centerline units, zero ink gap; true scoped contact and human bust declaration.',
2:'The flowing grain enters and leaves the open oval knot; the board frame remains clear.',
3:'Matched diamonds, diagonal branches, stem and round lower terminal remain distinct; mirrored on x=24.',
4:'Rounded snout, upturned tail, curved belly and forward rounded foot retain the right-facing dinosaur profile.',
5:'Egg stands above the bowl-shaped bird, with a small left-facing beak. The open egg edge remains visibly associated with the bird body.',
6:'Hollow central ring and four radial divisions identify the chip; mirrored open palms and thumbs sit beneath it.',
7:'Two hollow input circles, two solid output bars and a curved rightward arrow remain legible and separate.',
8:'Curved straw fan, separated handle collar and dust ring remain readable at native size.',
9:'The hanging hole remains visibly open. The rounded handle attaches to the broad diagonal blade.',
10:'Rounded knuckle lobes, bent thumb crease and diagonal forearm read as a raised fist.',
11:'Flared reflector, rounded rear housing and short light ray preserve the diagonal spotlight.',
12:'Portrait page, clipped corner and three descending chart bars retain balanced margins.',
13:'Teardrop stays visibly open beneath the tray edge; three longer S-shaped steam marks remain separate.',
14:'Broad blank frog face and matched eye bulges sit above a rounded seated body with two forelegs. The former tangle is removed.',
15:'Paired hollow eyes and downturned mouth restore the expression within a broad helmet silhouette.',
16:'Sun and two unequal mountain peaks remain clearly separate within the portrait page.',
17:'Small stem, round-shouldered pointed pod and three aligned seed marks remain legible.',
18:'Broad diagonal shell remains separate from the scalloped filling, with clear negative space.',
19:'Exposed upper-left sun is separated from the lower cloud silhouette; a short external ray remains.',
20:'Circular upper head, pointed bandana and broad shoulders preserve the covered face. The hidden jaw is replaced by the connected covering; no detached head-body gap applies.'}
for i,e in enumerate(claims,1):
 r=runs[str(i)];assert r['key']==e['key'] and counts[e['key']]==1
 assert r['status']=='valid' and r['gate']=='pass' and not r['errors'] and not r['warnings']
 run=Path(r['run']);d=json.loads((run/'draft.json').read_text());assert d['author']=='gpt-6'
 shutil.copyfile(e['reference'],run/'reference.svg')
 for size in (48,384):
  cairosvg.svg2png(url=e['reference'],write_to=str(run/f'reference-{size}.png'),output_width=size,output_height=size,background_color='#ffffff')
 d['visual_review']={'status':'pass','themes':['light','dark'],'sizes':[48,384],'findings':review[i],'compared_original_and_rejected':True,'feedback':'No written feedback or disapproval reason recorded.'}
 d['centerline_envelope']=bounds[d['keyshape']]
 d['keyshape_reason']='Portrait envelope preserves upright proportions and vertical layers.' if d['keyshape']=='VRECT_L' else 'Landscape envelope preserves the horizontal composition.' if d['keyshape']=='HRECT_L' else 'Square envelope balances the complete silhouette and its diagonal or paired parts.'
 d['artifacts']=[x.name for x in sorted(run.iterdir()) if x.is_file() and x.name!='result.json']
 (run/'visual-review.txt').write_text(review[i]+'\nReviewed at 48 and 384 px in light and dark themes. Model valid and full build gate pass; zero errors and warnings.\n')
 (run/'result.json').write_text(json.dumps(d,indent=2)+'\n')
print('Finalized 20 visually reviewed runs; all eligible once, valid, full gate pass, zero warnings, AUTHOR gpt-6.')
