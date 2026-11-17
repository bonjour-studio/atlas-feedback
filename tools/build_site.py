#!/usr/bin/env python3
"""Build a dependency-free, multilingual static product and support website."""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REPO = "https://github.com/bonjour-studio/atlas-feedback"
SITE = "https://atlas.bonjour.dev"
EMAIL = "support@bonjour.dev"

COPY = {
    "en": {
        "language": "English", "html_lang": "en", "path": "",
        "nav": ["Features", "Support", "Feedback"], "skip": "Skip to content",
        "title": "Your apps.<br>Within reach.",
        "eyebrow": "APP STORE CONNECT, ON THE GO",
        "lead": "Check a build. Read a log. Keep testing moving. Your everyday App Store Connect work, on iPhone and iPad.",
        "primary": "Explore Atlas", "secondary": "Get support", "availability": "For iPhone and iPad · App Store release coming soon",
        "overview_alt": "Atlas App Overview on iPhone, showing versions, builds, Xcode Cloud and TestFlight for the fictional Orbit Notes app.",
        "cloud_alt": "Atlas Xcode Cloud screen on iPhone, showing a completed build, its steps, logs and artifacts with example data.",
        "feature_title": "The next step.<br>Always close by.",
        "feature_intro": "Built around the work you do most. Follow a release from its latest build to the people testing it.",
        "features": [
            ["01", "Versions & builds", "Check processing and testing status, pick a build, and manage review details without losing your place."],
            ["02", "TestFlight", "Manage test groups and invitations. Review screenshot and crash feedback, then keep the next beta moving."],
            ["03", "Localized information", "Switch languages in context. Update app and version details, plus supported in-app purchase and subscription metadata."],
        ],
        "cloud_label": "XCODE CLOUD", "cloud_title": "Follow the build.<br>Read the details.",
        "cloud_body": "Open a workflow, follow its runs and inspect each step. Read build logs and preview or share downloadable artifacts, right from your phone.",
        "cloud_note": "Available operations depend on Apple’s APIs, your key’s permissions and the resource state.",
        "account_title": "Your key. Your device.",
        "account_body": "Connect with your App Store Connect API key. Atlas signs requests on your device and connects directly to Apple. Account data is stored in an encrypted local database.",
        "premium_title": "One account to start. More when you need them.",
        "premium_body": "Manage one developer account for free. Atlas Premium adds support for more accounts, with monthly and annual options. Prices and renewal terms appear before purchase.",
        "support_label": "A LITTLE HELP", "support_title": "Let’s get you<br>back to work.",
        "support_body": "Find an answer, report a problem or suggest a better way. Choose the channel that fits your question.",
        "support_cta": "Open feedback hub", "mail": "Email support", "faq_title": "Good to know",
        "faq": [
            ["What do I need to get started?", "An App Store Connect API key and access to the apps you want to manage. Import your key in Atlas. The actions available depend on that key’s role and app access."],
            ["Why is an action unavailable?", "Apple’s APIs, resource state and key permissions can limit an action. Check the resource’s current state and the key’s access in App Store Connect. If the result looks wrong, send the visible error and steps to reproduce; never share your key."],
            ["How do I restore or cancel Premium?", "Use Restore Purchases on the Atlas Premium screen with the Apple Account used for purchase. Manage or cancel your subscription in iOS Settings → your Apple Account → Subscriptions."],
            ["What should I include in a bug report?", "Your Atlas version and build, device, iOS or iPadOS version, reproduction steps and the visible error. Remove API keys, tokens, personal information and private app data from attachments."],
        ],
        "independent": "Atlas is an independent app by Bonjour, LLC. It is not affiliated with or endorsed by Apple.",
        "footer": ["Privacy", "Terms", "GitHub"], "feedback_title": "A better Atlas<br>starts with you.",
        "feedback_lead": "Questions, ideas and reproducible bugs all have a place here. Public feedback is hosted on GitHub; you need a GitHub account to post.",
        "channels": [
            ["Bug reports", "Something isn’t working as expected? Send clear reproduction steps and we’ll have a starting point.", "Report a bug", REPO + "/issues/new/choose"],
            ["Questions & ideas", "Ask for help, suggest an improvement or share how you use Atlas.", "Open Discussions", REPO + "/discussions"],
            ["Private support", "For billing, privacy, account-specific details or a security concern, contact us privately.", "Email support", "mailto:" + EMAIL + "?subject=Atlas%20Support"],
        ],
        "privacy_note": "Keep your API key private. Never upload .p8 files, JWTs, credentials or unredacted customer data to public issues or discussions. We do not need your private key to investigate a report.",
        "feedback_back": "Back to Atlas", "not_found": "This page isn’t here.", "not_found_body": "Return to the homepage or contact support if you followed a broken link.",
    },
    "zh-Hans": {
        "language": "简体中文", "html_lang": "zh-Hans", "path": "zh-Hans/",
        "nav": ["功能", "支持", "反馈"], "skip": "跳到正文",
        "title": "你的 App，<br>随手掌握。", "eyebrow": "随身管理 APP STORE CONNECT",
        "lead": "检查构建，阅读日志，跟进测试。将 App Store Connect 的日常工作，带到 iPhone 和 iPad。",
        "primary": "了解 Atlas", "secondary": "获取帮助", "availability": "适用于 iPhone 和 iPad · 即将登陆 App Store",
        "overview_alt": "Atlas 的 iPhone App 概览界面，使用虚构的 Orbit Notes 示例展示版本、构建、Xcode Cloud 和 TestFlight。",
        "cloud_alt": "Atlas 的 iPhone Xcode Cloud 界面，以示例数据展示构建结果、执行步骤、日志与产物。",
        "feature_title": "下一步，<br>就在手边。", "feature_intro": "围绕高频工作组织信息。从最新构建，到正在使用它的测试人员，顺着发布进度继续操作。",
        "features": [
            ["01", "版本与构建", "查看处理和测试状态，选择构建，管理审核资料。关键进度清晰可见。"],
            ["02", "TestFlight 测试", "管理测试组与邀请，查看截图和崩溃反馈，继续推进下一轮测试。"],
            ["03", "多语言资料", "在当前页面切换语言，编辑 App、版本，以及 API 支持的内购和订阅资料。"],
        ],
        "cloud_label": "XCODE CLOUD", "cloud_title": "跟进构建，<br>看清细节。", "cloud_body": "打开工作流，查看构建记录与每个执行步骤。直接在手机上阅读编译日志，预览或分享可下载的产物。", "cloud_note": "可用操作受 Apple API、密钥权限及资源当前状态限制。",
        "account_title": "你的密钥，保存在你的设备。", "account_body": "使用 App Store Connect API 密钥连接账号。Atlas 在设备上签名请求并直接连接 Apple，账号数据保存在本地加密数据库中。",
        "premium_title": "先管理一个账号，需要时再增加。", "premium_body": "免费版支持一个开发者账号。Atlas Premium 支持管理更多账号，提供月付和年付方案。价格与续订条款在购买前展示。",
        "support_label": "需要一点帮助？", "support_title": "解决问题，<br>继续手头的工作。", "support_body": "寻找答案，报告问题，或分享更好的想法。选择适合你的反馈方式。",
        "support_cta": "进入反馈中心", "mail": "联系支持", "faq_title": "常见问题",
        "faq": [
            ["开始使用需要什么？", "需要 App Store Connect API 密钥，以及相应的 App 访问权限。在 Atlas 中导入密钥即可连接；可用操作取决于密钥的角色和 App 访问范围。"],
            ["为什么某个操作不可用？", "Apple API、资源状态与密钥权限都可能限制操作。请核对资源当前状态和密钥的访问范围。如果结果不符合预期，请提供页面错误和复现步骤，不要发送私钥。"],
            ["如何恢复或取消 Premium 订阅？", "使用购买时的 Apple 账号，在 Atlas Premium 页面选择恢复购买。管理或取消订阅，请前往 iOS 设置 → Apple 账号 → 订阅。"],
            ["报告问题时需要提供什么？", "请提供 Atlas 版本和构建号、设备型号、系统版本、复现步骤及页面错误。上传前移除 API 密钥、令牌、个人信息和私有 App 数据。"],
        ],
        "independent": "Atlas 由 Bonjour, LLC 独立开发，与 Apple 无隶属或背书关系。", "footer": ["隐私政策", "服务条款", "GitHub"],
        "feedback_title": "更好的 Atlas，<br>从你的反馈开始。", "feedback_lead": "使用问题、功能建议与可复现的故障，都可以在这里反馈。公开反馈由 GitHub 承载，发布内容需要 GitHub 账号。",
        "channels": [
            ["报告问题", "遇到不符合预期的行为？提供清楚的复现步骤，帮助我们定位问题。", "提交问题", REPO + "/issues/new/choose"],
            ["使用交流与建议", "寻求帮助，提出改进建议，或分享你的 Atlas 使用方式。", "进入 Discussions", REPO + "/discussions"],
            ["私人支持", "付款、隐私、账号专属信息或安全问题，请通过邮件私下联系。", "联系支持", "mailto:" + EMAIL + "?subject=Atlas%20Support"],
        ],
        "privacy_note": "请保护你的 API 密钥。不要在公开 Issue 或 Discussion 中上传 .p8 文件、JWT、凭据或未经脱敏的用户数据。排查反馈不需要你的私钥。",
        "feedback_back": "返回 Atlas 官网", "not_found": "这个页面不在这里。", "not_found_body": "请返回首页；如果是失效链接，可以联系支持。",
    },
    "ja": {
        "language": "日本語", "html_lang": "ja", "path": "ja/",
        "nav": ["機能", "サポート", "フィードバック"], "skip": "本文へ移動",
        "title": "あなたの App を、<br>いつでも手元に。", "eyebrow": "APP STORE CONNECT を、外出先でも",
        "lead": "ビルドの確認も、ログの閲覧も、テストの管理も。App Store Connect の日々の作業を、iPhone と iPad で。",
        "primary": "Atlas の機能", "secondary": "サポート", "availability": "iPhone・iPad 対応 · App Store で近日公開予定",
        "overview_alt": "架空の Orbit Notes を使い、バージョン、ビルド、Xcode Cloud、TestFlight を表示する Atlas の iPhone 画面。", "cloud_alt": "サンプルデータでビルド結果、実行ステップ、ログ、成果物を表示する Atlas の Xcode Cloud 画面。",
        "feature_title": "次の作業へ、<br>すぐに。", "feature_intro": "よく使う作業を中心に情報を整理。最新ビルドからテスターまで、リリースの進行に沿って管理できます。",
        "features": [["01", "バージョンとビルド", "処理やテストの状態を確認し、ビルドを選択して審査情報を管理。必要な進捗をひと目で。"], ["02", "TestFlight", "テストグループや招待を管理。スクリーンショットやクラッシュのフィードバックを確認し、次のベータへ。"], ["03", "ローカライズ情報", "ページ内で言語を切り替え、App やバージョン、API が対応するアプリ内課金・サブスクリプション情報を編集。"]],
        "cloud_label": "XCODE CLOUD", "cloud_title": "ビルドを追って、<br>詳細まで確認。", "cloud_body": "ワークフローから実行履歴と各ステップを確認。ビルドログを読み、ダウンロード可能な成果物をプレビュー・共有できます。", "cloud_note": "利用できる操作は Apple API、キーの権限、リソースの状態によって異なります。",
        "account_title": "あなたのキーは、あなたのデバイスに。", "account_body": "App Store Connect API キーで接続。Atlas はデバイス上でリクエストに署名し、Apple に直接接続します。アカウントデータはローカルの暗号化データベースに保存されます。",
        "premium_title": "まずは 1 アカウント。必要に応じて追加。", "premium_body": "無料版では開発者アカウントを 1 つ管理できます。Atlas Premium は複数アカウントに対応し、月額・年額プランを用意。価格と更新条件は購入前に表示されます。",
        "support_label": "お困りのときは", "support_title": "解決して、<br>作業の続きを。", "support_body": "疑問の解消、不具合の報告、改善のご提案。それぞれに合った窓口をご利用ください。", "support_cta": "フィードバック窓口", "mail": "メールで問い合わせ", "faq_title": "よくある質問",
        "faq": [["利用開始に必要なものは？", "App Store Connect API キーと、管理対象 App へのアクセス権が必要です。Atlas にキーを読み込んで接続します。利用できる操作はキーの役割と App へのアクセス権によって異なります。"], ["操作が利用できないのはなぜ？", "Apple API、リソースの状態、キーの権限により操作が制限される場合があります。現在の状態とアクセス権を確認してください。不明な場合はエラーと再現手順をご連絡ください。秘密キーは送信しないでください。"], ["Premium の復元・解約方法は？", "購入時の Apple Account で、Atlas Premium 画面の「購入を復元」を使用します。管理・解約は iOS の設定 → Apple Account → サブスクリプションから行えます。"], ["不具合報告に必要な情報は？", "Atlas のバージョンとビルド番号、機種、OS、再現手順、表示されたエラーを記載してください。添付ファイルから API キー、トークン、個人情報、非公開の App データを削除してください。"]],
        "independent": "Atlas は Bonjour, LLC が開発する独立したアプリであり、Apple との提携・後援関係はありません。", "footer": ["プライバシー", "利用規約", "GitHub"],
        "feedback_title": "よりよい Atlas は、<br>あなたの声から。", "feedback_lead": "質問、アイデア、再現できる不具合をお寄せください。公開フィードバックは GitHub で受け付けています。投稿には GitHub アカウントが必要です。",
        "channels": [["不具合の報告", "期待どおりに動作しない場合は、再現手順を添えてご報告ください。", "不具合を報告", REPO + "/issues/new/choose"], ["質問とアイデア", "使い方の質問、改善の提案、Atlas の活用方法を共有できます。", "Discussions を開く", REPO + "/discussions"], ["個別のお問い合わせ", "請求、プライバシー、アカウント固有の情報、セキュリティの問題はメールでご連絡ください。", "メールで問い合わせ", "mailto:" + EMAIL + "?subject=Atlas%20Support"]],
        "privacy_note": "API キーを保護してください。.p8 ファイル、JWT、認証情報、未加工の顧客データを公開投稿に添付しないでください。調査のために秘密キーをお預かりすることはありません。",
        "feedback_back": "Atlas のホームへ", "not_found": "ページが見つかりません。", "not_found_body": "ホームページに戻るか、リンク切れの場合はサポートへご連絡ください。",
    },
}


