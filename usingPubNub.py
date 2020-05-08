from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pprint import pprint

class MySubscribeCallback(SubscribeCallback):
    def status(self, pubnub, status):
        pass

    def presence(self, pubnub, presence):
        pprint(presence.__dict__)

    def message(self, pubnub, message):
        pprint(message.__dict__)

def my_publish_callback(envelope, status):
    print(envelope, status)

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-3a36de98-914a-11ea-8dc6-429c98eb9bb1"
pnconfig.publish_key = "pub-c-804b176d-6b15-44d6-ad4f-71194c237b25"

pubnub = PubNub(pnconfig)

pubnub.add_listener(MySubscribeCallback())

pubnub.subscribe()\
    .channels("pubnub_onboarding_channel")\
    .with_presence()\
    .execute()\

pubnub.publish()\
    .channel("pubnub_onboarding_channel")\
    .message({"sender": pnconfig.uuid, "content": "Hello From Python SDK"})\
    .pn_async(my_publish_callback)