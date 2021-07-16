// $('#frm-add-post').on('submit', function (e) {
//     e.preventDefault();
//     console.log('in submit function');
//     let form = $(this);
//     let url = form.attr('action');
//     let csrftoken = $("[name=csrfmiddlewaretoken]").val();
//     let message = $('#submit-message');
//
//     $.ajax({
//         type: "post",
//
//         url: url,
//         headers: {
//             "X-CSRFToken": csrftoken
//         },
//         data: form.serialize(),
//
//         success: function () {
//             console.log('ok done');
//
//             message.css("background-color", "#06d6a0");
//             message.text('پست شما با موفقیت ثبت شد.');
//             message.show();
//
//             $('#sign-in-news').val(" ");
//             // $(".sign-in-form-container").load('div.sign-in-form-container');
//             error.fadeOut(5000);
//
//         },
//         error: function () {
//             console.log('error in get data');
//             message.css("background-color", "#f4a261");
//             message.text('در تکمیل پست شما خطایی رخ داده است!');
//             message.show();
//             message.fadeOut(5000);
//
//         },
//
//     });
// })