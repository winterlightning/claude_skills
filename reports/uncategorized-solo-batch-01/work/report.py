import ast,json,math
from pathlib import Path
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[3]
BATCH=ROOT/'reports/uncategorized-solo-batch-01'
p=json.loads((BATCH/'progress.json').read_text())
done=[e for e in p['entries'] if e['outcome']=='generated']
previews=ROOT/'icon_set/.local/previews-png/uncategorized-solo-batch-01'
for theme,bg,fg in [('light','white','#111111'),('dark','#171717','#eeeeee')]:
 sheet=Image.new('RGB',(1080,math.ceil(len(done)/6)*186),bg);d=ImageDraw.Draw(sheet)
 for i,e in enumerate(done):
  im=Image.open(ROOT/e['preview_'+theme]).convert('RGB');x=i%6*180;y=i//6*186
  sheet.paste(im.resize((96,96)),(x+42,y+6));sheet.paste(im,(x+66,y+106))
  d.text((x+8,y+162),f"{e['number']:02} "+e['icon_id'][:23],fill=fg)
 sheet.save(previews/f'completed-{theme}.png')

notes={
1:'Crown, round face and companion tent retained; neckline omitted. Detached head/body ink gap is exactly 4: face bottom centerline y=26 and shoulder top y=34, centered at x=34.',
8:'Three bubbles replace seven; headlamps omitted. Symmetric front car, paired tires, broad windshield.',
11:'Broad outlined ribbon strands reduced to one coherent loop and two crossing tails. Symmetric awareness-ribbon silhouette retained.',
14:'Blank rounded baby head with an integrated curl; ears reduced to short stubs. Forehead opening keeps the curl clear.',
15:'Cradle panel and rocker simplified; one central support replaces paired feet. Baby head ends at y=14 and panel begins at y=22: 4-unit visible gap.',
16:'Rectangular Backbone logo and crossing diagonals retained; graphic structure is intrinsic to the logo, not a hosted status badge.',
19:'Reoriented upright to fit three broad feather sections with legal spacing. Rounded cork attaches to the base. Fine feather texture omitted.',
20:'Reoriented upright to fit three broad feather sections with legal spacing. Rounded cork attaches to the base. Fine feather texture omitted.',
21:'Suitcase, handle, platform, post and dial retained. Hanging tag, case bands and dial needle omitted to keep the weighing scene readable.',
22:'Baguette is upright and paired with a round loaf in a shallow basket. Scoring marks omitted to preserve internal space.',
23:'Three rounded muffin lobes above a tapered paper cup. Tiny scallops removed; cup joins now share exact endpoints with the top.',
24:'Semicircular sieve with a long handle and three falling grain strokes. Two grain rows reduced to one.',
26:'Slightly oval balloon and curved string; small knot polygon omitted. Deliberate asymmetric string follows the source.',
27:'Left-facing foot and shin with two broad diagonal wrap lines. Toe-wrap detail removed in favor of readable shin bandages.',
28:'Circular planet retains one long band and a spot. Extra bands and interrupted edge omitted to prevent narrow regions.',
29:'Broad rounded soap bar and two rising bubbles. Smallest bubble omitted; bubble sizes differ deliberately.',
31:'Round head follows the upright torso axis. Head center (30,14), radius 4; torso starts (30,26), giving exactly 8 centerline / 4 visible units. Bat and limbs preserve the action.',
32:'Helmet dome, projecting brim and deep ear guard retained. Ear opening omitted. Brim is a separate attached stroke with no doubled-back segment.',
34:'Rounded palm, thumb gap and one web band retained; finger-tip count reduced for legal spacing.',
36:'Scoreboard over the fan-shaped field. Pennants and tiny foreground mound omitted; scoreboard lettering was not present in the source.',
37:'Round ball, equatorial seam and two curved panel seams retained; third upright seam omitted.',
38:'Reclining backrest, long seat and two supporting legs retained. Duplicated seat segment removed.',
39:'Physical parasol/lounger scene retained. Canopy made upright and unsegmented; chair legs and raised back remain.',
40:'Parasol, leaning pole, low sun and shoreline retained. Canopy ribs and extra horizon removed.',
44:'Bed and four-pane window retained. Small pillow removed to eliminate crowding beside the headboard.',
45:'Tall headboard, raised rounded pillow, mattress rail and low footboard retained. Pillow moved away from headboard to preserve a clear opening.',
46:'Cabinet, drawer divider, knob and two feet retained. Separate tabletop band omitted.',
47:'Broad rim band and tapered pint-glass silhouette retained; sides use straight geometric taper.',
49:'Rounded lower shell, head bulge, central seam, antennae and six legs retained. Head/body use one coherent outline; leg pairs derive from one axis.',
50:'Rounded lower shell, head bulge, central seam, antennae and six legs retained. Head/body use one coherent outline; leg pairs derive from one axis.'}

