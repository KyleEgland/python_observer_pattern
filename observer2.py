#! python
#
# MORE COMPLEX
#
# The Observer Pattern
# The idea behind the observer pattern is that there is an object to be
# observered (observable) that will change and there are other "observer"
# objects that need to be notified of this change.  Here, the words "publisher"
# and "subscriber" are used to describe the observable and the observer
# respectfully - hopefully that's less confusing.


# This class represents the observer - the things that need to recieve updates
class SubscriberOne:
    def __init__(self, name):
        self.name = name

    # This method is the means by which the subscriber is pushed updates by the
    # publisher.
    def update(self, message):
        print(f'{self.name} got message "{message}"')


# In this example, a second class is created to represent a different type of
# subscriber with a different update method
class SubscriberTwo:
    def __init__(self, name):
        self.name = name

    # This method is the means by which the subscriber is pushed updates by the
    # publisher.
    def receive(self, message):
        print(f'{self.name} got message "{message}"')


# This class represents the observable - the thing that the subscribers are
# watching.
class Publisher:
    def __init__(self):
        # Create an empty dictionary that will later contain a set of
        # subscribers and their associated update methods
        self.subscribers = dict()

    # This method allows objects to "subscribe" to the publishers updates
    def register(self, who, callback=None):
        # Callback = the method by which a subscriber is updated.  If no
        # callback is specified, get that attribute from the subscriber
        if callback is None:
            callback = getattr(who, 'update')
        # Assign that subscriber to the dictionary
        self.subscribers[who] = callback

    # This method allows objects to unregister from the publishers updates
    def unregister(self, who):
        del self.subscribers[who]

    # Method for pushing updates to the subscribers
    def dispatch(self, message):
        # Loop through the set of subscribers and callbacks
        for subscriber, callback in self.subscribers.items():
            # Call the subscriber's own method to give them the update
            callback(message)


# -------------- #
# Implementation #
# -------------- #

# Create a publisher object
pub = Publisher()

# Create subscriber objects
bob = SubscriberOne('Bob')
alice = SubscriberTwo('Alice')
john = SubscriberOne('John')

# Register subscriber objects to the publisher object
pub.register(bob, bob.update)
pub.register(alice, alice.receive)
pub.register(john)

# Push a notification to the subscribers
pub.dispatch('It\'s lunchtime!')

# Unregister a subscriber
pub.unregister(john)

# Push another notification - to show unsubscribe worked
pub.dispatch('Time for dinner')
