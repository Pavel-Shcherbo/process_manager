document.addEventListener('DOMContentLoaded', function() {
    var treeData = JSON.parse(document.getElementById('process-tree').dataset.tree);
    $('#process-tree').jstree({ 'core': { 'data': treeData } });
  });