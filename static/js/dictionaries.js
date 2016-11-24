/**
 * Created by zub on 21.11.2016.
 */
$(document).ready(function() {
    $.ajax({
         method: 'GET',
         url: "/dict_val_grid/cfg",
         success: function (data) {
             data['colNames'] = ['Значення'];
             $("#dict_vals").jqGrid(data)
         },
         error: function (data) {
                alert("An error occurred!");
                console.log(data);
            }
     });

    $.ajax({
         method: 'GET',
         url: "/dict_grid/cfg",
         success: function (data) {
             data['colNames'] = ['ID', 'Назва словника'];
             data['onSelectRow'] = function(id){
                 //alert(role);
                 //alert($("#dict_vals").jqGrid('getGridParam', 'url'));
                 var $grid = $("#dict_vals");
                 $grid.jqGrid('setGridParam', { url: "/dict_val_grid/" + id}).trigger("reloadGrid");
                 $grid.jqGrid('setCaption', "Значення словника \"" + $("#dicts").jqGrid ('getCell', id, 'name') + "\"");
             };
             $("#dicts").jqGrid(data)
         },
         error: function (data) {
                alert("An error occurred!");
                console.log(data);
            }
     });
});
