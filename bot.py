import discord
from discord.ext import commands
import datetime
import asyncio
from asyncio import sleep

client = commands.Bot(command_prefix =('/'))

@client.event

async def on_ready():
    print('Бот подключён!')

@client.command()
async def server(ctx):
    embed = discord.Embed(
        color = ctx.guild.owner.top_role.color
    )
    guild = ctx.guild
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    embed.add_field(name = f"Основная информация о **{ctx.guild.name}**: ", value = f"ID: **{ctx.guild.id}** \nСоздатель: **{ctx.guild.owner}** \nРегион: **{ctx.guild.region}** \n Дата-создания: **{ctx.guild.created_at}**  \n Уровень верефикации: **{str(ctx.guild.verification_level).upper()}** \nБусты **{guild.premium_subscription_count}** ")
    await sleep(1)
    embed.add_field(name = f"Информация о участниках **{ctx.guild.name}**: ", value = f"Участников **{guild.member_count}** \nОнлайн **{sum(member.status==discord.Status.online and not member.client for member in ctx.guild.members)}** \nОфлайн **{sum(member.status==discord.Status.offline and not member.client for member in ctx.guild.members)}** \nНе активен  **{sum(member.status==discord.Status.idle and not member.client for member in ctx.guild.members)}** \nНе беспокоить **{sum(member.status==discord.Status.dnd and not member.client for member in ctx.guild.members)}** \n Ботов **{sum(member.client for member in ctx.guild.members)}** ")
    await sleep(1)
    embed.add_field(name = f"Информация о каналах **{ctx.guild.name}**: ", value = f"Категорий: **{len(guild.channels)}** \n<Каналов: **{len(guild.channels)}** \nТекстовых: **{len(guild.text_channels)}** \nГолосовых: **{len(guild.voice_channels)}**")
    await ctx.send(embed=embed)
    
    bot.run('ваш токен')
