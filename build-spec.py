#!/usr/bin/env python3
"""Gera spec-b2b.html a partir de spec-hub-b2b.md (design CB Enterprise).

Uso: python3 build-spec.py   (requer pandoc)
Depois: Chrome headless --print-to-pdf=spec-hub-b2b.pdf (recipe no README)
"""
import re
import subprocess

MD = 'spec-hub-b2b.md'
OUT = 'spec-b2b.html'

CSS = """
  :root{
    --ink:#0C0D0E; --panel:#131416; --bone:#F4F5F1; --orange:#F4632F;
    --dim:rgba(244,245,241,.80); --faint:rgba(244,245,241,.56);
    --rule:rgba(244,245,241,.14); --rule-strong:rgba(244,245,241,.28);
    --sans:"Geist",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    --mono:"Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  body{background:var(--ink);color:var(--bone);font-family:var(--sans);line-height:1.55;-webkit-font-smoothing:antialiased}
  .wrap{max-width:940px;margin:0 auto;padding:48px 28px 120px}
  header.doc{border-bottom:1px solid var(--rule-strong);padding-bottom:28px;margin-bottom:8px}
  .lockup{display:flex;flex-wrap:wrap;align-items:center;gap:12px;font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);margin-bottom:26px}
  .lockup b{color:var(--bone);font-weight:500}
  .lockup .sep{width:1px;height:13px;background:var(--rule-strong)}
  .lockup .tag{color:var(--orange)}
  h1{font-size:clamp(30px,4.6vw,46px);line-height:1.06;font-weight:650;letter-spacing:-.02em;max-width:26ch}
  .lede{margin-top:14px;font-size:18px;color:var(--dim);max-width:66ch}
  .toc{margin:34px 0 0;border:1px solid var(--rule);background:var(--panel);padding:18px 22px}
  .toc h4{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--faint);font-weight:500;margin-bottom:10px}
  .toc ol{margin:0 0 0 18px;color:var(--dim);font-size:14px;columns:2;column-gap:34px}
  .toc li{margin:4px 0;break-inside:avoid}
  h2{font-size:clamp(21px,2.6vw,27px);font-weight:650;letter-spacing:-.015em;margin:64px 0 8px;padding-top:18px;border-top:1px solid var(--rule);scroll-margin-top:24px}
  h3{font-size:18px;font-weight:600;margin:34px 0 4px}
  h4{font-size:15px;font-weight:600;margin:22px 0 2px;color:var(--bone)}
  p{margin:12px 0;color:var(--dim);max-width:76ch}
  p strong, li strong, td strong{color:var(--bone);font-weight:600}
  ul,ol{margin:12px 0 12px 22px;color:var(--dim)}
  li{margin:7px 0;max-width:74ch}
  blockquote{border-left:3px solid var(--orange);background:var(--panel);padding:14px 20px;margin:20px 0;max-width:80ch}
  blockquote p{margin:5px 0}
  table{border-collapse:collapse;width:100%;margin:18px 0;font-size:14px}
  th{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--faint);text-align:left;padding:10px 14px 8px 0;border-bottom:1px solid var(--rule-strong);font-weight:500}
  td{padding:10px 14px 10px 0;border-bottom:1px solid var(--rule);color:var(--dim);vertical-align:top}
  td:first-child{color:var(--bone)}
  .tbl-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
  code{font-family:var(--mono);font-size:.9em;color:var(--bone);background:rgba(244,245,241,.07);padding:1px 5px}
  pre{font-family:var(--mono);font-size:12.5px;background:var(--panel);border:1px solid var(--rule);padding:16px 18px;overflow-x:auto;margin:16px 0;color:var(--dim);line-height:1.55}
  pre code{background:none;padding:0;color:var(--dim);font-size:inherit}
  a{color:var(--orange);text-decoration:none}
  a:hover{text-decoration:underline}
  ul.task-list{list-style:none;margin-left:2px}
  ul.task-list li{position:relative;padding-left:26px}
  ul.task-list input[type=checkbox]{position:absolute;left:0;top:5px;appearance:none;width:14px;height:14px;border:1px solid var(--rule-strong);background:transparent}
  hr{border:0;border-top:1px solid var(--rule);margin:44px 0}
  footer{margin-top:80px;border-top:1px solid var(--rule-strong);padding-top:18px;font-family:var(--mono);font-size:12px;color:var(--faint);line-height:1.7}
  @media (max-width:680px){.toc ol{columns:1}}
  @media print{body{background:#fff}:root{--bone:#111;--dim:#333;--faint:#666;--panel:#f4f4f2;--ink:#fff;--rule:#ddd;--rule-strong:#bbb}.wrap{padding:0}h2{page-break-after:avoid}pre,table{page-break-inside:avoid}}
"""

