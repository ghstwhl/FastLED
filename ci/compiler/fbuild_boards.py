"""Boards that use fbuild instead of PlatformIO for compilation."""

# These boards use fbuild (Rust-based build system) instead of direct PlatformIO CLI.
# fbuild provides faster builds via daemon-based caching and toolchain management.
#
# Supported platforms (fbuild orchestrator must exist):
#   - atmelavr  -> AvrOrchestrator  (avr-gcc with -mmcu=)
#   - espressif32 (pioarduino) -> Esp32Orchestrator (metadata-driven toolchain)
#   - teensy    -> TeensyOrchestrator (arm-none-eabi-gcc, Cortex-M7 only)
#
# NOT supported by fbuild (must stay on PlatformIO):
#   - atmelmegaavr boards (ATtiny1604, ATtiny1616, nano_every) -- platform not recognized
#   - esp32s2, esp32h2 -- missing MCU config in fbuild
#   - Teensy 3.x/LC (teensy30..36, teensylc) -- only Cortex-M7 config exists
#   - Specialized ESP32 variants (qemu, idf33, idf44, i2s) -- custom IDF versions
#   - uno_r4_wifi -- uses renesas-ra platform, no fbuild orchestrator
#   - atmega8a -- uses MiniCore framework (not registered in fbuild)
#   - leonardo (ATmega32U4) -- USB VID/PID defines not handled by fbuild
#   - ESP32 boards (Windows) -- zccache hits OS error 206 (path too long) on Windows
#   - teensy40, teensy41 -- lib/ discovery fails + command-line quoting broken
FBUILD_BOARDS: frozenset[str] = frozenset(
    {
        # AVR (atmelavr)
        "uno",
        "attiny85",
        "attiny88",
        "attiny4313",
    }
)
