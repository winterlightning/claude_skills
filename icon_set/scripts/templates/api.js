(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const quote = value => "'" + String(value).replaceAll("'", "'\\''") + "'";
  const iconQuery = () => '?icon=' + encodeURIComponent($('apiIcon').value.trim());
  const current = () => ({icon:$('apiIcon').value.trim(), svg_sha256:$('apiHash').value.trim() || 'CURRENT_SVG_SHA256'});
  const review = status => () => ({...current(),status});
  const operations = [
    ['List all icon records','GET','/gallery/icons.json',false,null,'Includes published icons and failed_icons. Join keys with /api/reviews for current stages.','200 · {icons: […], failed_icons: […]}'],
    ['Read all review stages','GET','/api/reviews',false,null,'Map of icon key to ready, pending, approve, or rejected.','200 · {"solo/example": "ready", …}'],
    ['Read reviewer attribution','GET','/api/reviews?include_approvers=1',false,null,'Current statuses and the reviewers responsible for decisions.','200 · {statuses, approved_by, disapproved_by, rejected_by, feedback_by}'],
    ['Read one review decision','GET',() => '/api/review-detail'+iconQuery(),false,null,'Reads the current SVG version’s decision and actor.','200 · {status, updated_by, updated_at}'],
    ['Read feedback history','GET',() => '/api/feedback'+iconQuery(),false,null,'Latest 100 feedback entries for this icon. Compare each svg_sha256 to the current version.','200 · Array of feedback entries'],
    ['Read disapproved uploaded icons','GET','/api/icon-types?type=uploaded&status=disapprove',false,null,'Filter by icon type and stage. This endpoint calls the disapproved status disapprove.','200 · {icons: [{icon, icon_type, status, svg_sha256, reason, feedback, …}]}'],
    ['Work queue: claimable disapproved icons','GET','/api/work/queue?family=sub&limit=20',false,null,'Disapproved icons no machine is fixing (work state open or expired), oldest first. Filters: family, category, type, limit 1–500, offset. Development servers forward this to production.','200 · {total, offset, next_offset, items: [{key, svg_sha256, python_source, reason, feedback, disapproved_by, work}]}'],
    ['Disapproved icons with work state','GET','/api/work/disapproved?family=sub&limit=50',false,null,'Every disapproved icon, claimable or not, with its review status and work state (open, working, expired, done, cannot-fix). Same filters and paging as the queue.','200 · {total, offset, next_offset, items: [{key, svg_sha256, status, reason, feedback, disapproved_by, work}]}'],
    ['Work: current claims','GET',() => '/api/work'+($('apiIcon').value.trim()?iconQuery():''),false,null,'Every claim joined to the current catalog, or one icon’s work state. States: open, working, expired, done, cannot-fix (superseded when the revision changed).','200 · {claims: [{icon, svg_sha256, state, worker, note, claimed_at, updated_at, expires_at, current, status}]}'],
    ['Work: claim an icon','POST','/api/work/claim',true,() => ({...current(),worker:'hostname/agent'}),'Disapproved + open/expired → working for 3 hours (lease_hours 1–24). 409 with the current work state when another worker holds it or it is done / cannot-fix.','201 · {saved: true, work: {state: "working", worker, expires_at}, item}'],
    ['Work: claim several icons','POST','/api/work/claim',true,() => ({worker:'hostname/agent',icons:[{icon:current().icon,svg_sha256:current().svg_sha256},'sub/another']}),'Claims each listed icon on its own: entries are icon keys or {icon, svg_sha256} objects (a key alone uses production’s current hash). Up to 500 per call.','200 · {saved, worker, claimed: [item…], refused: [{icon, status, error, work}]}'],
    ['Work: heartbeat','POST','/api/work/heartbeat',true,() => ({...current(),worker:'hostname/agent'}),'Extends your own working lease.','200 · {saved: true, work}'],
    ['Work: report done → Ready','POST','/api/work/done',true,() => ({...current(),worker:'hostname/agent',note:'sub/plus-v3'}),'Marks your claim done and returns this revision to Ready for the reviewer. Disapproval feedback is kept. Re-disapproving later reopens the icon for claiming.','200 · {saved: true, status: "ready", work: {state: "done"}}'],
    ['Work: cannot fix','POST','/api/work/cannot-fix',true,() => ({...current(),worker:'hostname/agent',note:'Why no meaning-preserving drawing passes.'}),'Gives up with a required note. Skipped by the queue until a reviewer disapproves the icon again.','200 · {saved: true, work: {state: "cannot-fix"}}'],
    ['Work: abandon claim','POST','/api/work/abandon',true,() => ({...current(),worker:'hostname/agent'}),'Releases your working claim so another machine can take it. A logged-in reviewer may release anyone’s claim.','200 · {saved: true, work: {state: "open"}}'],
    ['List icon families','GET','/api/icon-families',false,null,'Built-in and custom upload families with canvas sizes.','200 · {families: [{id, name, canvas_size, builtin}]}'],
    ['Create an icon family','POST','/api/icon-families',false,() => ({id:'rounded',name:'Rounded icons',canvas_size:48}),'Creates a persistent SVG upload family. Use its id in the upload request. Canvas: integer 16–256. Existing id: 409.','201 · {family: {id, name, canvas_size, builtin: false}}'],
    ['Read category choices','GET','/api/icon-categories',false,null,'Current categories, including manual_upload.','200 · {categories: […]}'],
    ['Download current SVG','GET',() => '/api/icon-artwork/svg'+iconQuery(),false,null,'Returns SVG content for the displayed version.','200 · image/svg+xml'],
    ['Upload a new SVG → Ready','POST','/api/icons/upload',false,() => ({name:'Circle outline',family:'solo',category:'shapes',bypass_validation:true,svg:'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><circle cx="24" cy="24" r="16"/></svg>'}),'Creates a separate icon in Ready. Blank or omitted category becomes manual_upload; type is uploaded.','201 · {status: "ready", record: {key, svg_sha256, validation, …}}'],
    ['Move to Ready','POST','/api/reviews',true,review('ready'),'Reopens an active icon for review and clears its feedback. Restore rejected icons first.','201 · {saved: true, status: "ready", updated_by}'],
    ['Approve','POST','/api/reviews',true,review('approve'),'Approves the current SVG from Ready or Disapproved. Requires its exact current hash.','201 · {saved: true, status: "approve", updated_by}'],
    ['Disapprove with feedback','POST','/api/reviews',true,() => ({...current(),status:'disapprove',reason:'other',feedback:'Describe what needs fixing.'}),'Moves Ready or Approved icons to Disapproved. Reasons: bad-stroke, meaning, manual-fix-request, other. Other requires nonempty feedback.','201 · {saved: true, status: "pending", updated_by, id, feedback}'],
    ['Reject','POST','/api/reviews',true,review('rejected'),'Excludes an icon from the active set. Use Restore before changing its decision again.','201 · {saved: true, status: "rejected", updated_by}'],
    ['Restore rejected icon → Ready','POST','/api/reject-combination/restore',true,current,'Restores any rejected icon to Ready, clears feedback, and deactivates active split requests.','200 · {saved: true, status: "ready"}'],
    ['Write feedback / disapprove','POST','/api/feedback',true,() => ({...current(),reason:'meaning',feedback:'Describe how to improve recognition.'}),'Writes feedback and sets active icons to pending. An already rejected icon stays rejected. Failed-build icons may receive feedback.','201 · {saved: true, status, id, feedback, updated_by}'],
    ['Read artwork choices','GET',() => '/api/icon-artwork'+iconQuery(),false,null,'Read this before saving edits. Its top-level svg_sha256 is the original source hash; choice.revision tracks saved artwork.','200 · {choice, source_mode, svg_sha256, edit_revision, preview_url, record}'],
    ['Save manual SVG candidate','POST','/api/icon-artwork',true,() => ({icon:current().icon,svg_sha256:'ORIGINAL_HASH_FROM_ARTWORK_RESPONSE',revision:0,source_mode:'use_org',action:'upload',filename:'edited.svg',svg:'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><circle cx="24" cy="24" r="16"/></svg>'}),'Replace revision and source_mode with the latest artwork response. Match the icon canvas. Saving a candidate does not change the displayed version or decision.','200 · Updated artwork choice and record'],
    ['Select saved manual SVG & approve','POST','/api/icon-artwork',true,() => ({icon:current().icon,svg_sha256:'ORIGINAL_HASH_FROM_ARTWORK_RESPONSE',revision:1,source_mode:'use_upload'}),'Use the revision returned after saving the candidate. Selects the saved SVG and approves it in the same operation. Restore rejected icons first.','200 · Artwork response; record.review_status is approve'],
    ['Read icon type','GET',() => '/api/icon-type'+iconQuery(),false,null,'Reads the current editable icon type tag.','200 · {icon_type, updated_by, updated_at}'],
    ['Write icon type','POST','/api/icon-type',true,() => ({icon:current().icon,icon_type:'uploaded'}),'Sets an icon type tag. Does not change the review decision.','200 · {icon_type, updated_by, updated_at}'],
    ['Start generation','POST','/api/generation',true,() => ({mode:'generate',name:'Watering can',family:'solo',prompt:'A watering can in side view.',model:''}),'Starts an asynchronous job. The server needs an authenticated Codex installation. Does not yet add an icon to the grid.','202 · Generation job with id and status'],
    ['Read generation jobs','GET','/api/generation',true,null,'Poll to see when a candidate is ready for acceptance.','200 · Generation job list'],
    ['Accept generated candidate','POST','/api/generation/accept',true,() => ({id:'JOB_ID'}),'Builds and adds the candidate to the review grid as Ready. Poll the job to confirm completion.','202 · Updated generation job'],
    ['Discard generated candidate','POST','/api/generation/discard',true,() => ({id:'JOB_ID'}),'Discards the generation candidate, not an existing reviewed icon.','202 · Updated generation job']
  ];
  function render() {
    const base = $('apiBase').value.trim().replace(/\/$/,'');
    const setup = 'API_BASE=' + quote(base);
    $('loginExample').textContent = setup + '\n\ncurl --fail-with-body --cookie-jar cookies.txt \\\n  -H \'Content-Type: application/json\' \\\n  --data '+quote(JSON.stringify({username:'YOUR_USERNAME',password:'YOUR_PASSWORD'}))+' \\\n  "$API_BASE/api/auth/login"';
    $('readExample').textContent = setup + '\n\ncurl --fail-with-body "$API_BASE/gallery/icons.json" -o icons.json\ncurl --fail-with-body "$API_BASE/api/reviews" -o reviews.json\njq --slurpfile reviews reviews.json --arg stage ready \\\n  '+quote('.icons[] | select($reviews[0][.key] == $stage)')+' icons.json';
    const [,method,pathValue,auth,payload,description,response] = operations[Number($('apiOperation').value)];
    const path = typeof pathValue==='function'?pathValue():pathValue;
    $('apiMethod').textContent = method;
    $('apiEndpoint').textContent = base + path;
    $('apiAuth').textContent = auth?'No login required · attributed to system; optional reviewer cookie':'No login required';
    $('apiDescription').textContent = description;
    $('apiResponse').textContent = response;
    let command = setup+'\n\ncurl --fail-with-body --request '+method;

    if(payload)command += ' \\\n  --header \'Content-Type: application/json\' \\\n  --data '+quote(JSON.stringify(payload(),null,2));
    // Paths come from fixed route definitions and URL-encoded icon keys.
    command += ' \\\n  "$API_BASE'+path+'"';
    $('requestExample').textContent = command;
    $('apiCopyStatus').textContent = '';
  }
  operations.forEach(([label],index) => {
    const option=document.createElement('option');option.value=index;option.textContent=label;$('apiOperation').append(option);
  });
  for(const id of ['apiBase','apiIcon','apiHash'])$(id).addEventListener('input',render);
  $('apiOperation').addEventListener('change',render);
  document.querySelectorAll('.copy-code').forEach(button => button.addEventListener('click',async () => {
    try {await navigator.clipboard.writeText($(button.dataset.copy).textContent);button.textContent='Copied';}
    catch {$('apiCopyStatus').textContent='Select and copy the command manually.';}
  }));
  render();
})();
