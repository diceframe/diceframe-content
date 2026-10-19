# DiceFrame User Guide

[中文](../zh/guide.md) | English

Whether you are a GM preparing a new adventure or a player joining the table, this is the place to start. The sections below cover everyday tasks—from creating a game, taking actions, and rolling dice to using chat bots and updating DiceFrame. For code and development details, see the relevant technical guides.

## Find your way around

| Navigation | Everyday tasks |
| --- | --- |
| Overview | Create an adventure or resume a save. |
| Play | Describe actions, view the party, open game tools and the GM workspace. |
| Characters | Reuse a card from the character card library or manage this game's characters. |
| Content | Open Content library, Lorebook, Content packages or Rules. The library toolbar opens the world gallery, adventure workbench, script import and source management. |
| Manage | Memory, Logs, Plugins and Settings. |

In **Manage → Settings**, search sits at the top of the sidebar and opens the matching field. On phones, the category list can fold beneath it.

| Settings group | Where to go |
| --- | --- |
| Models and AI | **Model API** saves providers and credentials; **Model Routing** assigns models and contains the folded Advanced generation settings. |
| Connection and integrations | Network Proxy, Share Address, Bot API; Backend Connection appears in the standalone frontend. |
| Security and privacy | Access Password and Security, including DiceFrame Hub and privacy. |
| General | **General** combines interface language, speech, DF Agent and maintenance. **Game** stores new-game defaults. **Appearance** changes theme/backgrounds. **About** contains updates and restart controls. These are separate pages in the same group. |

