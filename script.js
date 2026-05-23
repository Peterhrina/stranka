/* ============================================
   INFORMATIKA PRÍRUČKA – TAB SYSTEM & INTERACTIVITY
   Vanilla JS, No Dependencies
   ============================================ */

document.addEventListener("DOMContentLoaded", () => {
  initTabs();
  initCopyButtons();
  initSubNav();
  initSidebar();
  initSecretModal();
});

// ========== FAST SCROLL ==========
function fastScrollTo(targetY) {
  const startY = window.scrollY;
  const diff = targetY - startY;
  const duration = 250; // ms (rýchly a plynulý presun)
  let start;

  window.requestAnimationFrame(function step(timestamp) {
    if (!start) start = timestamp;
    const time = timestamp - start;
    const percent = Math.min(time / duration, 1);

    // easeOutQuart (rýchly štart, pomalšie spomalenie)
    const ease = 1 - Math.pow(1 - percent, 4);

    window.scrollTo(0, startY + diff * ease);
    if (time < duration) {
      window.requestAnimationFrame(step);
    }
  });
}

// ========== TAB SYSTEM ==========

function initTabs() {
  const buttons = document.querySelectorAll(".tabs__btn");
  const contents = document.querySelectorAll(".tab-content");

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const targetId = btn.dataset.tab;

      // Deactivate all
      buttons.forEach((b) => b.classList.remove("active"));
      contents.forEach((c) => c.classList.remove("active"));

      // Activate clicked
      btn.classList.add("active");
      const target = document.getElementById(targetId);
      if (target) {
        target.classList.add("active");
      }

      // Prepneme sidebar skupinu podľa aktívneho tabu
      syncSidebarToTab(targetId);

      // Reaplikujeme aktuálny filter na nový tab (aby search platil aj po prepnutí)
      const searchInput = document.getElementById("sidebar-search");
      if (searchInput) {
        searchInput.dispatchEvent(new Event("input"));
      }
    });
  });
}

function syncSidebarToTab(tabId) {
  const groups = document.querySelectorAll(".sidebar__group");
  groups.forEach((group) => {
    if (group.dataset.tab === tabId) {
      group.hidden = false;
    } else {
      group.hidden = true;
    }
  });
}

function getActiveTabId() {
  const activeTab = document.querySelector(".tab-content.active");
  return activeTab ? activeTab.id : null;
}

// ========== SUB-NAVIGATION (Anchor links within tabs) ==========

function initSubNav() {
  // Click handler for sub-nav links
  document.querySelectorAll(".subnav__link").forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const targetId = link.getAttribute("href").substring(1);
      const target = document.getElementById(targetId);
      if (target) {
        // Offset for sticky headers (tabs + subnav)
        const offset = 120;
        const top =
          target.getBoundingClientRect().top + window.pageYOffset - offset;
        fastScrollTo(top);
      }

      // Update active state within the same subnav
      const subnav = link.closest(".subnav");
      subnav
        .querySelectorAll(".subnav__link")
        .forEach((l) => l.classList.remove("active"));
      link.classList.add("active");
    });
  });

  // Scroll spy – highlight the sub-nav link for the visible section
  let ticking = false;
  window.addEventListener("scroll", () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        updateActiveSubnavLink();
        ticking = false;
      });
      ticking = true;
    }
  });
}

function updateActiveSubnavLink() {
  const activeTab = document.querySelector(".tab-content.active");
  if (!activeTab) return;

  const subnav = activeTab.querySelector(".subnav");
  if (!subnav) return;

  const links = subnav.querySelectorAll(".subnav__link");
  if (links.length === 0) return;

  const offset = 150;
  let currentSection = null;

  links.forEach((link) => {
    const targetId = link.getAttribute("href").substring(1);
    const section = document.getElementById(targetId);
    if (section) {
      const rect = section.getBoundingClientRect();
      if (rect.top <= offset) {
        currentSection = link;
      }
    }
  });

  if (currentSection) {
    links.forEach((l) => l.classList.remove("active"));
    currentSection.classList.add("active");
  }
}

