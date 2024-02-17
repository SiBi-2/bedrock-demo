from enum import Enum

class StylePreset(Enum):
    MODEL_3D = "3d-model"
    ANALOG_FILM = "analog-film"
    ANIME = "anime"
    CINEMATIC = "cinematic"
    COMIC_BOOK = "comic-book"
    DIGITAL_ART = "digital-art"
    ENHANCE = "enhance"
    FANTASY_ART = "fantasy-art"
    ISOMETRIC = "isometric"
    LINE_ART = "line-art"
    LOW_POLY = "low-poly"
    MODELING_COMPOUND = "modeling-compound"
    NEON_PUNK = "neon-punk"
    ORIGAMI = "origami"
    PHOTOGRAPHIC = "photographic"
    PIXEL_ART = "pixel-art"
    TILE_TEXTURE = "tile-texture"

class BedrockModels(Enum):
    LLAMA2_CHAT_13B = "meta.llama2-13b-chat-v1"
    LLAMA2_CHAT_70B = "meta.llama2-70b-chat-v1"
    J2_MID = "ai21.j2-mid-v1"
    J2_ULTRA = "ai21.j2-ultra-v1"
    CLAUDE2 = "anthropic.claude-v2"
    STABILITY_XL_1 = "stability.stable-diffusion-xl-v1"
    STABILITY_XL_0 = "stability.stable-diffusion-xl-v0"
    TITAN_TEXT_G1_LITE = "amazon.titan-text-lite-v1"
    TITAN_TEXT_G1_EXPRESS = "amazon.titan-text-express-v1"
    COHERE_COMMAND_TEXT_14 = "cohere.command-text-v14"
    COHERE_COMMAND_LIGHT_TEXT_14 = "cohere.command-light-text-v14"
    TITAN_EMBEDDING = "amazon.titan-embed-text-v1"

class OpenaiModels(Enum):
    GPT_3_5_TURBO_0125 = "gpt-3.5-turbo-0125"
    TEXT_EMBEDDING_3_SMALL = "text-embedding-3-small"
    GPT_4 = "gpt-4"
    SPEECH_TO_TEXT = "whisper-1"
    TEXT_TO_SPEECH = "tts-1"

class PineconeIndex(Enum):
    DEMO_MICHAEL_AI_V2 = "demo-michael-ai-v2"
    FULL_CONFLUENCE = "good-one"