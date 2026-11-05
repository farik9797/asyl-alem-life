# -*- coding: utf-8 -*-
"""Содержимое страниц asylalemlife.com в компонентах сайта СДЖ Шымкент.

Правило одно: на страницах нет ни одного факта, которого нет в брифе.
Там, где бриф молчит (телефон, почта, адрес магазина, условия вступления,
даты событий, имена спикеров, истории участников), страница говорит об этом
прямо. Миссия, видение, философия, слоган, заголовок баннера, названия программ,
зон и клубов взяты из брифа дословно.
"""
from build import lead_form


def ic(name, lg=True):
    return f'<svg class="ic{" ic-lg" if lg else ""}" aria-hidden="true"><use href="#i-{name}"/></svg>'


def tlink(href, text, dark=False):
    return f'<a class="tlink{" on-dark" if dark else ""}" href="{href}">{text}{ic("arrow-r", False)}</a>'


def pic(name, alt, w, h, cls="shot", rv=True):
    """Снимок в двух форматах: WebP основным, JPEG фолбэком, как на сайте СДЖ."""
    attr = " data-rv" if rv else ""
    return f'''<figure class="{cls}"{attr}>
          <picture>
            <source srcset="assets/{name}.webp" type="image/webp" />
            <img src="assets/{name}.jpg" alt="{alt}" width="{w}" height="{h}" loading="lazy" />
          </picture>
        </figure>'''


RESOURCE = pic("photo-resource", "Презентация у доски с материалами", 960, 720)
NETWORK = pic("photo-network", "Деловая встреча за столиком", 960, 640)


def cta_box(title, text, white=False):
    """Закрытие внутренней страницы: заявка, а не рассылка."""
    bg = ' style="background:var(--white)"' if white else ""
    return f'''      <div class="empty" data-rv{bg}>
        <div>
          <b>{title}</b>
          <p>{text}</p>
        </div>
        <button class="btn btn-primary" type="button" data-open-modal>Стать участником</button>
      </div>'''


FOUNDER = '''<div class="chair">
          <figure class="chair-shot">
            <picture>
              <source srcset="assets/photo-chair.webp" type="image/webp" />
              <img src="assets/photo-chair.jpg" alt="Алма Архабаева, основатель экосистемы ASYL ARMAN" width="600" height="800" loading="lazy" />
            </picture>
          </figure>
          <div class="chair-body">
            <span class="lbl">Основатель экосистемы ASYL ARMAN</span>
            <span class="nm">Алма Архабаева</span>
            <p>ASYL ALEM LIFE — новое направление экосистемы. В неё входят интернет-магазин ASYL ALEM, санаторий ASYL ARMAN, производство ASYL ARMAN HERBS, Академия MLM PRO и Фонд Asyl Arman.</p>
          </div>
        </div>'''

ECO_CARDS = f'''<div class="recog">
        <article class="recogcard" data-rv>
          <span class="fi">{ic("store")}</span>
          <b>Интернет-магазин ASYL ALEM</b>
          <p>Продажи и партнёрский бизнес. Финансовая аналитика, товарооборот, структура дистрибьюторов и начисления — в защищённом личном кабинете магазина.</p>
          <!-- Адрес магазина в брифе помечен «уточнить». Когда придёт — поставить ссылку здесь и в NAV. -->
        </article>
        <article class="recogcard" data-rv>
          <span class="fi">{ic("users")}</span>
          <b>ASYL ALEM LIFE</b>
          <p>Развитие человека, предпринимательская культура и сообщество: региональные клубы, программы и встречи.</p>
        </article>
        <article class="recogcard" data-rv>
          <span class="fi">{ic("layers")}</span>
          <b>Ещё четыре направления</b>
          <p>Санаторий ASYL ARMAN, производство ASYL ARMAN HERBS, Академия MLM PRO и Фонд Asyl Arman.</p>
        </article>
      </div>'''

ZONES = f'''<ul class="rcgrid rc3">
        <li data-rv>{ic("coffee")}<b>Клуб общения и ЗОЖ</b><p>Полезные завтраки, дегустации, встречи.</p></li>
        <li data-rv>{ic("stethoscope")}<b>Кабинет здоровья</b><p>Замеры, консультации специалистов по записи.</p></li>
        <li data-rv>{ic("cap")}<b>Центр обучения и развития</b><p>Четыре программы, тренинги, мастер-классы.</p></li>
      </ul>'''


def dircard(icon, n, title, text):
    """n — подпись над заголовком. Номера 01–04 не ставим: программы и роли —
    не последовательность, нумерация там была бы шаблонным приёмом."""
    label = f'\n          <span class="n">{n}</span>' if n else ""
    return f'''        <article class="dircard" data-rv>
          <span class="fi">{ic(icon)}</span>{label}
          <h3>{title}</h3>
          <p>{text}</p>
        </article>'''


