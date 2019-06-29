(function () {
    'use strict'

    feather.replace();

    $('#users-list thead tr').clone(true).appendTo('#users-list thead');
    $('#users-list thead tr:eq(1) th').each(function (i) {
        var title = $(this).text();
        $(this).html('<input type="text" placeholder="Search ' + title + '" />');

        $('input', this).on('keyup change', function () {
            if (table.column(i).search() !== this.value) {
                table
                    .column(i)
                    .search(this.value)
                    .draw();
            }
        });
    });

    var table = $('#users-list').DataTable({
        orderCellsTop: true,
        fixedHeader: true
    });

    /* --- DATA HREF --- */
    $('button[data-href]').click(function(e) {
        e.preventDefault();
        window.location.href = $(this).attr('data-href');
    });

}());