// ========== COPY TO CLIPBOARD (bez komentárov) ==========

function getCleanCode(codeElement) {
  // Vráti kód BEZ komentárov (elementy s triedou "cm")
  const clone = codeElement.cloneNode(true);

  // Odstráň všetky <span class="cm"> elementy
  clone.querySelectorAll(".cm").forEach((comment) => {
    // Ak komentár je na konci riadku, odstráň aj medzery pred ním
    const prevNode = comment.previousSibling;
    if (prevNode && prevNode.nodeType === 3) {
      // Trim trailing whitespace from the text node before the comment
      prevNode.textContent = prevNode.textContent.replace(/\s+$/, "");
    }
    comment.remove();
  });

  // Získaj text a vyčisti prázdne riadky, ktoré zostali po odstránení komentárov
  let text = clone.textContent;

  // Odstráň riadky, ktoré sú úplne prázdne (zostali po celých riadkoch komentárov)
  text = text
    .split("\n")
    .filter((line, i, arr) => {
      // Zachovaj riadky, ktoré majú nejaký obsah alebo sú medzi dvoma neprázdnymi riadkami
      if (line.trim() !== "") return true;
      // Zachovaj prázdne riadky, ktoré oddeľujú bloky kódu
      const prevHasContent = i > 0 && arr[i - 1].trim() !== "";
      const nextHasContent = i < arr.length - 1 && arr[i + 1].trim() !== "";
      return prevHasContent && nextHasContent;
    })
    .join("\n")
    .trim();

  return text;
}

function copyToClipboard(text, btn) {
  const writeAndFeedback = () => {
    btn.textContent = "✓ Skopírované";
    btn.classList.add("copied");
    setTimeout(() => {
      btn.textContent = "Kopírovať";
      btn.classList.remove("copied");
    }, 2000);
  };

  navigator.clipboard
    .writeText(text)
    .then(writeAndFeedback)
    .catch(() => {
      // Fallback for file:// protocol
      const textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.style.position = "fixed";
      textarea.style.opacity = "0";
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand("copy");
      document.body.removeChild(textarea);
      writeAndFeedback();
    });
}

function initCopyButtons() {
  document.querySelectorAll(".code-block__copy").forEach((btn) => {
    btn.addEventListener("click", () => {
      const codeBlock = btn.closest(".code-block");
      const code = codeBlock.querySelector("code");
      const cleanText = getCleanCode(code);
      copyToClipboard(cleanText, btn);
    });
  });
}

// ========== PRIDANIE NOVÉHO TABU ==========
// Použi túto funkciu na dynamické pridanie nového tabu.
// Príklad: pridajTab('🧮 Matematika', '<p>Vzorce...</p>');

function pridajTab(nazov, htmlObsah) {
  const tabList = document.querySelector(".tabs__list");
  const main = document.querySelector(".main");

  const id =
    "tab-" +
    nazov
      .replace(/[^\w\sáäčďéíľňóôŕšťúýž]/gi, "")
      .trim()
      .toLowerCase()
      .replace(/\s+/g, "-")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");

  const li = document.createElement("li");
  li.innerHTML = `<button class="tabs__btn" data-tab="${id}">${nazov}</button>`;
  tabList.appendChild(li);

  const div = document.createElement("div");
  div.id = id;
  div.className = "tab-content";
  div.innerHTML = htmlObsah;
  main.appendChild(div);

  initTabs();
  initSubNav();

  return id;
}

// ========== SIDEBAR (Hľadanie, Scroll a Navigácia) ==========