PROGRAM_CARDS = "\n".join([
    '<div class="dirs">',
    dircard("heart-pulse", "", "«Будь здоров»", "Здоровье, энергия и активное долголетие."),
    dircard("smile", "", "«Будь счастлив»", "Гармония, отношения и личностный рост."),
    dircard("banknote", "", "«Будь богат»", "Финансовая грамотность, достаток и материальное благополучие."),
    dircard("rocket", "", "«Будь предпринимателем»", "Предпринимательское мышление, лидерство и создание новых источников дохода."),
    "      </div>",
])

JOIN_FLOW = '''<ol class="flow">
            <li><i aria-hidden="true"></i>Заявка «Стать участником» на сайте</li>
            <li><i aria-hidden="true"></i>Выбор клуба в своём городе</li>
            <li><i aria-hidden="true"></i>Регистрация участника в клубе</li>
            <li><i aria-hidden="true"></i>Участие во встречах и программах</li>
          </ol>'''

STEPS_FLOW = '''<ol class="flow">
            <li><i aria-hidden="true"></i>Вводный курс</li>
            <li><i aria-hidden="true"></i>Практика</li>
            <li><i aria-hidden="true"></i>Мастер-классы</li>
            <li><i aria-hidden="true"></i>Углублённый уровень</li>
          </ol>'''


def contact_list(page=False):
    """Контакты. Телефона и почты в брифе нет, поэтому их строк нет совсем.
    Когда придут — добавить row("phone", ...) и row("mail", ...) первыми в список."""
    def row(icon, k, v):
        return f'''
          <li>
            <span class="fi">{ic(icon, False)}</span>
            <span><span class="k">{k}</span><span class="v">{v}</span></span>
          </li>'''
    rows = [
        row("pin", "Адрес клуба", "Казахстан, г. Шымкент, Орынбаева 23"),
        row("clock", "График работы", "Ежедневно 9:00–20:00<em>Клубы работают круглый год</em>"),
        row("globe", "География", "Казахстан<em>В дальнейшем — и за его пределами</em>"),
    ]
    if page:
        rows.append(row("building", "Юридическое лицо", "ТОО «ASYL ALEM LIFE»<em>Направление экосистемы ASYL ARMAN</em>"))
    return '<ul class="clist">' + "".join(rows) + "\n        </ul>"


