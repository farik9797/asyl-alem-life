#!/usr/bin/env python3
"""Сборка статических страниц asylalemlife.com.

Шапка, подвал и скрипт живут здесь в одном экземпляре: без сборщика их пришлось бы
править в восьми файлах. Содержимое страниц — в pages.py.
Запуск:  python3 .build/build.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Верхнее меню. Пункт называется «Экосистема» и ведёт на разбор «магазин и сообщество»
# на главной: ярлык «Магазин» обещал бы переход в сам магазин, а его адрес в брифе
# помечен «уточнить». Когда адрес придёт, пункт станет «Магазин» со внешней ссылкой.
NAV = [
    ("about.html", "О сообществе"),
    ("clubs.html", "Клубы"),
    ("programs.html", "Программы"),
    ("events.html", "События"),
    ("index.html#eco", "Экосистема"),
]

FOOT_NAV = [
    ("about.html", "О сообществе"),
    ("clubs.html", "Наши клубы"),
    ("programs.html", "Программы развития"),
    ("events.html", "Афиша событий"),
    ("experts.html", "Эксперты и наставники"),
    ("stories.html", "Истории участников"),
    ("join.html", "Стать участником"),
]


def header(current):
    links = []
    for href, label in NAV:
        here = ' aria-current="page"' if href == current else ""
        links.append(f'      <a href="{href}"{here}>{label}</a>')
    cta_here = ' aria-current="page"' if current == "join.html" else ""
    return f"""<header class="top field">
  <div class="container top__in">
    <a class="wordmark" href="index.html" aria-label="ASYL ALEM LIFE, на главную">ASYL ALEM LIFE</a>

    <button class="burger" type="button" aria-expanded="false" aria-controls="menu">Меню</button>

    <nav class="menu" id="menu" aria-label="Основная навигация">
{chr(10).join(links)}
    </nav>

    <a class="btn btn--quiet top__cta" href="join.html"{cta_here}>Стать участником</a>
  </div>
</header>"""


def footer(current):
    links = []
    for href, label in FOOT_NAV:
        here = ' aria-current="page"' if href == current else ""
        links.append(f'      <a href="{href}"{here}>{label}</a>')
    return f"""<footer class="foot field">
  <div class="container">
    <p class="foot__sign">ASYL ALEM LIFE</p>
    <p class="foot__line">Объединяемся, развиваемся, процветаем.</p>

    <nav class="foot__nav" aria-label="Разделы сайта">
{chr(10).join(links)}
    </nav>

    <p class="foot__legal">ТОО «ASYL ALEM LIFE». Казахстан, Шымкент, Орынбаева 23. Ежедневно с 9:00 до 20:00.</p>
  </div>
</footer>"""


SCRIPT = """<script>
document.documentElement.classList.add('js');
(() => {
  const burger = document.querySelector('.burger');
  const menu = document.getElementById('menu');
  if (!burger || !menu) return;
  const set = (open) => {
    burger.setAttribute('aria-expanded', String(open));
    menu.classList.toggle('is-open', open);
  };
  burger.addEventListener('click', () => set(burger.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') { set(false); burger.focus(); }
  });
})();

(() => {
  for (const form of document.querySelectorAll('form[data-endpoint]')) {
    const help = form.querySelector('[aria-live]');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      let bad = null;
      for (const el of form.querySelectorAll('[required]')) {
        const ok = el.checkValidity() && el.value.trim() !== '';
        el.toggleAttribute('aria-invalid', !ok);
        if (!ok && !bad) bad = el;
      }
      if (bad) { help.textContent = 'Заполните обязательные поля: имя и телефон.'; bad.focus(); return; }
      if (!form.dataset.endpoint) {
        help.textContent = 'Заявка никуда не ушла: форма пока не подключена к почте.';
        return;
      }
      fetch(form.dataset.endpoint, { method: 'POST', body: new FormData(form) })
        .then((r) => { help.textContent = r.ok ? 'Заявка получена, свяжемся в рабочее время.' : 'Не отправилось. Попробуйте через минуту.'; })
        .catch(() => { help.textContent = 'Не отправилось. Попробуйте через минуту.'; });
    });
  }
})();
</script>"""


def page(slug, title, description, body):
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{description}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Prata&family=Manrope:wght@400;500;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="style.css" />
</head>
<body>
<a class="skip" href="#main">К содержанию</a>

{header(slug)}

<main id="main">
{body}
</main>

{footer(slug)}

{SCRIPT}
</body>
</html>
"""


def build():
    import pages
    for spec in pages.PAGES:
        html = page(spec["slug"], spec["title"], spec["description"], spec["body"])
        with open(os.path.join(ROOT, spec["slug"]), "w", encoding="utf-8") as f:
            f.write(html)
        print("собрано", spec["slug"])


if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    build()
