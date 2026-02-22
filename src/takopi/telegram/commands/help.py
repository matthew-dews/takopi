from __future__ import annotations

from typing import TYPE_CHECKING

from ..types import TelegramIncomingMessage
from .menu import build_bot_commands
from .reply import make_reply

if TYPE_CHECKING:
    from ..bridge import TelegramBridgeConfig


async def _handle_help_command(
    cfg: TelegramBridgeConfig,
    msg: TelegramIncomingMessage,
) -> None:
    commands = build_bot_commands(
        cfg.runtime,
        include_file=cfg.files.enabled,
        include_topics=cfg.topics.enabled,
    )
    lines = [f"/{cmd['command']} — {cmd['description']}" for cmd in commands]
    reply = make_reply(cfg, msg)
    await reply(text="\n".join(lines))
