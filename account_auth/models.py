from django.contrib.auth.models import User
from django.db import models


class BlackListedTokens(models.Model):
    '''
        Everytime the user logs out of the account, as it is impossible to simply delete the access token
        before it expires,  it will be inserted as a record inside this table and a new validator will be created
        to check if the Token was blacklisted or not.  
    '''
    token = models.CharField(max_length = 500)
    user = models.ForeignKey(User, related_name = 'token_user', on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now = True)

    class Meta:
        unique_together = ('token', 'user')