// ========== ZVÝRAZNENIE TEXTU ==========
function highlightText(root, query) {
  // Najprv zmaž staré zvýraznenia (obnoví pôvodný HTML obsah sekcie zo zálohy, ak existuje)
  if (root.dataset.originalHtml) {
    root.innerHTML = root.dataset.originalHtml;
  } else {
    // Ak ešte nemáme zálohu (prvý search), vytvorme ju (bez whitespace, aby sme šetrili pamäť nevadí)
    root.dataset.originalHtml = root.innerHTML;
  }

  if (!query) return;

  const escapeRegex = (string) => string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const regex = new RegExp(`(${escapeRegex(query)})`, "gi");

  const treeWalker = document.createTreeWalker(
    root,
    NodeFilter.SHOW_TEXT,
    null,
    false,
  );

  const textNodes = [];
  let currentNode = treeWalker.nextNode();
  while (currentNode) {
    // Zvýrazňujeme len textové uzly v elementoch (ignorujeme <script>, <style> atď.)
    if (
      currentNode.parentNode.tagName !== "SCRIPT" &&
      currentNode.parentNode.tagName !== "STYLE" &&
      currentNode.textContent.trim() !== ""
    ) {
      textNodes.push(currentNode);
    }
    currentNode = treeWalker.nextNode();
  }

  textNodes.forEach((node) => {
    const text = node.textContent;
    if (regex.test(text)) {
      const fragment = document.createDocumentFragment();
      let lastIndex = 0;
      text.replace(regex, (match, p1, offset) => {
        fragment.appendChild(
          document.createTextNode(text.substring(lastIndex, offset)),
        );
        const mark = document.createElement("mark");
        mark.className = "search-highlight";
        mark.textContent = match;
        fragment.appendChild(mark);
        lastIndex = offset + match.length;
        return match;
      });
      fragment.appendChild(document.createTextNode(text.substring(lastIndex)));
      node.parentNode.replaceChild(fragment, node);
    }
  });

  // Opätovná inicializácia copy buttonov pre túto sekciu po prekreslení z originalHtml
  const copyBtns = root.querySelectorAll(".code-block__copy");
  copyBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const codeBlock = btn.closest(".code-block");
      const code = codeBlock.querySelector("code");
      const cleanText = getCleanCode(code);
      copyToClipboard(cleanText, btn);
    });
  });
}

function getActiveSidebarLinks() {
  const activeGroup = document.querySelector(".sidebar__group:not([hidden])");
  if (!activeGroup) return [];
  return activeGroup.querySelectorAll(".sidebar__link");
}

function getActiveSections() {
  const activeTab = document.querySelector(".tab-content.active");
  if (!activeTab) return [];
  return activeTab.querySelectorAll(".section");
}

