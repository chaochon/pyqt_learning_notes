from twisted.internet import defer, reactor

def show_name(name):
    print(name)
    return name

def show_sex(sex):
    print(sex)

d = defer.Deferred()

d.addCallback(show_name)
d.addCallback(show_sex)

d.callback("caochong")
reactor.callLater(5, d.callback, "caochong")
reactor.run()