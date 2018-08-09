#! python
#
# EVEN MORE COMPLEX
#
# The Observer Pattern
# The idea behind the observer pattern is that there is an object to be
# observered (observable) that will change and there are other "observer"
# objects that need to be notified of this change.  Here, the words "publisher"
# and "subscriber" are used to describe the observable and the observer
# respectfully - hopefully that's less confusing.


# This class represents the observer - the things that need to recieve updates
class Subscriber:
    def __init__(self, name):
        self.name = name

    # This method is the means by which the subscriber is pushed updates by the
    # publisher.
    def update(self, message):
        print(f'{self.name} got message "{message}"')


# This class represents the observable - the thing that the subscribers are
# watching.
class Publisher:
    def __init__(self, events):
        self.subscribers = {event: dict() for event in events}

    # "Helper" method
    def get_subscribers(self, event):
        return self.subscribers[event]

    # This method allows objects to "subscribe" to the publishers updates
    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    # This method allows objects to unregister from the publishers updates
    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    # Method for pushing updates to the subscribers
    def dispatch(self, event, message):
        # Loop through the dictionary of subscribers
        for subscriber, callback in self.get_subscribers(event).items():
            # Call the subscriber's own method to give them the update
            callback(message)


# -------------- #
# Implementation #
# -------------- #

# Create a publisher object
pub = Publisher(['lunch', 'dinner'])

# Create subscriber objects
bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

# Register subscriber objects to the publisher object
pub.register('lunch', bob)
pub.register('dinner', alice)
pub.register('lunch', john)
pub.register('dinner', john)

# Push a notification to the subscribers
pub.dispatch('lunch', 'It\'s lunchtime!')
pub.dispatch('dinner', 'Dinner is served')
