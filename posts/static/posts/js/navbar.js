document.addEventListener("DOMContentLoaded", () => {
  const profileBtn = document.querySelector(".nav-profile-btn");
  const menu = document.querySelector(".profile-menu");

  if (!profileBtn || !menu) {
    return;
  }

  profileBtn.addEventListener("click", (event) => {
    event.stopPropagation();

    const isOpen = menu.style.display === "flex";
    menu.style.display = isOpen ? "none" : "flex";
  });

  menu.addEventListener("click", (event) => {
    event.stopPropagation();
  });

  document.addEventListener("click", () => {
    menu.style.display = "none";
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      menu.style.display = "none";
    }
  });
});