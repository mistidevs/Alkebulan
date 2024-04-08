$(document).ready(function () {
  $(".main-user .user").click(function (event) {
    event.stopPropagation();
    $(".user-btn").toggleClass("show");
  });

  $(document).click(function (event) {
    if (!$(event.target).closest(".main-user").length) {
      $(".user-btn").removeClass("show");
    }
  });

  $(".item").click(function () {
    window.location.href = "../templates/details.html";
  });

  $(".shop-icon").click(function () {
    window.location.href = "../templates/shop.html";
  });

  $(".remove-btn").click(function () {
    console.log("Button clicked"); // Check if this message appears in the console
    $(".cartItem").remove("article")
});

  
});
