// scripts.js
document.getElementById('add-to-cart-btn').addEventListener('click', function() {
    document.getElementById('payment-modal').style.display = 'block';
});

document.querySelector('.close').addEventListener('click', function() {
    document.getElementById('payment-modal').style.display = 'none';
});

window.addEventListener('click', function(event) {
    if (event.target == document.getElementById('payment-modal')) {
        document.getElementById('payment-modal').style.display = 'none';
    }
});
