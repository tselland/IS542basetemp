/**
 * Created by travisselland on 3/13/15.
 */
$(function(){

    var container = $('#table_container');

    $('#previous_page_btn').off('click.page').on('click.page', function() {
        var page = parseInt(container.data('page'));
        console.log('previous page!');
        console.log(page);
        container.data('page', Math.max(0, page-1));
        //container.trigger('table_refresh');

    });

    $('#next_page_btn').off('click.page').on('click.page', function() {
        var page = parseInt(container.data('page'));
        console.log('next page!');
        container.data('page', Math.min(20, page+1));
        //container.trigger('table_refresh');
        console.log(page);
    });

    container.on('table_refresh', function() {
        $.ajax({
            url: '/pagination/get_table/',
            data: {
                table_page: container.data('page')
            }
        }).success(function(data) {
              container.html(data)
        });
    });
    container.trigger('table_refresh');
});