# AI Bot 驱动的软件开发流程 Demo

这是一个展示 AI Bot 如何协助完整软件开发流程的交互式演示。

## 功能特点

- 📱 **手机端聊天界面**: 模拟真实的 Bot 交互体验
- 📊 **实时工作流可视化**: 右侧面板展示每个步骤的进展
- 🎭 **多角色协作**: 开发者、测试人员、发布人员的完整流程
- ⏱️ **时间线追踪**: 记录每个关键节点

## 工作流程

1. **任务分配** - Bot 展示 JIRA 任务列表
2. **技术规范** - Bot 自动生成 Spec 文档
3. **代码审查** - 用户 Review 技术规范
4. **并行开发** - Bot 编码，用户可同时处理其他任务
5. **自动审查** - Bot 完成开发并进行 Code Review
6. **测试环境** - Bot 自动部署并通知测试人员
7. **自动化测试** - 测试人员批准，Bot 执行测试
8. **生产发布** - 发布人员完成部署

## 本地运行

```bash
cd dev-workflow-demo
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install fastapi uvicorn
python backend/app.py
```

然后访问 http://localhost:8080

## GitHub Pages 部署

将 `static/index.html` 上传到 GitHub 仓库的 `docs/` 目录或 `gh-pages` 分支即可。

## 技术栈

- 纯原生 HTML/CSS/JavaScript (无框架依赖)
- FastAPI 后端 (可选，用于本地开发)
- 响应式设计，支持桌面和平板

## 目录结构

```
dev-workflow-demo/
├── backend/
│   └── app.py          # FastAPI 服务器
├── static/
│   └── index.html      # 主页面 (可直接部署)
└── README.md
```

## 下一步扩展

- [ ] 添加真实的 GitHub API 集成
- [ ] 连接真实的 JIRA 数据
- [ ] 支持自定义工作流配置
- [ ] 添加 WebSocket 实时通信
- [ ] 多语言支持 (English, etc.)