# ======================================================================
INDEX = f'''  <!-- ================= HERO =================
       Снимок взят с сайта СДЖ Шымкент (сгенерирован, несуществующие люди).
       Своих фото у ASYL пока нет — заменить файл, разметку не трогать. -->
  <section class="hero">
    <div class="wrap hero-in">
      <div>
        <span class="eyebrow" data-hero>Здоровье · Гармония отношений · Благосостояние · Бизнес</span>
        <h1 data-hero>Пространство роста, единства и <span class="gold">созидания</span></h1>
        <p class="hero-lead" data-hero>Мы объединяем людей, которые стремятся к осознанной жизни, личностному росту и предпринимательскому развитию. В наших региональных клубах вы найдёте знания, поддержку, общение и возможности для реализации своего потенциала.</p>
        <div class="hero-cta" data-hero>
          <button class="btn btn-primary" type="button" data-open-modal>Стать участником</button>
          <a class="btn btn-outline" href="clubs.html">Наши клубы</a>
        </div>
      </div>
      <div class="hero-media" data-hero>
        <picture>
          <source srcset="assets/photo-hero.webp" type="image/webp" />
          <img src="assets/photo-hero.jpg" alt="" width="1920" height="1080" fetchpriority="high" />
        </picture>
      </div>
    </div>
    <div class="hero-rule" id="hero-rule"></div>

    <div class="hero-strip">
      <div class="wrap">
        <ul>
          <li data-strip><b data-count="4" data-pad="2">04</b><span>Программы развития</span></li>
          <li data-strip><b data-count="3" data-pad="2">03</b><span>Зоны в каждом клубе</span></li>
          <li data-strip><b>9:00–20:00</b><span>Ежедневно в клубе</span></li>
          <li data-strip><b>15.12.2026</b><span>Запуск сообщества</span></li>
        </ul>
      </div>
    </div>
  </section>

  <!-- ================= ПРОГРАММЫ ================= -->
  <section class="sec sec-surface" id="programs">
    <div class="wrap">
      <div class="sec-head" data-rv>
        <span class="eyebrow">Программы развития</span>
        <h2 class="h2">Четыре направления развития</h2>
        <p class="lead" style="margin-top:1rem">Основа всей образовательной системы клубов. Программы доступны и новичкам, и опытным лидерам: вводный курс, практика, мастер-классы, углублённый уровень.</p>
      </div>
      <p style="margin-top:-1.5rem;margin-bottom:2rem">{tlink("programs.html", "Подробно о каждой программе")}</p>
      {PROGRAM_CARDS}
    </div>
  </section>

  <!-- ================= О СООБЩЕСТВЕ ================= -->
  <section class="sec" id="about">
    <div class="wrap about-grid">
      <div data-rv>
        <span class="eyebrow">О сообществе</span>
        <h2 class="h2">Больше, чем бизнес. Больше, чем клуб.</h2>
        <p class="lead" style="margin-top:1.25rem">ASYL ALEM LIFE — сильное сообщество единомышленников, объединённых стремлением к здоровью, счастью, финансовому благополучию и процветанию. Мы создаём пространство возможностей, где каждый может раскрывать свой потенциал и создавать лучшее будущее для себя и своей семьи.</p>
        <p style="margin-top:1.5rem">{tlink("about.html", "Подробнее о сообществе")}</p>
        <ul class="checks">
          <li>{ic("check", False)}<span>Знания и полезные навыки для личностного роста</span></li>
          <li>{ic("check", False)}<span>Укрепление здоровья и активное долголетие</span></li>
          <li>{ic("check", False)}<span>Управление личными финансами и рост доходов</span></li>
          <li>{ic("check", False)}<span>Реализация предпринимательских идей</span></li>
          <li>{ic("check", False)}<span>Живое общение, обмен опытом и взаимная поддержка</span></li>
        </ul>
      </div>

      <div data-rv>
        {FOUNDER}
        <div class="sincecard">
          <b>2026</b>
          <span>Сообщество ASYL ALEM LIFE запускается 15 декабря 2026 года.</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= КЛУБЫ ================= -->
  <section class="sec rc on-dark" id="club">
    <div class="wrap">
      <div class="rc-head">
        <div data-rv>
          <span class="eyebrow on-dark">Региональные клубы</span>
          <h2 class="h2">Каждый клуб — три зоны</h2>
          <p class="lead" style="margin-top:1rem">Клубы работают по единым стандартам. Формат — от компактного пространства до полноценного центра. Первый клуб — в Шымкенте, Орынбаева 23.</p>
          <p style="margin-top:1rem">{tlink("clubs.html", "Подробнее о клубах", dark=True)}</p>
        </div>
        {RESOURCE}
      </div>
      {ZONES}
    </div>
  </section>

  <!-- ================= КАК ВСТУПИТЬ ================= -->
  <section class="sec sec-surface" id="how">
    <div class="wrap">
      <div class="sec-head row">
        <div data-rv>
          <span class="eyebrow">Схема участия</span>
          <h2 class="h2">Как стать участником</h2>
        </div>
        {NETWORK.replace('class="shot"', 'class="shot wide"')}
      </div>
      <div class="flow-grid">
        <article class="flowcard" data-rv>
          <h3><span class="fi">{ic("users")}</span>Путь участника</h3>
          {JOIN_FLOW}
        </article>
        <article class="flowcard" data-rv>
          <h3><span class="fi">{ic("sprout")}</span>Ступени каждой программы</h3>
          {STEPS_FLOW}
        </article>
      </div>
    </div>
  </section>

  <!-- ================= ЭКОСИСТЕМА ================= -->
  <section class="sec" id="eco">
    <div class="wrap">
      <div class="sec-head" data-rv>
        <span class="eyebrow">Экосистема ASYL ARMAN</span>
        <h2 class="h2">Магазин и сообщество делят работу</h2>
        <p class="lead" style="margin-top:1rem">ASYL ALEM отвечает за продажи и партнёрский бизнес, ASYL ALEM LIFE — за развитие человека, предпринимательскую культуру и сообщество. Сайт сообщества не дублирует магазин.</p>
      </div>
      {ECO_CARDS}
    </div>
  </section>

  <!-- ================= ВОПРОСЫ ================= -->
  <section class="sec sec-surface" id="faq">
    <div class="wrap faq-grid">
      <div data-rv>
        <span class="eyebrow">Вопросы и ответы</span>
        <h2 class="h2">Коротко о главном</h2>
        <p class="lead" style="margin-top:1rem">Не нашли ответ — оставьте заявку, ответим в рабочее время.</p>
        <a class="btn btn-outline" href="join.html" style="margin-top:1.75rem">Как вступить</a>
      </div>

      <div class="acc" data-rv>
        <details open>
          <summary>Нужно ли вступать в MLM-бизнес?{ic("chevron-down", False)}</summary>
          <div class="body">Нет. Участие в клубе не требует вступления в MLM-бизнес. В клубы приходят клиенты, гости и жители региона, а дистрибьюторы ASYL ALEM организуют деятельность и развивают клубы.</div>
        </details>
        <details>
          <summary>Кому подходит сообщество?{ic("chevron-down", False)}</summary>
          <div class="body">Потребителям, гостям и жителям региона, предпринимателям — всем, кто стремится к здоровью, счастью, благополучию и развитию. Описание «сообщество осознанных MLM-предпринимателей» относится только к программе «Будь предпринимателем» и клубу предпринимателей.</div>
        </details>
        <details>
          <summary>Сколько стоит участие?{ic("chevron-down", False)}</summary>
          <!-- Условия и суммы в брифе помечены «уточнить»: не публикуем до утверждения. -->
          <div class="body">Условия вступления и оплаты сейчас утверждаются. Они появятся на сайте до запуска сообщества; суммы до этого мы не публикуем.</div>
        </details>
        <details>
          <summary>Где находится клуб?{ic("chevron-down", False)}</summary>
          <div class="body">Первый клуб — в Шымкенте, Орынбаева 23, ежедневно с 9:00 до 20:00. Сеть клубов развивается по Казахстану, в дальнейшем — и за его пределами.</div>
        </details>
        <details>
          <summary>Подойдут ли программы новичку?{ic("chevron-down", False)}</summary>
          <div class="body">Да. Каждая программа начинается с вводного курса, дальше — практика, мастер-классы и углублённый уровень. Программы доступны и новичкам, и опытным лидерам.</div>
        </details>
        <details>
          <summary>Чем сообщество отличается от магазина ASYL ALEM?{ic("chevron-down", False)}</summary>
          <div class="body">Магазин отвечает за продажи и партнёрский бизнес, сообщество — за развитие человека, предпринимательскую культуру и живое общение. Продукция для здоровья — через интернет-магазин ASYL ALEM, производство ASYL ARMAN HERBS.</div>
        </details>
      </div>
    </div>
  </section>

  <!-- ================= АФИША И ИСТОРИИ =================
       ЗАГЛУШКИ: карточки описывают будущие разделы, без дат, имён и вымышленных заголовков. -->
  <section class="sec" id="news">
    <div class="wrap">
      <div class="sec-head" data-rv>
        <span class="eyebrow">Афиша и истории</span>
        <h2 class="h2">Что появится после запуска</h2>
      </div>
      <div class="newsgrid">
        <article class="ncard" data-rv>
          <span class="soon">Календарь готовится</span>
          <h3>Встречи и мастер-классы</h3>
          <p>Полезные завтраки, дегустации, тренинги и мастер-классы первого клуба.</p>
        </article>
        <article class="ncard" data-rv>
          <span class="soon">Состав собирается</span>
          <h3>Наставники клуба</h3>
          <p>Руководитель клуба, обученные спикеры, специалисты кабинета здоровья и основатели клубов.</p>
        </article>
        <article class="ncard" data-rv>
          <span class="soon">После запуска</span>
          <h3>Истории участников</h3>
          <p>Реальные истории развития — только с согласия участников, без выдуманных отзывов.</p>
        </article>
      </div>
      <p class="tpl-note">Разделы наполняются: <a href="events.html" style="color:var(--brand);font-weight:600">афиша</a>, <a href="experts.html" style="color:var(--brand);font-weight:600">наставники</a>, <a href="stories.html" style="color:var(--brand);font-weight:600">истории</a>.</p>
    </div>
  </section>

  <!-- ================= КОНТАКТЫ ================= -->
  <section class="sec contact" id="contacts">
    <div class="wrap cgrid">
      <div data-rv>
        <span class="eyebrow">Контакты</span>
        <h2 class="h2">Стать участником</h2>
        <p class="lead" style="margin-top:1rem">Оставьте заявку — подскажем ближайший клуб и встречу. Участие в клубе не требует вступления в MLM-бизнес.</p>
        {contact_list()}
      </div>

      <div class="form" data-rv>
        <h3>Оставить заявку</h3>
        <p class="hint">Заявка → выбор клуба в своём городе → участие во встречах и программах.</p>
        {lead_form("p", "p-success")}
      </div>
    </div>
  </section>'''


