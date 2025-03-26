from discord_webhook import DiscordWebhook
import aiohttp
import os

from weather_data import charlotte_weather, port_washington_weather


def send_discord_update():
    """
    This function will utilize a Discord webhook to send a message to my
    MongoDB Weather Database Discord server. Three different
    conditions will trigger a message being sent:
    1.) If the temperature is higher in Port Washington, WI than in
    Charlotte, NC.
    2.) If there is any recorded snowfall in Charlotte, NC.
    3.) If there is more recorded snowfall in Charlotte, NC than in
    Port Washington, WI.

    Args:
        None

    Returns:
        None
    """
    # Use the MongoDB connection string
    DISCORD_WEBHOOK_URL = os.environ["discord_webhook_url"]
    
    # Obtain the weather data for both Charlotte, NC & Port Washington, WI
    charlotte_temp = charlotte_weather["temp"]
    charlotte_snow = charlotte_weather["snow"]
    
    port_washington_temp = port_washington_weather["temp"]
    port_washington_snow = port_washington_weather["snow"]
    
    # If it is warmer in Port Washington, WI than in Charlotte, NC send a Discord message
    if charlotte_temp < port_washington_temp:
        webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL, content=f"In Charlotte, NC it is currently {charlotte_temp}°F, and in Port Washington, WI it is currently {port_washington_temp}°F. Who would have thought it was warmer in Port Washington, WI than in Charlotte, NC today?")
    
    # If there is any amount of snow on the ground in Charlotte, NC send a Discord message
    if charlotte_snow != 0:
        webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL, content=f"In Charlotte, NC there is currently {charlotte_snow} inches of snow on the ground. What a rare sight to see in Charlotte, NC!")
    
    # If there is more snow on the ground in Charlotte, NC than in Port Washington, WI send a Discord message
    if charlotte_snow > port_washington_snow:
        webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL, content=f"In Charlotte, NC there is currently {charlotte_snow} inches of snow on the ground and in Port Washington, WI there is currently {port_washington_snow} inches of snow on the ground. How could there possibly more snow in Charlotte, NC than in Port Washignton, WI?")
