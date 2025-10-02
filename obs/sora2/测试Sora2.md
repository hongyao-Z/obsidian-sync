---
title: 测试Sora2
project: Sora2
author: 我
---

这是一次测试提交，用来验证 **GitHub Actions → Notion** 是否打通。
预期结果：在 Notion 的「Sora2 更新资料库」里，生成或更新一条标题为「测试Sora2」的记录。

内容要点：
- 这是一段纯文本，方便脚本写入为 Notion 段落块。
- 以后我只要在 `obs/sora2/` 下新增或修改 `.md` 文件并推送，工作流就会自动把变更同步到 Notion。
- 如果数据库字段名不是「名称 / 最近更新」，记得在 Actions 的 **变量** 里设置 `TITLE_PROP` 和 `UPDATED_PROP`。

本行作为结尾，用于观察追加更新：第一次提交后，我会再改这一段的最后一个词 —— **完成**。