def escape(value):
    return html.escape(value, quote=True)


def document(lang, kind, body, title=None):
    c = COPY[lang]
    path = c["path"]
    is_home = kind == "home"
    depth = len([x for x in path.split("/") if x]) + (0 if is_home else len(kind.split("/")))
    base = "../" * depth or "./"
    home = base + path
    feedback = home + "feedback/"
    title = title or ("Atlas — " + ("App Store Connect, within reach" if is_home else c["nav"][2]))
    canonical = SITE + "/" + path + ("" if is_home else kind + "/")
    languages = "".join(
        f'<a href="{base}{v["path"]}{"" if is_home else kind + "/"}" lang="{v["html_lang"]}" hreflang="{v["html_lang"]}"'
        + (' aria-current="page"' if k == lang else "") + f'>{v["language"]}</a>'
        for k, v in COPY.items()
    )
    alternates = "".join(f'<link rel="alternate" hreflang="{v["html_lang"]}" href="{SITE}/{v["path"]}{"" if is_home else kind + "/"}">' for v in COPY.values())
    return f'''<!doctype html>
<html lang="{c['html_lang']}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title><meta name="description" content="{escape(c['lead'])}">
<meta name="theme-color" content="#eff3f8"><meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(c['lead'])}"><meta property="og:type" content="website">
<meta property="og:image" content="{SITE}/assets/app-icon.png"><link rel="canonical" href="{canonical}">
{alternates}<link rel="icon" href="{base}assets/app-icon.png"><link rel="stylesheet" href="{base}assets/site.css">
</head>
<body><a class="skip" href="#main">{c['skip']}</a>
<header class="topbar"><nav class="shell nav" aria-label="Atlas">
<a class="brand" href="{home}"><img src="{base}assets/app-icon.png" width="36" height="36" alt=""><span>Atlas</span></a>
<div class="nav-links"><a href="{home}#features">{c['nav'][0]}</a><a href="{home}#support">{c['nav'][1]}</a><a href="{feedback}">{c['nav'][2]}</a></div>
<details class="language"><summary><span aria-hidden="true">◎</span> {c['language']}</summary><div class="language-menu">{languages}</div></details>
</nav></header>
<main id="main">{body}</main>
<footer class="footer shell"><div><a class="brand" href="{home}">Atlas</a><p>© 2026 Bonjour, LLC.</p></div><div class="footer-right"><nav aria-label="Footer"><a href="{feedback}">{c['nav'][2]}</a><a href="{base}legal/privacy/">{c['footer'][0]}</a><a href="{base}legal/terms/">{c['footer'][1]}</a><a href="{REPO}">{c['footer'][2]}</a></nav><p>{c['independent']}</p></div></footer>
</body></html>'''


