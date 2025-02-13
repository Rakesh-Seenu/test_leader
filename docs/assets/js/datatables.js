$(document).ready(function () {
    $("table").DataTable({
        paging: true,
        searching: true,
        order: [[1, "desc"]],
        buttons: ["copy", "csv", "excel", "pdf", "print"],
        dom: "Bfrtip",
    });
});