# ======================================================================
ABOUT = f'''  <section class="sec">
    <div class="wrap">
      <div class="sec-head" data-rv>
        <span class="eyebrow">Миссия, видение и философия</span>
        <h2 class="h2">Зачем мы объединяем людей</h2>
      </div>
      <div class="dirs dirs-3">
{dircard("target", "Миссия", "Объединять людей в сильное сообщество", "Создавать условия для личностного роста, укрепления здоровья, финансового благополучия и реализации предпринимательского потенциала ради повышения качества жизни и совместного процветания.")}
{dircard("globe", "Видение", "Масштабное сообщество с сетью клубов", "Стать сообществом единомышленников с сетью региональных клубов, где каждый получает возможности для развития, общения, обучения и самореализации.")}
{dircard("sprout", "Философия", "Процветание человека", "Процветание человека. Благополучие семьи. Развитие общества.")}
      </div>
    </div>
  </section>

  <section class="sec sec-surface">
    <div class="wrap about-grid">
      <div data-rv>
        <span class="eyebrow">Открытое сообщество</span>
        <h2 class="h2">Кому открыт клуб</h2>
        <p class="lead" style="margin-top:1.25rem">Модель — открытое сообщество с партнёрским ядром. Основа сообщества — сеть региональных клубов: пространств для живого общения, обучения, обмена опытом, взаимной поддержки и совместного роста.</p>
        <ul class="checks">
          <li>{ic("check", False)}<span>Клиенты и гости клуба</span></li>
          <li>{ic("check", False)}<span>Жители региона</span></li>
          <li>{ic("check", False)}<span>Предприниматели</span></li>
          <li>{ic("check", False)}<span>Дистрибьюторы ASYL ALEM организуют деятельность и развивают клубы</span></li>
        </ul>
      </div>
      <div>
        {NETWORK}
        <div class="sincecard" data-rv>
          <b>Без MLM</b>
          <span>Участие в клубе не требует вступления в MLM-бизнес. Описание «сообщество осознанных MLM-предпринимателей» относится только к клубу предпринимателей.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="about-grid">
        <div data-rv>
          <span class="eyebrow">Экосистема ASYL ARMAN</span>
          <h2 class="h2">Новое направление экосистемы</h2>
          <p class="lead" style="margin-top:1.25rem">ASYL ALEM отвечает за продажи и партнёрский бизнес, ASYL ALEM LIFE — за развитие человека, предпринимательскую культуру и сообщество.</p>
        </div>
        <div data-rv>
          {FOUNDER}
        </div>
      </div>
      {ECO_CARDS}
{cta_box("Хотите в клуб?", "Оставьте заявку — подскажем ближайший клуб и первую встречу.")}
    </div>
  </section>'''


