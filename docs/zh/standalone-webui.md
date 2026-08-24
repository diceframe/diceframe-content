# 独立部署 WebUI

中文 | [English](../en/standalone-webui.md)

DiceFrame 默认由后端同时提供 WebUI，桌面版、Windows 打包版和 Docker 部署都可以继续使用这种同源模式。只有在希望把浏览器页面放到 Cloudflare Pages 等静态托管、而 DiceFrame 后端继续运行在 NAS、家用电脑或服务器上时，才需要独立部署 WebUI。

独立 WebUI 只是前端页面，不包含 DiceFrame 后端、存档或 API Key。浏览器仍会直接连接你指定的 DiceFrame 后端：

```text
浏览器 → HTTPS 静态 WebUI → HTTPS DiceFrame 后端 → data/ 与模型服务
```

## 准备工作

- 使用包含 `npm run build:standalone` 的 DiceFrame 版本或最新源码。
- 准备 Node.js 与 npm；Cloudflare Pages 也可以在云端完成构建。
- 为 DiceFrame 后端提供浏览器可访问的 HTTPS 地址，例如通过反向代理或 Cloudflare Tunnel。
- 知道静态 WebUI 的完整 Origin，例如 `https://diceframe.pages.dev`。

如果静态 WebUI 使用 HTTPS，浏览器会阻止它调用普通 HTTP 后端。仅给静态页面启用 HTTPS 不够，后端也必须是 HTTPS。

## 方式一：Cloudflare Pages

连接 DiceFrame GitHub 仓库后，使用以下构建设置：

| 设置 | 值 |
| --- | --- |
| Root directory | `frontend-v2` |
| Build command | `npm run build:standalone` |
| Build output directory | `dist` |

构建不需要 API Key，也不要把后端密码、模型密钥或其他秘密写进 Pages 环境变量。部署完成后记下 Pages 分配的域名；自定义域名启用后，应以实际访问域名作为下文的 Origin。

## 方式二：构建后上传到其他静态托管

在 DiceFrame 源码目录执行：

```bash
cd frontend-v2
npm ci
npm run build:standalone
```

将生成的 `frontend-v2/dist/` 整个目录部署到支持 HTTPS 的静态托管。不要使用普通的 `npm run build`：它生成的是由 DiceFrame 后端内置提供的同源前端。

## 配置后端允许访问

后端必须明确允许独立 WebUI 的 Origin。Origin 只包含协议、域名和可选端口，不包含路径。

推荐先打开后端自带的 WebUI，在 **设置 → 分享地址 → 独立前端跨域白名单** 中填写：

```text
https://diceframe.pages.dev
```

多个 Origin 可以用逗号或分号分隔。保存后会写入后端的 `data/config.json` 并立即生效。

自动化部署也可以设置环境变量：

```env
TRPG_WEB_CORS_ORIGINS=https://diceframe.pages.dev,https://play.example.com
```

环境变量优先于 WebUI 配置；修改后需要重启 DiceFrame，设置页中的白名单会显示为只读。请填写实际前端 Origin，不要填写后端地址，不要添加路径，也不要使用 `*`。

## 第一次连接

1. 打开已经部署的独立 WebUI。
2. 在登录页填写 DiceFrame 后端的 HTTPS 地址，例如 `https://api.example.com`。
3. 如果后端位于反向代理子路径下，填写完整路径，例如 `https://example.com/diceframe`。
4. 点击连接，然后输入 DiceFrame 访问密码。

浏览器会在本机保存最近使用的后端地址。由独立 WebUI 创建的分享链接也会携带后端地址，但不会携带访问密码或模型 API Key。

## 升级与兼容性

- Windows 打包版、Docker 和 `python web_server.py` 的启动方式不变；不使用独立 WebUI 就不需要设置 CORS。
- 独立 WebUI 与后端最好来自同一 DiceFrame 版本。升级后端时，同时重新构建和部署静态页面，可以避免前后端接口版本不一致。
- 存档、配置和插件数据仍全部保存在后端的 `data/`，重新部署静态页面不会迁移或清空这些数据。

## 安全建议

- 只允许你实际控制的前端 Origin，切勿使用通配符 `*`。
- 对公网后端启用 DiceFrame 访问密码，并通过可信的 HTTPS 反向代理或隧道暴露服务。
- 不要把模型 API Key、DiceFrame 访问密码或 `.env` 打包进 `dist/`；静态站点中的文件对访问者可见。
- 如果只在本机或局域网使用，继续使用后端自带 WebUI 通常更简单。

## 排查问题

### 页面能打开，但连接服务器失败

依次确认后端地址可以从当前浏览器访问、使用 HTTPS，并且没有漏掉反向代理路径。直接在浏览器访问 `后端地址/api/config` 也应能收到 DiceFrame 响应，而不是代理服务器的 404 页面。

### 浏览器提示 CORS 错误

检查白名单填写的是静态 WebUI 的 Origin，例如 `https://play.example.com`，而不是后端地址。域名、协议和端口必须完全一致；配置中不能带路径。

### 浏览器提示 Mixed Content

静态 WebUI 是 HTTPS，而后端仍是 HTTP。需要先为后端配置 HTTPS，不能通过放宽 CORS 解决。

### 更新后页面或功能异常

重新构建并部署 `dist/`，清理静态托管缓存，然后确认前后端使用相同版本。若仍有问题，可以先访问后端自带 WebUI，区分是静态部署问题还是后端问题。
