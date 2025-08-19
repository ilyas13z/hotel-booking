from rest_framework import viewsets
from rest_framework.response import Response

from rooms.models import Room
from rooms.serializerers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    def list(self, request, *args, **kwargs):
        sort_order = request.query_params.get('ordering')
        
        rooms = self.get_queryset()
        if sort_order is not None:
            if any([i in sort_order for i in ['price', 'date_added']]):
                rooms = rooms.order_by(sort_order)
        
        serializer = self.get_serializer(rooms, many=True)
        
        return Response(serializer.data)