CLUBS = f'''  <section class="sec">
    <div class="wrap about-grid">
      <div data-rv>
        <span class="eyebrow">Первый клуб</span>
        <h2 class="h2">Шымкент, Орынбаева 23</h2>
        <p class="lead" style="margin-top:1.25rem">Клубы — пространства для живого общения, обучения, обмена опытом, взаимной поддержки и совместного роста. Здесь получают знания, учатся управлять личными финансами и находят возможности для своего дела.</p>
        <ul class="checks">
          <li>{ic("check", False)}<span>Ежедневно с 9:00 до 20:00</span></li>
          <li>{ic("check", False)}<span>Кабинет здоровья — по предварительной записи</span></li>
          <li>{ic("check", False)}<span>Участие не требует вступления в MLM-бизнес</span></li>
          <li>{ic("check", False)}<span>Работа круглый год, без сезонов</span></li>
        </ul>
      </div>
      <div data-rv>
        <div class="sincecard">
          <b>15.12.2026</b>
          <span>Запуск сообщества ASYL ALEM LIFE.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="sec rc on-dark">
    <div class="wrap">
      <div class="rc-head">
        <div data-rv>
          <span class="eyebrow on-dark">Единые стандарты</span>
          <h2 class="h2">Три зоны в каждом клубе</h2>
          <p class="lead" style="margin-top:1rem">Формат — от компактного пространства до полноценного центра. Набор зон в любом городе один и тот же.</p>
        </div>
        {RESOURCE}
      </div>
      {ZONES}
    </div>
  </section>

  <section class="sec sec-surface">
    <div class="wrap">
      <div class="sec-head" data-rv>
        <span class="eyebrow">Стандарт клуба</span>
        <h2 class="h2">Что есть в каждом клубе</h2>
      </div>
      <div class="dirs">
{dircard("users", "", "Руководитель клуба", "Отвечает за работу клуба и связь с участниками.")}
{dircard("cap", "", "Обученные спикеры", "Ведут программы, тренинги и мастер-классы.")}
{dircard("calendar", "", "Календарь мероприятий", "Расписание встреч и занятий клуба.")}
{dircard("check", "", "Регистрация и обратная связь", "Запись участников и отзывы о встречах.")}
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec-head" data-rv>
        <span class="eyebrow">Внутри сообщества</span>
        <h2 class="h2">Три клуба</h2>
        <p class="lead" style="margin-top:1rem">Казахстан, в дальнейшем — и за его пределами. Условия вступления и оплаты утверждаются и появятся на сайте до запуска.</p>
      </div>
      <div class="recog">
        <article class="recogcard" data-rv>
          <span class="fi">{ic("users")}</span>
          <b>Клуб потребителей</b>
          <p>Клиенты, гости и жители региона: здоровье, общение и программы развития.</p>
        </article>
        <article class="recogcard" data-rv>
          <span class="fi">{ic("briefcase")}</span>
          <b>Клуб предпринимателей</b>
          <p>Сообщество осознанных MLM-предпринимателей, программа «Будь предпринимателем».</p>
        </article>
        <article class="recogcard" data-rv>
          <span class="fi">{ic("building")}</span>
          <b>Клуб основателей</b>
          <p>Основатели клубов, которые открывают и развивают клуб в своём регионе.</p>
        </article>
      </div>
{cta_box("Клуба в вашем городе ещё нет?", "Укажите город в заявке — сообщим, когда клуб откроется.")}
    </div>
  </section>'''


