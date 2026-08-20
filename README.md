# Método Builder — deck interno

Deck de alinhamento interno da Cultura Builder: o que precisa acontecer para o Método Builder virar máquina (faixas, liturgia, esteira de onboarding, banco de professores, fases do hub).

- **Live:** https://metodo.brunopessoa.com (+ `/metodo-builder.pdf`)
- 16 slides, PT-BR, formato palco (sparse — Bruno narra).
- Navegação: setas / espaço / clique (terço esquerdo volta), deep link `#N`.

## Editar

Editar `index.html` direto (arquivo único, CSS/JS inline). Depois:

```bash
# regenerar o PDF (Chrome headless, 1280x720 por slide)
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=metodo-builder.pdf "file://$PWD/index.html"

git add -A && git commit -m "..." && git push
# redeploy Coolify (uuid no memory file project_cb_metodo_builder_aug17)
```

Design: CB Enterprise (ink #0C0D0E / bone #F4F5F1 / orange #F4632F, Geist + Geist Mono), sem gradientes. Assinatura visual: a faixa (belt) — capa, slide de níveis e barra de progresso.

## Spec da camada B2B do hub

- `spec-hub-b2b.md` — fonte (é o arquivo que vai para o dev do hub / Claude Code dele)
- `spec-b2b.html` — versão publicada em https://metodo.brunopessoa.com/spec-b2b.html
- `spec-hub-b2b.pdf` — PDF para enviar por WhatsApp/e-mail

Editar sempre o `.md` e regerar:

```bash
python3 build-spec.py            # requer pandoc
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=spec-hub-b2b.pdf "file://$PWD/spec-b2b.html"
git add -A && git commit -m "..." && git push
# redeploy: Coolify app igfglw7z9w8dgoxpzar3dbvt
```

Arquivo novo só aparece no ar depois de ganhar uma linha `COPY` no `Dockerfile`.
