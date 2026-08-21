(() => {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const root = document.documentElement;

  /* =====================================================================
     A. 모바일 메뉴 — 모션과 무관하게 항상 동작해야 한다.
     ===================================================================== */
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.getElementById("site-nav");

  if (toggle && nav) {
    const close = () => {
      nav.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
    };

    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        close();
        toggle.focus();
      }
    });

    document.addEventListener("click", (e) => {
      if (!nav.classList.contains("is-open")) return;
      if (nav.contains(e.target) || toggle.contains(e.target)) return;
      close();
    });

    window.matchMedia("(min-width: 901px)").addEventListener("change", (e) => {
      if (e.matches) close();
    });
  }

  /* =====================================================================
     B. 첫 화면 정착 — 이 페이지의 유일한 연출된 순간.
        타이밍은 전부 CSS가 갖고 있고, JS는 시작 신호만 준다.
        이 클래스가 없으면(JS 미실행) 모든 콘텐츠는 그냥 보인다.
     ===================================================================== */
  root.classList.add("motion-ready");

  /* =====================================================================
     C. 지속 상태 — 스크롤하면 헤더가 조여들고 히어로 배경이 느리게 밀린다.
        섹션 등장 효과가 아니라 위치 신호다.
     ===================================================================== */
  const header = document.querySelector(".site-header");
  const heroBg = document.querySelector(".hero__bg");
  const hero = document.querySelector(".hero");

  let queued = false;

  const onScroll = () => {
    const y = window.scrollY;

    // 헤더 상태는 클래스 토글 하나뿐이므로 프레임을 기다리지 않는다.
    // rAF 안에 두면 탭이 백그라운드일 때 플래그가 걸려 상태가 멈춘다.
    if (header) {
      header.classList.toggle("is-compact", y > 120);
    }

    if (!heroBg || !hero || reduceMotion || queued) return;
    queued = true;

    requestAnimationFrame(() => {
      queued = false;
      const top = window.scrollY;
      if (top < hero.offsetHeight) {
        heroBg.style.translate = `0 ${Math.round(top * 0.14)}px`;
      }
    });
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

})();
