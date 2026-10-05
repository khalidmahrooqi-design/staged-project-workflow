# Staged Project Workflow

An agent skill by Khalid Hamad Al Mahrouqi for taking work from a clear brief to a verified result.

**Brief → Architecture → Plan and checklists → Execute → Check results and logs → Plan justified updates**

The skill applies to software, documents, analysis, and operational tasks. Small tasks use a compact version; substantive projects get a visible structure and phased checklist. It reuses existing authorization and asks for input when a missing decision affects the work.

## Install globally for Codex

```sh
npx skills add khalidmahrooqi-design/staged-project-workflow --skill staged-project-workflow --agent codex --global --yes
```

The [Skills CLI](https://github.com/vercel-labs/skills) provides the installation command. You can inspect the available skill first:

```sh
npx skills add khalidmahrooqi-design/staged-project-workflow --list
```

For manual installation, copy `skills/staged-project-workflow/` into your agent's user-level skills directory. The skill itself needs no runtime dependencies or account connection. Refresh your agent's skill inventory or start a new chat if it does not appear.

## Use

```text
Use $staged-project-workflow to build this project. Brief me if needed,
show the architecture and staged checklist, execute the plan, check the
results and relevant logs, and prepare a next update plan if warranted.
```

Automatic selection is enabled in the included Codex metadata. To make this your default across Codex chats, add the [global rule](GLOBAL-RULE.md) to your existing global instructions. Installing the skill alone does not edit those instructions. Other agents must support the SKILL.md format; their installation paths and metadata support vary.

## What completion means

Checklist items need completion evidence. The final report distinguishes passed, failed, and unperformed checks. Required fixes remain part of the current task; optional improvements get a separate next plan. Unavailable evidence is reported explicitly.

See the [skill instructions](skills/staged-project-workflow/SKILL.md), [plan template](skills/staged-project-workflow/references/plan-template.md), and [worked example](examples/document-task.md). The workflow preserves your permissions, approved destinations, source-handling rules, and project boundaries. It does not authorize external actions or activate background monitoring.

## العربية

مهارة من إعداد خالد بن حمد المحروقي لتنفيذ المهام والمشاريع على مراحل:

**تحديد المطلوب → تصميم هيكل المشروع → إعداد الخطة وقوائم التحقق → التنفيذ → فحص النتائج والسجلات ذات الصلة → إعداد خطة تحديث عند الحاجة**

تتناسب التفاصيل مع حجم المهمة. تعرض المهارة هيكل المشروع وخطواته ومعايير قبول النتائج قبل تنفيذ الأعمال الجوهرية، وتطلب توضيحاً عندما يؤثر قرار ناقص في العمل. تتحقق من النتيجة الفعلية، وتوضح الفحوص التي نجحت أو فشلت أو لم تُنفذ. يمكن تثبيتها عالمياً باستخدام الأمر أعلاه، وإضافة القاعدة المرفقة إلى تعليمات الوكيل لتطبيقها افتراضياً.

## Contribute and share

Issues and pull requests are welcome. Describe the scenario, expected behavior, and observed problem; omit private records and credentials. This original skill is shared under the [MIT license](LICENSE), allowing use, modification, and redistribution with the license notice retained.
