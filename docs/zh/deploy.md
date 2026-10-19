# Docker / Linux 部署说明

中文 | [English](../en/deploy.md)

想用 Docker 可以直接照下面部署；习惯在电脑上运行的用户不用改用法。Windows、macOS 和 Linux 仍然可以这样启动：

```bash
pip install -r requirements.txt
python web_server.py
```

Docker 里固定把运行数据放在 `/app/data`，compose 会映射到项目根目录的 `./data`。存档、配置、访问令牌、插件运行数据都留在宿主机，不会被镜像重建清掉。用户安装的插件源码也落在 `/app/data/plugin-packages/`，随 data 卷保留，升级或重建容器后不会丢失；`/app/plugins` 仅内置示例，随镜像更新。

如果只想把浏览器页面部署到 Cloudflare Pages 等静态托管、后端仍运行在自己的设备上，请改看[独立部署 WebUI](standalone-webui.md)。这种模式是可选项，不影响本页的 Windows、Linux 或 Docker 部署方式。

## 快速启动

使用发布镜像：

Compose 命令必须在含有 `docker-compose.yml` 的 DiceFrame 部署目录执行。请先克隆仓库或下载并解压 GitHub Release 的源码包，再进入其根目录：

```bash
git clone --depth 1 https://github.com/diceframe/diceframe.git
cd diceframe
test -f docker-compose.yml
```

如果使用的是下载的源码包，只需把 `cd diceframe` 换成实际解压目录。最后一条命令没有输出才表示目录正确。

> 启动后，在**管理 → 设置 → 模型接口**的“AI 服务商”中保存连接，再到**管理 → 设置 → 模型配置**分配模型。`.env` 只用于端口等部署选项；旧 AI 地址、密钥、模型环境变量不再生效，也不会自动转换。服务商设置见[用户手册](guide.md)。

```bash
cp .env.example .env
# 按需编辑 .env 中的宿主机端口等部署选项。
docker compose pull
docker compose up -d
```

默认 Compose 和 `latest` 标签只跟随正式版。预览版同样提供 GHCR 与 Docker Hub 镜像，但必须显式指定完整版本标签，不会覆盖 `latest`：

```bash
docker pull ghcr.io/diceframe/diceframe:2.3.0-beta.1
docker pull falconku/diceframe:2.3.0-beta.1
```

需要向量记忆时，先在**管理 → 设置 → 模型接口**保存 Embedding 服务商的地址、密钥和模型目录，再到**模型配置**启用向量记忆、选择该服务商/模型，按需设置最大输入并测试连接。Docker 内的 Ollama 服务商地址可使用 `http://host.docker.internal:11434` 或其他可达的宿主机地址；容器内的 `127.0.0.1` 指容器自身。本地服务商密钥可留空，AI 能力通过 WebUI 配置，不再使用旧向量环境变量。

启动后打开：

```text
http://localhost:9876
```

如果要换宿主机端口，改 `.env`：

```env
DICEFRAME_HTTP_PORT=8080
```

然后访问 `http://localhost:8080`。容器内部端口仍是 `9876`，这样 WebUI、插件托管和内部 API 地址保持稳定。

## 常用命令

以下命令同样需要在上述部署目录执行：

```bash
docker compose pull
docker compose up -d
docker compose logs -f
docker compose down
```

如果提示 `no configuration file provided: not found`，不是镜像故障，而是当前目录没有 Compose 配置文件。请进入原部署目录并确认 `docker-compose.yml` 存在。如果最初使用 `docker run` 或 NAS 容器管理界面创建容器，这些 Compose 命令不适用；请保留原来的端口、环境变量和 `data` 挂载，拉取新镜像后在原管理方式中重新创建容器。

如果你在本地修改了源码，需要重新构建自己的镜像：

```bash
docker compose up -d --build
docker compose build --no-cache
```

支持托管更新且 Python/系统运行时兼容的 Docker/NAS，可以在“管理 → 设置 → 关于”的版本更新区应用普通程序更新；候选版本验证失败时会恢复旧程序和可读数据。旧基线镜像或基础运行时变化，需要拉取镜像，并按原来的 `data/` 挂载、端口和环境变量重新创建容器。升级前请备份完整 `data/`，包括 `data/_updater`。各安装方式、数据保留和回滚行为见[应用更新说明](https://github.com/diceframe/diceframe/blob/main/docs/zh/updates.md)。

## 数据与密钥

- `./data` 是运行时目录，已经在 `.gitignore` 和 `.dockerignore` 中排除。
- `.env` 只放本机部署配置，已经在 `.gitignore` 和 `.dockerignore` 中排除。
- `.env.example` 可以提交，里面不应写真实 API key、token、群号或私有地址。
- 若不设置 `TRPG_ACCESS_TOKEN`，服务会自动生成首次访问口令并写入 `./data/access_token.txt`。
- 若忘记 WebUI 访问密码，在挂载出来的 `./data` 目录新建 `reset_access_password.txt`，写入新密码并重启容器；重置成功后该文件会自动删除。

## QQ / NapCat

Docker 版主服务仍然使用内置插件宿主。启用 QQ 插件时，Bot 作为主服务容器内的子进程运行，和 PC 版的插件生命周期一致。

推荐流程：

1. 先启动 WebUI：`docker compose up -d`
2. 在“管理 → 插件”启用 `QQ / NapCat`
3. 如果 NapCat 不在容器内，填写宿主机或 NAS 上可从容器访问的 `NAPCAT_HOST` / `NAPCAT_PORT`

内置 QQ 插件不需要填写 DiceFrame Bot API Token，服务会自动生成并持久化。外部 MaiBot Bridge 可在 WebUI 的“管理 → 设置 → Bot API”复制 Token。

也可以在首次启动前写入 `.env`：

```env
# 可选：固定全局 Bot API Token；留空则自动生成
TRPG_BOT_TOKEN=
NAPCAT_HOST=192.168.1.10
NAPCAT_PORT=3001
NAPCAT_TOKEN=
```

注意：Linux Docker 里 `127.0.0.1` 指容器自身，不是宿主机。NapCat 如果跑在宿主机，请填宿主机局域网 IP，或使用 compose 已映射的 `host.docker.internal`。

## PC 与 Docker 共存

PC 直接运行默认读项目内 `data/`；Docker compose 也映射同一个 `./data`。这意味着你可以在本机直接跑，也可以改用 Docker 跑，存档和设置仍是同一份。

如果想分开两套环境：

```bash
TRPG_DATA_DIR=./data-docker docker compose up
```

或把 compose 的 volume 改成：

```yaml
volumes:
  - ./data-docker:/app/data
```
