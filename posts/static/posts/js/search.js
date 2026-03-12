document.addEventListener("DOMContentLoaded", () => {
  const searchBar = document.getElementById("searchBar");
  const resultsBox = document.getElementById("searchResults");
  const searchBox = document.querySelector(".search-box");

  if (!searchBar || !resultsBox || !searchBox) {
    return;
  }

  const hideResults = () => {
    resultsBox.innerHTML = "";
    resultsBox.style.display = "none";
  };

  searchBar.addEventListener("input", async () => {
    const query = searchBar.value.trim();

    if (!query) {
      hideResults();
      return;
    }

    try {
      const response = await fetch(
        `/search/ajax/?q=${encodeURIComponent(query)}`
      );

      if (!response.ok) {
        hideResults();
        return;
      }

      const data = await response.json();
      const results = data.results || [];

      if (!results.length) {
        resultsBox.innerHTML = `
          <div class="search-item">No results found</div>
        `;
        resultsBox.style.display = "block";
        return;
      }

      resultsBox.innerHTML = results
        .map((item) => {
          return `
            <div class="search-item" data-url="/post/${item.id}/">
              <strong>${item.title}</strong><br>
              <small>@${item.author}</small>
            </div>
          `;
        })
        .join("");

      resultsBox.style.display = "block";
    } catch (error) {
      hideResults();
    }
  });

  resultsBox.addEventListener("click", (event) => {
    const item = event.target.closest(".search-item");
    if (!item || !item.dataset.url) {
      return;
    }

    window.location.href = item.dataset.url;
  });

  document.addEventListener("click", (event) => {
    if (!event.target.closest(".search-box")) {
      resultsBox.style.display = "none";
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      resultsBox.style.display = "none";
    }
  });
});