function initSidebar() {
  const searchInput = document.getElementById("sidebar-search");
  const scrollTopBtn = document.getElementById("scroll-top-btn");
  const scrollBotBtn = document.getElementById("scroll-bot-btn");

  // Inicializuj sidebar pre aktívny tab
  syncSidebarToTab(getActiveTabId());

  // Hľadanie – pracuje len so sekciami a linkmi aktívneho tabu
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      const query = e.target.value.trim();
      const queryLower = query.toLowerCase();

      const sections = getActiveSections();
      const activeGroup = document.querySelector(
        ".sidebar__group:not([hidden])",
      );

      sections.forEach((section) => {
        const keywords = section.getAttribute("data-keywords") || "";
        const allText = section.textContent.toLowerCase();
        const titleEl = section.querySelector(".section__title");
        const titleText = titleEl ? titleEl.textContent.toLowerCase() : "";

        const sectionMatches =
          query === "" ||
          titleText.indexOf(queryLower) !== -1 ||
          keywords.indexOf(queryLower) !== -1 ||
          allText.indexOf(queryLower) !== -1;

        const link = activeGroup
          ? activeGroup.querySelector(
              `.sidebar__link[href="#${section.id}"]`,
            )
          : null;

        if (sectionMatches) {
          section.style.display = "";
          if (link) link.style.display = "";

          highlightText(section, query);

          if (query !== "" && titleText.indexOf(queryLower) === -1) {
            const subsections = section.querySelectorAll(".subsection");
            subsections.forEach((sub) => {
              const subText = sub.textContent.toLowerCase();
              sub.style.display =
                subText.indexOf(queryLower) !== -1 ? "" : "none";
            });
          } else {
            // Reset podsekcií (zobraziť všetky)
            section
              .querySelectorAll(".subsection")
              .forEach((sub) => (sub.style.display = ""));
          }
        } else {
          section.style.display = "none";
          if (link) link.style.display = "none";

          highlightText(section, "");
        }
      });
    });
  }

  // Scroll tlačidlá
  if (scrollTopBtn) {
    scrollTopBtn.addEventListener("click", () => {
      fastScrollTo(0);
    });
  }

  if (scrollBotBtn) {
    scrollBotBtn.addEventListener("click", () => {
      fastScrollTo(document.body.scrollHeight);
    });
  }

  // Kliknutie na sidebar link – delegovanie cez sidebar (funguje aj pre nové linky)
  const sidebar = document.querySelector(".sidebar");
  if (sidebar) {
    sidebar.addEventListener("click", (e) => {
      const link = e.target.closest(".sidebar__link");
      if (!link) return;
      e.preventDefault();

      const targetId = link.getAttribute("href").substring(1);
      const target = document.getElementById(targetId);
      if (target) {
        const offset = 120;
        const top =
          target.getBoundingClientRect().top + window.pageYOffset - offset;
        fastScrollTo(top);
      }

      const links = getActiveSidebarLinks();
      links.forEach((l) => l.classList.remove("active"));
      link.classList.add("active");
    });
  }

  // Scroll spy pre sidebar – pracuje len s linkmi aktívneho tabu
  let ticking = false;
  window.addEventListener("scroll", () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const targetOffset = 150;
        let currentSectionId = null;

        const links = getActiveSidebarLinks();
        links.forEach((link) => {
          const targetId = link.getAttribute("href").substring(1);
          const section = document.getElementById(targetId);
          if (section && section.style.display !== "none") {
            const rect = section.getBoundingClientRect();
            if (rect.top <= targetOffset) {
              currentSectionId = targetId;
            }
          }
        });

        if (currentSectionId) {
          links.forEach((l) => l.classList.remove("active"));
          const currentLink = Array.from(links).find(
            (l) => l.getAttribute("href") === `#${currentSectionId}`,
          );
          if (currentLink) {
            currentLink.classList.add("active");
          }
        }

        ticking = false;
      });
      ticking = true;
    }
  });
}

// ========== SECRET MODAL (POMOC → zobraz, ESC → skry) ==========

const SECRET_TASKS_GRAFICKE = [
  "1. Háďa",
  "3. Displej v električke",
  "6. Noty",
  "8. Nájdi puknutý tanier",
  "9. Preteky lodičiek",
  "10. Vykreslenie krížovky 1",
  "13. Žrút",
  "15. Zobrazenie zátvoriek - NEDOROBENE",
  "18. Kresliaci robot 1",
  "19. Preklopenie obrázka",
  "26. Krajina",
  "30. NIM",
  "31. Čiernobiely obrázok",
  "33. Spektrum odtieňov",
  "35. Vykreslenie komprimovaného obrázka",
  "36. Vykreslenie krížovky 2",
  "41. Výber jedla",
  "42. Zachráň padajúce vajíčko",
  "43. Pyrotechnik",
  "44. Uhádni padajúce slovo",
  "47. Čiarový kód",
  "49. Rezervácia miesteniek",
  "50. Obrys obrázka",
  "53. Zástavba na ulici",
  "54. Lodičky",
  "55. Kresliaci robot 2",
  "56. Editor levelov 1",
  "57. Editor levelov 2",
  "58. Trasa linky metra",
  "59. Vyťaženosť autobusovej linky",
  "60. Kalkulačka",
  "61. Delenie",
  "62. Anketa",
  "64. Zasadací poriadok",
];

