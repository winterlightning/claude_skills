(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  $('copyUploadCurl').addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText($('uploadCurl').textContent);
      $('copyUploadStatus').textContent = 'API example copied.';
    } catch {
      $('copyUploadStatus').textContent = 'Select and copy the example above.';
    }
  });
  async function loadCategories() {
    try {
      const response = await fetch('../api/icon-categories');
      if (!response.ok) throw Error('Could not load categories.');
      const data = await response.json();
      if (!Array.isArray(data.categories) || !data.categories.every(value => typeof value === 'string')) throw Error('Invalid categories.');
      $('uploadCategories').replaceChildren(...data.categories.map(value => {
        const option = document.createElement('option');
        option.value = value;
        return option;
      }));
      $('uploadCategoriesStatus').textContent = '';
    } catch {
      $('uploadCategoriesStatus').textContent = 'Current categories could not be loaded. You can still type a category.';
    }
  }
  loadCategories();
  let previewURL = null, busy = false;
  $('uploadFile').addEventListener('change', async () => {
    if (previewURL) URL.revokeObjectURL(previewURL);
    $('uploadPreview').hidden = true;
    $('uploadResult').hidden = true;
    $('uploadMessage').textContent = '';
    const file = $('uploadFile').files[0];
    if (!file) return;
    if (file.size > 1024 * 1024 || !/\.svg$/i.test(file.name)) {
      $('uploadMessage').textContent = 'Choose an SVG file up to 1 MB.';
      $('uploadFile').value = '';
      return;
    }
    if (!$('uploadName').value.trim()) $('uploadName').value = file.name.replace(/\.svg$/i, '').replace(/[-_]/g, ' ').slice(0, 120);
    const text = await file.text();
    if ($('uploadFile').files[0] !== file) return;
    const svg = new DOMParser().parseFromString(text, 'image/svg+xml').documentElement;
    const view = (svg.getAttribute('viewBox') || '').trim().split(/[\s,]+/).map(Number);
    if (view.length === 4 && view[0] === 0 && view[1] === 0 && view[2] === view[3]) {
      const family = {32:'sub',48:'solo',64:'container'}[view[2]];
      if (family) $('uploadFamily').value = family;
    }
    previewURL = URL.createObjectURL(new Blob([text], {type:'image/svg+xml'}));
    $('uploadPreview').src = previewURL;
    $('uploadPreview').hidden = false;
  });
  $('uploadForm').addEventListener('submit', async event => {
    event.preventDefault();
    if (busy) return;
    const file = $('uploadFile').files[0];
    if (!file) return;
    busy = true;
    const inputs = [...$('uploadForm').querySelectorAll('input,select,button')];
    const data = {name:$('uploadName').value.trim(), family:$('uploadFamily').value, category:$('uploadCategory').value.trim(), bypass_validation:!$('uploadValidation').checked};
    inputs.forEach(input => input.disabled = true);
    $('uploadMessage').textContent = 'Uploading…';
    $('uploadResult').hidden = true;
    try {
      data.svg = await file.text();
      const response = await fetch('../api/icons/upload', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
      const result = await response.json();
      if (!response.ok) throw Error([result.error || 'Could not upload the icon.', ...(result.validation?.errors || [])].join(' '));
      $('uploadReview').href = 'index.html?' + new URLSearchParams({status:'ready',family:result.record.family,q:result.record.icon_id});
      $('uploadResult').hidden = false;
      $('uploadMessage').textContent = 'Saved. Your icon is Ready for review.';
      $('uploadForm').reset();
      loadCategories();
      $('uploadPreview').hidden = true;
      if (previewURL) { URL.revokeObjectURL(previewURL); previewURL = null; }
      $('uploadReview').focus();
    } catch (error) {
      $('uploadMessage').textContent = error.message || 'Unable to connect. Please retry.';
    } finally {
      busy = false;
      inputs.forEach(input => input.disabled = false);
    }
  });
})();
