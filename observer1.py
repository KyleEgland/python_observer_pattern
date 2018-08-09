#! python
#
# SIMPLE
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
    def __init__(self):
        # Create an empty set that will later contain a set of subscribers
        self.subscribers = set()

    # This method allows objects to "subscribe" to the publishers updates
    def register(self, who):
        self.subscribers.add(who)

    # This method allows objects to unregister from the publishers updates
    def unregister(self, who):
        self.subscribers.discard(who)

    # Method for pushing updates to the subscribers
    def dispatch(self, message):
        # Loop through the set of subscribers
        for subscriber in self.subscribers:
            # Call the subscriber's own method to give them the update
            subscriber.update(message)


# -------------- #
# Implementation #
# -------------- #

# Create a publisher object
pub = Publisher()

# Create subscriber objects
bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

# Register subscriber objects to the publisher object
pub.register(bob)
pub.register(alice)
pub.register(john)

# Push a notification to the subscribers
pub.dispatch('It\'s lunchtime!')

# Unregister a subscriber
pub.unregister(john)

# Push another notification - to show unsubscribe worked
pub.dispatch('Time for dinner')
