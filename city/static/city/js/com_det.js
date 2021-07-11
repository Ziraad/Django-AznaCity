function submitLike(id_form) {
    event.preventDefault();
    let form = $('#frm-like-' + id_form)
    let comment_id = id_form;
    let csrftoken = $("[name=csrfmiddlewaretoken]").val();

    $.ajax({
        type: "POST",
        headers: {
            "X-CSRFToken": csrftoken
        },
        url: form.attr('action'),
        data: {
            'comment_id': comment_id,
        },
        success: function (e) {
            $('body').html(e)

        },
        error: function (rs, e) {
            console.log('error');
        },

    });
}

function submitDislike(id_form) {
    event.preventDefault();
    let form = $('#frm-dislike-' + id_form)
    let comment_id = id_form;
    let csrftoken = $("[name=csrfmiddlewaretoken]").val();

    $.ajax({
        type: "POST",
        headers: {
            "X-CSRFToken": csrftoken
        },
        url: form.attr('action'),
        data: {
            'comment_id': comment_id,
        },
        success: function (e) {
            console.log('ok done');
            console.log('comment_id', comment_id);
            $('body').html(e)
        },
        error: function (rs, e) {
            console.log('error');
        },
    });
}