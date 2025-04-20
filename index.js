let slideIndex = 0;
const slides = document.querySelectorAll(".slide");

function moveSlide(step) {
  slideIndex += step;

  if (slideIndex >= slides.length) {
    slideIndex = 0;
  } else if (slideIndex < 0) {
    slideIndex = slides.length - 1;
  }

  document.querySelector(".slider").style.transform = `translateX(-${slideIndex * 100}%)`;
}

// Auto-slide every 7 seconds
setInterval(() => moveSlide(1), 7000);

  // Generic function to initialize modals
  function setupModal(modalId, openBtnId, closeBtnId) {
    const modal = document.getElementById(modalId);
    const openBtn = document.getElementById(openBtnId);
    const closeBtn = document.getElementById(closeBtnId);
    const cancelBtn = modal.querySelector(".cancelbtn");

    // Open modal
    openBtn.addEventListener("click", (e) => {
      e.preventDefault();
      modal.style.display = "block";
    });

    // Close with 'X'
    closeBtn.addEventListener("click", () => {
      modal.style.display = "none";
    });

    // Close with 'Cancel'
    cancelBtn.addEventListener("click", () => {
      modal.style.display = "none";
    });

    // Close if clicking outside the modal content
    window.addEventListener("click", (e) => {
      if (e.target === modal) {
        modal.style.display = "none";
      }
    });
  }

  // Setup for both Login and Signup modals
  setupModal("loginModal", "openLogin", "closeLogin");
  setupModal("signupModal", "openSignup", "closeSignup");
