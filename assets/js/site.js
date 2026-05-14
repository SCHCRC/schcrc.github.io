(() => {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const isMobile = window.matchMedia("(max-width: 720px)").matches;

  if (reduceMotion || isMobile) {
    return;
  }

  const selectors = [
    ".page-hero .site-shell",
    ".section__heading",
    ".archive-item",
    ".person-row",
    ".resource-item",
    ".timeline__item",
    ".post__header",
    ".post__content",
  ];

  const targets = [...document.querySelectorAll(selectors.join(","))].slice(0, 32);

  if (!targets.length) {
    return;
  }

  document.documentElement.classList.add("motion-ready");

  targets.forEach((target, index) => {
    target.classList.add("reveal-on-scroll");
    target.style.setProperty("--reveal-delay", `${Math.min(index % 3, 2) * 50}ms`);
  });

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) {
          return;
        }

        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    {
      rootMargin: "0px 0px -12% 0px",
      threshold: 0.12,
    }
  );

  targets.forEach((target) => observer.observe(target));
})();
