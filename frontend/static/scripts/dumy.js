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
  
    $(document).on("click", ".item", function (event) {
      if ($(event.target).is("#add-to-cart")) {
        event.preventDefault();
        // addItem($(this).attr("product-id"));
      } else {
        window.location.href = "../templates/details.html";
      }
    });
  
    $(document).on("click", "#add-to-cart", function (event) {
      let id_product = $(this).parent().data("id");
      addToCart(id_product);
    });
  
    const addToCart = (product_id) => {
      let positionThisProductInCart = cart.findIndex(
        (value) => value.product_id == product_id
      );
      if (cart.length <= 0) {
        cart = [
          {
            product_id: product_id,
            quantity: 1,
          },
        ];
      } else if (positionThisProductInCart < 0) {
        cart.push({
          product_id: product_id,
          quantity: 1,
        });
      } else {
        cart[positionThisProductInCart].quantity =
          cart[positionThisProductInCart].quantity + 1;
      }
      addCartToHTML();
      addCartToMemory();
    };
  
    const addCartToMemory = () => {
      localStorage.setItem("cart", JSON.stringify(cart));
    };
  
    const addCartToHTML = () => {
      $listCartHTML.empty();
      let totalQuantity = 0;
      if (cart.length > 0) {
        $.each(cart, function (index, item) {
          totalQuantity += item.quantity;
          let positionProduct = products.findIndex(
            (value) => value.id == item.product_id
          );
          let info = products[positionProduct];
          let $newItem = $("<div>")
            .addClass("item")
            .attr("data-id", item.product_id)
            .html(
              `<div class="image"><img src="${info.image}"></div>
                   <div class="name">${info.name}</div>
                   <div class="totalPrice">$${info.price * item.quantity}</div>
                   <div class="quantity">
                       <span class="minus"><</span>
                       <span>${item.quantity}</span>
                       <span class="plus">></span>
                   </div>`
            );
          $listCartHTML.append($newItem);
        });
      }
      $(".shop-icon span").text(totalQuantity);
    };
    $(".shop-icon").click(function () {
      window.location.href = "../templates/shop.html";
    });
  
    $(".remove-btn").click(function () {
      console.log("Button clicked");
      $(".cartItem").remove("article");
    });
  
    $.ajax({
      url: "/Alkebulan/frontend/products.json",
      type: "GET",
      dataType: "json",
      success: function (data) {
        $.each(data.slice(0, 3), function (index, product) {
          let productHTML = `<article class="item" data-id="${product.id}">
                                  <img src="${product.image}" alt="" class="product-image" />
                                  <h2>${product.name}</h2>
                                  <div class="price">
                                      <div class="newPrice"><span>$${product.price}</span></div>
                                      <div class="oldPrice"><del>$${product.wasPrice}</del></div>
                                  </div>
                              <button class="add-to-cart-btn" id="add-to-cart"><i class="fas fa-shopping-cart"></i>&nbsp; ADD TO CART</button>
                            </article>`;
  
          $("#add-product").append(productHTML);
        });
      },
      error: function (jqXHR, textStatus, errorThrown) {
        console.log("Error:", errorThrown);
      },
    });
    let cart = [];
    $.ajax({
      url: "/Alkebulan/frontend/products.json",
      type: "GET",
      dataType: "json",
      success: function (data) {
        $.each(data, function (index, product) {
          let productHTML = `<article class="item" data-id="${product.id}">
                                  <img src="${product.image}" alt="" class="product-image" />
                                  <h2>${product.name}</h2>
                                  <div class="price">
                                      <div class="newPrice"><span>$${product.price}</span></div>
                                      <div class="oldPrice"><del>$${product.wasPrice}</del></div>
                                  </div>
                              <button class="add-to-cart-btn" id="add-to-cart"><i class="fas fa-shopping-cart"></i>&nbsp; ADD TO CART</button>
                            </article>`;
          cart.push(product);
          $(".products").append(productHTML);
        });
      },
    });
  
    $.ajax({
      url: "/Alkebulan/frontend/products.json",
      type: "GET",
      datatype: "json",
      success: function (data) {
        $.each(data.slice(0, 3), function (index, product) {
          let productHTML = `<article class="item" data-id="${product.id}">
                                  <img src="${product.image}" alt="" class="product-image" />
                                  <h2>${product.name}</h2>
                                  <div class="price">
                                      <div class="newPrice"><span>$${product.price}</span></div>
                                      <div class="oldPrice"><del>$${product.wasPrice}</del></div>
                                  </div>
                              <button class="add-to-cart-btn" id="add-to-cart"><i class="fas fa-shopping-cart"></i>&nbsp; ADD TO CART</button>
                            </article>`;
          $(".related-products").append(productHTML);
        });
      },
    });
  });
  
  $(document).ready(function() {
    let $listProductHTML = $('.listProduct');
    let $listCartHTML = $('.listCart');
    let $iconCart = $('.icon-cart');
    let $iconCartSpan = $('.icon-cart span');
    let $body = $('body');
    let $closeCart = $('.close');
    let products = [];
    let cart = [];

    $iconCart.on('click', function() {
        $body.toggleClass('showCart');
    });

    $closeCart.on('click', function() {
        $body.toggleClass('showCart');
    });

    const addDataToHTML = () => {
        // Remove default data from HTML
        // Add new data
        if (products.length > 0) { // If there is data
            $.each(products, function(index, product) {
                let $newProduct = $('<div>').addClass('item').attr('data-id', product.id).html(
                    `<img src="${product.image}" alt="">
                     <h2>${product.name}</h2>
                     <div class="price">$${product.price}</div>
                     <button class="addCart">Add To Cart</button>`
                );
                $listProductHTML.append($newProduct);
            });
        }
    };

    $listProductHTML.on('click', '.addCart', function(event) {
        let id_product = $(this).parent().data('id');
        addToCart(id_product);
    });

    const addToCart = (product_id) => {
        let positionThisProductInCart = cart.findIndex((value) => value.product_id == product_id);
        if (cart.length <= 0) {
            cart = [{
                product_id: product_id,
                quantity: 1
            }];
        } else if (positionThisProductInCart < 0) {
            cart.push({
                product_id: product_id,
                quantity: 1
            });
        } else {
            cart[positionThisProductInCart].quantity = cart[positionThisProductInCart].quantity + 1;
        }
        addCartToHTML();
        addCartToMemory();
    };

    const addCartToMemory = () => {
        localStorage.setItem('cart', JSON.stringify(cart));
    };

    const addCartToHTML = () => {
        $listCartHTML.empty();
        let totalQuantity = 0;
        if (cart.length > 0) {
            $.each(cart, function(index, item) {
                totalQuantity += item.quantity;
                let positionProduct = products.findIndex((value) => value.id == item.product_id);
                let info = products[positionProduct];
                let $newItem = $('<div>').addClass('item').attr('data-id', item.product_id).html(
                    `<div class="image"><img src="${info.image}"></div>
                     <div class="name">${info.name}</div>
                     <div class="totalPrice">$${info.price * item.quantity}</div>
                     <div class="quantity">
                         <span class="minus"><</span>
                         <span>${item.quantity}</span>
                         <span class="plus">></span>
                     </div>`
                );
                $listCartHTML.append($newItem);
            });
        }
        $iconCartSpan.text(totalQuantity);
    };

    $listCartHTML.on('click', '.minus, .plus', function(event) {
        let product_id = $(this).closest('.item').data('id');
        let type = $(this).hasClass('plus') ? 'plus' : 'minus';
        changeQuantityCart(product_id, type);
    });

    const changeQuantityCart = (product_id, type) => {
        let positionItemInCart = cart.findIndex((value) => value.product_id == product_id);
        if (positionItemInCart >= 0) {
            let info = cart[positionItemInCart];
            switch (type) {
                case 'plus':
                    cart[positionItemInCart].quantity = cart[positionItemInCart].quantity + 1;
                    break;
                default:
                    let changeQuantity = cart[positionItemInCart].quantity - 1;
                    if (changeQuantity > 0) {
                        cart[positionItemInCart].quantity = changeQuantity;
                    } else {
                        cart.splice(positionItemInCart, 1);
                    }
                    break;
            }
        }
        addCartToHTML();
        addCartToMemory();
    };

    const initApp = () => {
        // Get product data
        $.getJSON('products.json', function(data) {
            products = data;
            addDataToHTML();

            // Get cart data from memory
            if (localStorage.getItem('cart')) {
                cart = JSON.parse(localStorage.getItem('cart'));
                addCartToHTML();    
            }
        });
    };

    initApp();
});







