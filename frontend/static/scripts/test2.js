$(document).ready(function () {
    let products = [];
    let cart = [];
  
    /* icon shop send you to shop page */
    $(".shop-icon").on("click", function () {
      window.location.href = "../templates/shop.html";
    });
  
    $.getJSON("/Alkebulan/frontend/products.json", function (data) {
      products = data;
      if (localStorage.getItem('cart')) {
        cart = JSON.parse(localStorage.getItem('cart'));
        addCartToHTML();    
    }
    });
    
    /* ds */
    $(document).on("click", ".item", function (e) {
      if ($(e.target).is("#add-to-cart")) {
        e.preventDefault();
        let product_id = $(this).attr("data-id");
        addToCart(product_id);
      } else {
        window.location.href = "../templates/details.html";
      }
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
      addCartToHTML();
      addToMemory();
    }
  
    const addCartToHTML = () => {
      $(".shop").empty();
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
              `<div class="image"><img src="${info.images[0]}"></div>
                   <div class="name">${info.name}</div>
                   <div class="totalPrice">$${info.price * item.quantity}</div>
                   <div class="quantity">
                       <span class="minus"><</span>
                       <span>${item.quantity}</span>
                       <span class="plus">></span>
                   </div>`
            );
          $(".shop").append($newItem);
        });
      }
      $(".shop-icon span").text(totalQuantity);
    };
  
    /* Store cart items in local storage */
    const addToMemory = () => {
      localStorage.setItem("cart", JSON.stringify(cart));
    };
    // const addToHtml = () => {
    //   $(".shop").empty();
    //   let totalQuantity = 0;
  
    //   if (cart.length > 0) {
    //     $.each(cart, function (index, item) {
    //       totalQuantity += item.quantity;
    //       let positionProduct = products.findIndex(
    //         (value) => value.id == item.product_id
    //       );
    //       let info = products[positionProduct];
    //       let productHTML = `<article class="cartItem">
    //                       <div class="leftItem">
    //                         <!-- <div class="left-details"> -->
    //                         <div class="left-item-img-title">
    //                           <img
    //                             src="${info.images[0]}"
    //                             alt=""
    //                             class="cartItemImage"
    //                           />
    //                           <p>${info.name}</p>
    //                         </div>
    //                         <!-- </div>  -->
    //                         <button class="add-to-cart-btn remove-btn">
    //                           <i class="fa-solid fa-trash"></i> &nbsp REMOVE
    //                         </button>
    //                       </div>
  
    //                       <div class="rightItem">
    //                         <div class="price">
    //                           <div class="newPrice"><span>$${info.newprice}</span></div>
    //                         </div>
    //                         <div class="quantity">
    //                           <span class="minus"><</span>
    //                           <span>1</span>
    //                           <span class="plus">></span>
    //                         </div>
    //                       </div>
    //                     </article>
    //                     <article class="checkout-bg">
    //                     <h2 class="cart-title cart-summary">CART SUMMARY</h2>
    //                     <div class="checkout">
    //                       <div class="price newPrice"><span>$${totalQuantity}</span></div>
    //                       <button class="btn checkout-btn">Checkout</button>
    //                     </div>
    //                   </article>
    //                     `;
    //       // return productHTML;
    //       $("#addItemToShop").append(productHTML);
    //     });
    //   } else {
    //     $(".shop").append("<div class='cartItem'> Not FOUND </div1>");
    //   }
    // };
  
    /* load data to products */
  
    /* using ajax to import data */
  
    /* import data for best-selling-products at home page */
    $.ajax({
      url: "/Alkebulan/frontend/products.json",
      type: "GET",
      datatype: "json",
      success: function (data) {
        $.each(data.slice(10, 13), function (index, product) {
          let productHTML = `<article class="item" data-id="${product.id}" data-name="${product.name}">
                              <img
                                src="${product.images[0]}"
                                alt=""
                                class="product-image"
                              />
                              <h2>${product.name}</h2>
                              <div class="price">
                                <div class="newPrice"><span>$${product.newprice}</span></div>
                                <button class="add-to-cart-btn" id="add-to-cart"><i class="fas fa-shopping-cart"></i>&nbsp;&nbsp; ADD TO CART</button>
                              </div>
                            </article>`;
  
          $(".bestSellingProducts").append(productHTML);
        });
      },
    });
  
    /* import data for products-list at home page*/
    $.ajax({
      url: "/Alkebulan/frontend/products.json",
      type: "GET",
      datatype: "json",
      success: function (data) {
        $.each(data.slice(0, 6), function (index, product) {
          let productHTML = `<article class="item" data-id="${product.id}" data-name="${product.name}">
                                  <img
                                  src="${product.images[0]}"
                                  alt=""
                                  class="product-image"
                                  />
                                <h2>${product.name}</h2>
                                <div class="price">
                                    <div class="newPrice"><span>$${product.newprice}</span></div>
                                    <div class="oldPrice"><del>$${product.oldprice}</del></div>
                                </div>
                                <button class="add-to-cart-btn" id="add-to-cart"><i class="fas fa-shopping-cart"></i>&nbsp; ADD TO CART</button>
                              </article>`;
  
          $(".listProductsHome").append(productHTML);
        });
      },
    });
  
    /* import data for products at products pages */
    $.ajax({
      url: "/Alkebulan/frontend/products.json",
      type: "GET",
      datatype: "json",
      success: function (data) {
        let num = 0;
        $.each(data, function (index, product) {
          let productHTML = `<article class="item" data-id="${product.id}" data-name="${product.name}">
                              <img
                              src="${product.images[0]}"
                              alt=""
                              class="product-image"
                              />
                              <h2>${product.name}</h2>
                              <div class="price">
                                  <div class="newPrice"><span>$${product.newprice}</span></div>
                                  <div class="oldPrice"><del>$${product.oldprice}</del></div>
                              </div>
                          <button class="add-to-cart-btn" id="add-to-cart"><i class="fas fa-shopping-cart"></i>&nbsp; ADD TO CART</button>
                        </article>`;
          num += 1;
          if (num === 9) {
            let productDot = `<h1>...</h1>`;
            $(".products").append(productDot);
            // $(".products").append(productHTML).hide();
          } else {
            $(".products").append(productHTML);
          }
        });
      },
    });
  
    /* import data for related-product at details page */
    $.ajax({
      url: "/Alkebulan/frontend/products.json",
      type: "GET",
      datatype: "json",
      success: function (data) {
        $.each(data.slice(0, 3), function (index, product) {
          let productHTML = `<article class="item" data-id="${product.id}" data-name="${product.name}">
                            <img src="${product.images[0]}" alt="" class="product-image" />
                            <h2>${product.name}</h2>
                            <div class="price">
                                <div class="newPrice"><span>$${product.newprice}</span></div>
                                <div class="oldPrice"><del>$${product.oldprice}</del></div>
                            </div>
                        <button class="add-to-cart-btn" id="add-to-cart"><i class="fas fa-shopping-cart"></i>&nbsp; ADD TO CART</button>
                      </article>`;
          $(".related-products").append(productHTML);
        });
      },
    });
  });
  