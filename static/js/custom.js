function sendArticleComment(articleId) {
    var comment = $('#conmmentText').val();
    var parentId = $('#parent_id').val();
    $.get('/articles/add-article-comment', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId,
    }).then(res => {
        $('#commentsArea').html(res);
        $('#conmmentText').val('');
        $('#parent_id').val('');

        if (parentId != null && parentId !== '') {
            document.getElementById('singleCommentBox' + parentId).scrollIntoView({behavior: "smooth"});
        } else {
            document.getElementById('commentsArea').scrollIntoView({behavior: "smooth"});
        }
    });
}


function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('commentForm').scrollIntoView({behavior: "smooth"})
}


function filterProducts(){
    const filterPrice = $('#sl2').val();
    const startPrice = filterPrice.split(',')[0];
    const endPrice = filterPrice.split(',')[1];
    $('#startPrice').val(startPrice);
    $('#endPrice').val(endPrice);
    $('#filterForm').submit();
}

function fillPage(page){
    $('#page').val(page);
    $('#filterForm').submit();
}


function showLargeImage(imageSrc){
    $('#mainImage').attr('src',imageSrc);
    $('#showLargeImageModal').attr('href',imageSrc);

}

















