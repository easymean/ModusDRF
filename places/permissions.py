from common.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated


class IsHostAuthenticated(IsOwner):
    def has_permission(self, request, view):

        if IsAuthenticated(request, view):
            host = request.user
            print(host)
            # if host.is_auth is True:
            #     return True
            # else:
            #     return False
        else:
            return False
