import json
from urllib import request
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import message, room

from entry.models import usrinfo

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        mssg_text = text_data_json['message']
        overall_message=text_data_json['overall_message']
        receiver_txt=text_data_json['receiver']
        user_role=text_data_json['user_role']
        usr=self.scope['user']
        usr=User.objects.get(username=(usr.username))
        receiver=User.objects.get(username=receiver_txt)
        
        mssg=message.objects.create(mssg=mssg_text,sender=usr,receiver=receiver)
        sent_time=str(mssg.time_send)
        if user_role=="guide":
            rm=room.objects.get(room_name=str(usr)+"_"+str(receiver))
        elif user_role=="guidee":
            rm=room.objects.get(room_name=str(receiver)+"_"+str(usr))
        
        rm.messages.add(mssg)
        rm.save()
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': overall_message,
                'msg':mssg_text,
                'user_role':user_role,
                'sent_time':sent_time,
                'receiver':receiver_txt,

            }
        )

    # Receive message from room group
    def chat_message(self, event):
        msg = event['message']
        msg_str=str(event['msg'])
        sent_time=str(event['sent_time'])
        receiver_txt=str(event['receiver'])
        user_role=str(event['user_role'])
        usr=self.scope['user']
        usr=User.objects.get(username=(usr.username))
        receiver=User.objects.get(username=receiver_txt)
        msgs=message.objects.filter(mssg=msg_str,sender=usr,receiver=receiver)
        
        print(msgs)
        for mssg in msgs:
            print(str(mssg.time_send),"  ",sent_time)
            if str(mssg.time_send)==sent_time:
                print(user_role=="guidee")
                if user_role =="guide":
                    mssg.status="gd1"
                elif user_role =="guidee":
                    mssg.status="gde1"
                mssg.save()
                print(mssg.status)
                break  
        
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': msg
        }))