def program_block(anchor, icon, n, title, lead, where, what, who):
    li = lambda xs: "\n".join(f"            <li>{x}</li>" for x in xs)
    return f'''      <article class="dirblock" id="{anchor}" data-rv>
        <div class="dirblock-head">
          <span class="fi">{ic(icon)}</span>
          <div><h2>{title}</h2></div>
        </div>
        <p class="lead">{lead}</p>
        <div class="dirblock-grid">
          <div>
            <h3>Где проходит</h3>
            <ul>
{li(where)}
            </ul>
          </div>
          <div>
            <h3>Что входит</h3>
            <ul>
{li(what)}
            </ul>
          </div>
          <div>
            <h3>Кому подойдёт</h3>
            <ul>
{li(who)}
            </ul>
          </div>
        </div>
      </article>'''


PROGRAMS = f'''  <section class="sec">
    <div class="wrap">
      <div class="sec-head" data-rv style="max-width:46rem">
        <span class="eyebrow">Образовательная система</span>
        <h2 class="h2">Четыре направления — центральный элемент сообщества</h2>
        <p class="lead" style="margin-top:1rem">Здоровье даёт энергию, счастье наполняет жизнь смыслом, финансовая грамотность создаёт устойчивое благополучие, предпринимательство открывает возможности для самореализации.</p>
      </div>
{program_block("health", "heart-pulse", "01", "«Будь здоров»", "Здоровье, энергия и активное долголетие.",
    ["Кабинет здоровья", "Клуб общения и ЗОЖ"],
    ["Замеры и консультации специалистов по записи", "Полезные завтраки и дегустации"],
    ["Всем участникам клуба", "Новичкам и опытным участникам"])}
{program_block("happy", "smile", "02", "«Будь счастлив»", "Гармония, отношения и личностный рост.",
    ["Центр обучения и развития", "Клуб общения и ЗОЖ"],
    ["Тренинги и мастер-классы", "Встречи и обмен опытом"],
    ["Тем, кто хочет гармонии в жизни и семье", "Тем, кто работает над личностным ростом"])}
{program_block("rich", "banknote", "03", "«Будь богат»", "Финансовая грамотность, достаток и материальное благополучие.",
    ["Центр обучения и развития"],
    ["Управление личными финансами", "Поиск возможностей для увеличения доходов"],
    ["Тем, кто хочет устойчивого благополучия", "Новичкам в финансовой грамотности"])}
{program_block("business", "rocket", "04", "«Будь предпринимателем»", "Предпринимательское мышление, лидерство и создание новых источников дохода.",
    ["Центр обучения и развития", "Клуб предпринимателей"],
    ["Предпринимательское мышление и лидерство", "Реализация предпринимательских идей"],
    ["Сообществу осознанных MLM-предпринимателей", "Тем, кто строит своё дело"])}
    </div>
  </section>

  <section class="sec sec-surface">
    <div class="wrap">
      <div class="sec-head" data-rv>
        <span class="eyebrow">Как проходит обучение</span>
        <h2 class="h2">От вводного курса до углублённого уровня</h2>
      </div>
      <div class="flow-grid">
        <article class="flowcard" data-rv>
          <h3><span class="fi">{ic("sprout")}</span>Ступени каждой программы</h3>
          {STEPS_FLOW}
        </article>
        <article class="flowcard" data-rv>
          <h3><span class="fi">{ic("users")}</span>Как начать</h3>
          {JOIN_FLOW}
        </article>
      </div>
{cta_box("Не знаете, с какой программы начать?", "Выбирать заранее не нужно: на первой встрече руководитель клуба поможет определиться.", white=True)}
    </div>
  </section>'''


