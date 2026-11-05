#!/usr/bin/env python3
"""Сборка страниц asylalemlife.com в дизайн-системе сайта СДЖ Шымкент.

Шапка, мобильное меню, подвал и модальное окно заявки живут здесь в одном
экземпляре; содержимое страниц — в pages.py. Руками .html не правим.
Запуск:  python3 .build/build.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
SPRITE = open(os.path.join(HERE, "sprite.svg"), encoding="utf-8").read()

# Пункт «Экосистема» ведёт на разбор «магазин и сообщество» на главной:
# адрес интернет-магазина ASYL ALEM в брифе помечен «уточнить». Когда придёт,
# пункт станет «Магазин» со внешней ссылкой.
NAV = [
    ("О сообществе", [("О сообществе", "about.html", "about"),
                      ("Эксперты и наставники", "experts.html", "experts"),
                      ("Истории участников", "stories.html", "stories")], "group-about"),
    ("Клубы", "clubs.html", "clubs"),
    ("Программы", "programs.html", "programs"),
    ("Афиша", "events.html", "events"),
    ("Экосистема", "index.html#eco", "eco"),
    ("Участие", "join.html", "join"),
]


def nav_html(active, home, mobile=False):
    out = []
    for label, href, key in NAV:
        if isinstance(href, list):
            keys = [k for _, _, k in href]
            cur_group = ' aria-current="page"' if active in keys else ""
            if mobile:
                out.append(f'      <li class="mgroup"><span>{label}</span><ul>')
                for sl, sh, sk in href:
                    c = ' aria-current="page"' if sk == active else ""
                    out.append(f'        <li><a href="{sh}"{c}>{sl}</a></li>')
                out.append("      </ul></li>")
            else:
                gid = key.replace("group-", "sub-")
                out.append('      <div class="nav-group">')
                out.append(f'        <button class="nav-toggle" type="button" aria-expanded="false" '
                           f'aria-controls="{gid}"{cur_group}>{label}'
                           f'<svg class="ic" aria-hidden="true"><use href="#i-chevron-down"/></svg></button>')
                out.append(f'        <div class="nav-sub" id="{gid}">')
                for sl, sh, sk in href:
                    c = ' aria-current="page"' if sk == active else ""
                    out.append(f'          <a href="{sh}"{c}>{sl}</a>')
                out.append("        </div>")
                out.append("      </div>")
            continue
        h = href.replace("index.html#", "#") if home and href.startswith("index.html#") else href
        cur = ' aria-current="page"' if key == active else ""
        out.append(f'      <a href="{h}"{cur}>{label}</a>' if not mobile
                   else f'      <li><a href="{h}"{cur}>{label}</a></li>')
    return "\n".join(out)


def brand(home):
    href = "#top" if home else "index.html"
    # Логотипа пока нет (в брифе «уточнить»): марка набрана шрифтом, логотип не выдуман
    return f'''<a class="brand" href="{href}" aria-label="ASYL ALEM LIFE — на главную">
      <span><b>ASYL ALEM LIFE</b><span>Сообщество развития</span></span>
    </a>'''


def header(active, home):
    return f'''<header class="hdr">
  <div class="wrap hdr-in">
    {brand(home)}
    <nav class="nav" aria-label="Основная навигация">
{nav_html(active, home)}
    </nav>
    <div class="hdr-act">
      <button class="btn btn-primary btn-sm" type="button" data-open-modal>Стать участником</button>
      <button class="burger" type="button" aria-label="Открыть меню" aria-expanded="false" aria-controls="mnav" id="burger">
        <svg class="ic" aria-hidden="true"><use href="#i-menu"/></svg>
      </button>
    </div>
  </div>
</header>'''


def mnav(active, home):
    return f'''<div class="mnav" id="mnav">
  <div class="wrap">
    <ul>
{nav_html(active, home, mobile=True)}
    </ul>
    <button class="btn btn-primary" type="button" data-open-modal>Стать участником</button>
  </div>
</div>'''


def footer(home):
    top = "#top" if home else "index.html"
    eco = "#eco" if home else "index.html#eco"
    return f'''<footer class="ftr">
  <div class="wrap">
    <div class="ftr-grid">
      <div>
        <a class="brand" href="{top}">
          <span><b>ASYL ALEM LIFE</b><span>Сообщество развития</span></span>
        </a>
        <p class="ftr-about">ASYL ALEM LIFE — объединяемся, развиваемся, процветаем! Сеть региональных клубов для здоровья, гармонии отношений, благосостояния и бизнеса.</p>
      </div>

      <nav class="ftr-col" aria-label="Разделы сайта">
        <h3>Разделы</h3>
        <ul>
          <li><a href="about.html">О сообществе</a></li>
          <li><a href="clubs.html">Наши клубы</a></li>
          <li><a href="programs.html">Программы развития</a></li>
          <li><a href="events.html">Афиша событий</a></li>
          <li><a href="experts.html">Эксперты и наставники</a></li>
          <li><a href="stories.html">Истории участников</a></li>
          <li><a href="join.html">Стать участником</a></li>
        </ul>
      </nav>

      <nav class="ftr-col" aria-label="Контакты">
        <h3>Контакты</h3>
        <ul>
          <li>г. Шымкент, Орынбаева 23</li>
          <li>Ежедневно 9:00–20:00</li>
          <li>Телефон: <em class="fill">уточняется</em></li>
          <li><a href="{eco}">Экосистема ASYL ARMAN</a></li>
        </ul>
      </nav>
    </div>

    <div class="ftr-bot">
      <span>© 2026 ТОО «ASYL ALEM LIFE»</span>
      <span>Направление экосистемы ASYL ARMAN</span>
    </div>
  </div>
</footer>'''


CLUB_OPTIONS = '''<option value="">Пока не выбрал(а)</option>
              <option>Клуб потребителей</option>
              <option>Клуб предпринимателей</option>
              <option>Клуб основателей</option>'''


def lead_form(prefix, success_id):
    """Форма заявки. data-endpoint пустой — точка подключения почты или CRM."""
    return f'''<form class="fgrid" id="{prefix}-form" data-lead="#{success_id}" data-endpoint="" novalidate>
          <div>
            <label for="{prefix}-name">Имя *</label>
            <input id="{prefix}-name" name="name" type="text" autocomplete="name" placeholder="Как к вам обращаться" required />
          </div>
          <div>
            <label for="{prefix}-phone">Телефон *</label>
            <input id="{prefix}-phone" name="phone" type="tel" autocomplete="tel" placeholder="+7 ___ ___ __ __" required />
          </div>
          <div>
            <label for="{prefix}-city">Город</label>
            <input id="{prefix}-city" name="city" type="text" autocomplete="address-level2" placeholder="Где вам удобен клуб" />
          </div>
          <div>
            <label for="{prefix}-club">Какой клуб ближе</label>
            <select id="{prefix}-club" name="club">
              {CLUB_OPTIONS}
            </select>
          </div>
          <div class="full">
            <label for="{prefix}-note">Вопрос или пожелание</label>
            <textarea id="{prefix}-note" name="note" rows="3" placeholder="Например: интересует программа «Будь здоров»"></textarea>
          </div>
          <div class="full">
            <button class="btn btn-gold" type="submit">Отправить заявку</button>
          </div>
          <p class="msg" aria-live="polite"></p>
          <p class="note full">Данные используются только для связи по заявке.</p>
        </form>
        <div class="fsuccess" id="{success_id}" hidden>
          <span class="fi"><svg class="ic ic-lg" aria-hidden="true"><use href="#i-check"/></svg></span>
          <h3>Заявка получена</h3>
          <p>Спасибо! Руководитель клуба свяжется с вами в рабочее время: ежедневно 9:00–20:00.</p>
        </div>'''


MODAL = f'''<!-- Заявка открывается модальным окном: кнопки в шапке и на страницах ведут сюда,
     чтобы оставить заявку можно было с любого экрана без прокрутки вниз. -->
<div class="modal" id="modal" hidden>
  <div class="modal-bd" data-close-modal></div>
  <div class="modal-panel form" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <div class="modal-head">
      <div>
        <span class="eyebrow">Заявка</span>
        <h2 id="modal-title">Стать участником</h2>
      </div>
      <button class="modal-x" type="button" aria-label="Закрыть окно" data-close-modal>
        <svg class="ic" aria-hidden="true"><use href="#i-x"/></svg>
      </button>
    </div>
    <p class="modal-hint">Заявка → выбор клуба в своём городе → участие во встречах и программах. Поля со звёздочкой обязательны.</p>
        {lead_form("m", "m-success")}
  </div>
</div>'''


HEAD = '''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta property="og:type" content="website" />
<meta property="og:locale" content="ru_KZ" />
<meta property="og:site_name" content="ASYL ALEM LIFE" />
<meta property="og:title" content="{og}" />
<meta property="og:description" content="{desc}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
<script>
/* Флаг ставим до первой отрисовки, иначе контент мелькнёт до старта reveal.
   Без JS класс не появится — весь контент останется видимым. */
if (!matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window)
  document.documentElement.className += ' rv';
</script>
<link rel="stylesheet" href="assets/style.css" />
</head>
<body>

'''


def page(spec):
    home = spec["slug"] == "index.html"
    active = spec.get("active", "")
    if home:
        top = spec["body"]
    else:
        top = f'''  <section class="page-head">
    <div class="wrap">
      <nav class="crumbs" aria-label="Хлебные крошки">
        <a href="index.html">Главная</a><span class="sep">/</span><span aria-current="page">{spec["crumb"]}</span>
      </nav>
      <h1>{spec["h1"]}</h1>
      <p>{spec["lead"]}</p>
    </div>
  </section>

{spec["body"]}'''
    html = (HEAD.format(title=spec["title"], desc=spec["description"], og=spec.get("h1", spec["title"]))
            + SPRITE + "\n\n"
            + header(active, home) + "\n\n"
            + mnav(active, home) + "\n\n"
            + '<main id="top">\n\n' + top + "\n</main>\n\n"
            + footer(home) + "\n\n"
            + MODAL + "\n\n"
            + '<script src="assets/app.js" defer></script>\n</body>\n</html>\n')
    with open(os.path.join(ROOT, spec["slug"]), "w", encoding="utf-8") as f:
        f.write(html)
    print("собрано", spec["slug"], f"{len(html)//1024} КБ")


if __name__ == "__main__":
    sys.path.insert(0, HERE)
    import pages
    for spec in pages.PAGES:
        page(spec)
