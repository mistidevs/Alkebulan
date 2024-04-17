$(document).ready(function () {
  let products = [];
  let cart = [];
  let details;
  let totalPrice = 0;
  let totalQuantity = 0;

  /* ds */
  $(document).on("click", ".item", function (e) {
    let product_id = $(this).attr("data-id");
    let ceckID = cart.find((ele) => ele.product_id == product_id);
    if ($(e.target).is("#add-to-cart")) {
      e.preventDefault();
      if (ceckID) {
        e.preventDefault();
      } else {
        setInterval(autoRefresh, 100);
        addToCart(product_id);
      }
    } else {
      let positionProduct = products.findIndex(
        (value) => value.id == product_id
      );
      item = products[positionProduct];
      let details = item;
      let productHTML = `<div class="product-img-list">
          <img src="${details.picture}" alt="Product Image"/>
        </div>

        <div class="product-info">
          <h2>${details.name}</h2>
          <div class="price">
            <span class="newPrice">$${details.recommended_price}</span> <del class="oldPrice">$${details.oldprice}</del>
          </div>
          <p>${details.description}</p>
          <button class="add-to-cart-btn" id="#add-to-cart-item"><i class="fas fa-shopping-cart"></i> &nbsp; ADD TO CART</button>
        </div>`;
      $(".selected-product").empty().append(productHTML);
      localStorage.setItem("details", JSON.stringify(details));
    }
  });
  $(".selected-product").on("click", function (event) {
    e.preventDefault();
    let product_id = $(this).attr("data-id");
    addToCart(product_id);
  });
  /* add item to cart */
  function addToCart(product_id) {
    let checkItemExistence = cart.findIndex(
      (element) => element.product_id == product_id
    );

    if (cart.length <= 0) {
      cart = [
        {
          product_id: product_id,
          quantity: 1,
        },
      ];
    } else if (checkItemExistence < 0) {
      cart.push({
        product_id: product_id,
        quantity: 1,
      });
    } else {
      cart[checkItemExistence].quantity += 1;
    }
    addToMemory();
  }

  const addToMemory = () => {
    localStorage.setItem("cart", JSON.stringify(cart));
    localStorage.setItem("details", JSON.stringify(details));
  };

  const addToHtml = () => {
    $(".shop").empty();

    if (cart.length > 0) {
      $.each(cart, function (index, item) {
        totalQuantity += item.quantity;
        let positionProduct = products.findIndex(
          (value) => value.id == item.product_id
        );
        let info = products[positionProduct];
        let itemPrice = totalQuantity * info.recommended_price;
        totalPrice += itemPrice;
        let productHTML = `<article class="cartItem" data-id="${item.product_id}">
                        <div class="leftItem">
                          <div class="left-item-img-title">
                            <img
                              src="${info.image}"
                              alt=""
                              class="cartItemImage"
                            />
                            <p>${info.name}</p>
                          </div>
                          
                        </div>

                        <div class="rightItem">
                          <div class="price">
                            <div class="newPrice"><span>$${info.recommended_price}</span></div>
                          </div>
                          <div class="quantity">
                            <span class="minus"><</span>
                            <span>${item.quantity}</span>
                            <span class="plus">></span>
                          </div>
                        </div>
                      </article>
                      `;
        $(".shop").append(productHTML);
      });
    } else {
      $(".shop").append(
        "<div class='not-found' > Your basket is empty! </div1>"
      );

      $(".cart-title span").append("<p>0</p>");
    }
    if (cart.length > 0) {
      $(".shop").append(`<article class="checkout-bg">
        <h2 class="cart-title cart-summary">CART SUMMARY</h2>
        <div class="checkout">
          <div class="price newPrice"><span>$${totalPrice.toFixed(
            2
          )}</span></div>
          <button class="btn checkout-btn">Checkout</button>
        </div>
      </article>`);
      $(".cart-title span").append(totalQuantity);
    }
    $(".shop-icon span").append(totalQuantity);
  };

  $(".shop").on("click", ".minus, .plus", function (event) {
    let product_id = $(this).closest(".cartItem").data("id");
    let type = $(this).hasClass("plus") ? "plus" : "minus";
    setInterval(autoRefresh, 100);
    changeQuantityCart(product_id, type);
  });

  const changeQuantityCart = (product_id, type) => {
    let positionItemInCart = cart.findIndex(
      (value) => value.product_id == product_id
    );
    if (positionItemInCart >= 0) {
      let info = cart[positionItemInCart];
      if (type === "plus") {
        info.quantity += 1;
      } else if (type === "minus") {
        let changeQuantity = info.quantity - 1;
        if (changeQuantity > 0) {
          info.quantity = changeQuantity;
        } else {
          cart.splice(positionItemInCart, 1);
        }
      }
    }
    addToHtml();
    recalculateTotalPrice();
    addToMemory();
  };

  const recalculateTotalPrice = () => {
    totalPrice = 0;
    cart.forEach((item) => {
      let positionProduct = products.findIndex(
        (value) => value.id == item.product_id
      );
      let info = products[positionProduct];
      totalPrice += item.quantity * info.recommended_price;
    });
    $(".newPrice span").text(`$${totalPrice.toFixed(2)}`);
  };

  $.getJSON("/static/scripts/products.json", function (data) {
    products = data;
    if (localStorage.getItem("cart")) {
      cart = JSON.parse(localStorage.getItem("cart"));
      addToHtml();
    }
  });

  /* function to realod page when the user */
  /* add item to the cart or try to increas it */
  function autoRefresh() {
    location.reload();
  }
});
