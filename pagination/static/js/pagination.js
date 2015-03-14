/**
 * Created by travisselland on 3/13/15.
 */
$(function(){

    var container = $('#table_container');

    $('#previous_page_btn').off('click.page').on('click.page', function() {
        var page = parseInt(container.data('page'));
        console.log('previous page!');
        container.data('page', Math.max(20, page-1));
        container.trigger('table_refresh');
    });

    $('#next_page_btn').off('click.page').on('click.page', function() {
        var page = parseInt(container.data('page'));
        console.log('next page!');
        container.data('page', Math.min(0, page+1));
        container.trigger('table_refresh');
    });

    container.on('table_refresh', function() {
        $.ajax({
            url: '/pagination/tabledemo.get_table/',
            data: {
                table_page: container.data('page')
            }
        }).success(function(data) {
              container.html(data)
        });
    }).trigger('table_refresh');
});