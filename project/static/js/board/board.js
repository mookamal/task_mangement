// start change desc
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
// end change desc
// start show form add checklist
$(document).on("click", ".plugin", function (event) {
  event.preventDefault();
  let idCard = $(this).attr("data-id-card");

  const toastLiveExample = document.getElementById(
    `checklistformshow-${idCard}`
  );
  const toast = new bootstrap.Toast(toastLiveExample);

  toast.show();
});
// end show form add checklist
// start show checklist
function _showCheckList(cardId,checklist) {
  let toJson = JSON.parse(checklist);
  toJson = toJson[0]
  const fields = toJson.fields;
  const title = fields.title;

  let checklistArea = $(`#checklist-area-${cardId}`);
  let card = `<div class="show-checklist">
  <div class="row header-checklist">
      <div class="col-1">
          <i class="fa-solid fa-list-check"></i>
      </div>
      <div class="col-9">
          <h6>${title}</h6>
      </div>
      <div class="col-2 text-end">
          <button type="button" class="btn btn-light btn-ms">Delete</button>
      </div>
  </div>
  <!-- start progress -->
  <div class="p-3">
      <div class="progress">
          <div class="progress-bar bg-info" role="progressbar" aria-label="Info example" style="width: 0%;" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
      </div>
  </div>
  <!-- start items list -->
  <div class="list-form-check">
  
  </div>
  <!-- start add item to checklist -->
  <div class="input-group mb-3 p-5">
      <input type="text" class="form-control" placeholder="add an item" aria-describedby="button-addon2" />
      <button class="btn btn-light" type="button" id="button-addon2">Add</button>
  </div>
</div>
`;
  checklistArea.append(card);
}
// end show checklist
// start add checklist
$(document).on("submit", ".formchecklist", function (event) {
  event.preventDefault();
  const formData = $(this).serialize();
  const cardId = $(this).find('[name="id-card"]').val();

  $.ajax({
    type: "POST",
    url: addChecklist,
    data: formData,
    headers: { "X-CSRFToken": csrfToken },
    dataType: "json",
  }).done(function (data) {
    if (data.success) {
      const toastLiveExample = document.getElementById(
        `checklistformshow-${cardId}`
      );
      const toast = new bootstrap.Toast(toastLiveExample);

      toast.hide();
      _showCheckList(cardId,data.checkList);
      _showMessage(data.success);
    }
  }); // end ajax
});
// end add checklist