counts={s:sum(e['outcome']==s for e in p['entries']) for s in ('generated','already-existing','blocked')}
lines=[f"# Uncategorized solo batch 01 — results",'',
f"All 50 ordered briefs accounted for: **{counts['generated']} generated, {counts['already-existing']} already-existing, {counts['blocked']} blocked**. Of the blocked entries, 5 require another family, 2 require component splits, 6 retain release-QA failures, and 7 failed semantic visual review.",'',
'The 30 completed icons have Python originals under `icon_set/model/icons/solo/`, exact source UUID/path provenance, and `AUTHOR = "gpt-6-astra"`. This introduces the author label confirmed by the user. Blocked drawing candidates are retained under `icon_set/.local/candidates/uncategorized-solo-batch-01/`, outside the active registry. No substitute icons or extra components were generated.', '',
'[Completed light preview](../../icon_set/.local/previews-png/uncategorized-solo-batch-01/completed-light.png) · [Completed dark preview](../../icon_set/.local/previews-png/uncategorized-solo-batch-01/completed-dark.png) · [Completed gallery](../../icon_set/.local/batches/uncategorized-solo-batch-01/completed/gallery/index.html) · [Progress and provenance](progress.json)', '',
'## Validation and workflow', '',
'Each completed model passes vector validation with zero warnings and release QA, including holes/pinches and internal spacing. Native 48px previews were inspected in both themes, alongside enlarged views. All source SVGs were rendered and inspected; all 50 original brief hashes match the manifest. Exact source UUID, path and registry-ID searches found no existing matches (substring-only matches were excluded).', '',
f"Final targeted completed-set build exit code: **{p.get('completed_build',{}).get('exit_code','pending')}**. [Build log](work/completed-build.log). The default output directory was locked by another process; after the requested default-path attempts, targeted builds used an isolated batch directory. The completed manifest is at `icon_set/.local/batches/uncategorized-solo-batch-01/completed/solo48/manifest.json`; the default manifest was not updated.", '',
'The generation, metadata and profile/keyshape tests passed: **28 tests** ([log](work/targeted-tests.log)). The workflow suite ran 25 tests with 19 errors because the sandbox disallowed loopback HTTP socket binding ([log](work/workflow-tests.log)). A broader initial run including avatar corpus checks failed (56 tests; 36 failures, 26 errors), so the full suite is not claimed green. No validators, thresholds or contracts were changed. `doctor` found zero tracked generated files. Unrelated working changes and production state were preserved.', '',
'## Per-brief outcomes', '',
'Keyshape choices follow the subject envelope: CIRCLE for spheres; SQUARE for compact scenes; HRECT for wide objects/scenes; VRECT for upright objects. The exact four visible bounds are saved in progress.json. Directional poses, side views, accessories and strings intentionally preserve asymmetry; otherwise paired geometry uses shared dimensions.', '',
'| # | Brief / source | Outcome | Keyshape | Decision / simplification |',
'|---:|---|---|---|---|']
for e in p['entries']:
 n=e['number'];note=notes.get(n,e.get('reason',''))
 module=e.get('module');outcome=e['outcome']
 if module:outcome=f'[{outcome}](../../{module})'
 lines.append(f"| {n} | [{e['concept']}]({e['brief_file']}) | {outcome} | {e.get('keyshape','—')} | {note.replace('|','/')} |")