def event_card(kind, title, place="Шымкент, Орынбаева 23"):
    return f'''        <article class="ncard tpl" data-rv>
          <span class="soon">Анонс готовится</span>
          <span class="kind" style="margin-top:.875rem">{kind}</span>
          <h3 style="margin-top:.25rem">{title}</h3>
          <div class="card-meta">
            <span>{ic("pin", False)}{place}</span>
          </div>
        </article>'''


EVENTS = f'''  <section class="sec">
    <div class="wrap">
      <div class="sec-head" data-rv>
        <span class="eyebrow">Форматы встреч</span>
        <h2 class="h2">Что будет в афише</h2>
        <p class="lead" style="margin-top:1rem">У каждого клуба свой календарь мероприятий. Ни одной даты и ни одного названия мы не придумываем: анонсы появятся, когда календарь будет утверждён.</p>
      </div>
      <!-- Дат, площадок и названий мероприятий в брифе нет. Публиковать — только по календарю заказчицы. -->
      <div class="newsgrid">
{event_card("Встреча клуба", "Полезные завтраки и дегустации")}
{event_card("Тренинг", "Занятия по четырём программам развития")}
{event_card("Мастер-класс", "Практика с обученными спикерами клуба")}
{event_card("Кабинет здоровья", "Замеры и консультации по записи")}
{event_card("Центр обучения", "Вводный курс для новых участников")}
{event_card("Встреча сообщества", "Обмен опытом и взаимная поддержка")}
      </div>
{cta_box("Календарь собирается", "Оставьте заявку — приглашение на первую встречу придёт раньше, чем афиша появится на сайте.")}
    </div>
  </section>'''


EXPERTS = f'''  <section class="sec">
    <div class="wrap">
      <div class="sec-head" data-rv>
        <span class="eyebrow">Роли в клубе</span>
        <h2 class="h2">Кто ведёт программы и встречи</h2>
        <p class="lead" style="margin-top:1rem">Набор одинаковый во всех региональных клубах.</p>
      </div>
      <div class="dirs">
{dircard("users", "", "Руководитель клуба", "Отвечает за работу клуба, календарь мероприятий и связь с участниками.")}
{dircard("cap", "", "Обученные спикеры", "Ведут четыре программы развития, тренинги и мастер-классы.")}
{dircard("stethoscope", "", "Специалисты кабинета здоровья", "Проводят замеры и консультации по предварительной записи.")}
{dircard("sprout", "", "Основатели клубов", "Открывают и развивают клубы в своих регионах.")}
      </div>
    </div>
  </section>

  <section class="sec sec-surface">
    <div class="wrap about-grid">
      <div data-rv>
        <span class="eyebrow">Основатель</span>
        <h2 class="h2">У истоков экосистемы</h2>
        <p class="lead" style="margin-top:1.25rem">ASYL ALEM LIFE — новое направление экосистемы ASYL ARMAN. Имена наставников и спикеров первого клуба появятся здесь, когда состав будет утверждён: придумывать людей и регалии мы не станем.</p>
      </div>
      <div data-rv>
        {FOUNDER}
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
{cta_box("Хотите вести программу в своём городе?", "Укажите это в заявке и выберите «Клуб основателей».")}
    </div>
  </section>'''


STORIES = f'''  <section class="sec">
    <div class="wrap">
      <div class="sec-head" data-rv>
        <span class="eyebrow">Истории развития</span>
        <h2 class="h2">О чём будут эти истории</h2>
        <p class="lead" style="margin-top:1rem">Реальные истории участников по четырём направлениям — только настоящие и только с их согласия.</p>
      </div>
      <div class="dirs">
{dircard("heart-pulse", "", "Здоровье", "Что изменилось после кабинета здоровья и программы «Будь здоров».")}
{dircard("smile", "", "Отношения", "Как программа «Будь счастлив» повлияла на жизнь и семью.")}
{dircard("banknote", "", "Финансы", "Что дала финансовая грамотность и программа «Будь богат».")}
{dircard("rocket", "", "Своё дело", "Как участники клуба предпринимателей начали и развили бизнес.")}
      </div>
      <!-- Ни одной истории, цитаты, имени или фото участника в брифе нет. -->
{cta_box("Историй пока нет", "Сообщество запускается 15 декабря 2026 года. Отзывов и историй, которых не было, здесь не появится — станьте участником, и ваша история может стать одной из первых.")}
    </div>
  </section>'''