TOC = """
<div class="toc">
  <h4>Neste documento</h4>
  <ol start="0">
    <li><a href="#como-usar-este-documento">Como usar / princípios inegociáveis</a></li>
    <li><a href="#o-que-estamos-construindo">O que estamos construindo</a></li>
    <li><a href="#modelo-de-dados-base">Modelo de dados (base)</a></li>
    <li><a href="#módulo-1-onboarding-de-empresa-prioridade-1">M1 — Onboarding de empresa</a></li>
    <li><a href="#módulo-2-identidade-do-usuário">M2 — Identidade do usuário</a></li>
    <li><a href="#módulo-3-progressão-o-strava-do-build">M3 — Progressão (Strava do build)</a></li>
    <li><a href="#módulo-4-painel-da-empresa">M4 — Painel da empresa</a></li>
    <li><a href="#módulo-5-admin-cb-clusterização-e-audiências">M5 — Admin CB e audiências</a></li>
    <li><a href="#módulo-6-feed-com-escopo-comunidade-canal-da-empresa">M6 — Feed com escopo</a></li>
    <li><a href="#permissões-e-privacidade">Permissões e privacidade</a></li>
    <li><a href="#backlog-recomendado-depois-do-núcleo-em-ordem-de-valor">Backlog recomendado</a></li>
    <li><a href="#ordem-de-implementação">Ordem de implementação</a></li>
    <li><a href="#perguntas-que-precisamos-responder-na-primeira-call">Perguntas para a primeira call</a></li>
  </ol>
</div>
"""


def main() -> None:
    md = open(MD, encoding='utf-8').read()
    # o cabecalho do .md (titulo + nota) vira o header da pagina
    body_md = '## 0. Como usar' + md.split('---\n\n## 0. Como usar', 1)[1]

    html_body = subprocess.run(
        ['pandoc', '-f', 'markdown+task_lists+pipe_tables', '-t', 'html5', '--wrap=none'],
        input=body_md, capture_output=True, text=True, check=True).stdout

    html_body = re.sub(r'<table>', '<div class="tbl-scroll"><table>', html_body)
    html_body = re.sub(r'</table>', '</table></div>', html_body)

    page = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Spec — Hub Cultura Builder: camada B2B</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">

<header class="doc">
  <div class="lockup"><b>CULTURA BUILDER</b><span class="sep"></span><span class="tag">Spec de implementação · hub</span><span class="sep"></span><span>20 Agosto 2026</span><span class="sep"></span><a href="/briefing-produto.html" style="color:inherit">← briefing anterior</a></div>
  <h1>Hub Cultura Builder — camada B2B</h1>
  <p class="lede">O que precisa ser construído para a empresa existir dentro do produto: onboarding self-service do time, identidade completa do usuário, progressão por construção (o &ldquo;Strava do build&rdquo;), painel da empresa, clusterização no admin e feed com escopo. Modelo de dados, telas, endpoints e critérios de aceite por módulo.</p>
  {TOC}
</header>

{html_body}

<footer>
  CULTURA BUILDER · SPEC HUB B2B · INTERNO · 20.08.2026<br>
  Contexto: <a href="/plano.html">plano B2B completo</a> · <a href="/briefing-produto.html">spec F0–F4 anterior</a> · <a href="/index.html">deck do Método Builder</a>
</footer>

</div>
</body>
</html>
"""
    open(OUT, 'w', encoding='utf-8').write(page)
    print(f'{OUT}: {len(page)} bytes')


if __name__ == '__main__':
    main()
