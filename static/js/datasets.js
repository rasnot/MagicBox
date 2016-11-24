
$(".remover-link").on('click', function(e) {
    row = $(this).closest("tr");
    id = row.attr("id");
    $.ajax({
        url: '/delete_dataset/' + id,
        success: function (data) {
            if (data['is_delete']) {
                row.fadeOut("normal");
            } else {
                alert("Існують пов'язані дані");
            }
        }
    });
});

$(document).ready(function(){
    $("table").tablesorter({headers: { 1: { sorter: false}}});

    $.ajax({
        method: 'GET',
        url: "/dataset_grid/cfg",
        success: function (data) {
            data['pager'] = '#pager_ds';
            data['colNames'] = ['', 'ІД', 'Назва', ''];
            data['colModel'].unshift({name:'show',index:'show', width:6, sortable:false});
            data['colModel'].push({name:'del',index:'del', width:6, sortable:false});
            data['gridComplete'] = function(){
                var table = $("#datasets");
                var ids = table.jqGrid('getDataIDs');
                for(var i=0;i < ids.length;i++){
                    var cl = ids[i];
                    var row_id = table.jqGrid('getCell',cl, 'id');
                    var str1 = "<a class='del_dataset_row' index='"+ row_id +"'><button>X</button></a>";
                    var str2 = "<a class='show_dataset_row' index='"+ row_id +"' href='/dataset/"+ row_id +"'><button>"+row_id+"</button></a>";
                    table.jqGrid('setRowData',ids[i],{del:str1});
                    table.jqGrid('setRowData',ids[i],{show:str2});
                }
                $('.del_dataset_row').on('click', function(e){
                    var row = $(this).closest("tr");
                    var id = $(this).closest("a").attr("index");
                    $.ajax({
                        url: '/delete_dataset/' + id,
                        success: function (d) {
                            if (d['is_delete']) {
                                row.fadeOut("normal");
                            } else {
                                alert("Існують пов'язані дані");
                            }
                        }
                    });
                });
            };
            $("#datasets")
                .jqGrid(data)
                .navGrid('#pager_ds',
                    {add: false, edit: false, del: false, view: false},
                    {}, // edit options
                    {}, // add options
                    {}, // del options
                    {multipleSearch: false, closeOnEscape: false}, // search options
                    {jqModal: false, closeOnEscape: false} // view options
                );
            $('.ui-jqgrid-titlebar').hide();
        },
        error: function (data) {
                alert("An error occurred!");
                console.log(data);
            }
    });



});

//$(".ui-jqgrid-titlebar").hide();


