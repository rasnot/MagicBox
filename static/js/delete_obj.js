// function del_obj(id) {
//    row = $(this).closest("tr")
//    id1 = row.attr("id")
//    alert(id1)
//    $.ajax({
//    url: '/delete_dataset/' + id + '/',
//    success: function(data) {
//            row.fadeOut("normal", function() {
//            $(this).remove();
//        });
//    }
//    });
//}

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
})