def home(lang):
    c = COPY[lang]
    base = "../" if c["path"] else "./"
    features = "".join(f'<article><span class="number">{n}</span><h3>{title}</h3><p>{text}</p></article>' for n, title, text in c["features"])
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in c["faq"])
    return document(lang, "home", f'''
<section class="hero"><div class="shell hero-grid"><div class="hero-copy"><p class="eyebrow">{c['eyebrow']}</p><h1>{c['title']}</h1><p class="lead">{c['lead']}</p><div class="actions"><a class="button" href="#features">{c['primary']} <span aria-hidden="true">↓</span></a><a class="text-link" href="#support">{c['secondary']} <span aria-hidden="true">↗</span></a></div><p class="availability">{c['availability']}</p></div><figure class="hero-visual"><img src="{base}assets/overview-{lang}.png" width="520" height="1063" alt="{c['overview_alt']}" fetchpriority="high"></figure></div></section>
<section class="features shell" id="features"><div class="section-intro"><h2>{c['feature_title']}</h2><p>{c['feature_intro']}</p></div><div class="feature-grid">{features}</div></section>
<section class="cloud"><div class="shell cloud-grid"><figure><img src="{base}assets/cloud-{lang}.png" width="520" height="1063" alt="{c['cloud_alt']}" loading="lazy"></figure><div><p class="eyebrow">{c['cloud_label']}</p><h2>{c['cloud_title']}</h2><p class="lead">{c['cloud_body']}</p><p class="fine">{c['cloud_note']}</p></div></div></section>
<section class="account shell"><article><span class="number" aria-hidden="true">⌘</span><h3>{c['account_title']}</h3><p>{c['account_body']}</p></article><article><span class="number" aria-hidden="true">＋</span><h3>{c['premium_title']}</h3><p>{c['premium_body']}</p></article></section>
<section class="support" id="support"><div class="shell"><div class="section-intro"><div><p class="eyebrow">{c['support_label']}</p><h2>{c['support_title']}</h2></div><div><p>{c['support_body']}</p><div class="actions"><a class="button" href="feedback/">{c['support_cta']} <span aria-hidden="true">↗</span></a><a class="text-link" href="mailto:{EMAIL}?subject=Atlas%20Support">{c['mail']}</a></div></div></div><div class="faq"><h3>{c['faq_title']}</h3><div>{faq}</div></div></div></section>''')