JOIN = f'''  <section class="sec">
    <div class="wrap cpage">
      <div data-rv>
        <span class="eyebrow">Контакты</span>
        <h2 class="h2">Как с нами связаться</h2>
        {contact_list(page=True)}
      </div>

      <div class="form" data-rv>
        <h3>Оставить заявку</h3>
        <p class="hint">Заявка → выбор клуба в своём городе → участие во встречах и программах.</p>
        {lead_form("j", "j-success")}
      </div>
    </div>
  </section>

  <section class="sec sec-surface">
    <div class="wrap">
      <div class="sec-head" data-rv>
        <span class="eyebrow">Схема участия</span>
        <h2 class="h2">Как вступить и какой клуб выбрать</h2>
        <p class="lead" style="margin-top:1rem">Участие в клубе не требует вступления в MLM-бизнес. Условия вступления и оплаты утверждаются и появятся на сайте до запуска.</p>
      </div>
      <div class="flow-grid">
        <article class="flowcard" data-rv>
          <h3><span class="fi">{ic("users")}</span>Путь участника</h3>
          {JOIN_FLOW}
        </article>
        <article class="flowcard" data-rv>
          <h3><span class="fi">{ic("layers")}</span>Три клуба на выбор</h3>
          <ol class="flow">
            <li><i aria-hidden="true"></i>Клуб потребителей</li>
            <li><i aria-hidden="true"></i>Клуб предпринимателей</li>
            <li><i aria-hidden="true"></i>Клуб основателей</li>
          </ol>
        </article>
      </div>
    </div>
  </section>'''


PAGES = [
    dict(slug="index.html", active="",
         title="ASYL ALEM LIFE — сообщество развития и процветания",
         description="Сеть региональных клубов ASYL ALEM LIFE: четыре программы развития, кабинет здоровья и центр обучения. Первый клуб в Шымкенте, запуск 15 декабря 2026 года.",
         h1="Пространство роста, единства и созидания", body=INDEX),
    dict(slug="about.html", active="about", crumb="О сообществе",
         title="О сообществе — ASYL ALEM LIFE",
         description="Миссия, видение и философия ASYL ALEM LIFE, кому открыты клубы и как сообщество связано с экосистемой ASYL ARMAN.",
         h1="О сообществе ASYL ALEM LIFE",
         lead="Сильное сообщество единомышленников, объединённых стремлением к здоровью, счастью, финансовому благополучию и процветанию.",
         body=ABOUT),
    dict(slug="clubs.html", active="clubs", crumb="Наши клубы",
         title="Наши клубы — ASYL ALEM LIFE",
         description="Первый клуб ASYL ALEM LIFE в Шымкенте, Орынбаева 23. Три зоны клуба, единые стандарты и три клуба внутри сообщества.",
         h1="Наши клубы",
         lead="Сеть региональных клубов — основа сообщества. Первый клуб открывается в Шымкенте.",
         body=CLUBS),
    dict(slug="programs.html", active="programs", crumb="Программы развития",
         title="Программы развития — ASYL ALEM LIFE",
         description="Четыре программы клубов ASYL ALEM LIFE: «Будь здоров», «Будь счастлив», «Будь богат», «Будь предпринимателем». Вводный курс, практика, мастер-классы, углублённый уровень.",
         h1="Программы развития",
         lead="«Будь здоров», «Будь счастлив», «Будь богат», «Будь предпринимателем» — доступны и новичкам, и опытным лидерам.",
         body=PROGRAMS),
    dict(slug="events.html", active="events", crumb="Афиша событий",
         title="Афиша событий — ASYL ALEM LIFE",
         description="Встречи, тренинги и мастер-классы клубов ASYL ALEM LIFE. Календарь первого клуба выйдет до запуска 15 декабря 2026 года.",
         h1="Афиша событий",
         lead="Тренинги, встречи и мастер-классы. Календарь первого клуба выйдет на сайт до запуска 15 декабря 2026 года.",
         body=EVENTS),
    dict(slug="experts.html", active="experts", crumb="Эксперты и наставники",
         title="Эксперты и наставники — ASYL ALEM LIFE",
         description="Руководители клубов, обученные спикеры, специалисты кабинета здоровья и основатели клубов ASYL ALEM LIFE.",
         h1="Эксперты и наставники",
         lead="Специалисты, спикеры и основатели клубов: кто ведёт программы и встречи.",
         body=EXPERTS),
    dict(slug="stories.html", active="stories", crumb="Истории участников",
         title="Истории участников — ASYL ALEM LIFE",
         description="Реальные истории развития участников клубов ASYL ALEM LIFE появятся после запуска сообщества 15 декабря 2026 года.",
         h1="Истории участников",
         lead="Реальные истории развития. Первые появятся после запуска сообщества.",
         body=STORIES),
    dict(slug="join.html", active="join", crumb="Стать участником",
         title="Стать участником — ASYL ALEM LIFE",
         description="Заявка на участие в клубе ASYL ALEM LIFE: контакты, три шага до первой встречи и три клуба на выбор.",
         h1="Стать участником",
         lead="Заявка → выбор клуба в своём городе → участие во встречах и программах.",
         body=JOIN),
]
