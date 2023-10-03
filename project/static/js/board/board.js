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
  const checklistId = toJson.pk;
  const fields = toJson.fields;
  const title = fields.title;

  let checklistArea = $(`#checklist-area-${cardId}`);
  let card = `<div class="show-checklist" id="box-checklist-${checklistId}">
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
  <!-- start items list -->
  <div class="p-3" id="list-form-check-${checklistId}">

  </div>
  <!-- start add item to checklist -->
  <!-- start add item to checklist -->
  <form  method="post" class="form-item-checklist">
      <div class="input-group mb-3 p-2">
          <input type="hidden" name="id-checklist" value="${checklistId}">
          <input type="text" class="form-control" name="item-checklist-name" placeholder="add an item" aria-describedby="button-addon2" />
          <button class="btn btn-light" type="submit" id="button-addon2">Add</button>
      </div>
  </form>
</div>
`;
  checklistArea.append(card);
}
// end show checklist
// start show items checklist
function _showItemChecklist(id_checklist,item) {
  item = JSON.parse(item);
  item = item[0];
  const idItem  = item.pk;
  const nameItem = item.fields.name;
  let itemsChecklistArea = $(`#list-form-check-${id_checklist}`);
  let element = `<div class="form-check">
  <input class="form-check-input" type="checkbox" value="${idItem}" id="flexCheckDefault">
  <label class="form-check-label" for="flexCheckDefault">
    ${nameItem}
  </label>
</div>`;
itemsChecklistArea.append(element);
}
// end show items checklist
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
// add item to checklist
$(document).on("submit" ,".form-item-checklist" , function (event) {
  event.preventDefault();
  const formData = $(this).serialize();
  const checklistId = $(this).find('[name="id-checklist"]').val();

  $.ajax({
    type: "POST",
    url: addItemToChecklist,
    data: formData,
    headers: { "X-CSRFToken": csrfToken },
    dataType: "json",
  }).done(function (data) {
    if (data.success) {
      _showItemChecklist(checklistId,data.item);
      _showMessage(data.success);
    }
  }); // end ajax
});
// end add item to checklist
// start change status checklist item
$(document).on("change",".form-check-input" , function (params) {
  const itemId = $(this).val();
  $.ajax({
    type: "POST",
    url: changeStatusItemChecklist,
    data: {"id-item":itemId},
    headers: { "X-CSRFToken": csrfToken },
    dataType: "json",
  }).done(function (data) {
  }); // end ajax
});
// end change status checklist item

