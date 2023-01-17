from Accounts.models import Account


def account_info(request):
    user = request.user
    if user.is_active:
        account = Account.objects.filter(pk=request.user.pk)
        user_id = account.model.get_user_id(self=user)
        first_name = account.model.get_first_name(self=user)
        user_image = account.model.get_user_image(self=user)
        return {
            'first_name': first_name,
            'user_image': user_image,
        }

    else:
        return {
            'first_name': 'user',
            'user_image': 'img',
        }