lines+=['','## Construction references and blockers','',
'Every source path and UUID is retained in progress.json and in each authored module. Lucide construction references inspected as original renders plus atomic geometry: `car-front` (rounded body and paired tires), `ribbon` (loop and crossing tails), `baby` (integrated curl), `balloon` (outline/string flow), `soup` (semicircular bowl), `hand` (rounded fingers/palm), `bed-single` (coherent furniture junctions), `glass-water` (vessel taper), `umbrella` (canopy), and `bug` (body/seam/paired legs). The original Lucide `bed` and `hat-glasses` renders also informed the furniture and rejected cap layouts. No useful exact Lucide subject match was found for the remaining specialized scenes; their supplied source renders determined their content.', '',
'Human construction used `icon_set/references/human_ref/user.svg` and `full_body_ref.png`. Successful detached figures have the analytical gap evidence in the per-brief notes. The failed portraits were reviewed through the icon-avatar specialization; their missing beard cues prevent acceptance. `icon-making` routing produced two standalone component handoffs each for entries 9 and 10, saved under [handoffs](handoffs/) using files-only mode; no review database or remote queue was changed.', '',
'Remaining release blockers (no warnings counted as passes):','']
for e in p['entries']:
 if e.get('release_qa',{}).get('status') not in (None,'pass'):
  lines.append(f"- **{e['number']}: {e['icon_id']}** — "+'; '.join(e['release_qa']['errors']+e['release_qa']['warnings'])+f". [Full QA](work/{e['number']:02}-qa.json).")
lines+=['','## Token usage and API-equivalent cost','',
'Model: **gpt-6-astra**, explicitly confirmed by the user. Reasoning setting and actual service tier are not exposed. No task-scoped input, cached-input, output, or separately billed cache-write counters are exposed by this runtime. This includes setup, tool calls, source review, rendered-image review, repair attempts, tests and reporting. Shared overhead is therefore explicitly **unmeasured**, not treated as zero.', '',
'At the 5-entry and 25-entry checkpoints, measured averages and projected 50-entry token/cost totals were unavailable. Final accounting has the same limitation:','',
'| Metric | Numerator / denominator | Result |','|---|---|---|',
'| Batch tokens per attempted entry | unavailable total / **50 attempts** | unavailable |',
f"| Batch tokens per successfully generated icon | unavailable total / **{len(done)} generated** | unavailable |",
'| Already-existing skips | **0**; excluded from generation accounting | 0 |',
'| Directly attributable per-icon usage | no counters | unavailable |',
'| Allocated average including shared overhead | no batch total | unavailable |',
'| Total API-equivalent USD | no billable-category totals or confirmed tier | unavailable |',
f"| API-equivalent USD per generated icon | unavailable USD / **{len(done)}** | unavailable |",'',
'Official pricing checked **2026-09-21**: standard GPT-6 Astra rates per million tokens are $10 uncached input, $1 cached input, $12.50 cache writes, and $50 output. For requests above 272K input tokens, input/cache rates double and output rates multiply by 1.5. These are reference rates, not a claim about the tier used by this session. [Official model page](https://developers.openai.com/api/docs/models/gpt-6-astra) · [Official pricing](https://developers.openai.com/api/docs/pricing).','',
'A cost calculation would sum mutually exclusive billed uncached-input, cache-read, cache-write and output categories at the actual tier/context rates, plus separately billed tool charges. Cached input is a subset of total input, and reasoning must not be added again when included in output. With no category counters, cache-write accounting, tier or tool-charge data, no defensible low/base/high planning estimate is supplied. Any such figure would be an **API-equivalent estimate**, not an additional subscription bill. [Pricing record](work/pricing.json).','']
(BATCH/'REPORT.md').write_text('\n'.join(lines))
print(counts)
