/**
 * Created by travisselland on 3/21/15.
 */
$(function() {

    var file = $('#id_upload_file');

    file.off('change.uploader').on('change.uploader', function() {
        var fd = new FormData();
        var file = this.files[0];
        fd.append("upload", file);
        $.ajax({
            url: '/uploader_upload/',
            type: 'POST',
            contentType: false,
            processData: false,
            data: fd,
            xhr: function() {
                var xhr = jQuery.ajaxSettings.xhr();
                if (xhr.upload) {
                    xhr.upload.addEventListener('progress', function (evt) {
                        if (evt.lengthComputable) {
                            //update the WUI
                            console.log(evt);
                        }
                    }, false);
                }
                return xhr;
            },
            success: function(data) {
                $('id_upload_fullname').val(data);
                console.log('Success');
                console.log(data);
            },
            error: function(err) {
                console.log('Error');
                console.log(err);
            }
        });//ajax
    });//change

    file.closest('form').off('submit.uploader').on('submit.uploader', function(){
        file.remove();
    });

});//ready