For exact configuration behavior, see [AI and interface settings](https://github.com/diceframe/diceframe/blob/main/docs/en/ai-settings.md). These instructions follow the current main branch; older releases may have different menus.

## First Launch

Start the WebUI and open the address printed in the terminal, normally:

```text
http://localhost:18000
```

### AI providers and model routing (required, configure in the WebUI)

The model API powers adventure generation, check adjudication, and narration. **Configure it directly in the WebUI—no config files to edit:**

1. Open **Manage → Settings → Model API**, then add the provider name, API format (OpenAI-compatible or Anthropic), Base URL, and API key under AI Providers.
2. Fetch the provider's model catalog or add supported model IDs manually.
3. Open **Manage → Settings → Model Routing** and assign a saved provider and model to the main role. Add two fallbacks or assign embedding, TTS, ASR, and image-generation roles when needed.
4. Save and use the relevant connection-test buttons to verify each service.

Store each provider endpoint and credential once, then reuse it for the main model, fallbacks, embeddings, speech, and image generation. Current versions require saved providers and capability references. Old inline connection fields and AI environment variables are not activated or automatically converted: add providers and assign the roles manually after upgrading. A missing or deleted provider leaves its capability unconfigured; it does not revive old credentials. Browser/system voices and Edge TTS need no provider, and local providers may use an empty key.

### Long-term memory (vector memory) configuration (optional)

DiceFrame stores confirmed plot points as long-term memory and recalls them when generating new content. By default it uses keyword matching; enabling vector memory switches to semantic recall, which helps for long campaigns or information-heavy plots. Vector memory is **not required** — the game works fine without it.

Configure it in two places: first save the embedding service's address, key and model catalog under **Manage → Settings → Model API**. Then open **Manage → Settings → Model Routing**, enable Vector Memory, select that provider and model, set the maximum input if needed, and use **Test vector connection** before saving.

| Field | Description |
|-------|-------------|
| Provider | A saved provider from Model API; its address and key are edited there |
| Model | Embedding model name |
| Max input | `0` for automatic detection, or set per model |

**Option 1: local deployment (recommended, also the default model)**

Run an embedding model locally with [Ollama](https://ollama.com). Nothing leaves your machine and no service key is needed:

```powershell
ollama pull nomic-embed-text
```

Create a provider under **Manage → Settings → Model API** with Base URL `http://127.0.0.1:11434`, an empty API key and model `nomic-embed-text`; select it in Vector Memory under **Model Routing**. Ollama listens on port `11434` by default and DiceFrame uses its native endpoint. You can also install `bge-m3` with `ollama pull bge-m3` and add it to the provider's model catalog. When DiceFrame runs in Docker, use `http://host.docker.internal:11434` (or a reachable host address), because `127.0.0.1` inside the container refers to the container itself.

**Option 2: online service (alternative)**

For an online embedding service, save its endpoint and key in Model API and select its supported embedding model in Model Routing. For example, a SiliconFlow provider can use Base URL `https://api.siliconflow.cn/v1` and model `BAAI/bge-m3`, subject to that service's availability. This is a configuration example, not a partnership or sponsorship.

Failures are logged and long-term memory falls back to keyword matching, so normal play is unaffected.

## Optional voice features

Text-to-speech and voice input are optional. See [Optional voice features](voice.md) for browser voices, online or local engines, voice mapping, voice input, and troubleshooting.

## Start a Game

1. Open **Overview** and select **Create Adventure**.
2. Choose the game language.
3. Select a world template, generate one with AI, or enter your own setting.
4. Choose the rules and difficulty.
5. Create a character, or generate a draft and edit it.
6. Enter Play.
7. Submit an action such as “I inspect the runes on the wall.”

DiceFrame sends the action to the GM model, parses narrative state tags, and records changes to HP, inventory, gold, experience, scene, and related state.

## Content library and adventures

Use **Content → Content library** to find worlds, lorebooks and adventures. A world supplies the setting, default rules and associated books; lorebooks provide detailed NPC, place and background references. Each lorebook card shows its own title and separately identifies bound worlds. Search and the content-language filter narrow the cards; **Lorebook** follows the selected world/game scope.

For ready-made content, open **Content → Content packages**, preview the installation, resolve blocking messages and confirm. Check the completion or error status, then choose an installed adventure to start a game. A pack can contain adventures and reusable resources; it is not limited to D&D. The selected adventure and installed rules runtime must be compatible, and prose imports do not add executable rules.

To bring your own material, open **Import script** from the library toolbar:

1. Import UTF-8 Markdown/TXT, a text-layer PDF, Foundry Adventure export JSON, or unencrypted Fantasy Grounds XML/`.mod`. Scanned PDFs need OCR first.
2. Review extracted scenes, chapters, references and GM notes. Imported material starts GM-only; choose what to make public.
3. Correct validation errors or explicitly retain unsupported references as prose. The publication checklist explains why **Publish as adventure** is unavailable.
4. Validate and publish, then use the adventure to create a game.

Optional AI organization sends the draft to the configured main model and consumes tokens. Confirm the notice first; progress and Cancel are available. Completed calls may still be billed after cancellation. Review and adopt the result before publishing. The import does not execute external module scripts. See [Content, characters and play](https://github.com/diceframe/diceframe/blob/main/docs/en/content-and-play.md) for authoring and compatibility details.

## Languages and Content

Interface language changes WebUI text. Game language is stored in the save and controls GM narration, opening scenes, summaries, quick actions, and AI-generated content.

World templates, lorebooks, and content packs have their own `language`. Create prioritizes matching content but still shows other languages. Selecting Chinese content in an English UI does not translate the content, and vice versa.

Content V2 rules use one canonical core `<rule_id>.json` with typed overlays at
`locales/<locale>/<rule_id>.json`. Overlays may change display fields but never mechanics. Legacy
`<rule_id>_en.json`/`<rule_id>_ja.json` files are V1 compatibility inputs only and must not be used
for new content.

## Turns and Actions

Solo games progress after one action is submitted.

In multiplayer, each active player may submit one action per round. DiceFrame advances when every active player has submitted, or when the GM manually forces progression. There is no timeout: a slow or disconnected player remains in the waiting list until the GM decides. A player may revise the current action within the configured limit; only the final version is sent to the GM model.

## Multiplayer

The GM creates a game and uses **Invite Player** beneath the party member list to copy an invitation URL. Players open that URL directly; they do not extract or type a room/host identifier. Players can:

- Join the current game.
- Create a character.
- Claim an existing character.
- Submit actions from their own player page.

The GM opens **⋯ Member actions** at the right of a member card for a control link, editing, Away/return, AI control or removal, as permitted by that member's state. A **Control link** resumes an existing character; **Invite Player** invites newcomers. These owner controls are not shown to ordinary players. Mark a temporarily absent player Away so they stop blocking the round; restore them when they return.

**Party actions** sits between the member list and Rules recap. Rules that support rest expose party-rest controls there; the GM can request rolls, while players can resume pending rolls or view their roll history. On phones, open **Game tools → Party**. The left-edge Character status button reopens a closed character panel.

## Dice Flow

Some actions resolve directly; others require a check. Players describe actions naturally and never need to type “check” or click a roll button. After the action batch closes, a separate GM adjudication phase reads every action and calls `dice_checks` with existing players, attributes/skills, and targets. The server rolls exactly once and the narration phase must follow that fixed result:

1. A player submits an action.
2. A solo action advances immediately; multiplayer advances when everyone acts or the GM forces it.
3. The adjudication phase decides which actions warrant checks.
4. The server rolls once and shows reveal cards in action order.
5. The GM narrates from those immutable results.

New games reveal dice automatically by default. The GM can change this under **GM workspace → Rules → Check flow → Dice reveal**; an existing save keeps its recorded choice. CoC failures that can spend Luck still pause for the owning player or GM to decide. That decision never rerolls the die.

**Manage → Settings → Game**, directly below General, sets defaults for new games, including dice reveal, supported Push behavior, action suggestions and narration preferences. Changing defaults does not rewrite existing saves. The GM adjusts a running game's preferences in its workspace.

When available, the skill selector sits above the action button inside the input frame. A successful submission resets it to automatic judgment; a failed draft keeps the selection for retry. Each player can use **Suggestions** beside the action panel title to hide or show suggestions on their device without losing free-form input.

## DF Agent

The owner's DF Agent can inspect current state, search bundled help and prepare changes. Review and confirm proposed writes in the application. It uses the main model and may consume tokens; ordinary player pages do not expose it.

On phones, fold the task workspace to leave room for conversation. **Manage → Settings → General → DF Agent** controls its visibility, restores a misplaced launcher and sets its output budget (default 4096 tokens per model request). This is not a total task cost cap; generation tools keep their own budgets.

## Reading State Changes

After GM narration, the State changes panel shows what was actually committed to the save:

- HP damage or healing.
- Items gained, lost, or consumed.
- Gold gained, paid, or deducted.
- Experience and level changes.
- Scene or situation changes.
- Character-private perceptions.

If prose and recorded state conflict, the recorded state is authoritative.

### Confirming a Purchase

When the story offers something that costs money, DiceFrame asks the paying player to confirm first. No money is deducted and no item is added before confirmation.

In multiplayer, the player who is paying confirms the purchase. The purchase completes only when that character has enough money; rejecting it or having insufficient funds leaves both the balance and inventory unchanged.

## Chat Bot

DiceFrame can connect a Web game to QQ group chat through the built-in QQ/NapCat plugin. The adapter uses HTTP APIs and does not read saves directly.

1. Open QQ / NapCat under **Manage → Plugins**.
2. Enter the NapCat WebSocket address, port, and token.
3. Enable QQ / NapCat.
4. Copy the Bot binding command from the game page.
5. Send it to the target group.

The built-in plugin receives its DiceFrame Bot API Token automatically. For an external bridge such as MaiBot, copy the DiceFrame URL and token from **Manage → Settings → Bot API** into that bridge. Regenerating the token invalidates the old value.

The Bot follows the current game's language for help, status, recap, map, payment, character-creation, and error messages. The examples below use the English commands; Chinese games retain the corresponding Chinese commands.

## Using the Plugin Store

Open **Manage → Plugins → Plugin Store**. The store is an index: authors retain their source repositories while DiceFrame pins the latest stable Release to an exact commit during installation.

- Supported means the integration exists now. Partial means only the listed subset works. Reserved types cannot be installed from the store.
- Source pinned means installation resolves the latest stable GitHub Release to an exact commit and checks the plugin ID, version, and permissions again. It is not a code-safety guarantee.

The store prefers DiceFrame Hub for catalog metadata, review state, aggregate statistics, likes, ratings, and a sanitized README. If Hub is offline, DiceFrame uses its disk cache or the public registry mirrors, and local play remains available. Plugin packages are still downloaded directly from the author's repository; Hub does not proxy package bodies. Browsing the public catalog creates no installation identity. A local token is created only when an install event, like, or rating needs one. First start requires active acceptance of the Terms and acknowledgment of the Privacy Policy. Anonymous usage statistics are separate and off by default; heartbeats begin only after active opt-in and confirmation. The choice can be disabled or cleared in the DiceFrame Hub and privacy section under **Manage → Settings → Security**. Heartbeats contain only the DiceFrame version, coarse operating system, and time bucket—not games, characters, plugin lists, model settings, logs, or game content.
- `official`, `verified`, and `community` describe source/review level, not absolute safety. Install process plugins only from trusted authors.
- A disabled Install button is accompanied by a reason. Bundled plugins update with DiceFrame; entries without a public repository or stable Release cannot be installed.
- After installation, review permissions, enter the plugin's own settings, and enable it. QQ/NapCat still needs no manually entered DiceFrame Bot Token.
- The store checks for plugin updates and notifies users; installing or updating requires manual confirmation. Process plugins only notify and require confirmation; permission or runtime expansion also requires confirmation.
- Privately shared plugins should use a `.dfplugin` file produced by the packaging script. Select it under Local Install. After manually copying a plugin directory, use Rescan Local Plugins.
- Chat presentation extensions may add commands or replace status, map, and other replies with custom text, images, or cards. If an extension fails, DiceFrame keeps using its built-in presentation; the extension cannot rewrite authoritative character state, rolls, or payment results.

## Common Chat Commands

The examples below use `@bot` for mentioning the Bot:

```text
@bot help
@bot join CharacterName
@bot create character
@bot AI character
@bot invite
@bot recap
@bot map
@bot status
@bot sense
@bot pay
@bot confirm pay
@bot reject pay
@bot I inspect the runes on the wall
@bot advance
@bot away
@bot back
```

- `join CharacterName`: bind the platform account to a Web character.
- `create character`: get character-creation instructions or an entry link.
- `AI character`: generate a character draft for confirmation.
- `invite`: send the player join link.
- `recap`: show the public recap and recent turns.
- `map`: show the current and known locations.
- `status`: show the claimed character summary.
- `sense`: request character-private information, normally by direct message.
- `pay`: view pending payments; use `confirm pay` or `reject pay` to decide.
- `advance`: let the GM or an authorized account advance.
- `away` / `back`: leave temporarily or resume participation.

## Chat Actions

Players may mention the Bot and send a natural-language action:

```text
@bot I circle behind the guard and look for the key on his belt
```

Chat and Web use the same adjudication and full-table/manual progression flow. When a check is needed, the server rolls automatically and the Bot sends a compact line such as `🎲 Character · Strength Check d20=… vs DC … → Success`, followed by GM narration and recorded state changes.

The compatibility command `roll` only explains this automatic flow; it never rolls again or confirms a pending die.

## Private Information

Some clues belong to one character, such as hidden doors, hallucinations, dreams, private thoughts, or unique perceptions. In group chat, send:

```text
@bot sense
```

The Bot attempts a direct message. If that fails, it asks the player to check temporary-session or friend settings.

## Updating DiceFrame

Check for a new version in the Version Update section under **Manage → Settings → About**. The apply method depends on the installation:

- Windows portable builds can download and apply an update in the WebUI. A failed candidate returns to the old version.
- Extracted source releases can apply an update and then ask for a manual restart.
- Git development checkouts should use `git pull`.
- Managed Docker installations with a compatible Python/system runtime can apply application updates from **Manage → Settings → About**. Failed candidate validation returns to the previous program and its readable data.
- Legacy Docker images and base-runtime changes require pulling an image and recreating the container with its existing data mount, ports and environment. In the original Compose directory, use `docker compose pull` followed by `docker compose up -d`. Keep a `docker run` deployment's original options when recreating it.

Back up the complete `data/` directory, including updater-managed data and binding records. `latest` follows stable releases; preview images require their explicit version tag. Initial migration to managed updates may require one image replacement. See [Application Updates](https://github.com/diceframe/diceframe/blob/main/docs/en/updates.md) for the installation-specific steps, retained datasets and rollback behavior.

## Troubleshooting

### The AI does not respond

Check model settings and Test connection. Common causes are an incorrect API key, model name, incompatible base URL, or network failure.

### Update check returns HTTP 403

The anonymous request quota used for version checking is temporarily exhausted. Only update notifications are affected; games, saves, and model calls continue to work. Retry later or open the project's Releases page directly.

### A player cannot act

The character may be dead, not joined to the game, waiting during resolution, or viewed through GM preview. Check player status before refreshing.

### The Bot does not respond

Confirm that QQ/NapCat is enabled, then check the NapCat WebSocket host, port, and token. The group must also be bound to a game.

### Group chat does not progress

A multiplayer round may still be waiting for another active player. The GM can send `@bot 推进` or force progression in the WebUI.

### State looks wrong

Refresh the game detail. If narration conflicts with State changes, the recorded changes are authoritative. Preserve the save instead of deleting `data/` if further investigation is needed.

### Will upgrades delete custom worlds or rules?

No. Bundled templates are synchronized into `data/templates/`, while custom and AI-generated content is kept as user data. Upgrades refresh built-ins without overwriting user content. Copy the complete `data/` directory when moving computers.

If `data/config.json` or `data/secrets.json` is damaged, DiceFrame preserves it as `*.corrupt-timestamp.json` and starts with a safe empty configuration. Do not publish the preserved copy because it may contain API keys or credentials.

### Can I publish saves or chat logs?

This is not recommended. `data/` may contain API keys, access credentials, real group IDs, private messages, and complete campaign records. Never commit `data/`, `.env`, logs, or caches to a public repository.
