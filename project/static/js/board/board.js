$(document).on("submit", "#update-desc-form", function (event) {
  event.preventDefault();
  // Rest of your code
  var formData = $(this).serialize();
  $.ajax({
    type: "POST",
    url: changeDescInCard,
    data: formData,
    headers: { "X-CSRFToken": csrfToken },
    dataType: "json",
  }).done(function (data) {
    if (data.success) {
        _showMessage(data.success);
    }
  }); // end ajax
});
