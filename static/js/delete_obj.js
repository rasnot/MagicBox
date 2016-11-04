
$(".remover-link").on('click', function(e) {
    row = $(this).closest("tr");
    id = row.attr("id");
    $.ajax({
        url: '/delete_dataset/' + id + '/',
        success: function (data) {
            if (data['is_delete']) {
                row.fadeOut("normal", function () {
                    $(this).remove();
                });
            } else {
                alert("Існують пов'язані дані");
            }
        }
    });
});

$(document).ready(function(){
    $("table").tablesorter({headers: { 1: { sorter: false}}});
});
