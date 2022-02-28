import time
from discord.ext import commands
from discord import FFmpegPCMAudio
from keep_alive import keep_alive

client = commands.Bot(command_prefix="-")

@client.command(pass_context = True)
async def start(ctx, work_time, short_break, long_break, intervals):
  if ctx.author.voice:
    voiceChannel = ctx.message.author.voice.channel
    voice = await voiceChannel.connect()
    await ctx.send("Pomodoro starts now!")
    join_vc = FFmpegPCMAudio("join_VC.mp3")
    voice.play(join_vc)
    while True:
      for i in range(int(intervals) - 1):
        t = int(work_time) * 60
        while t:
          time.sleep(1)
          t -= 1
        await ctx.send("Short Break Time!!")
        break_time = FFmpegPCMAudio("timer_end_I_break.mp3")
        voice.play(break_time)

        t = int(short_break) * 60
        while t:
          time.sleep(1)
          t -= 1
        await ctx.send("Study Time!!")
        timer_start = FFmpegPCMAudio("timer_start.mp3")
        voice.play(timer_start)

      t = int(work_time) * 60
      while t:
        time.sleep(1)
        t -= 1
      await ctx.send("Long Break Time!!")
      break_time = FFmpegPCMAudio("timer_end_I_break.mp3")
      voice.play(break_time)

      t = int(long_break) * 60
      while t:
        time.sleep(1)
        t -= 1
      await ctx.send("Study Time!!")
      timer_start = FFmpegPCMAudio("timer_start.mp3")
      voice.play(timer_start)
  else:
    await ctx.send("You need to join a voice channel.")

@client.command(pass_context = True)
async def stop(ctx):
  if ctx.voice_client:
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Good job :)")
  else:
    await ctx.send("I'm not in a voice channel.")

keep_alive()
client.run("ODg0MTQ0MDY4NDc1NjUwMTE4.YTUNVA.r2EzfB-P-cxpKSwe_VB0uszb-6g")
