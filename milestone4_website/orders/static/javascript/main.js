console.log("Sanity check!");

// Get Stripe publishable key
fetch("/orders/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
  // Event handler
  document.querySelector("#submitBtn").addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/orders/create-checkout-session/",{
        method: "POST",
        body:'[{"price": "price_1NMCoqBbL1wWy0xHQg7EtitO","quantity": 1}]'
    })
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});