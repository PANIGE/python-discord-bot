def SameChannelAndAuthor(ctx):
    def inner_check(message):
        return message.author.id == ctx.message.author.id and message.channel.id == ctx.message.channel.id
    return inner_check

def SameChannel(ctx):
    def inner_check(message):
        return message.channel.id == ctx.message.channel.id
    return inner_check

def SameAuthor(ctx):
    def inner_check(message):
        return message.author.id == ctx.message.author.id
    return inner_check
