//news
KindEditor.ready(function(K) {
    K.create('textarea[id="id_body"]', {
        width : "800px",
        height : "500px",
        uploadJson: '/admin/uploads/kindeditor',
    });
});