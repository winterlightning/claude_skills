(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const number = value => value.toLocaleString();
  const name = value => value.charAt(0).toUpperCase() + value.slice(1);
  const outcomes = ['approved', 'disapproved', 'rejected'];
  let request = 0, snapshot = null;
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
    if (!custom) {
      $('end').value = today();
      $('start').value = shiftDate($('end').value, 1 - Number($('period').value));
    }
  }
  function restoreURL() {
    const params = new URLSearchParams(location.search);
    for (const id of ['timezone', 'period']) {
      if ([...$(id).options].some(option => option.value === params.get(id))) $(id).value = params.get(id);
    }
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
    for (const id of ['reviewer', 'period', 'timezone']) if ($(id).value) params.set(id, $(id).value);
    if ($('period').value === 'custom') for (const id of ['start', 'end']) params.set(id, $(id).value);
    history.replaceState(null, '', '?' + params);
  }
  function cell(row, value, tag = 'td') {
    const element = document.createElement(tag);
    element.textContent = typeof value === 'number' ? number(value) : value;
    row.append(element);
    return element;
  }
  function draw(data) {
    for (const key of ['total', ...outcomes]) $(key).textContent = number(data.totals[key]);
    $('uniqueCount').textContent = number(data.unique_icons) + ' distinct icons across the period';
    $('rangeTitle').textContent = `${data.reviewer ? name(data.reviewer) : 'All reviewers'} · ${dateLabel(data.start, true)}${data.start === data.end ? '' : ' – ' + dateLabel(data.end, true)}`;
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
      link.href = 'index.html?' + new URLSearchParams({reviewer: reviewer.reviewer, family: ''});
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
      ? 'Activity history starts ' + new Intl.DateTimeFormat('en', {timeZone: data.timezone, dateStyle: 'medium'}).format(new Date(data.history_since)) + '. Reviews made before activity tracking began are not included.'
      : 'No activity history has been recorded yet. New reviews will appear here.';
    $('updatedAt').textContent = 'Updated ' + new Date().toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'});
    const selected = $('reviewer').value;
    $('reviewer').replaceChildren(new Option('All reviewers', ''), ...data.available_reviewers.map(user => new Option(name(user), user)));
    $('reviewer').value = selected;
  }
  async function refresh() {
    syncDates();
    const current = ++request;
    snapshot = null;
    $('dashboardContent').hidden = true;
    $('updatedAt').textContent = '';
    $('dashboardStatus').dataset.error = 'false';
    $('dashboardStatus').textContent = 'Loading review activity…';
    $('refresh').disabled = true;
    try {
      if (!$('start').value || !$('end').value) throw Error('Choose a start and end date.');
      const params = new URLSearchParams();
      for (const key of ['start', 'end', 'timezone', 'reviewer']) params.set(key, $(key).value);
      saveURL();
      const response = await fetch('../api/reviewer-stats?' + params, {cache: 'no-store'});
      const data = await response.json();
      if (!response.ok) throw Error(data.error || 'Could not load reviewer activity.');
      if (current !== request) return;
      draw(data); snapshot = data;
      $('dashboardContent').hidden = false;
      $('dashboardStatus').textContent = '';
    } catch (error) {
      if (current !== request) return;
      $('dashboardStatus').dataset.error = 'true';
      $('dashboardStatus').textContent = (error.message || 'Could not load reviewer activity.') + ' Use Refresh to try again.';
    } finally {
      if (current === request) $('refresh').disabled = false;
    }
  }
  $('dashboardFilters').onsubmit = event => {event.preventDefault(); refresh();};
  for (const id of ['reviewer', 'period', 'timezone', 'start', 'end']) $(id).onchange = refresh;
  $('exportCsv').onclick = () => {
    if (!snapshot) return;
    const rows = [['Date', 'Reviewer', 'Time zone', 'Reviewed', 'Approved', 'Disapproved', 'Rejected'],
      ...snapshot.reviewer_daily.map(day => [day.date, day.reviewer, snapshot.timezone, day.total, day.approved, day.disapproved, day.rejected])];
    const csv = rows.map(row => row.map(value => '"' + String(value).replace(/^[=+@-]/, "'$&").replaceAll('"', '""') + '"').join(',')).join('\r\n');
    const url = URL.createObjectURL(new Blob(['\uFEFF' + csv], {type: 'text/csv;charset=utf-8;'}));
    const link = document.createElement('a'); link.href = url; link.download = `reviewers-${snapshot.start}-${snapshot.end}.csv`; link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  restoreURL(); refresh();
})();
