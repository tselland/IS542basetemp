/**
 * Created by travisselland on 2/14/15.
 */
function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    console.log("Completed JS");
}

$(function() {
    $(".datepicker").datepicker();

    $('#add_event').click(function() {
        cloneMore('div.table:last', 'eventForm');
    });
    $('#add_announcement').click(function() {
        cloneMore('div.table:last', 'announcementForm');
    });
})
