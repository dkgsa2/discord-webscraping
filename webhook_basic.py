from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_url = r'https://discord.com/api/webhooks/925789154133041213/QtbOOovXjoHCHEuEz8qBZpjw8dH5ry_VT7FY33AP7ihV2AfveWzMSftzq3b-NnlA6pz-'


def basic_webhook(content: str):
    """
    post to discord webhook with selected content

    :param content:
    :return:
    """
    allowed_mentions = {
        "parse": ["users", "roles"],
    }
    # use <@XXXXXX> for users and <@&XXXXXX> for roles
    webhook = DiscordWebhook(url=webhook_url, content= content,allowed_mentions = allowed_mentions)
    response = webhook.execute()

