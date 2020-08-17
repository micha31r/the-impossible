import json
from channels.generic.websocket import AsyncWebsocketConsumer

from . import database_actions

class ChatConsumer(AsyncWebsocketConsumer):
    # self.scope is similar to request in a normal django view

    # This runs when a new websocket connections is made
    async def connect(self):
        # Obtain the chat group slug
        self.chat_group_slug = self.scope['url_route']['kwargs']['chat_group_slug']

        # Create group name based on chat group slug
        self.group_name = f'chat_{self.chat_group_slug}'

        # Add this consumer to a channel group
        # https://channels.readthedocs.io/en/latest/tutorial/part_2.html
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # Check if user has access to this group
        allow_connection = await database_actions.user_in_chat_group(
            self.scope["user"],
            self.chat_group_slug
        )

        if allow_connection:
            # This accepts the websocket connection
         # If this is not called then the connection will be refused
            await self.accept()

    # This runs when a websocket connection is terminated
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from websocket
    async def receive(self, text_data):
        # Convert json string to json object and retrieve posted message
        data = json.loads(text_data)
        message = data['message']

        # Save posted message
        await database_actions.save_message(self.scope["user"], message, self.chat_group_slug)

        # Send message to channel group (the chat group)
        # The 'type' attribute tells the system what function to run when a message is received
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'username': self.scope["user"].username,
                'message': message
            }
        )

    # Send new text messages in this channel group (the chat group) back to users
    async def chat_message(self, event):
        message = event['message']

        # Send message to websocket
        await self.send(
            text_data = json.dumps(
                {   
                    'username': event['username'],
                    'message': message
                }
            )
        )