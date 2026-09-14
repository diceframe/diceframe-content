# DiceFrame Optional Voice Features

[中文](../zh/voice.md) | English

Voice is not required for a game. This page covers text-to-speech (TTS), voice input (ASR), voice mapping, and troubleshooting. DiceFrame handles the connection, playback, and settings; local programs such as Kokoro and GPT-SoVITS generate the audio.

## Text-to-speech (TTS)

### Start with browser voices

This is the simplest option and downloads no model:

1. Open **Management → Settings → Model Routing** and choose Browser / system voice for the TTS role.
2. Open **Management → Settings → Advanced → Text-to-speech**.
3. Enable automatic GM narration if you want it, then save.

The available voices come from the current browser and operating system. When automatic speech is off, public narration can still be played manually from the Play page.

### Use Kokoro

If Docker Desktop is already installed, start the open-source Kokoro-FastAPI CPU service:

```powershell
docker run --name diceframe-kokoro -p 8880:8880 ghcr.io/remsky/kokoro-fastapi-cpu:v0.6.0
```

The first run downloads the image and model. Leave the service running, then configure DiceFrame:

1. Open **Management → Settings → Model API**, add the service, set Base URL to `http://127.0.0.1:8880/v1`, leave API key empty, and add the model `kokoro`.
2. Open **Management → Settings → Model Routing** and assign this provider and `kokoro` to TTS.
3. Install and enable **Kokoro Chinese Voice Presets** from the plugin store or Local Install. A preset is optional; you can instead enter an existing service Voice ID such as `zf_xiaobei` under My voices.
4. Open **Management → Settings → Advanced → Text-to-speech**, choose the default, GM, and player voices, and select Save and test.
5. Once preview works, optionally enable automatic narration.

When DiceFrame itself runs in Docker, `127.0.0.1` refers to the DiceFrame container rather than the host. Use `http://host.docker.internal:8880/v1` in the common desktop setup, or the TTS service name when both containers share a network.

### Use GPT-SoVITS

Start the GPT-SoVITS HTTP API using its own instructions, then select GPT-SoVITS under **Management → Settings → Model Routing** and configure its provider. Each personal voice also needs a reference WAV, an exact transcript, and the prompt language:

- Upload the WAV when DiceFrame and the TTS service can read the same local file.
- For another computer or container, use Server-visible path. The path must be readable from the TTS service itself.

### TTS troubleshooting

- **Connection failed**: open Kokoro's `http://127.0.0.1:8880/docs` first, then check that the Base URL ends in `/v1`.
- **Voice not found**: enable the installed preset, or verify that the Voice ID exists in the active TTS server.
- **Browser speech works but local speech fails**: this is normally a server, port, or container-network issue. Switching back to Browser voice does not affect saves.
- A remote TTS service receives the public narration that it is asked to speak. Prefer a local service for private sessions, and never expose the admin UI or local TTS port directly to the public internet.

## Voice input (ASR)

Voice input transcribes a recording from the action composer. It requires browser microphone permission and an HTTPS or `localhost` page.

1. In **Management → Settings → Model Routing**, open the Speech recognition model card, choose OpenAI-compatible, and select a saved provider and model.
2. In **Management → Settings → Advanced → Speech recognition**, set the timeout and save.
3. Select Save & record test to verify the endpoint. During play, click the microphone button beside the action composer; the transcript is returned to the input box after recording stops.

The endpoint must support OpenAI's `/v1/audio/transcriptions`; common models include `whisper-1` and `SenseVoice`. Select Off when you do not need voice input; the microphone button is then hidden.