def feedback(lang):
    c = COPY[lang]
    channels = "".join(f'<article><span class="number">0{i+1}</span><h2>{title}</h2><p>{text}</p><a class="text-link" href="{escape(url)}">{label} <span aria-hidden="true">↗</span></a></article>' for i, (title, text, label, url) in enumerate(c["channels"]))
    return document(lang, "feedback", f'<section class="shell feedback"><p class="eyebrow">ATLAS / {c["nav"][2]}</p><h1>{c["feedback_title"]}</h1><p class="lead narrow">{c["feedback_lead"]}</p><div class="channel-grid">{channels}</div><aside class="privacy-note">{c["privacy_note"]}</aside></section>')


def inline(text):
    text = escape(text)
    for tag in ["b", "code"]:
        text = text.replace(f'&lt;{tag}&gt;', f'<{tag}>').replace(f'&lt;/{tag}&gt;', f'</{tag}>')
    text = text.replace('&lt;br /&gt;', '<br>')
    return re.sub(r'\[([^\]]+)\]\((https://[^\s)]+|mailto:[^\s)]+)\)', r'<a href="\2">\1</a>', text)


def legal_html(source):
    parts = []
    for block in source.split("\n\n"):
        if not block.strip():
            continue
        if block.startswith("- "):
            items = block.splitlines()
            parts.append("<ul>")
            nested = False
            for line in items:
                is_nested = line.startswith("  ")
                if is_nested and not nested:
                    parts.append("<ul>"); nested = True
                if not is_nested and nested:
                    parts.append("</ul></li>"); nested = False
                elif not is_nested and len(parts) > 1 and parts[-1].startswith("<li>"):
                    parts[-1] += "</li>"
                text = inline(line.strip().removeprefix("- "))
                parts.append("<li>" + text + ("</li>" if is_nested else ""))
            if nested:
                parts.append("</ul></li>")
            elif parts[-1].startswith("<li>"):
                parts[-1] += "</li>"
            parts.append("</ul>")
        else:
            heading = re.match(r'^<b>(\d+\.[^<]+)</b>(?:<br />)?(.*)', block, re.S)
            if heading:
                parts.append(f'<h2>{escape(heading[1])}</h2>')
                if heading[2].strip():
                    parts.append(f'<p>{inline(heading[2])}</p>')
            else:
                parts.append(f'<p>{inline(block)}</p>')
    return "\n".join(parts)


