(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const number = value => value.toLocaleString();
  const name = value => value.charAt(0).toUpperCase() + value.slice(1);
  const outcomes = ['approved', 'disapproved', 'rejected'];
  const AUTO_REFRESH_MS = 60000;
  let request = 0, snapshot = null, loading = false, loadedAt = 0;
  const localZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  if (localZone && ![...$('timezone').options].some(option => option.value === localZone)) {
    $('timezone').add(new Option('Local · ' + localZone.replaceAll('_', ' '), localZone));
  }
  function today() {
    const parts = new Intl.DateTimeFormat('en-US', {timeZone: $('timezone').value, year: 'numeric', month: '2-digit', day: '2-digit'}).formatToParts(new Date());
    const part = key => parts.find(item => item.type === key).value;
    return `${part('year')}-${part('month')}-${part('day')}`;
  }
  function shiftDate(day, offset) {
    const date = new Date(day + 'T12:00:00Z');
    date.setUTCDate(date.getUTCDate() + offset);
    return date.toISOString().slice(0, 10);
  }
  function dateLabel(value, long = false) {
    return new Intl.DateTimeFormat('en', {timeZone: 'UTC', month: 'short', day: 'numeric', ...(long ? {year: 'numeric'} : {})}).format(new Date(value + 'T12:00:00Z'));
  }
  function syncDates() {
    const custom = $('period').value === 'custom';
    $('startLabel').hidden = $('endLabel').hidden = !custom;
    $('start').required = $('end').required = custom;
    if ($('period').value === 'all') {
      $('end').value = today();
    } else if (!custom) {
      $('end').value = today();
      $('start').value = shiftDate($('end').value, 1 - Number($('period').value));
    }
  }
  function restoreURL() {
    const params = new URLSearchParams(location.search);
    for (const id of ['timezone', 'period', 'family']) {
      if ([...$(id).options].some(option => option.value === params.get(id))) $(id).value = params.get(id);
    }
    // Like Icon review: no family in the URL means Solo; an empty family means all.
    if (!params.has('family')) $('family').value = 'solo';
    const user = params.get('reviewer') || '';
    if (user && ![...$('reviewer').options].some(option => option.value === user)) $('reviewer').add(new Option(name(user), user));
    $('reviewer').value = user;
    syncDates();
    if ($('period').value === 'custom') {
      $('start').value = params.get('start') || shiftDate(today(), -6);
      $('end').value = params.get('end') || today();
    }
  }
  function saveURL() {
    const params = new URLSearchParams();
    for (const id of ['reviewer', 'family', 'period', 'timezone']) if ($(id).value || id === 'family') params.set(id, $(id).value);
    if ($('period').value === 'custom') for (const id of ['start', 'end']) params.set(id, $(id).value);
    history.replaceState(null, '', '?' + params);
  }
  function cell(row, value, tag = 'td') {
    const element = document.createElement(tag);
    element.textContent = typeof value === 'number' ? number(value) : value;
    row.append(element);
    return element;
  }
  function familyRows(target, rows, keys) {
    const fragment = document.createDocumentFragment();
    for (const family of rows) {
      const row = document.createElement('tr'); cell(row, name(family.family));
      for (const key of keys) cell(row, family[key]);
      fragment.append(row);
    }
    $(target).replaceChildren(fragment);
  }
  function drawCurrent(current, reviewer, family) {
    // Different families are separate sets; never present one combined total.
    $('currentCards').hidden = !family;
    $('currentFamilies').hidden = !!family;
    for (const key of ['approved', 'disapproved', 'rejected', 'ready']) $('current' + name(key)).textContent = number(current.totals[key]);
    $('currentReviewed').textContent = number(current.totals.total - current.totals.ready);
    $('currentScope').textContent = (reviewer ? 'By ' + name(reviewer) + ' · ' : '') + number(current.totals.total) + ' icons in catalog';
    $('currentSummary').textContent = `Live from the review database, the same numbers as Icon review${family ? ' filtered to ' + name(family) : ''}, for all time.`;
    familyRows('familyRows', current.families, ['total', 'approved', 'disapproved', 'rejected', 'ready']);
    const people = document.createDocumentFragment();
    for (const person of current.reviewers) {
      const row = document.createElement('tr'); cell(row, name(person.reviewer));
      for (const key of ['total', 'approved', 'disapproved', 'rejected']) cell(row, person[key]);
      people.append(row);
    }
    $('currentReviewerRows').replaceChildren(people);
  }
  function draw(data) {
    drawCurrent(data.current, data.reviewer, data.family);
    $('rangeTitle').textContent = `${data.reviewer ? name(data.reviewer) : 'All reviewers'}${data.family ? ' · ' + name(data.family) : ''} · ${dateLabel(data.start, true)}${data.start === data.end ? '' : ' – ' + dateLabel(data.end, true)}`;
    $('activitySummary').textContent = `${(data.totals.total / data.daily.length).toLocaleString(undefined, {maximumFractionDigits: 1})} reviews per day on average · ${data.timezone.replaceAll('_', ' ')}`;
    $('emptyActivity').hidden = data.totals.total !== 0;
    const maximum = Math.max(1, ...data.daily.map(day => day.total));
    const chart = document.createDocumentFragment();
    for (const day of data.daily) {
      const column = document.createElement('div');
      column.className = 'chart-day';
      column.setAttribute('role', 'listitem');
      column.setAttribute('aria-label', `${dateLabel(day.date, true)}: ${day.total} reviewed, ${day.approved} approved, ${day.disapproved} disapproved, ${day.rejected} rejected`);
      column.title = column.getAttribute('aria-label');
      const track = document.createElement('div'); track.className = 'chart-track';
      const total = document.createElement('span'); total.className = 'chart-total'; total.textContent = number(day.total);
      const stack = document.createElement('div'); stack.className = 'chart-stack';
      stack.style.height = (day.total / maximum * 158) + 'px';
      for (const outcome of outcomes) {
        const segment = document.createElement('div'); segment.className = 'chart-segment ' + outcome;
        segment.style.height = (day.total ? day[outcome] / day.total * 100 : 0) + '%';
        stack.append(segment);
      }
      track.append(total, stack);
      const label = document.createElement('span'); label.textContent = dateLabel(day.date);
      column.append(track, label); chart.append(column);
    }
    $('dailyChart').replaceChildren(chart);
    const team = document.createDocumentFragment();
    for (const reviewer of data.reviewers) {
      const row = document.createElement('tr');
      const identity = cell(row, '');
      const label = document.createElement('span'); label.className = 'reviewer-name';
      const avatar = document.createElement('span'); avatar.className = 'avatar'; avatar.setAttribute('aria-hidden', 'true'); avatar.textContent = reviewer.reviewer.slice(0, 2).toUpperCase();
      label.append(avatar, document.createTextNode(name(reviewer.reviewer))); identity.append(label);
      for (const key of ['total', ...outcomes, 'active_days']) cell(row, reviewer[key]);
      const link = document.createElement('a'); link.textContent = 'View icons ↗';
      link.href = 'index.html?' + new URLSearchParams({reviewer: reviewer.reviewer, family: data.family});
      link.setAttribute('aria-label', 'View current icons reviewed by ' + name(reviewer.reviewer));
      cell(row, '').append(link); team.append(row);
    }
    $('reviewerRows').replaceChildren(team);
    const days = document.createDocumentFragment();
    for (const day of [...data.daily].reverse()) {
      const row = document.createElement('tr'); cell(row, dateLabel(day.date, true));
      for (const key of ['total', ...outcomes]) cell(row, day[key]);
      days.append(row);
    }
    $('dailyRows').replaceChildren(days);
    $('historyNote').textContent = data.history_since
      ? 'The oldest current decision was made ' + new Intl.DateTimeFormat('en', {timeZone: data.timezone, dateStyle: 'medium'}).format(new Date(data.history_since)) + '. Legacy decisions keep their original date and are attributed to their reviewer.'
      : 'No icons have been reviewed yet. New reviews will appear here.';
    $('updatedAt').textContent = 'Updated ' + new Date().toLocaleTimeString([], {hour: '2-digit', minute: '2-digit', second: '2-digit'}) + ' · refreshes every minute';
    // Rebuilding an unchanged list would close it while someone is choosing.
    const known = [...$('reviewer').options].slice(1).map(option => option.value).join();
    if (known !== data.available_reviewers.join()) {
      const selected = $('reviewer').value;
      $('reviewer').replaceChildren(new Option('All reviewers', ''), ...data.available_reviewers.map(user => new Option(name(user), user)));
      $('reviewer').value = selected;
    }
  }
  // Background refreshes keep the current numbers on screen and never interrupt a manual load.
  async function refresh(background = false) {
    if (background && (loading || !snapshot)) return;
    syncDates();
    const current = ++request;
    loading = true;
    if (!background) {
      snapshot = null;
      $('dashboardContent').hidden = true;
      $('updatedAt').textContent = '';
      $('dashboardStatus').dataset.error = 'false';
      $('dashboardStatus').textContent = 'Loading review activity…';
      $('refresh').disabled = true;
    }
    try {
      if ((!$('start').value && $('period').value !== 'all') || !$('end').value) throw Error('Choose a start and end date.');
      const params = new URLSearchParams();
      for (const key of ['end', 'timezone', 'reviewer', 'family']) params.set(key, $(key).value);
      if ($('period').value === 'all') params.set('period', 'all'); else params.set('start', $('start').value);
      saveURL();
      const response = await fetch('../api/reviewer-stats?' + params, {cache: 'no-store'});
      const data = await response.json();
      if (!response.ok) throw Error(data.error || 'Could not load reviewer activity.');
      if (current !== request) return;
      $('start').value = data.start;
      draw(data); snapshot = data; loadedAt = Date.now();
      $('dashboardContent').hidden = false;
      $('dashboardStatus').textContent = '';
    } catch (error) {
      if (current !== request) return;
      if (background) {
        $('updatedAt').textContent = 'Could not refresh at ' + new Date().toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'}) + ' · retrying';
        return;
      }
      $('dashboardStatus').dataset.error = 'true';
      $('dashboardStatus').textContent = (error.message || 'Could not load reviewer activity.') + ' Use Refresh to try again.';
    } finally {
      if (current === request) {
        loading = false;
        $('refresh').disabled = false;
      }
    }
  }
  $('dashboardFilters').onsubmit = event => {event.preventDefault(); refresh();};
  for (const id of ['reviewer', 'family', 'period', 'timezone', 'start', 'end']) $(id).onchange = () => refresh();
  setInterval(() => { if (!document.hidden) refresh(true); }, AUTO_REFRESH_MS);
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden && Date.now() - loadedAt >= AUTO_REFRESH_MS) refresh(true);
  });
  $('exportCsv').onclick = () => {
    if (!snapshot) return;
    const rows = [['Date', 'Reviewer', 'Time zone', 'Reviewed', 'Approved', 'Disapproved', 'Rejected'],
      ...snapshot.reviewer_daily.map(day => [day.date, day.reviewer, snapshot.timezone, day.total, day.approved, day.disapproved, day.rejected])];
    const csv = rows.map(row => row.map(value => '"' + String(value).replace(/^[=+@-]/, "'$&").replaceAll('"', '""') + '"').join(',')).join('\r\n');
    const url = URL.createObjectURL(new Blob(['\uFEFF' + csv], {type: 'text/csv;charset=utf-8;'}));
    const link = document.createElement('a'); link.href = url; link.download = `reviewers-${snapshot.start}-${snapshot.end}.csv`; link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  // Pull production's reviewing data into this machine's database, then reload the numbers.
  const SYNC_KEY = 'pictographic-sync-source';
  const when = stamp => new Date(stamp).toLocaleString([], {dateStyle: 'medium', timeStyle: 'short'});
  function syncMessage(text, error = false) { $('syncStatus').textContent = text; $('syncStatus').dataset.error = String(error); }
  async function loadSync() {
    try {
      const response = await fetch('../api/feedback-db/sync', {cache: 'no-store'});
      if (!response.ok) return;
      const data = await response.json();
      let saved = '';
      try { saved = localStorage.getItem(SYNC_KEY) || ''; } catch {}
      if (!$('syncSource').value) $('syncSource').value = saved || data.default_source || '';
      if (data.last_sync) syncMessage(`Last synced ${when(data.last_sync.created_at)} by ${name(data.last_sync.user)} from ${data.last_sync.source}.`);
      $('syncForm').hidden = false;
    } catch {}
  }
  $('syncForm').onsubmit = async event => {
    event.preventDefault();
    const source = $('syncSource').value.trim();
    $('syncNow').disabled = true; $('syncNow').textContent = 'Syncing…';
    syncMessage('Downloading the production database…');
    try {
      const response = await fetch('../api/feedback-db/sync', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({source})});
      const data = await response.json().catch(() => ({}));
      if (!response.ok) throw Error(data.error || 'Sync failed. Please retry.');
      try { localStorage.setItem(SYNC_KEY, source); } catch {}
      const counts = data.counts;
      syncMessage(`Synced from ${data.source}: ${number(counts.feedback)} feedback, ${number(counts.reviews)} reviews, ${number(counts.icon_flags)} flags. Previous database saved as ${data.backup}.`);
      refresh();
    } catch (error) {
      syncMessage(error.message, true);
    } finally {
      $('syncNow').disabled = false; $('syncNow').textContent = 'Sync now';
    }
  };
  restoreURL(); refresh(); loadSync();
})();