else {
  let productHTML = `<div class="product-img-list">
  <img src="../static/images/vegetable2.jpeg" alt="Product Image"/>
  <div class="product-next-img">
    <img src="../static/images/vegetable2.jpeg" alt="Product Image" />
    <img src="../static/images/vegetable2.jpeg" alt="Product Image" />
    <img src="../static/images/vegetable2.jpeg" alt="Product Image" />
  </div>
</div>

<div class="product-info">
  <h2>Multiphos</h2>
  <div class="price">
    <span class="newPrice">$200</span> <del class="oldPrice">$20</del>
  </div>
  <p>
    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Hic ea corporis doloremque iste doloribus voluptas saepe provident, inventore dolor, necessitatibus magnam omnis reiciendis minima eum aliquam laboriosam itaque? Officia, aperiam?
  </p>
  <button class="add-to-cart-btn" id="#add-to-cart-details"><i class="fas fa-shopping-cart"></i> &nbsp; ADD TO CART</button>
</div>`;

  window.location.href = "../templates/details.html";
  $(".selected-product").append(productHTML);
}



$("#add-to-cart-details").on("click", function (event) {
  setInterval(autoRefresh, 100);
  let product_id = $(this).attr("data-id");
  let ceckID = cart.find((ele) => ele.product_id == product_id);
  if (ceckID) {
    e.preventDefault();
  } else {
    setInterval(autoRefresh, 100);
    addToCart(product_id);
  }
});