def build():
    for lang, c in COPY.items():
        folder = DOCS / c["path"]
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "index.html").write_text(home(lang))
        (folder / "feedback").mkdir(exist_ok=True)
        (folder / "feedback/index.html").write_text(feedback(lang))
    for slug, filename, title in [("privacy", "privacy-policy.md", "Privacy Policy"), ("terms", "terms-of-use.md", "Terms of Use")]:
        source = (DOCS / "legal" / filename).read_text()
        body = f'<article class="shell legal"><p class="eyebrow">ATLAS / LEGAL</p><h1>{title}</h1>{legal_html(source)}</article>'
        for route in [slug, "legal/" + slug]:
            (DOCS / route).mkdir(parents=True, exist_ok=True)
            page = document("en", route, body, f"Atlas — {title}")
            # Keep legacy GitHub Pages links working, but use the directly
            # served legal paths on the custom domain as canonical URLs.
            page = page.replace(f'href="{SITE}/{slug}/"', f'href="{SITE}/legal/{slug}/"')
            # The published legal text is authoritative in English.
            page = re.sub(r'<details class="language">.*?</details>', '', page)
            page = re.sub(r'<link rel="alternate"[^>]+>', '', page)
            (DOCS / route / "index.html").write_text(page)
    c = COPY["en"]
    # Absolute fallback links are needed when a missing path has unknown depth.
    (DOCS / "404.html").write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Atlas — Page not found</title><body style="font:18px system-ui;max-width:600px;margin:15vh auto;padding:24px"><h1>{c["not_found"]}</h1><p>{c["not_found_body"]}</p><p><a href="{SITE}/">{c["feedback_back"]}</a></p></body></html>')
    (DOCS / ".nojekyll").touch()
    (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    urls = [f'{SITE}/{c["path"]}{suffix}' for c in COPY.values() for suffix in ["", "feedback/"]] + [SITE + "/legal/privacy/", SITE + "/legal/terms/"]
    (DOCS / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join('<url><loc>'+url+'</loc></url>' for url in urls) + '</urlset>\n')
    print(f"Built {len(list(DOCS.rglob('*.html')))} static pages.")


if __name__ == "__main__":
    build()
