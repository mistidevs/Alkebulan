$(document).ready(function () {
  // Toggle .show class when .user is clicked
  $(".main-user .user").click(function (event) {
    event.stopPropagation(); // Prevent event bubbling
    $(".user-btn").toggleClass("show");
  });

  // Close .user-btn when clicking outside of .main-user
  $(document).click(function (event) {
    if (!$(event.target).closest(".main-user").length) {
      $(".user-btn").removeClass("show");
    }
  });
});
// document.addEventListener("DOMContentLoaded", function () {
//   const showDetailsBtns = document.querySelectorAll(".show-details-btn");
//   const modalContainer = document.querySelector(".modal-container");
//   const closeBtn = document.querySelector(".close");

//   showDetailsBtns.forEach(function (btn) {
//     btn.addEventListener("click", function () {
//       modalContainer.style.display = "block";
//     });
//   });

//   closeBtn.addEventListener("click", function () {
//     modalContainer.style.display = "none";
//   });

//   // Close modal when clicking outside of it
//   window.addEventListener("click", function (event) {
//     if (event.target === modalContainer) {
//       modalContainer.style.display = "none";
//     }
//   });
// });

// document.addEventListener("DOMContentLoaded", function () {
//   const modal = document.querySelector(".modal");
//   const closeModal = document.querySelector(".close");
//   const bookNowBtn = document.querySelector(".book-now");

//   // Show modal when "More Details" button is clicked
//   const showDetailsBtns = document.querySelectorAll(".show-details-btn");
//   showDetailsBtns.forEach(function (btn) {
//     btn.addEventListener("click", function () {
//       modal.style.display = "block";
//     });
//   });

//   // Close modal when the close button is clicked
//   closeModal.addEventListener("click", function () {
//     modal.style.display = "none";
//   });

//   // Close modal when clicking outside of it
//   window.addEventListener("click", function (event) {
//     if (event.target === modal) {
//       modal.style.display = "none";
//     }
//   });

//   // Additional functionality, like booking the item, can be added here
//   bookNowBtn.addEventListener("click", function () {
//     // Add your booking logic here
//     alert("Booking functionality can be added here!");
//   });
// });

document.addEventListener("DOMContentLoaded", function () {
  const showDetailsBtn = document.querySelector(".show-details-btn");
  const modalContainer = document.querySelector(".modal-container");
  const closeBtn = document.querySelector(".close");

  // Show modal with product details
  showDetailsBtn.addEventListener("click", function () {
    modalContainer.style.display = "block";
  });

  // Close modal when close button is clicked
  closeBtn.addEventListener("click", function () {
    modalContainer.style.display = "none";
  });

  // Close modal when clicking outside of it
  window.addEventListener("click", function (event) {
    if (event.target === modalContainer) {
      modalContainer.style.display = "none";
    }
  });

  // Add functionality to related products carousel (if applicable)
  // You can use libraries like Swiper or Slick for carousel functionality
});