const SECRET_TASKS_KONZOLOVE = [
  "2. Háďa - priebeh hry",
  "4. Záznamy z meteorologických staníc",
  "5. Označené jedlá",
  "7. Náhodné skúšanie",
  "11. Súťaž v behu",
  "12. Vyťaženosť liniek dopravného podniku",
  "14. Skok do diaľky",
  "16. Mená v stĺpcoch",
  "17. Tajná tabuľka",
  "20. Tabuľka početnosti",
  "21. Poprehadzovaný text 1",
  "22. Poprehadzovaný text 2",
  "23. Zašifrovaný text 1",
  "24. Zašifrovaný text 2",
  "25. Lotéria",
  "27. Vírus",
  "28. Hlasovanie 1",
  "29. Kompresia obrázka",
  "32. Konverzia súboru 1",
  "34. Dekompresia obrázka",
  "44. Hlasovanie 2",
];

const SECRET_BASE_PATH =
  "../../Škola-hodiny/Precvičovanie/Material_dudo";

function buildSecretListItem(folderName, categoryFolder) {
  const match = folderName.match(/^(\d+)\.\s*(.+)$/);
  const num = match ? match[1] : "•";
  const rawName = match ? match[2] : folderName;
  const isUnfinished = /NEDOROBENE/i.test(rawName);
  const displayName = rawName.replace(/\s*-\s*NEDOROBENE\s*$/i, "");

  const href =
    SECRET_BASE_PATH +
    "/" +
    encodeURIComponent(categoryFolder) +
    "/" +
    encodeURIComponent(folderName);

  const li = document.createElement("li");
  const a = document.createElement("a");
  a.href = href;
  a.target = "_blank";
  a.rel = "noopener";

  const numSpan = document.createElement("span");
  numSpan.className = "secret-list__num";
  numSpan.textContent = num + ".";

  const nameSpan = document.createElement("span");
  nameSpan.className = "secret-list__name";
  nameSpan.textContent = displayName;

  a.appendChild(numSpan);
  a.appendChild(nameSpan);

  if (isUnfinished) {
    const tag = document.createElement("span");
    tag.className = "secret-list__tag";
    tag.textContent = "nedorobené";
    a.appendChild(tag);
  }

  li.appendChild(a);
  return li;
}

function populateSecretLists() {
  const grafList = document.getElementById("secret-list-graf");
  const konList = document.getElementById("secret-list-kon");
  if (!grafList || !konList) return;
  if (grafList.dataset.filled === "1") return;

  const byNumber = (a, b) => parseInt(a, 10) - parseInt(b, 10);

  SECRET_TASKS_GRAFICKE.slice()
    .sort(byNumber)
    .forEach((folder) => {
      grafList.appendChild(buildSecretListItem(folder, "Grafické úlohy"));
    });

  SECRET_TASKS_KONZOLOVE.slice()
    .sort(byNumber)
    .forEach((folder) => {
      konList.appendChild(buildSecretListItem(folder, "Konzolové úlohy"));
    });

  grafList.dataset.filled = "1";
}

function showSecretModal() {
  const overlay = document.getElementById("secret-overlay");
  if (!overlay) return;
  populateSecretLists();
  overlay.hidden = false;
  document.body.style.overflow = "hidden";
}

function hideSecretModal() {
  const overlay = document.getElementById("secret-overlay");
  if (!overlay) return;
  overlay.hidden = true;
  document.body.style.overflow = "";
}

function initSecretModal() {
  const overlay = document.getElementById("secret-overlay");
  if (!overlay) return;

  const SECRET_CODE = "pomoc";
  let buffer = "";

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      if (!overlay.hidden) hideSecretModal();
      buffer = "";
      return;
    }

    const tag = (e.target && e.target.tagName) || "";
    if (tag === "INPUT" || tag === "TEXTAREA" || e.target.isContentEditable) {
      return;
    }

    if (e.key.length !== 1) return;
    buffer = (buffer + e.key.toLowerCase()).slice(-SECRET_CODE.length);
    if (buffer === SECRET_CODE) {
      showSecretModal();
      buffer = "";
    }
  });

  const closeBtn = document.getElementById("secret-close");
  if (closeBtn) closeBtn.addEventListener("click", hideSecretModal);

  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) hideSecretModal();
  });
}
