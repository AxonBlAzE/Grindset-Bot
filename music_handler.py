def repeat(guild, voice, audio, fn):
    fn('in')
    voice.play(audio, after=lambda e: repeat(guild, voice, audio))
    voice.is_playing()