function _showMessage(msg) {
    let card = `<div class="position-fixed top-0 end-0 p-3" style="z-index: 1000;">
      <div class="alert alert-warning alert-dismissible fade show" role="alert">
        ${msg}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
    </div>`;
    $("body").prepend(card);
  
    // Automatically close the message after 5 seconds
    setTimeout(function () {
      $(".alert").alert('close');
    }, 5000);
  }
  