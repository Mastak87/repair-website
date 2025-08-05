document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();
  alert("Дякую за звернення! Я зв’яжусь із вами найближчим часом.");
  this.reset();
});
